"""Purpose and priority aware memory distribution for PCECE and DMACCE.

The allocator prevents memory hogging by assigning memory according to
minimum viable need, task purpose, criticality, expected value, deadline,
recomputation cost and active reference state. Queued work receives only a
reservation unless its priority justifies promotion. Memory is reclaimed when
a task completes or its references expire.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple


def _clip(value: float) -> float:
    return max(0.0, min(1.0, value))


@dataclass(frozen=True)
class MemoryRequest:
    request_id: str
    task_id: str
    purpose: str
    minimum_units: float
    preferred_units: float
    maximum_units: float
    criticality: float
    expected_value: float
    deadline_pressure: float
    recomputation_cost: float
    active_reference: bool
    queued_only: bool
    protected_function: bool = False

    def __post_init__(self) -> None:
        if not self.purpose.strip():
            raise ValueError("purpose is required")
        if self.minimum_units < 0:
            raise ValueError("minimum_units cannot be negative")
        if not self.minimum_units <= self.preferred_units <= self.maximum_units:
            raise ValueError("memory units must satisfy minimum <= preferred <= maximum")
        for name in (
            "criticality",
            "expected_value",
            "deadline_pressure",
            "recomputation_cost",
        ):
            value = getattr(self, name)
            if not 0.0 <= value <= 1.0:
                raise ValueError(f"{name} must be between 0 and 1")

    @property
    def priority_score(self) -> float:
        protected_bonus = 0.15 if self.protected_function else 0.0
        active_bonus = 0.10 if self.active_reference else 0.0
        queue_penalty = 0.20 if self.queued_only and not self.active_reference else 0.0
        return _clip(
            0.35 * self.criticality
            + 0.25 * self.expected_value
            + 0.20 * self.deadline_pressure
            + 0.10 * self.recomputation_cost
            + protected_bonus
            + active_bonus
            - queue_penalty
        )


@dataclass(frozen=True)
class MemoryGrant:
    request_id: str
    task_id: str
    purpose: str
    granted_units: float
    state: str
    priority_score: float
    reclaim_on_completion: bool
    rationale: Tuple[str, ...]


@dataclass(frozen=True)
class MemoryDistributionPlan:
    total_capacity: float
    granted_units: float
    free_units: float
    grants: Tuple[MemoryGrant, ...]


def distribute_memory(
    requests: Tuple[MemoryRequest, ...],
    total_capacity: float,
    reserve_fraction: float = 0.10,
) -> MemoryDistributionPlan:
    if total_capacity < 0:
        raise ValueError("total_capacity cannot be negative")
    if not 0.0 <= reserve_fraction < 1.0:
        raise ValueError("reserve_fraction must be between 0 and 1")

    usable_capacity = total_capacity * (1.0 - reserve_fraction)
    remaining = usable_capacity
    grants = []

    ordered = sorted(
        requests,
        key=lambda request: (
            request.protected_function,
            request.active_reference,
            request.priority_score,
            request.deadline_pressure,
        ),
        reverse=True,
    )

    for request in ordered:
        reasons = [f"purpose:{request.purpose}"]

        if remaining <= 0:
            grant = 0.0
            state = "deferred"
            reasons.append("capacity_exhausted")
        elif request.queued_only and not request.active_reference:
            reservation = min(request.minimum_units, request.preferred_units * 0.25)
            grant = min(remaining, reservation)
            state = "reserved" if grant > 0 else "deferred"
            reasons.append("queued_request_limited_to_reservation")
        else:
            minimum_grant = min(remaining, request.minimum_units)
            remaining_after_minimum = remaining - minimum_grant

            demand_above_minimum = request.preferred_units - request.minimum_units
            priority_fraction = request.priority_score
            adaptive_extra = min(
                remaining_after_minimum,
                demand_above_minimum * priority_fraction,
            )
            grant = minimum_grant + adaptive_extra

            if request.protected_function and grant < request.minimum_units:
                state = "critical_underprovisioned"
                reasons.append("protected_minimum_not_met")
            elif grant >= request.preferred_units * 0.95:
                state = "preferred_grant"
            elif grant >= request.minimum_units:
                state = "minimum_viable_grant"
                reasons.append("shared_capacity_preserved")
            elif grant > 0:
                state = "partial_grant"
                reasons.append("minimum_not_met")
            else:
                state = "deferred"

        grant = min(grant, request.maximum_units)
        remaining -= grant
        grants.append(
            MemoryGrant(
                request_id=request.request_id,
                task_id=request.task_id,
                purpose=request.purpose,
                granted_units=grant,
                state=state,
                priority_score=request.priority_score,
                reclaim_on_completion=True,
                rationale=tuple(reasons),
            )
        )

    granted_units = sum(grant.granted_units for grant in grants)
    free_units = max(0.0, total_capacity - granted_units)
    return MemoryDistributionPlan(
        total_capacity=total_capacity,
        granted_units=granted_units,
        free_units=free_units,
        grants=tuple(grants),
    )


def reclaim_completed_memory(
    grants: Tuple[MemoryGrant, ...],
    completed_task_ids: Tuple[str, ...],
) -> Tuple[MemoryGrant, ...]:
    completed = set(completed_task_ids)
    reclaimed = []
    for grant in grants:
        if grant.task_id in completed and grant.reclaim_on_completion:
            reclaimed.append(
                MemoryGrant(
                    request_id=grant.request_id,
                    task_id=grant.task_id,
                    purpose=grant.purpose,
                    granted_units=0.0,
                    state="reclaimed",
                    priority_score=grant.priority_score,
                    reclaim_on_completion=False,
                    rationale=grant.rationale + ("task_completed", "memory_reclaimed"),
                )
            )
        else:
            reclaimed.append(grant)
    return tuple(reclaimed)
