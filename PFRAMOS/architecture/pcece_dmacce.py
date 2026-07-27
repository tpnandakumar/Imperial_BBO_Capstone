"""PCECE and DMACCE for cost, energy and memory efficiency.

PCECE is the system-level efficiency objective. DMACCE is the dynamic memory
controller that allocates, shares, compresses, demotes and releases memory
according to live computational demand and dependency state.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import FrozenSet, Tuple


def _clip(value: float) -> float:
    return max(0.0, min(1.0, value))


@dataclass(frozen=True)
class PCECEMeasurement:
    validated_quality: float
    coherence: float
    robustness: float
    useful_work: float
    compute_cost: float
    energy_cost: float
    memory_cost: float
    routing_friction: float
    idle_resource_fraction: float

    def __post_init__(self) -> None:
        for name, value in self.__dict__.items():
            if not 0.0 <= value <= 1.0:
                raise ValueError(f"{name} must be between 0 and 1")

    @property
    def pcece_score(self) -> float:
        benefit = (
            self.validated_quality
            * self.coherence
            * self.robustness
            * self.useful_work
        )
        burden = (
            1.0
            + self.compute_cost
            + self.energy_cost
            + self.memory_cost
            + self.routing_friction
            + self.idle_resource_fraction
        )
        return _clip(benefit / burden)


@dataclass(frozen=True)
class MemoryAllocation:
    allocation_id: str
    owner_task_id: str
    size_units: float
    priority: float
    recomputation_cost: float
    compression_ratio: float
    persistent: bool
    active_references: FrozenSet[str]
    queued_references: FrozenSet[str]
    dependent_references: FrozenSet[str]
    last_used_tick: int
    location: str = "active"

    def __post_init__(self) -> None:
        if self.size_units < 0:
            raise ValueError("size_units cannot be negative")
        for name in ("priority", "recomputation_cost", "compression_ratio"):
            value = getattr(self, name)
            if not 0.0 <= value <= 1.0:
                raise ValueError(f"{name} must be between 0 and 1")
        if self.last_used_tick < 0:
            raise ValueError("last_used_tick cannot be negative")
        if self.location not in {"active", "compressed", "cold", "released"}:
            raise ValueError("invalid memory location")

    @property
    def reference_count(self) -> int:
        return (
            len(self.active_references)
            + len(self.queued_references)
            + len(self.dependent_references)
        )

    @property
    def releasable(self) -> bool:
        return not self.persistent and self.reference_count == 0


@dataclass(frozen=True)
class DMACCEDecision:
    allocation_id: str
    action: str
    target_location: str
    released_units: float
    retained_units: float
    rationale: Tuple[str, ...]


def dmacce_decide(
    allocation: MemoryAllocation,
    current_tick: int,
    memory_pressure: float,
    energy_pressure: float,
) -> DMACCEDecision:
    if current_tick < allocation.last_used_tick:
        raise ValueError("current_tick cannot precede last_used_tick")
    for value in (memory_pressure, energy_pressure):
        if not 0.0 <= value <= 1.0:
            raise ValueError("pressure values must be between 0 and 1")

    idle_ticks = current_tick - allocation.last_used_tick

    if allocation.location == "released":
        return DMACCEDecision(
            allocation_id=allocation.allocation_id,
            action="no_action",
            target_location="released",
            released_units=0.0,
            retained_units=0.0,
            rationale=("already_released",),
        )

    if allocation.reference_count > 0:
        return DMACCEDecision(
            allocation_id=allocation.allocation_id,
            action="retain_active",
            target_location="active",
            released_units=0.0,
            retained_units=allocation.size_units,
            rationale=("referenced_by_computation",),
        )

    if allocation.persistent:
        if memory_pressure >= 0.70 and allocation.location == "active":
            retained = allocation.size_units * max(0.05, allocation.compression_ratio)
            return DMACCEDecision(
                allocation_id=allocation.allocation_id,
                action="compress_persistent",
                target_location="compressed",
                released_units=allocation.size_units - retained,
                retained_units=retained,
                rationale=("persistent_memory", "high_memory_pressure"),
            )
        return DMACCEDecision(
            allocation_id=allocation.allocation_id,
            action="retain_persistent",
            target_location=allocation.location,
            released_units=0.0,
            retained_units=allocation.size_units,
            rationale=("persistent_memory",),
        )

    if allocation.releasable and (
        memory_pressure >= 0.60
        or energy_pressure >= 0.70
        or idle_ticks >= 5
    ):
        return DMACCEDecision(
            allocation_id=allocation.allocation_id,
            action="release",
            target_location="released",
            released_units=allocation.size_units,
            retained_units=0.0,
            rationale=("unreferenced", "release_condition_met"),
        )

    if allocation.releasable and memory_pressure >= 0.35:
        retained = allocation.size_units * max(0.10, allocation.compression_ratio)
        return DMACCEDecision(
            allocation_id=allocation.allocation_id,
            action="compress",
            target_location="compressed",
            released_units=allocation.size_units - retained,
            retained_units=retained,
            rationale=("unreferenced", "moderate_memory_pressure"),
        )

    if allocation.releasable and idle_ticks >= 2 and allocation.recomputation_cost < 0.40:
        return DMACCEDecision(
            allocation_id=allocation.allocation_id,
            action="demote_to_cold",
            target_location="cold",
            released_units=0.0,
            retained_units=allocation.size_units,
            rationale=("unreferenced", "low_recomputation_cost", "idle"),
        )

    return DMACCEDecision(
        allocation_id=allocation.allocation_id,
        action="retain_active",
        target_location="active",
        released_units=0.0,
        retained_units=allocation.size_units,
        rationale=("retain_for_near_term_use",),
    )


def aggregate_released_units(decisions: Tuple[DMACCEDecision, ...]) -> float:
    return sum(decision.released_units for decision in decisions)
