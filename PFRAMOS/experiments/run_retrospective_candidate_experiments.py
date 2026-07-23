"""Retrospective pathway construction and controlled Week 12 experiments.

This script uses only the validated canonical Weeks 1 to 11 history. It creates
private candidate research outputs and public aggregate validation outputs.
It does not submit any candidate.
"""

from __future__ import annotations

import csv
import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Mapping, Sequence, Tuple

import numpy as np

from PFRAMOS.adapters.imperial_bbo.dataset import Observation, load_history
from PFRAMOS.core.coherence_engine import CoherenceEvidence, signed_coherence
from PFRAMOS.core.quality_energy_scheduler import ExecutionOption, select_quality_first
from PFRAMOS.core.terminality_engine import NodeActivity, select_terminal_node


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
PFRAMOS_ROOT = Path(__file__).resolve().parents[1]
PUBLIC_DIR = PFRAMOS_ROOT / "outputs" / "public" / "experiments"
PRIVATE_DIR = PFRAMOS_ROOT / "outputs" / "private"
RNG = np.random.default_rng(20260723)


@dataclass(frozen=True)
class CandidateAssessment:
    function: int
    coordinates: Tuple[float, ...]
    predicted_quality: float
    coherence_index: float
    robustness: float
    uncertainty: float
    terminal_node: str
    terminal_unresolved: bool
    source: str


def _features(x: np.ndarray, quadratic: bool) -> np.ndarray:
    if quadratic:
        return np.concatenate(([1.0], x, x * x))
    return np.concatenate(([1.0], x))


def _fit(observations: Sequence[Observation], quadratic: bool, ridge: float) -> np.ndarray:
    design = np.vstack([
        _features(np.asarray(item.coordinates, dtype=float), quadratic)
        for item in observations
    ])
    target = np.asarray([float(item.output) for item in observations], dtype=float)
    penalty = np.eye(design.shape[1]) * ridge
    penalty[0, 0] = 0.0
    return np.linalg.pinv(design.T @ design + penalty) @ design.T @ target


def _predict(coefficients: np.ndarray, x: np.ndarray, quadratic: bool) -> float:
    return float(_features(x, quadratic) @ coefficients)


