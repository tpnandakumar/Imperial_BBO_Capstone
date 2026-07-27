from datetime import datetime, timezone

from PFRAMOS.continuous_dataset.records import (
    DatasetSnapshot,
    EvidenceRecord,
    RetrainingEvidence,
    content_digest,
    record_fingerprint,
    retraining_decision,
)


NOW = datetime(2026, 7, 23, 20, 0, tzinfo=timezone.utc)
EARLIER = datetime(2026, 7, 22, 20, 0, tzinfo=timezone.utc)


def _record(**overrides):
    values = dict(
        record_id="r1",
        source_id="source-1",
        source_type="bbo_observation",
        acquired_at=NOW,
        event_at=EARLIER,
        content_hash=content_digest(b"record"),
        licence_status="project_owned",
        lineage=("source-1",),
        transformations=("canonicalised",),
        quality=0.9,
        relevance=0.9,
        independence=0.8,
        conflict=0.1,
        privacy_cleared=True,
        safety_cleared=True,
        nodal_roles=("trajectory",),
        validation_state="validated",
    )
    values.update(overrides)
    return EvidenceRecord(**values)


def test_validated_record_is_training_eligible() -> None:
    assert _record().training_eligible


def test_conflicted_record_is_not_training_eligible() -> None:
    assert not _record(conflict=0.8).training_eligible


def test_record_fingerprint_is_deterministic() -> None:
    record = _record()
    assert record_fingerprint(record) == record_fingerprint(record)


def test_snapshot_detects_temporal_leakage() -> None:
    snapshot = DatasetSnapshot(
        snapshot_id="s1",
        created_at=NOW,
        record_ids=("r1",),
        maximum_event_time=NOW,
    )
    assert snapshot.contains_future_leakage(EARLIER)


def test_retraining_requires_positive_gain_and_trigger() -> None:
    approved, reasons = retraining_decision(
        RetrainingEvidence(
            new_validated_records=20,
            minimum_new_records=10,
            drift_score=0.1,
            drift_threshold=0.3,
            performance_degradation=0.0,
            degradation_threshold=0.1,
            new_validated_node=False,
            expected_quality_gain=0.05,
            unresolved_conflicts=0,
            leakage_detected=False,
        )
    )
    assert approved
    assert "sufficient new validated evidence" in reasons


def test_leakage_blocks_retraining() -> None:
    approved, reasons = retraining_decision(
        RetrainingEvidence(
            new_validated_records=20,
            minimum_new_records=10,
            drift_score=0.5,
            drift_threshold=0.3,
            performance_degradation=0.2,
            degradation_threshold=0.1,
            new_validated_node=True,
            expected_quality_gain=0.5,
            unresolved_conflicts=0,
            leakage_detected=True,
        )
    )
    assert not approved
    assert "leakage" in reasons[0]
