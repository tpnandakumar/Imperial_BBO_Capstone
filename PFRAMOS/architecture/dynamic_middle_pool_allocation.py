"""Dynamic middle-pool memory allocation.

The guaranteed half of usable memory preserves the 70/30 principle:
35 percent for high priority and 15 percent for medium and low priority.
The remaining 50 percent is a central dynamic pool allocated by current need,
purpose, dynamic function priority, minimum viable demand, deadline,
dependency pressure and Reference-Aware Retention state.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

from PFRAMOS.architecture.dynamic_function_priority import FunctionPriority
from PFRAMOS.architecture.purpose_priority_memory_distribution import MemoryRequest


@dataclass(frozen=True)
class DynamicPoolRequest:
    request: MemoryRequest
    priority: FunctionPriority
    dependency_pressure: float
    rar_retention_score: float

    def __post_init__(self) -> None:
        for name in ("dependency_pressure", "rar_retention_score"):
            value = getattr(self, name)
            if not 0.0 <= value <= 1.0:
                raise ValueError(f"{name} must be between 0 and 1")

    @property
    def band(self) -> str:
        if self.priority.level >= 10:
            return "high"
        if self.priority.level >= 5:
            return "medium"
        return "low"

    @property
    def dynamic_score(self) -> float:
        request = self.request
        return min(
            1.0,
            0.30 * (self.priority.rank / 1599.0)
            + 0.20 * request.criticality
            + 0.15 * request.expected_value
            + 0.15 * request.deadline_pressure
            + 0.10 * self.dependency_pressure
            + 0.10 * self.rar_retention_score,
        )


@dataclass(frozen=True)
class DynamicPoolGrant:
    request_id: str
    task_id: str
    band: str
    guaranteed_units: float
    dynamic_units: float
    total_units: float
    reclaimable_dynamic_units: float
    state: str


@dataclass(frozen=True)
class DynamicMiddlePoolPlan:
    total_capacity: float
    usable_capacity: float
    high_guarantee_pool: float
    medium_low_guarantee_pool: float
    dynamic_pool: float
    dynamic_pool_used: float
    free_units: float
    grants: Tuple[DynamicPoolGrant, ...]


def _allocate_guarantee(
    requests: Tuple[DynamicPoolRequest, ...],
    pool: float,
) -> dict[str, float]:
    remaining = pool
    grants: dict[str, float] = {}
    ordered = sorted(requests, key=lambda item: item.priority.rank, reverse=True)
    for item in ordered:
        minimum = item.request.minimum_units
        grant = min(remaining, minimum)
        grants[item.request.request_id] = grant
        remaining -= grant
        if remaining <= 0:
            break
    for item in requests:
        grants.setdefault(item.request.request_id, 0.0)
    return grants


def allocate_dynamic_middle_pool(
    requests: Tuple[DynamicPoolRequest, ...],
    total_capacity: float,
    reserve_fraction: float = 0.10,
) -> DynamicMiddlePoolPlan:
    if total_capacity < 0:
        raise ValueError("total_capacity cannot be negative")
    if not 0.0 <= reserve_fraction < 1.0:
        raise ValueError("reserve_fraction must be between 0 and 1")

    usable = total_capacity * (1.0 - reserve_fraction)
    high_pool = usable * 0.35
    medium_low_pool = usable * 0.15
    dynamic_pool = usable * 0.50

    high_requests = tuple(item for item in requests if item.band == "high")
    medium_low_requests = tuple(item for item in requests if item.band != "high")

    guaranteed = _allocate_guarantee(high_requests, high_pool)
    guaranteed.update(_allocate_guarantee(medium_low_requests, medium_low_pool))

    remaining_dynamic = dynamic_pool
    dynamic_grants: dict[str, float] = {item.request.request_id: 0.0 for item in requests}

    ordered = sorted(
        requests,
        key=lambda item: (
            item.dynamic_score,
            item.request.protected_function,
            item.request.active_reference,
            item.priority.rank,
        ),
        reverse=True,
    )

    for item in ordered:
        if remaining_dynamic <= 0:
            break
        request = item.request
        already = guaranteed.get(request.request_id, 0.0)

        if request.queued_only and not request.active_reference:
            target = min(request.minimum_units * 0.25, request.preferred_units * 0.10)
        else:
            target = max(0.0, request.preferred_units - already)

        dynamic_need = min(
            request.maximum_units - already,
            target * item.dynamic_score,
        )
        grant = max(0.0, min(remaining_dynamic, dynamic_need))
        dynamic_grants[request.request_id] = grant
        remaining_dynamic -= grant

    grants = []
    for item in requests:
        request = item.request
        guaranteed_units = guaranteed.get(request.request_id, 0.0)
        dynamic_units = dynamic_grants.get(request.request_id, 0.0)
        total_units = guaranteed_units + dynamic_units

        if total_units >= request.preferred_units * 0.95:
            state = "preferred_grant"
        elif total_units >= request.minimum_units:
            state = "minimum_viable_grant"
        elif total_units > 0:
            state = "partial_grant"
        else:
            state = "deferred"

        grants.append(
            DynamicPoolGrant(
                request_id=request.request_id,
                task_id=request.task_id,
                band=item.band,
                guaranteed_units=guaranteed_units,
                dynamic_units=dynamic_units,
                total_units=total_units,
                reclaimable_dynamic_units=dynamic_units,
                state=state,
            )
        )

    dynamic_used = sum(grant.dynamic_units for grant in grants)
    total_used = sum(grant.total_units for grant in grants)
    return DynamicMiddlePoolPlan(
        total_capacity=total_capacity,
        usable_capacity=usable,
        high_guarantee_pool=high_pool,
        medium_low_guarantee_pool=medium_low_pool,
        dynamic_pool=dynamic_pool,
        dynamic_pool_used=dynamic_used,
        free_units=max(0.0, total_capacity - total_used),
        grants=tuple(grants),
    )
