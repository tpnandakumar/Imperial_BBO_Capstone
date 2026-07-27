"""EFAMES: Error-Focused Adaptive Micro-Expert System.

Implements certainty locking, residual error memory, error-risk routing,
progressive micro-expert recruitment, compact rescue and final full rescue.
The controller is fitted on development data only and uses no holdout labels
at inference.
"""

from __future__ import annotations

from dataclasses import dataclass
from time import perf_counter_ns
from typing import Mapping, Sequence
import os

import numpy as np
import psutil
from sklearn.linear_model import LogisticRegression, Ridge
from sklearn.neighbors import NearestNeighbors
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

Array = np.ndarray


@dataclass(frozen=True)
class EFAMESPolicy:
    certainty_confidence: float = 0.92
    certainty_margin: float = 0.55
    certainty_entropy: float = 0.18
    specialist_threshold: float = 0.42
    second_specialist_threshold: float = 0.58
    compact_rescue_threshold: float = 0.70
    full_rescue_threshold: float = 0.84
    memory_neighbours: int = 7
    residual_gain: float = 0.35
    memory_gain: float = 0.20


@dataclass
class EFAMESResult:
    probabilities: Array
    active_sets: list[Array]
    route: Array
    certainty_lock_rate: float
    first_specialist_rate: float
    second_specialist_rate: float
    compact_rescue_rate: float
    full_rescue_rate: float
    memory_match_rate: float
    mean_active_models: float
    latency_ms: float
    rss_delta_bytes: int


class ResidualErrorMemory:
    def __init__(self, n_neighbours: int = 7) -> None:
        self.n_neighbours = n_neighbours
        self.index: NearestNeighbors | None = None
        self.residuals: Array | None = None
        self.specialists: Array | None = None

    def fit(self, vectors: Array, residuals: Array, specialists: Array) -> None:
        if len(vectors) == 0:
            self.index = None
            return
        self.residuals = np.asarray(residuals, dtype=float)
        self.specialists = np.asarray(specialists, dtype=int)
        self.index = NearestNeighbors(
            n_neighbors=min(self.n_neighbours, len(vectors)), metric="cosine"
        )
        self.index.fit(np.asarray(vectors, dtype=float))

    def query(self, vectors: Array) -> tuple[Array, Array, Array]:
        if self.index is None:
            n = len(vectors)
            return np.zeros((n, 0)), np.zeros((n, 0), dtype=int), np.zeros((n, 0), dtype=int)
        distances, neighbours = self.index.kneighbors(vectors)
        return distances, neighbours, self.specialists[neighbours]

    def correction(self, neighbours: Array, distances: Array) -> Array:
        if self.residuals is None or neighbours.shape[1] == 0:
            return np.zeros((len(neighbours), 0))
        weights = 1.0 / np.clip(distances, 1e-6, None)
        weights /= weights.sum(axis=1, keepdims=True)
        return np.sum(weights[:, :, None] * self.residuals[neighbours], axis=1)


