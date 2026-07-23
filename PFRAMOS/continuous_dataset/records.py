"""Core contracts for the PFRAMOS Continuous Evidence Dataset."""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from datetime import datetime
from typing import Mapping, Tuple


@dataclass(frozen=True)
class EvidenceRecord:
    record_id: str
    source_id: str
    source_type: str
    acquired_at: datetime
    event_at: datetime
    content_hash: str
    licence_status: str
    lineage: Tuple[str, ...]
    transformations: Tuple[str, ...]
    quality: float
    relevance: float
    independence: float
    conflict: float
    privacy_cleared: bool
    safety_cleared: bool
    nodal_roles: Tuple[str, ...]
    validation_state: str

    def __post_init__(self) -> None:
        for name in ("quality", "relevance", "independence", "conflict"):
            value = getattr(self, name)
            if not 0.0 <= value <= 1.0:
                raise ValueError(f"{name} must be between 0 and 1")
        if self.event_at > self.acquired_at:
            raise ValueError("event_at cannot be later than acquired_at")
        if not self.lineage:
            raise ValueError("Evidence lineage is required")

    @property
    def training_eligible(self) -> bool:
        return (
            self.validation_state == "validated"
            and self.privacy_cleared
            and self.safety_cleared
            and self.licence_status in {"approved", "project_owned", "permitted_metadata"}
            and self.quality >= 0.60
            and self.relevance >= 0.50
            and self.conflict <= 0.40
        )


def content_digest(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def record_fingerprint(record: EvidenceRecord) -> str:
    payload = "|".join(
        (
            record.source_id,
            record.source_type,
            record.event_at.isoformat(),
            record.content_hash,
            ",".join(record.lineage),
        )
    )
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class DatasetSnapshot:
    snapshot_id: str
    created_at: datetime
    record_ids: Tuple[str, ...]
    maximum_event_time: datetime
    parent_snapshot_id: str | None = None

    def contains_future_leakage(self, decision_time: datetime) -> bool:
        return self.maximum_event_time > decision_time


@dataclass(frozen=True)
class RetrainingEvidence:
    new_validated_records: int
    minimum_new_records: int
    drift_score: float
    drift_threshold: float
    performance_degradation: float
    degradation_threshold: float
    new_validated_node: bool
    expected_quality_gain: float
    unresolved_conflicts: int
    leakage_detected: bool


def retraining_decision(evidence: RetrainingEvidence) -> tuple[bool, Tuple[str, ...]]:
    reasons = []
    if evidence.leakage_detected:
        return False, ("train-test or temporal leakage detected",)
    if evidence.unresolved_conflicts > 0:
        return False, ("unresolved source conflicts remain",)
    if evidence.expected_quality_gain <= 0.0:
        return False, ("no positive validated quality gain is expected",)

    if evidence.new_validated_records >= evidence.minimum_new_records:
        reasons.append("sufficient new validated evidence")
    if evidence.drift_score >= evidence.drift_threshold:
        reasons.append("distribution drift threshold reached")
    if evidence.performance_degradation >= evidence.degradation_threshold:
        reasons.append("performance degradation threshold reached")
    if evidence.new_validated_node:
        reasons.append("new validated nodal capability available")

    return bool(reasons), tuple(reasons or ["retraining threshold not reached"])
