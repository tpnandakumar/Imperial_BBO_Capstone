"""Return unused working memory to the central dynamic pool.

All active memory allocations are reclaimable. When no active, queued,
dependent, or justified anticipated computation references an allocation, its
working-memory capacity is returned to the central 50 percent dynamic pool.
Persistent information may survive through checkpointing or durable storage,
but it does not retain resident working memory merely because it is persistent.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class ReclaimableMemoryState:
    allocation_id: str
    allocated_units: float
    active_reference_count: int
    queued_reference_count: int
    dependent_reference_count: int
    anticipated_reference_count: int
    anticipated_reference_justified: bool
    checkpoint_required: bool
    checkpoint_complete: bool
    computation_complete: bool

    def __post_init__(self) -> None:
        if self.allocated_units < 0:
            raise ValueError("allocated_units cannot be negative")
        for name in (
            "active_reference_count",
            "queued_reference_count",
            "dependent_reference_count",
            "anticipated_reference_count",
        ):
            if getattr(self, name) < 0:
                raise ValueError(f"{name} cannot be negative")

    @property
    def live_reference_count(self) -> int:
        return (
            self.active_reference_count
            + self.queued_reference_count
            + self.dependent_reference_count
        )

    @property
    def anticipated_reference_blocks_reclaim(self) -> bool:
        return (
            self.anticipated_reference_count > 0
            and self.anticipated_reference_justified
        )

    @property
    def checkpoint_safe(self) -> bool:
        return not self.checkpoint_required or self.checkpoint_complete

    @property
    def reclaimable(self) -> bool:
        return (
            self.live_reference_count == 0
            and not self.anticipated_reference_blocks_reclaim
            and self.checkpoint_safe
        )


@dataclass(frozen=True)
class MiddlePoolReturnDecision:
    allocation_id: str
    action: str
    returned_units: float
    remaining_allocated_units: float
    target_pool: str
    rationale: Tuple[str, ...]


def decide_middle_pool_return(
    state: ReclaimableMemoryState,
) -> MiddlePoolReturnDecision:
    if state.allocated_units == 0:
        return MiddlePoolReturnDecision(
            allocation_id=state.allocation_id,
            action="no_action",
            returned_units=0.0,
            remaining_allocated_units=0.0,
            target_pool="dynamic_middle_pool",
            rationale=("no_allocated_memory",),
        )

    if state.live_reference_count > 0:
        return MiddlePoolReturnDecision(
            allocation_id=state.allocation_id,
            action="retain_for_live_reference",
            returned_units=0.0,
            remaining_allocated_units=state.allocated_units,
            target_pool="current_allocation",
            rationale=("live_reference_present",),
        )

    if state.anticipated_reference_blocks_reclaim:
        return MiddlePoolReturnDecision(
            allocation_id=state.allocation_id,
            action="retain_minimum_reservation",
            returned_units=0.0,
            remaining_allocated_units=state.allocated_units,
            target_pool="current_allocation",
            rationale=("justified_anticipated_reference",),
        )

    if not state.checkpoint_safe:
        return MiddlePoolReturnDecision(
            allocation_id=state.allocation_id,
            action="checkpoint_before_return",
            returned_units=0.0,
            remaining_allocated_units=state.allocated_units,
            target_pool="current_allocation",
            rationale=("checkpoint_incomplete",),
        )

    reasons = ["no_reference_in_use", "return_to_dynamic_middle_pool"]
    if state.computation_complete:
        reasons.append("computation_complete")

    return MiddlePoolReturnDecision(
        allocation_id=state.allocation_id,
        action="return_to_middle_pool",
        returned_units=state.allocated_units,
        remaining_allocated_units=0.0,
        target_pool="dynamic_middle_pool",
        rationale=tuple(reasons),
    )


def aggregate_middle_pool_returns(
    decisions: Tuple[MiddlePoolReturnDecision, ...],
) -> float:
    return sum(decision.returned_units for decision in decisions)
