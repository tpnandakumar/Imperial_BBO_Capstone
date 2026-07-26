"""PGC 008CE adaptive, cost-aware targeting controller.

Implements:
1. Development-only intervention-benefit prediction.
2. Stack-aware targeting selection.
3. Measured-oscillation stability spin.
5. Progressive model recruitment.
6. Runtime and memory instrumentation.

Electrical energy is intentionally not estimated. It must be measured by an
external energy meter or supported hardware counter.
"""

from __future__ import annotations

from dataclasses import dataclass
from time import perf_counter_ns
from typing import Sequence
import os

import numpy as np
import psutil
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


Array = np.ndarray


@dataclass(frozen=True)
class TargetingPolicy:
    sparse_max: int = 5
    transition_size: int = 7
    sparse_threshold: float = 0.48
    transition_threshold: float = 0.55
    dense_threshold: float = 0.62
    specialist_offset: float = 0.18
    fbw_gain: float = 0.38
    dual_gain: float = 0.24
    ils_gain: float = 0.10
    spin_gain: float = 0.10


@dataclass
class CostRecord:
    latency_ns: int
    latency_ms: float
    rss_before_bytes: int
    rss_after_bytes: int
    rss_delta_bytes: int
    active_models_mean: float
    electrical_energy_joules: float | None = None
    monetary_cost_gbp: float | None = None


@dataclass
class ControllerResult:
    probabilities: Array
    active_sets: list[Array]
    protocol: str
    benefit_probability: Array
    specialist_recruitment_rate: float
    full_recruitment_rate: float
    oscillation_rate: float
    spin_activation_rate: float
    cost: CostRecord