def _candidate_pool(observations: Sequence[Observation], count: int = 600) -> np.ndarray:
    points = np.asarray([item.coordinates for item in observations], dtype=float)
    outputs = np.asarray([float(item.output) for item in observations], dtype=float)
    best = points[int(np.argmax(outputs))]
    dimension = points.shape[1]

    scales = (0.0025, 0.005, 0.01, 0.02, 0.04)
    generated = [best]
    for scale in scales:
        samples = best + RNG.normal(0.0, scale, size=(max(1, count // len(scales)), dimension))
        generated.extend(np.clip(samples, 0.0, 1.0))

    generated.extend(points)
    rounded = np.round(np.asarray(generated, dtype=float), 6)
    return np.unique(rounded, axis=0)


def _normalise(values: np.ndarray) -> np.ndarray:
    minimum = float(np.min(values))
    maximum = float(np.max(values))
    if math.isclose(minimum, maximum):
        return np.ones_like(values)
    return (values - minimum) / (maximum - minimum)


def _assess_function(function: int, observations: Sequence[Observation]) -> CandidateAssessment:
    models = [
        ("linear_light", False, 1e-3),
        ("linear_strong", False, 1e-1),
        ("quadratic_sparse", True, 1e-2),
    ]
    fitted = [(name, quadratic, _fit(observations, quadratic, ridge)) for name, quadratic, ridge in models]
    pool = _candidate_pool(observations)

    prediction_matrix = np.vstack([
        np.asarray([_predict(coefficients, point, quadratic) for point in pool])
        for _, quadratic, coefficients in fitted
    ])
    normalised = np.vstack([_normalise(row) for row in prediction_matrix])
    consensus_quality = np.mean(normalised, axis=0)
    model_uncertainty = np.std(normalised, axis=0)

    shortlist = np.argsort(consensus_quality - 0.35 * model_uncertainty)[-40:]
    best_assessment: CandidateAssessment | None = None

    for index in shortlist:
        point = pool[index]
        predictions = prediction_matrix[:, index]
        centred = predictions - np.mean(predictions)
        agreement = 1.0 - min(1.0, float(np.std(normalised[:, index])))
        evidence = [
            CoherenceEvidence(
                source_id=name,
                support=agreement,
                conflict=1.0 - agreement,
                confidence=max(0.0, 1.0 - float(model_uncertainty[index])),
                independence=0.75,
                lineage=(name,),
            )
            for name, _, _ in fitted
        ]
        coherence = signed_coherence(evidence).index

        perturbations = np.clip(
            point + RNG.normal(0.0, 0.003, size=(64, len(point))),
            0.0,
            1.0,
        )
        perturbation_scores = []
        for perturbed in perturbations:
            local = [
                _predict(coefficients, perturbed, quadratic)
                for _, quadratic, coefficients in fitted
            ]
            perturbation_scores.append(float(np.mean(local)))
        local_mean = float(np.mean(perturbation_scores))
        local_sd = float(np.std(perturbation_scores))
        scale = abs(local_mean) + 1e-12
        robustness = max(0.0, min(1.0, 1.0 - local_sd / scale))
        uncertainty = max(0.0, min(1.0, float(model_uncertainty[index])))

        activities = [
            NodeActivity("quality", float(consensus_quality[index]), agreement, robustness, max(0.0, coherence), uncertainty, 1.0 - robustness, 0.10),
            NodeActivity("coherence", agreement, max(0.0, coherence), robustness, agreement, uncertainty, 1.0 - robustness, 0.15),
            NodeActivity("robustness", robustness, robustness, robustness, agreement, uncertainty, 1.0 - robustness, 0.10),
            NodeActivity("uncertainty_control", 1.0 - uncertainty, agreement, robustness, agreement, uncertainty, 1.0 - robustness, 0.10),
        ]
        terminal = select_terminal_node(activities, minimum_supporting_nodes=2, tie_tolerance=0.015)

        assessment = CandidateAssessment(
            function=function,
            coordinates=tuple(float(value) for value in point),
            predicted_quality=float(consensus_quality[index]),
            coherence_index=float(coherence),
            robustness=robustness,
            uncertainty=uncertainty,
            terminal_node=terminal.terminal_node_id,
            terminal_unresolved=terminal.unresolved,
            source="model-consensus local perturbation experiment",
        )

        if best_assessment is None:
            best_assessment = assessment
            continue

        current_key = (
            assessment.terminal_unresolved,
            -assessment.predicted_quality,
            -assessment.coherence_index,
            -assessment.robustness,
            assessment.uncertainty,
        )
        best_key = (
            best_assessment.terminal_unresolved,
            -best_assessment.predicted_quality,
            -best_assessment.coherence_index,
            -best_assessment.robustness,
            best_assessment.uncertainty,
        )
        if current_key < best_key:
            best_assessment = assessment

    assert best_assessment is not None
    return best_assessment


def main() -> None:
    history = load_history(REPOSITORY_ROOT, 1, 11)
    PUBLIC_DIR.mkdir(parents=True, exist_ok=True)
    PRIVATE_DIR.mkdir(parents=True, exist_ok=True)

    assessments = [
        _assess_function(function, observations)
        for function, observations in sorted(history.items())
    ]

    public_summary = {
        "experiment": "retrospective_candidate_experiments_002",
        "functions_assessed": len(assessments),
        "resolved_terminal_count": sum(not item.terminal_unresolved for item in assessments),
        "mean_coherence": float(np.mean([item.coherence_index for item in assessments])),
        "mean_robustness": float(np.mean([item.robustness for item in assessments])),
        "mean_uncertainty": float(np.mean([item.uncertainty for item in assessments])),
        "candidate_coordinates_withheld_from_public_artifacts": True,
        "ready_for_human_review": all(
            not item.terminal_unresolved
            and item.coherence_index >= 0.40
            and item.robustness >= 0.70
            for item in assessments
        ),
        "functions": [
            {
                "function": item.function,
                "predicted_quality": item.predicted_quality,
                "coherence_index": item.coherence_index,
                "robustness": item.robustness,
                "uncertainty": item.uncertainty,
                "terminal_node": item.terminal_node,
                "terminal_unresolved": item.terminal_unresolved,
            }
            for item in assessments
        ],
    }
    (PUBLIC_DIR / "retrospective_candidate_experiments_002.json").write_text(
        json.dumps(public_summary, indent=2), encoding="utf-8"
    )

    private_payload = {
        "status": "controlled_experiment_only_not_submitted",
        "assessments": [asdict(item) for item in assessments],
    }
    (PRIVATE_DIR / "week_12_candidate_research.json").write_text(
        json.dumps(private_payload, indent=2), encoding="utf-8"
    )

    print(json.dumps(public_summary, indent=2))
    if not public_summary["ready_for_human_review"]:
        raise SystemExit("Candidate experiment completed, but one or more functions remain below the review gate")


if __name__ == "__main__":
    main()
