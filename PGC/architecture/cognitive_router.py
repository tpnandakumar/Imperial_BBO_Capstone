"""Evidence-aware cognitive router for PGC.

The router ranks candidate configurations. It does not execute models or apply
parameter updates. Scores must be derived from recorded evidence, not invented
performance values.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Tuple


@dataclass(frozen=True)
class CandidateConfiguration:
    candidate_id: str
    task_fitness: float
    evidence_validity: float
    coherence: float
    robustness: float
    uncertainty: float
    safety: float
    efficiency: float
    hard_block: bool = False


@dataclass(frozen=True)
class RoutingDecision:
    selected_candidate_id: str | None
    selected_score: float | None
    ranked_candidate_ids: Tuple[str, ...]
    abstained: bool
    reason: str


def _bounded(value: float, name: str) -> float:
    if not 0.0 <= value <= 1.0:
        raise ValueError(f"{name} must be within [0, 1]")
    return value


def score(candidate: CandidateConfiguration) -> float:
    if candidate.hard_block:
        return float("-inf")

    fitness = _bounded(candidate.task_fitness, "task_fitness")
    evidence = _bounded(candidate.evidence_validity, "evidence_validity")
    coherence = _bounded(candidate.coherence, "coherence")
    robustness = _bounded(candidate.robustness, "robustness")
    uncertainty = _bounded(candidate.uncertainty, "uncertainty")
    safety = _bounded(candidate.safety, "safety")
    efficiency = _bounded(candidate.efficiency, "efficiency")

    quality_gate = min(fitness, evidence, safety)
    if quality_gate < 0.50:
        return float("-inf")

    return (
        0.24 * fitness
        + 0.22 * evidence
        + 0.18 * coherence
        + 0.14 * robustness
        + 0.12 * (1.0 - uncertainty)
        + 0.07 * safety
        + 0.03 * efficiency
    )


def route(
    candidates: Iterable[CandidateConfiguration],
    minimum_score: float = 0.60,
) -> RoutingDecision:
    candidate_list = tuple(candidates)
    if not candidate_list:
        return RoutingDecision(None, None, (), True, "no_candidate_configuration")

    scored = tuple((candidate, score(candidate)) for candidate in candidate_list)
    ranked = tuple(
        candidate.candidate_id
        for candidate, candidate_score in sorted(
            scored,
            key=lambda item: item[1],
            reverse=True,
        )
        if candidate_score != float("-inf")
    )

    eligible = tuple(
        (candidate, candidate_score)
        for candidate, candidate_score in scored
        if candidate_score != float("-inf") and candidate_score >= minimum_score
    )
    if not eligible:
        return RoutingDecision(None, None, ranked, True, "no_candidate_passed_quality_and_score_gates")

    selected, selected_score = max(eligible, key=lambda item: item[1])
    return RoutingDecision(
        selected_candidate_id=selected.candidate_id,
        selected_score=selected_score,
        ranked_candidate_ids=ranked,
        abstained=False,
        reason="strongest_validated_configuration",
    )