class EFAMESController:
    def __init__(self, policy: EFAMESPolicy | None = None) -> None:
        self.policy = policy or EFAMESPolicy()
        self.error_router = None
        self.residual_learner = None
        self.memory = ResidualErrorMemory(self.policy.memory_neighbours)
        self.specialist_order: Array | None = None

    @staticmethod
    def normalise(p: Array) -> Array:
        p = np.clip(np.asarray(p, dtype=float), 1e-12, None)
        return p / p.sum(axis=1, keepdims=True)

    @staticmethod
    def entropy(p: Array) -> Array:
        return -np.sum(p * np.log(np.clip(p, 1e-12, 1)), axis=1) / np.log(p.shape[1])

    def features(self, base: Array, model_probabilities: Sequence[Array]) -> Array:
        ordered = np.sort(base, axis=1)
        predictions = np.stack([p.argmax(axis=1) for p in model_probabilities], axis=1)
        n_classes = base.shape[1]
        counts = np.stack([(predictions == c).sum(axis=1) for c in range(n_classes)], axis=1)
        return np.column_stack([
            ordered[:, -1],
            ordered[:, -1] - ordered[:, -2],
            self.entropy(base),
            counts.max(axis=1) / len(model_probabilities),
            counts / len(model_probabilities),
        ])

    def fit(
        self,
        development_base: Array,
        development_model_probabilities: Sequence[Array],
        y_development: Array,
        classes: Array,
        specialist_predictions: Mapping[int, Array],
    ) -> None:
        features = self.features(development_base, development_model_probabilities)
        base_pred = classes[development_base.argmax(axis=1)]
        error = (base_pred != y_development).astype(int)

        if error.min() != error.max():
            self.error_router = make_pipeline(
                StandardScaler(),
                LogisticRegression(max_iter=600, class_weight="balanced", random_state=0),
            )
            self.error_router.fit(features, error)

        true_column = np.searchsorted(classes, y_development)
        target = np.zeros_like(development_base)
        target[np.arange(len(y_development)), true_column] = 1.0
        residual = target - development_base
        self.residual_learner = make_pipeline(StandardScaler(), Ridge(alpha=2.0))
        self.residual_learner.fit(features, residual)

        specialist_ids = sorted(specialist_predictions)
        gains = []
        best_specialist = np.zeros(len(y_development), dtype=int)
        best_gain = np.full(len(y_development), -np.inf)
        base_true = development_base[np.arange(len(y_development)), true_column]
        for specialist_id in specialist_ids:
            p = specialist_predictions[specialist_id]
            gain = p[np.arange(len(y_development)), true_column] - base_true
            gains.append(float(gain.mean()))
            improved = gain > best_gain
            best_gain[improved] = gain[improved]
            best_specialist[improved] = specialist_id
        self.specialist_order = np.asarray(
            [specialist_ids[i] for i in np.argsort(gains)[::-1]], dtype=int
        )

        rows = np.where(error == 1)[0]
        self.memory.fit(features[rows], residual[rows], best_specialist[rows])

    def predict(
        self,
        base: Array,
        model_probabilities: Sequence[Array],
        selected_indices: Array,
        specialist_predictions: Mapping[int, Array],
        compact_rescue_indices: Array,
        full_rescue: Array,
    ) -> EFAMESResult:
        process = psutil.Process(os.getpid())
        rss_before = process.memory_info().rss
        started = perf_counter_ns()

        features = self.features(base, model_probabilities)
        ordered = np.sort(base, axis=1)
        certainty = (
            (ordered[:, -1] >= self.policy.certainty_confidence)
            & ((ordered[:, -1] - ordered[:, -2]) >= self.policy.certainty_margin)
            & (self.entropy(base) <= self.policy.certainty_entropy)
        )
        risk = np.zeros(len(base)) if self.error_router is None else self.error_router.predict_proba(features)[:, 1]
        residual = np.zeros_like(base) if self.residual_learner is None else self.residual_learner.predict(features)
        distances, neighbours, memory_specialists = self.memory.query(features)
        memory_residual = self.memory.correction(neighbours, distances)
        memory_match = np.zeros(len(base), dtype=bool) if distances.shape[1] == 0 else distances.mean(axis=1) < 0.20

        first = (~certainty) & (risk >= self.policy.specialist_threshold)
        second = (~certainty) & (risk >= self.policy.second_specialist_threshold)
        compact = (~certainty) & (risk >= self.policy.compact_rescue_threshold)
        full = (~certainty) & (risk >= self.policy.full_rescue_threshold)

        output = base.copy()
        active_sets = [np.asarray(selected_indices, dtype=int).copy() for _ in range(len(base))]
        route = np.full(len(base), "core", dtype=object)
        route[certainty] = "certainty_lock"

        for row in np.where(first)[0]:
            specialist_id = int(memory_specialists[row, 0]) if memory_match[row] and memory_specialists.shape[1] else int(self.specialist_order[0])
            memory_term = self.policy.memory_gain * memory_residual[row] if memory_residual.shape[1] else 0
            output[row] = self.normalise((
                0.72 * output[row]
                + 0.18 * specialist_predictions[specialist_id][row]
                + self.policy.residual_gain * residual[row]
                + memory_term
            )[None, :])[0]
            active_sets[row] = np.union1d(active_sets[row], [specialist_id]).astype(int)
            route[row] = "micro_expert_1"

        for row in np.where(second & ~compact)[0]:
            specialist_id = int(self.specialist_order[min(1, len(self.specialist_order)-1)])
            output[row] = self.normalise((0.80 * output[row] + 0.20 * specialist_predictions[specialist_id][row])[None, :])[0]
            active_sets[row] = np.union1d(active_sets[row], [specialist_id]).astype(int)
            route[row] = "micro_expert_2"

        compact_prediction = self.normalise(np.mean([model_probabilities[m] for m in compact_rescue_indices], axis=0))
        output[compact] = compact_prediction[compact]
        for row in np.where(compact)[0]:
            active_sets[row] = np.asarray(compact_rescue_indices, dtype=int)
            route[row] = "compact_rescue"

        output[full] = full_rescue[full]
        for row in np.where(full)[0]:
            active_sets[row] = np.arange(len(model_probabilities))
            route[row] = "full_rescue"

        elapsed = perf_counter_ns() - started
        rss_after = process.memory_info().rss
        return EFAMESResult(
            probabilities=self.normalise(output),
            active_sets=active_sets,
            route=route,
            certainty_lock_rate=float(certainty.mean()),
            first_specialist_rate=float(first.mean()),
            second_specialist_rate=float((second & ~compact).mean()),
            compact_rescue_rate=float(compact.mean()),
            full_rescue_rate=float(full.mean()),
            memory_match_rate=float(memory_match.mean()),
            mean_active_models=float(np.mean([len(x) for x in active_sets])),
            latency_ms=elapsed / 1e6,
            rss_delta_bytes=max(0, rss_after - rss_before),
        )
