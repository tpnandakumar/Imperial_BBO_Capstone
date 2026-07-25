"""Concurrent multi-source schooling for PFRAMOS.

Training lanes are isolated, reproducible and non-promoting by default.
Each lane receives a frozen dataset snapshot and writes its own checkpoint,
metrics and append-only training-log entry.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Iterable, Tuple


@dataclass(frozen=True)
class ResourceBudget:
    cpu_cores: int
    gpu_units: float
    memory_gb: float
    storage_gb: float
    maximum_runtime_minutes: int
    energy_proxy_limit: float

    def __post_init__(self) -> None:
        if self.cpu_cores < 1:
            raise ValueError("cpu_cores must be positive")
        for name in ("gpu_units", "memory_gb", "storage_gb", "energy_proxy_limit"):
            if getattr(self, name) < 0:
                raise ValueError(f"{name} cannot be negative")
        if self.maximum_runtime_minutes < 1:
            raise ValueError("maximum_runtime_minutes must be positive")


@dataclass(frozen=True)
class TrainingLane:
    lane_id: str
    purpose: str
    dataset_snapshot_id: str
    baseline_model_version: str
    random_seed: int
    expected_quality_gain: float
    coherence: float
    novelty: float
    relevance: float
    estimated_compute_cost: float
    estimated_memory_cost: float
    estimated_energy_cost: float
    risk: float
    protected_test_id: str
    resource_budget: ResourceBudget

    def __post_init__(self) -> None:
        for name in (
            "expected_quality_gain",
            "coherence",
            "novelty",
            "relevance",
            "estimated_compute_cost",
            "estimated_memory_cost",
            "estimated_energy_cost",
            "risk",
        ):
            value = getattr(self, name)
            if not 0.0 <= value <= 1.0:
                raise ValueError(f"{name} must be between 0 and 1")
        if not self.dataset_snapshot_id or not self.protected_test_id:
            raise ValueError("dataset snapshot and protected test are required")

    @property
    def p_c4_priority(self) -> float:
        positive = (
            self.expected_quality_gain
            * self.coherence
            * self.novelty
            * self.relevance
        )
        cost = 1.0 + self.estimated_compute_cost + self.estimated_memory_cost + self.estimated_energy_cost
        return max(0.0, min(1.0, (positive / cost) * (1.0 - self.risk)))


@dataclass(frozen=True)
class TrainingLaneResult:
    lane_id: str
    started_at: datetime
    completed_at: datetime
    checkpoint_id: str
    baseline_score: float
    validation_score: float
    protected_test_score: float
    coherence_score: float
    robustness_score: float
    calibration_score: float
    regression_count: int
    catastrophic_forgetting_detected: bool
    runtime_minutes: float
    peak_memory_gb: float
    energy_proxy: float
    reproducible: bool

    @property
    def validated_gain(self) -> float:
        return self.protected_test_score - self.baseline_score

    @property
    def promotion_eligible(self) -> bool:
        return (
            self.validated_gain > 0
            and self.coherence_score >= 0.70
            and self.robustness_score >= 0.70
            and self.calibration_score >= 0.60
            and self.regression_count == 0
            and not self.catastrophic_forgetting_detected
            and self.reproducible
        )


@dataclass(frozen=True)
class ConcurrentTrainingPlan:
    plan_id: str
    created_at: datetime
    lanes: Tuple[TrainingLane, ...]
    maximum_parallel_lanes: int
    live_analysis_active: bool = False
    final_decision_proximity: float = 0.0

    def __post_init__(self) -> None:
        if not self.lanes:
            raise ValueError("at least one training lane is required")
        if self.maximum_parallel_lanes < 1:
            raise ValueError("maximum_parallel_lanes must be positive")
        if not 0.0 <= self.final_decision_proximity <= 1.0:
            raise ValueError("final_decision_proximity must be between 0 and 1")
        lane_ids = [lane.lane_id for lane in self.lanes]
        if len(lane_ids) != len(set(lane_ids)):
            raise ValueError("duplicate lane identifiers are not allowed")

    @property
    def training_allowed(self) -> bool:
        return not self.live_analysis_active and self.final_decision_proximity < 0.85

    def scheduled_batches(self) -> Tuple[Tuple[str, ...], ...]:
        if not self.training_allowed:
            return ()
        ordered = sorted(self.lanes, key=lambda lane: lane.p_c4_priority, reverse=True)
        size = self.maximum_parallel_lanes
        return tuple(
            tuple(lane.lane_id for lane in ordered[index : index + size])
            for index in range(0, len(ordered), size)
        )


def select_synthesis_candidates(results: Iterable[TrainingLaneResult]) -> Tuple[str, ...]:
    return tuple(
        result.lane_id
        for result in results
        if result.promotion_eligible
    )
