from datetime import datetime, timezone

from PFRAMOS.schooling.concurrent_training import (
    ConcurrentTrainingPlan,
    ResourceBudget,
    TrainingLane,
    TrainingLaneResult,
    select_synthesis_candidates,
)
from PFRAMOS.schooling.training_log import TrainingLogEntry, verify_log_chain


NOW = datetime(2026, 7, 25, 9, 0, tzinfo=timezone.utc)


def _budget() -> ResourceBudget:
    return ResourceBudget(2, 0.0, 4.0, 10.0, 60, 1.0)


def _lane(identifier: str, gain: float, risk: float = 0.1) -> TrainingLane:
    return TrainingLane(
        lane_id=identifier,
        purpose="test",
        dataset_snapshot_id=f"snapshot-{identifier}",
        baseline_model_version="pframos-0.1",
        random_seed=42,
        expected_quality_gain=gain,
        coherence=0.9,
        novelty=0.8,
        relevance=0.9,
        estimated_compute_cost=0.2,
        estimated_memory_cost=0.2,
        estimated_energy_cost=0.2,
        risk=risk,
        protected_test_id=f"test-{identifier}",
        resource_budget=_budget(),
    )


def test_lanes_are_sorted_by_p_c4_priority() -> None:
    plan = ConcurrentTrainingPlan(
        plan_id="p1",
        created_at=NOW,
        lanes=(_lane("low", 0.2), _lane("high", 0.9)),
        maximum_parallel_lanes=1,
    )
    assert plan.scheduled_batches()[0] == ("high",)


def test_training_pauses_near_final_decision() -> None:
    plan = ConcurrentTrainingPlan(
        plan_id="p2",
        created_at=NOW,
        lanes=(_lane("a", 0.5),),
        maximum_parallel_lanes=1,
        final_decision_proximity=0.9,
    )
    assert not plan.training_allowed
    assert plan.scheduled_batches() == ()


def test_only_validated_lane_enters_synthesis() -> None:
    good = TrainingLaneResult(
        lane_id="good",
        started_at=NOW,
        completed_at=NOW,
        checkpoint_id="c1",
        baseline_score=0.5,
        validation_score=0.7,
        protected_test_score=0.7,
        coherence_score=0.8,
        robustness_score=0.8,
        calibration_score=0.7,
        regression_count=0,
        catastrophic_forgetting_detected=False,
        runtime_minutes=10,
        peak_memory_gb=1,
        energy_proxy=0.1,
        reproducible=True,
    )
    bad = TrainingLaneResult(
        lane_id="bad",
        started_at=NOW,
        completed_at=NOW,
        checkpoint_id="c2",
        baseline_score=0.5,
        validation_score=0.6,
        protected_test_score=0.4,
        coherence_score=0.8,
        robustness_score=0.8,
        calibration_score=0.7,
        regression_count=0,
        catastrophic_forgetting_detected=False,
        runtime_minutes=10,
        peak_memory_gb=1,
        energy_proxy=0.1,
        reproducible=True,
    )
    assert select_synthesis_candidates((good, bad)) == ("good",)


def _log(previous_hash=None, session_id="s1") -> TrainingLogEntry:
    return TrainingLogEntry(
        session_id=session_id,
        lane_id="lane-a",
        created_at=NOW,
        dataset_snapshot_id="snapshot-a",
        dataset_source_ids=("source-a",),
        dataset_hashes=("abc",),
        licence_states=("approved",),
        baseline_model_version="pframos-0.1",
        candidate_checkpoint_id="checkpoint-a",
        random_seed=42,
        hyperparameters={"lr": 0.001},
        software_environment={"python": "3.12"},
        train_record_count=100,
        validation_record_count=20,
        protected_test_record_count=20,
        baseline_metrics={"score": 0.5},
        validation_metrics={"score": 0.6},
        protected_test_metrics={"score": 0.6},
        coherence_score=0.8,
        robustness_score=0.8,
        calibration_score=0.7,
        runtime_minutes=10,
        peak_memory_gb=1,
        compute_proxy=0.2,
        energy_proxy=0.1,
        regressions=(),
        catastrophic_forgetting_detected=False,
        decision="shadow_validate",
        decision_reason="positive protected-test gain",
        temporary_data_removed=True,
        deletion_record_id="delete-a",
        previous_entry_hash=previous_hash,
    )


def test_training_log_hash_chain() -> None:
    first = _log()
    second = _log(previous_hash=first.entry_hash, session_id="s2")
    assert verify_log_chain((first, second))
