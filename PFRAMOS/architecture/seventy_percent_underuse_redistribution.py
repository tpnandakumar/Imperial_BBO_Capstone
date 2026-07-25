"""Redistribute underused memory through the common dynamic pool.

When more than half of a pool is unused, the common pool is filled first.
Any remaining unused capacity is divided equally between the high-priority
reserve and the medium-low-priority reserve. Both reserve groups may pull
additional capacity from the common pool when active need, priority and
purpose justify it.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class UnderuseState:
    total_units: float
    used_units: float

    def __post_init__(self) -> None:
        if self.total_units < 0 or self.used_units < 0:
            raise ValueError("memory units cannot be negative")
        if self.used_units > self.total_units:
            raise ValueError("used_units cannot exceed total_units")

    @property
    def unused_units(self) -> float:
        return self.total_units - self.used_units

    @property
    def unused_fraction(self) -> float:
        if self.total_units == 0:
            return 0.0
        return self.unused_units / self.total_units


@dataclass(frozen=True)
class UnderuseRedistribution:
    trigger_met: bool
    unused_units: float
    to_central_pool: float
    to_high_reserve: float
    to_medium_low_reserve: float
    retained_in_origin: float


def redistribute_if_more_than_half_unused(
    state: UnderuseState,
    central_pool_deficit: float = 0.0,
    trigger_fraction: float = 0.50,
) -> UnderuseRedistribution:
    if central_pool_deficit < 0:
        raise ValueError("central_pool_deficit cannot be negative")
    if not 0.0 <= trigger_fraction <= 1.0:
        raise ValueError("trigger_fraction must be between 0 and 1")

    if state.unused_fraction <= trigger_fraction:
        return UnderuseRedistribution(
            trigger_met=False,
            unused_units=state.unused_units,
            to_central_pool=0.0,
            to_high_reserve=0.0,
            to_medium_low_reserve=0.0,
            retained_in_origin=state.unused_units,
        )

    to_central = min(state.unused_units, central_pool_deficit)
    remaining = state.unused_units - to_central
    to_high = remaining / 2.0
    to_medium_low = remaining - to_high

    return UnderuseRedistribution(
        trigger_met=True,
        unused_units=state.unused_units,
        to_central_pool=to_central,
        to_high_reserve=to_high,
        to_medium_low_reserve=to_medium_low,
        retained_in_origin=0.0,
    )


def redistribute_if_seventy_percent_unused(
    state: UnderuseState,
    trigger_fraction: float = 0.50,
) -> UnderuseRedistribution:
    """Backward-compatible alias using the current common-pool-first rule."""
    return redistribute_if_more_than_half_unused(
        state=state,
        central_pool_deficit=state.unused_units * 0.50,
        trigger_fraction=trigger_fraction,
    )


@dataclass(frozen=True)
class CentralPoolPullRequest:
    requester_band: str
    requested_units: float
    minimum_viable_units: float
    active: bool
    purpose_validated: bool
    priority_rank: int

    def __post_init__(self) -> None:
        if self.requester_band not in {"high", "medium_low"}:
            raise ValueError("requester_band must be high or medium_low")
        if self.requested_units < 0 or self.minimum_viable_units < 0:
            raise ValueError("requested memory cannot be negative")
        if self.minimum_viable_units > self.requested_units:
            raise ValueError("minimum_viable_units cannot exceed requested_units")
        if self.priority_rank < 100 or self.priority_rank > 1599:
            raise ValueError("priority_rank must represent P1.00 to P15.99")


@dataclass(frozen=True)
class CentralPoolPullDecision:
    granted_units: float
    remaining_central_units: float
    state: str


def pull_from_central_pool(
    request: CentralPoolPullRequest,
    central_available_units: float,
) -> CentralPoolPullDecision:
    if central_available_units < 0:
        raise ValueError("central_available_units cannot be negative")

    if not request.active or not request.purpose_validated:
        return CentralPoolPullDecision(
            granted_units=0.0,
            remaining_central_units=central_available_units,
            state="deferred",
        )

    priority_fraction = request.priority_rank / 1599.0
    desired = max(
        request.minimum_viable_units,
        request.requested_units * priority_fraction,
    )
    granted = min(central_available_units, desired)

    if granted >= request.requested_units * 0.95:
        state = "preferred_grant"
    elif granted >= request.minimum_viable_units:
        state = "minimum_viable_grant"
    elif granted > 0:
        state = "partial_grant"
    else:
        state = "deferred"

    return CentralPoolPullDecision(
        granted_units=granted,
        remaining_central_units=central_available_units - granted,
        state=state,
    )
