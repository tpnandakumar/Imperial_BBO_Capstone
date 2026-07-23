"""Second-stage constrained candidate experiments for F3, F4, F5 and F8."""

from __future__ import annotations

import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, List, Sequence, Tuple

import numpy as np

from PFRAMOS.adapters.imperial_bbo.dataset import Observation, load_history
from PFRAMOS.core.coherence_engine import CoherenceEvidence, signed_coherence
from PFRAMOS.core.terminality_engine import NodeActivity, select_terminal_node
from PFRAMOS.experiments.run_retrospective_candidate_experiments import (
    REPOSITORY_ROOT,
    _fit,
    _normalise,
    _predict,
)


PFRAMOS_ROOT = Path(__file__).resolve().parents[1]
PUBLIC_DIR = PFRAMOS_ROOT / "outputs" / "public" / "experiments"
PRIVATE_DIR = PFRAMOS_ROOT / "outputs" / "private"
RNG = np.random.default_rng(20260724)
TARGETS = {3: 0.25, 4: 0.20, 5: 0.05, 8: 0.12}
BOUNDARY_EPSILON = 0.0001


@dataclass(frozen=True)
class ConstrainedAssessment:
    function: int
    coordinates: Tuple[float, ...]
    predicted_quality: float
    coherence_index: float
    robustness: float
    uncertainty: float
    distance_from_incumbent: float
    terminal_node: str
    terminal_unresolved: bool


def _models(observations: Sequence[Observation]):
    specs = [
        ("linear_light", False, 1e-3),
        ("linear_strong", False, 1e-1),
        ("quadratic_sparse", True, 1e-2),
    ]
    return [
        (name, quadratic, _fit(observations, quadratic, ridge))
        for name, quadratic, ridge in specs
    ]


