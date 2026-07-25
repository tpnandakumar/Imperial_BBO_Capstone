"""Reference-Aware Retention guided DMACCE.

RaR means Reference-Aware Retention. It governs whether memory remains active,
is compressed, is demoted, or is released. Reference state takes precedence
over recency and relevance so memory is never released while required by an
active, queued, dependent, or anticipated computation.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import FrozenSet, Tuple

from PFRAMOS.architecture.pcece_dmacce import DMACCEDecision, MemoryAllocation


def _clip(value: float) -> float:
    return max(0.0, min(1.0, value))


@dataclass(frozen=True)
class ReferenceAwareRetentionState:
    active_references: FrozenSet[str]
    queued_references: FrozenSet[str]
    dependent_references: FrozenSet[str]
    anticipated_references: FrozenSet[str]
    reference_strength: float
    recent_activity: float
    current_relevance: float
    anticipated_relevance: float
    recomputation_risk: float

    def __post_init__(self) -> None:
        for name in (
            "reference_strength",
            "recent_activity",
            "current_relevance",
            "anticipated_relevance",
            "recomputation_risk",
        ):
            value = getattr(self, name)
            if not 0.0 <= value <= 1.0:
                raise ValueError(f"{name} must be between 0 and 1")

    @property
    def total_reference_count(self) -> int:
        return (
            len(self.active_references)
            + len(self.queued_references)
            + len(self.dependent_references)
            + len(self.anticipated_references)
        )

    @property
    def has_live_reference(self) -> bool:
        return bool(
            self.active_references
            or self.queued_references
            or self.dependent_references
        )

    @property
    def has_anticipated_reference(self) -> bool:
        return bool(self.anticipated_references)

    @property
    def retention_score(self) -> float:
        reference_component = 1.0 if self.has_live_reference else self.reference_strength
        anticipated_component = 1.0 if self.has_anticipated_reference else self.anticipated_relevance
        return _clip(
            0.50 * reference_component
            + 0.15 * anticipated_component
            + 0.15 * self.recent_activity
            + 0.10 * self.current_relevance
            + 0.10 * self.recomputation_risk
        )


@dataclass(frozen=True)
class RaRDecision:
    allocation_id: str
    action: str
    target_location: str
    retention_score: float
    released_units: float
    retained_units: float
    rationale: Tuple[str, ...]


def rar_guided_dmacce_decide(
    allocation: MemoryAllocation,
    state: ReferenceAwareRetentionState,
    current_tick: int,
    memory_pressure: float,
    energy_pressure: float,
) -> RaRDecision:
    if current_tick < allocation.last_used_tick:
        raise ValueError("current_tick cannot precede last_used_tick")
    for value in (memory_pressure, energy_pressure):
        if not 0.0 <= value <= 1.0:
            raise ValueError("pressure values must be between 0 and 1")

    retention = state.retention_score
    idle_ticks = current_tick - allocation.last_used_tick

    if allocation.location == "released":
        return RaRDecision(
            allocation_id=allocation.allocation_id,
            action="no_action",
            target_location="released",
            retention_score=retention,
            released_units=0.0,
            retained_units=0.0,
            rationale=("already_released",),
        )

    if state.has_live_reference:
        return RaRDecision(
            allocation_id=allocation.allocation_id,
            action="retain_active",
            target_location="active",
            retention_score=1.0,
            released_units=0.0,
            retained_units=allocation.size_units,
            rationale=("live_reference_present",),
        )

    if state.has_anticipated_reference and retention >= 0.60:
        retained = allocation.size_units * max(0.10, allocation.compression_ratio)
        return RaRDecision(
            allocation_id=allocation.allocation_id,
            action="retain_compressed",
            target_location="compressed",
            retention_score=retention,
            released_units=allocation.size_units - retained,
            retained_units=retained,
            rationale=("anticipated_reference_present", "retain_for_expected_use"),
        )

    if allocation.persistent:
        if memory_pressure >= 0.70:
            retained = allocation.size_units * max(0.05, allocation.compression_ratio)
            return RaRDecision(
                allocation_id=allocation.allocation_id,
                action="compress_persistent",
                target_location="compressed",
                retention_score=max(retention, 0.70),
                released_units=allocation.size_units - retained,
                retained_units=retained,
                rationale=("persistent_memory", "high_memory_pressure"),
            )
        return RaRDecision(
            allocation_id=allocation.allocation_id,
            action="retain_persistent",
            target_location=allocation.location,
            retention_score=max(retention, 0.70),
            released_units=0.0,
            retained_units=allocation.size_units,
            rationale=("persistent_memory",),
        )

    if retention >= 0.65:
        return RaRDecision(
            allocation_id=allocation.allocation_id,
            action="retain_active",
            target_location="active",
            retention_score=retention,
            released_units=0.0,
            retained_units=allocation.size_units,
            rationale=("high_reference_aware_retention",),
        )

    if retention >= 0.40:
        retained = allocation.size_units * max(0.10, allocation.compression_ratio)
        return RaRDecision(
            allocation_id=allocation.allocation_id,
            action="compress",
            target_location="compressed",
            retention_score=retention,
            released_units=allocation.size_units - retained,
            retained_units=retained,
            rationale=("moderate_reference_aware_retention",),
        )

    if idle_ticks >= 2 and allocation.recomputation_cost < 0.50:
        return RaRDecision(
            allocation_id=allocation.allocation_id,
            action="demote_to_cold",
            target_location="cold",
            retention_score=retention,
            released_units=0.0,
            retained_units=allocation.size_units,
            rationale=("low_retention", "low_recomputation_cost", "idle"),
        )

    if memory_pressure >= 0.60 or energy_pressure >= 0.70 or idle_ticks >= 5:
        return RaRDecision(
            allocation_id=allocation.allocation_id,
            action="release",
            target_location="released",
            retention_score=retention,
            released_units=allocation.size_units,
            retained_units=0.0,
            rationale=("no_reference", "low_retention", "release_condition_met"),
        )

    return RaRDecision(
        allocation_id=allocation.allocation_id,
        action="retain_active",
        target_location="active",
        retention_score=retention,
        released_units=0.0,
        retained_units=allocation.size_units,
        rationale=("retain_until_release_condition",),
    )
