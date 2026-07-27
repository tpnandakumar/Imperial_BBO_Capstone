"""Seventy-thirty memory allocation across dynamic priority bands.

Seventy percent of usable memory is reserved for high-priority functions.
Thirty percent is reserved for medium and low-priority functions together.
Unused capacity may be borrowed across pools, but borrowed capacity remains
reclaimable when higher-priority demand returns.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

from PFRAMOS.architecture.dynamic_function_priority import FunctionPriority
from PFRAMOS.architecture.purpose_priority_memory_distribution import MemoryRequest


@dataclass(frozen=True)
class PriorityBandRequest:
    request: MemoryRequest
    priority: FunctionPriority

    @property
    def band(self) -> str:
        if self.priority.level >= 10:
            return "high"
        if self.priority.level >= 5:
            return "medium"
        return "low"


@dataclass(frozen=True)
class BandGrant:
    request_id: str
    task_id: str
    band: str
    priority: FunctionPriority
    granted_units: float
    borrowed_units: float
    state: str


@dataclass(frozen=True)
class Priority7030Plan:
    total_capacity: float
    usable_capacity: float
    high_pool: float
    medium_low_pool: float
    high_used: float
    medium_low_used: float
    borrowed_to_high: float
    borrowed_to_medium_low: float
    free_units: float
    grants: Tuple[BandGrant, ...]


def _allocate_within_pool(
    requests: Tuple[PriorityBandRequest, ...],
    pool: float,
) -> Tuple[Tuple[BandGrant, ...], float]:
    remaining = pool
    grants = []

    ordered = sorted(
        requests,
        key=lambda item: (
            item.priority.rank,
            item.request.protected_function,
            item.request.active_reference,
            item.request.deadline_pressure,
            item.request.expected_value,
        ),
        reverse=True,
    )

    for item in ordered:
        request = item.request
        if remaining <= 0:
            grant = 0.0
            state = "deferred"
        elif request.queued_only and not request.active_reference:
            reservation = min(request.minimum_units, request.preferred_units * 0.25)
            grant = min(remaining, reservation)
            state = "reserved" if grant > 0 else "deferred"
        else:
            minimum = min(remaining, request.minimum_units)
            remaining_after_minimum = remaining - minimum
            extra_need = max(0.0, request.preferred_units - request.minimum_units)
            priority_fraction = item.priority.rank / 1599.0
            extra = min(remaining_after_minimum, extra_need * priority_fraction)
            grant = min(request.maximum_units, minimum + extra)
            if grant >= request.preferred_units * 0.95:
                state = "preferred_grant"
            elif grant >= request.minimum_units:
                state = "minimum_viable_grant"
            elif grant > 0:
                state = "partial_grant"
            else:
                state = "deferred"

        remaining -= grant
        grants.append(
            BandGrant(
                request_id=request.request_id,
                task_id=request.task_id,
                band=item.band,
                priority=item.priority,
                granted_units=grant,
                borrowed_units=0.0,
                state=state,
            )
        )

    return tuple(grants), remaining


def allocate_70_30(
    requests: Tuple[PriorityBandRequest, ...],
    total_capacity: float,
    reserve_fraction: float = 0.10,
    allow_borrowing: bool = True,
) -> Priority7030Plan:
    if total_capacity < 0:
        raise ValueError("total_capacity cannot be negative")
    if not 0.0 <= reserve_fraction < 1.0:
        raise ValueError("reserve_fraction must be between 0 and 1")

    usable = total_capacity * (1.0 - reserve_fraction)
    high_pool = usable * 0.70
    medium_low_pool = usable * 0.30

    high_requests = tuple(item for item in requests if item.band == "high")
    medium_low_requests = tuple(item for item in requests if item.band != "high")

    high_grants, high_remaining = _allocate_within_pool(high_requests, high_pool)
    medium_low_grants, medium_low_remaining = _allocate_within_pool(
        medium_low_requests,
        medium_low_pool,
    )

    borrowed_to_high = 0.0
    borrowed_to_medium_low = 0.0

    if allow_borrowing and high_remaining > 0 and medium_low_requests:
        underfunded = tuple(
            item
            for item in medium_low_requests
            if next(
                grant for grant in medium_low_grants if grant.request_id == item.request.request_id
            ).granted_units < item.request.preferred_units
        )
        if underfunded:
            extra_grants, extra_remaining = _allocate_within_pool(underfunded, high_remaining)
            extra_map = {grant.request_id: grant.granted_units for grant in extra_grants}
            updated = []
            for grant in medium_low_grants:
                extra = extra_map.get(grant.request_id, 0.0)
                updated.append(
                    BandGrant(
                        request_id=grant.request_id,
                        task_id=grant.task_id,
                        band=grant.band,
                        priority=grant.priority,
                        granted_units=grant.granted_units + extra,
                        borrowed_units=extra,
                        state="borrowed_capacity" if extra > 0 else grant.state,
                    )
                )
            borrowed_to_medium_low = high_remaining - extra_remaining
            high_remaining = extra_remaining
            medium_low_grants = tuple(updated)

    if allow_borrowing and medium_low_remaining > 0 and high_requests:
        underfunded = tuple(
            item
            for item in high_requests
            if next(
                grant for grant in high_grants if grant.request_id == item.request.request_id
            ).granted_units < item.request.preferred_units
        )
        if underfunded:
            extra_grants, extra_remaining = _allocate_within_pool(
                underfunded,
                medium_low_remaining,
            )
            extra_map = {grant.request_id: grant.granted_units for grant in extra_grants}
            updated = []
            for grant in high_grants:
                extra = extra_map.get(grant.request_id, 0.0)
                updated.append(
                    BandGrant(
                        request_id=grant.request_id,
                        task_id=grant.task_id,
                        band=grant.band,
                        priority=grant.priority,
                        granted_units=grant.granted_units + extra,
                        borrowed_units=extra,
                        state="borrowed_capacity" if extra > 0 else grant.state,
                    )
                )
            borrowed_to_high = medium_low_remaining - extra_remaining
            medium_low_remaining = extra_remaining
            high_grants = tuple(updated)

    grants = high_grants + medium_low_grants
    high_used = sum(grant.granted_units for grant in high_grants)
    medium_low_used = sum(grant.granted_units for grant in medium_low_grants)
    free_units = max(0.0, total_capacity - high_used - medium_low_used)

    return Priority7030Plan(
        total_capacity=total_capacity,
        usable_capacity=usable,
        high_pool=high_pool,
        medium_low_pool=medium_low_pool,
        high_used=high_used,
        medium_low_used=medium_low_used,
        borrowed_to_high=borrowed_to_high,
        borrowed_to_medium_low=borrowed_to_medium_low,
        free_units=free_units,
        grants=grants,
    )