def _pool(incumbent: np.ndarray, trust_radius: float, count: int = 2000) -> np.ndarray:
    dimension = len(incumbent)
    points = [incumbent]
    for scale in (0.01, 0.025, 0.05, 0.10):
        samples = incumbent + RNG.normal(0.0, scale, size=(count // 4, dimension))
        distances = np.linalg.norm(samples - incumbent, axis=1)
        samples = samples[distances <= trust_radius]
        points.extend(samples)
    values = np.clip(np.asarray(points), BOUNDARY_EPSILON, 1.0 - BOUNDARY_EPSILON)
    return np.unique(np.round(values, 6), axis=0)


def _evaluate(function: int, observations: Sequence[Observation]) -> ConstrainedAssessment:
    incumbent = np.asarray(observations[-1].coordinates, dtype=float)
    models = _models(observations)
    pool = _pool(incumbent, TARGETS[function])
    predictions = np.vstack([
        np.asarray([_predict(coefficients, point, quadratic) for point in pool])
        for _, quadratic, coefficients in models
    ])
    normalised = np.vstack([_normalise(row) for row in predictions])
    quality = np.mean(normalised, axis=0)
    uncertainty = np.std(normalised, axis=0)
    distance = np.linalg.norm(pool - incumbent, axis=1)
    score = quality - 0.35 * uncertainty - 0.10 * (distance / TARGETS[function])
    shortlist = np.argsort(score)[-80:]

    best: ConstrainedAssessment | None = None
    for index in shortlist:
        point = pool[index]
        agreement = 1.0 - min(1.0, float(uncertainty[index]))
        evidence = [
            CoherenceEvidence(
                source_id=name,
                support=agreement,
                conflict=1.0 - agreement,
                confidence=agreement,
                independence=0.75,
                lineage=(name,),
            )
            for name, _, _ in models
        ]
        coherence = signed_coherence(evidence).index

        perturbations = np.clip(
            point + RNG.normal(0.0, 0.0025, size=(96, len(point))),
            BOUNDARY_EPSILON,
            1.0 - BOUNDARY_EPSILON,
        )
        local_scores = []
        for perturbed in perturbations:
            local_scores.append(
                float(np.mean([
                    _predict(coefficients, perturbed, quadratic)
                    for _, quadratic, coefficients in models
                ]))
            )
        local_mean = float(np.mean(local_scores))
        local_sd = float(np.std(local_scores))
        robustness = max(0.0, min(1.0, 1.0 - local_sd / (abs(local_mean) + 1e-12)))
        uncertainty_value = float(uncertainty[index])

        activities = [
            NodeActivity("quality", float(quality[index]), agreement, robustness, max(0.0, coherence), uncertainty_value, 1.0 - robustness, 0.10),
            NodeActivity("coherence", agreement, max(0.0, coherence), robustness, agreement, uncertainty_value, 1.0 - robustness, 0.15),
            NodeActivity("robustness", robustness, robustness, robustness, agreement, uncertainty_value, 1.0 - robustness, 0.10),
            NodeActivity("movement_control", 1.0 - float(distance[index] / TARGETS[function]), agreement, robustness, agreement, uncertainty_value, 1.0 - robustness, 0.10),
        ]
        terminal = select_terminal_node(activities, minimum_supporting_nodes=2, tie_tolerance=0.015)
        assessment = ConstrainedAssessment(
            function=function,
            coordinates=tuple(float(value) for value in point),
            predicted_quality=float(quality[index]),
            coherence_index=float(coherence),
            robustness=robustness,
            uncertainty=uncertainty_value,
            distance_from_incumbent=float(distance[index]),
            terminal_node=terminal.terminal_node_id,
            terminal_unresolved=terminal.unresolved,
        )
        key = (
            assessment.terminal_unresolved,
            -assessment.predicted_quality,
            -assessment.coherence_index,
            -assessment.robustness,
            assessment.uncertainty,
            assessment.distance_from_incumbent,
        )
        if best is None:
            best = assessment
        else:
            best_key = (
                best.terminal_unresolved,
                -best.predicted_quality,
                -best.coherence_index,
                -best.robustness,
                best.uncertainty,
                best.distance_from_incumbent,
            )
            if key < best_key:
                best = assessment

    assert best is not None
    return best


def main() -> None:
    history = load_history(REPOSITORY_ROOT, 1, 11)
    assessments = [_evaluate(function, history[function]) for function in sorted(TARGETS)]

    PUBLIC_DIR.mkdir(parents=True, exist_ok=True)
    PRIVATE_DIR.mkdir(parents=True, exist_ok=True)
    ready = all(
        not item.terminal_unresolved
        and item.coherence_index >= 0.40
        and item.robustness >= 0.95
        and item.distance_from_incumbent <= TARGETS[item.function]
        and all(BOUNDARY_EPSILON <= value <= 1.0 - BOUNDARY_EPSILON for value in item.coordinates)
        for item in assessments
    )

    public = {
        "experiment": "constrained_candidate_experiments_003",
        "functions": [item.function for item in assessments],
        "all_passed": ready,
        "mean_coherence": float(np.mean([item.coherence_index for item in assessments])),
        "mean_robustness": float(np.mean([item.robustness for item in assessments])),
        "mean_uncertainty": float(np.mean([item.uncertainty for item in assessments])),
        "coordinates_withheld": True,
        "results": [
            {
                "function": item.function,
                "predicted_quality": item.predicted_quality,
                "coherence_index": item.coherence_index,
                "robustness": item.robustness,
                "uncertainty": item.uncertainty,
                "distance_from_incumbent": item.distance_from_incumbent,
                "terminal_node": item.terminal_node,
                "terminal_unresolved": item.terminal_unresolved,
            }
            for item in assessments
        ],
    }
    (PUBLIC_DIR / "constrained_candidate_experiments_003.json").write_text(
        json.dumps(public, indent=2), encoding="utf-8"
    )
    (PRIVATE_DIR / "week_12_constrained_candidate_research.json").write_text(
        json.dumps(
            {
                "status": "private_controlled_experiment_not_submitted",
                "assessments": [asdict(item) for item in assessments],
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    print(json.dumps(public, indent=2))
    if not ready:
        raise SystemExit("One or more constrained candidates failed the final gate")


if __name__ == "__main__":
    main()