class AdaptiveTargetingController:
    """Development-fitted controller with progressive model recruitment."""

    def __init__(self, policy: TargetingPolicy | None = None) -> None:
        self.policy = policy or TargetingPolicy()
        self._benefit_model = None
        self._benefit_prevalence = 0.0

    @staticmethod
    def _normalise(p: Array) -> Array:
        p = np.clip(np.asarray(p, dtype=float), 1e-12, None)
        return p / p.sum(axis=1, keepdims=True)

    @staticmethod
    def _agreement(probabilities: Sequence[Array], indices: Array) -> Array:
        pred = np.stack([probabilities[i].argmax(axis=1) for i in indices], axis=1)
        n_classes = probabilities[0].shape[1]
        counts = np.stack([(pred == c).sum(axis=1) for c in range(n_classes)], axis=1)
        return counts.max(axis=1) / len(indices)

    def _features(
        self,
        base: Array,
        target: Array,
        probabilities: Sequence[Array],
        indices: Array,
    ) -> Array:
        ordered = np.sort(base, axis=1)
        confidence = base.max(axis=1)
        margin = ordered[:, -1] - ordered[:, -2]
        entropy = -np.sum(base * np.log(np.clip(base, 1e-12, 1)), axis=1)
        entropy /= np.log(base.shape[1])
        agreement = self._agreement(probabilities, indices)
        full_indices = np.arange(len(probabilities))
        target_agreement = self._agreement(probabilities, full_indices)
        l1_distance = 0.5 * np.sum(np.abs(target - base), axis=1)
        cosine = np.sum(base * target, axis=1)
        cosine /= np.linalg.norm(base, axis=1) * np.linalg.norm(target, axis=1) + 1e-12
        target_ordered = np.sort(target, axis=1)
        target_margin = target_ordered[:, -1] - target_ordered[:, -2]
        return np.column_stack(
            [
                confidence,
                margin,
                entropy,
                agreement,
                target_agreement,
                l1_distance,
                1 - np.clip(cosine, -1, 1),
                target.max(axis=1) - confidence,
                target_margin - margin,
                np.full(len(base), len(indices) / len(probabilities)),
            ]
        )

    def fit_benefit_predictor(
        self,
        development_base: Array,
        development_target: Array,
        development_probabilities: Sequence[Array],
        selected_indices: Array,
        y_development: Array,
        classes: Array,
    ) -> None:
        """Fit only on development predictions and labels."""
        features = self._features(
            development_base,
            development_target,
            development_probabilities,
            selected_indices,
        )
        base_pred = classes[development_base.argmax(axis=1)]
        target_pred = classes[development_target.argmax(axis=1)]
        true_column = np.searchsorted(classes, y_development)
        probability_gain = (
            development_target[np.arange(len(y_development)), true_column]
            - development_base[np.arange(len(y_development)), true_column]
        )
        benefit = (
            ((base_pred != y_development) & (target_pred == y_development))
            | (probability_gain > 0.05)
        ).astype(int)
        self._benefit_prevalence = float(benefit.mean())
        if benefit.min() == benefit.max():
            self._benefit_model = None
            return
        self._benefit_model = make_pipeline(
            StandardScaler(),
            LogisticRegression(
                max_iter=500,
                class_weight="balanced",
                random_state=0,
            ),
        )
        self._benefit_model.fit(features, benefit)

    def _protocol(self, stack_size: int) -> tuple[str, float, float]:
        p = self.policy
        if stack_size <= p.sparse_max:
            return "FBW_PVF", p.sparse_threshold, p.fbw_gain
        if stack_size == p.transition_size:
            return "DUAL_MG_DMHLP_LOS_SSV", p.transition_threshold, p.dual_gain
        return "ILS_H", p.dense_threshold, p.ils_gain

    def apply(
        self,
        base: Array,
        full_target: Array,
        model_probabilities: Sequence[Array],
        selected_indices: Array,
        ranked_models: Array,
    ) -> ControllerResult:
        """Apply targeting without using holdout labels."""
        process = psutil.Process(os.getpid())
        rss_before = process.memory_info().rss
        started = perf_counter_ns()

        features = self._features(
            base, full_target, model_probabilities, selected_indices
        )
        if self._benefit_model is None:
            benefit_probability = np.full(len(base), self._benefit_prevalence)
        else:
            benefit_probability = self._benefit_model.predict_proba(features)[:, 1]

        protocol, full_threshold, gain = self._protocol(len(selected_indices))
        specialist_threshold = max(
            0.30, full_threshold - self.policy.specialist_offset
        )

        core = np.asarray(
            [m for m in ranked_models if m in selected_indices][
                : min(3, len(selected_indices))
            ],
            dtype=int,
        )
        specialist = int(ranked_models[0])
        core_prediction = self._normalise(
            np.mean([model_probabilities[m] for m in core], axis=0)
        )
        specialist_prediction = model_probabilities[specialist]
        stage_two = self._normalise(
            0.82 * core_prediction + 0.18 * specialist_prediction
        )

        full_recruit = benefit_probability >= full_threshold
        specialist_recruit = benefit_probability >= specialist_threshold

        class_one = core_prediction.argmax(axis=1)
        class_two = stage_two.argmax(axis=1)
        class_three = full_target.argmax(axis=1)
        conf_one = core_prediction.max(axis=1)
        conf_two = stage_two.max(axis=1)
        conf_three = full_target.max(axis=1)

        oscillation = (
            ((class_one != class_two) & (class_two != class_three))
            | ((conf_two - conf_one) * (conf_three - conf_two) < 0)
        )

        output = base.copy()
        active_sets = [
            np.asarray(selected_indices, dtype=int).copy() for _ in range(len(base))
        ]

        specialist_only = specialist_recruit & ~full_recruit
        output[specialist_only] = stage_two[specialist_only]
        for row in np.where(specialist_only)[0]:
            active_sets[row] = np.union1d(core, [specialist]).astype(int)

        output[full_recruit] = self._normalise(
            base[full_recruit]
            + gain * (full_target[full_recruit] - base[full_recruit])
        )
        for row in np.where(full_recruit)[0]:
            active_sets[row] = np.arange(len(model_probabilities))

        spin_rows = full_recruit & oscillation
        output[spin_rows] = self._normalise(
            (1 - self.policy.spin_gain) * output[spin_rows]
            + self.policy.spin_gain
            * ((base[spin_rows] + full_target[spin_rows]) / 2)
        )

        elapsed = perf_counter_ns() - started
        rss_after = process.memory_info().rss
        active_mean = float(np.mean([len(v) for v in active_sets]))

        return ControllerResult(
            probabilities=self._normalise(output),
            active_sets=active_sets,
            protocol=protocol,
            benefit_probability=benefit_probability,
            specialist_recruitment_rate=float(specialist_recruit.mean()),
            full_recruitment_rate=float(full_recruit.mean()),
            oscillation_rate=float(oscillation.mean()),
            spin_activation_rate=float(spin_rows.mean()),
            cost=CostRecord(
                latency_ns=elapsed,
                latency_ms=elapsed / 1e6,
                rss_before_bytes=rss_before,
                rss_after_bytes=rss_after,
                rss_delta_bytes=max(0, rss_after - rss_before),
                active_models_mean=active_mean,
            ),
        )
