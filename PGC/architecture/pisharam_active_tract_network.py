"""Active high-speed network formation for Pisharam Computational Tracts.

Pisharam Computational Tracts are not passive fixed links. Eligible tracts may
assemble into a temporary high-speed task network, exchange information through
coherence junctions, and dissolve when the task is complete or no longer
justifies the allocated resources.

This module defines configuration and selection logic only. It does not claim
measured speed, energy or cognitive gains until those are experimentally
validated.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Tuple


@dataclass(frozen=True)
class TractCandidate:
    tract_id: str
    source_domain: str
    target_domain: str
    task_relevance: float
    evidence_validity: float
    coherence: float
    robustness: float
    uncertainty: float
    estimated_latency: float
    estimated_cost: float
    estimated_energy: float
    available_capacity: float
    hard_block: bool = False


@dataclass(frozen=True)
class ActiveTract:
    tract_id: str
    source_domain: str
    target_domain: str
    activation_score: float
    bandwidth_share: float
    priority_class: str


@dataclass(frozen=True)
class ActiveTractNetwork:
    network_id: str
    task_id: str
    active_tracts: Tuple[ActiveTract, ...]
    temporary_terminal_node: str | None
    estimated_network_latency: float
    estimated_network_cost: float
    estimated_network_energy: float
    laminarity_score: float
    state: str


def _bounded(value: float, name: str) -> float:
    if not 0.0 <= value <= 1.0:
        raise ValueError(f"{name} must be within [0, 1]")
    return value


def activation_score(tract: TractCandidate) -> float:
    if tract.hard_block:
        return float("-inf")

    relevance = _bounded(tract.task_relevance, "task_relevance")
    evidence = _bounded(tract.evidence_validity, "evidence_validity")
    coherence = _bounded(tract.coherence, "coherence")
    robustness = _bounded(tract.robustness, "robustness")
    uncertainty = _bounded(tract.uncertainty, "uncertainty")
    latency = _bounded(tract.estimated_latency, "estimated_latency")
    cost = _bounded(tract.estimated_cost, "estimated_cost")
    energy = _bounded(tract.estimated_energy, "estimated_energy")
    capacity = _bounded(tract.available_capacity, "available_capacity")

    quality_gate = min(relevance, evidence, coherence, robustness)
    if quality_gate < 0.50 or uncertainty > 0.60:
        return float("-inf")

    return (
        0.24 * relevance
        + 0.20 * evidence
        + 0.18 * coherence
        + 0.14 * robustness
        + 0.10 * (1.0 - uncertainty)
        + 0.06 * capacity
        + 0.04 * (1.0 - latency)
        + 0.02 * (1.0 - cost)
        + 0.02 * (1.0 - energy)
    )


def _priority_class(score_value: float) -> str:
    if score_value >= 0.85:
        return "high_speed_core"
    if score_value >= 0.72:
        return "active_support"
    return "reserve_support"


def _normalised_bandwidth(scores: Tuple[float, ...]) -> Tuple[float, ...]:
    total = sum(scores)
    if total <= 0.0:
        return tuple(0.0 for _ in scores)
    return tuple(value / total for value in scores)


def _laminarity(active: Tuple[ActiveTract, ...], candidates: Tuple[TractCandidate, ...]) -> float:
    if not active:
        return 0.0
    by_id = {candidate.tract_id: candidate for candidate in candidates}
    coherence_mean = sum(by_id[item.tract_id].coherence for item in active) / len(active)
    uncertainty_mean = sum(by_id[item.tract_id].uncertainty for item in active) / len(active)
    duplication_penalty = max(0.0, (len(active) - len({(item.source_domain, item.target_domain) for item in active})) / len(active))
    return max(0.0, min(1.0, coherence_mean * (1.0 - uncertainty_mean) * (1.0 - duplication_penalty)))


def form_active_network(
    task_id: str,
    candidates: Iterable[TractCandidate],
    *,
    minimum_activation_score: float = 0.68,
    maximum_active_tracts: int = 8,
) -> ActiveTractNetwork:
    candidate_tuple = tuple(candidates)
    if maximum_active_tracts < 1:
        raise ValueError("maximum_active_tracts must be at least 1")

    scored = tuple(
        (candidate, activation_score(candidate))
        for candidate in candidate_tuple
    )
    eligible = tuple(
        (candidate, score_value)
        for candidate, score_value in scored
        if score_value != float("-inf") and score_value >= minimum_activation_score
    )
    ranked = tuple(sorted(eligible, key=lambda item: item[1], reverse=True)[:maximum_active_tracts])

    if not ranked:
        return ActiveTractNetwork(
            network_id=f"pctn:{task_id}",
            task_id=task_id,
            active_tracts=(),
            temporary_terminal_node=None,
            estimated_network_latency=0.0,
            estimated_network_cost=0.0,
            estimated_network_energy=0.0,
            laminarity_score=0.0,
            state="abstained_no_valid_tract_network",
        )

    bandwidth = _normalised_bandwidth(tuple(score_value for _, score_value in ranked))
    active = tuple(
        ActiveTract(
            tract_id=candidate.tract_id,
            source_domain=candidate.source_domain,
            target_domain=candidate.target_domain,
            activation_score=score_value,
            bandwidth_share=bandwidth[index],
            priority_class=_priority_class(score_value),
        )
        for index, (candidate, score_value) in enumerate(ranked)
    )

    candidate_by_id = {candidate.tract_id: candidate for candidate in candidate_tuple}
    latency = sum(candidate_by_id[item.tract_id].estimated_latency * item.bandwidth_share for item in active)
    cost = sum(candidate_by_id[item.tract_id].estimated_cost * item.bandwidth_share for item in active)
    energy = sum(candidate_by_id[item.tract_id].estimated_energy * item.bandwidth_share for item in active)
    terminal_node = ranked[0][0].target_domain

    return ActiveTractNetwork(
        network_id=f"pctn:{task_id}",
        task_id=task_id,
        active_tracts=active,
        temporary_terminal_node=terminal_node,
        estimated_network_latency=latency,
        estimated_network_cost=cost,
        estimated_network_energy=energy,
        laminarity_score=_laminarity(active, candidate_tuple),
        state="active_high_speed_network",
    )


def dissolve_network(network: ActiveTractNetwork) -> ActiveTractNetwork:
    return ActiveTractNetwork(
        network_id=network.network_id,
        task_id=network.task_id,
        active_tracts=(),
        temporary_terminal_node=None,
        estimated_network_latency=0.0,
        estimated_network_cost=0.0,
        estimated_network_energy=0.0,
        laminarity_score=0.0,
        state="dissolved_resources_returned",
    )
