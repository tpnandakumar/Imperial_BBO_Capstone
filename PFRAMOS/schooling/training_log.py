"""Append-only training log contracts for PFRAMOS schooling sessions."""

from __future__ import annotations

import hashlib
import json
from dataclasses import asdict, dataclass
from datetime import datetime
from typing import Mapping, Tuple


@dataclass(frozen=True)
class TrainingLogEntry:
    session_id: str
    lane_id: str
    created_at: datetime
    dataset_snapshot_id: str
    dataset_source_ids: Tuple[str, ...]
    dataset_hashes: Tuple[str, ...]
    licence_states: Tuple[str, ...]
    baseline_model_version: str
    candidate_checkpoint_id: str
    random_seed: int
    hyperparameters: Mapping[str, object]
    software_environment: Mapping[str, str]
    train_record_count: int
    validation_record_count: int
    protected_test_record_count: int
    baseline_metrics: Mapping[str, float]
    validation_metrics: Mapping[str, float]
    protected_test_metrics: Mapping[str, float]
    coherence_score: float
    robustness_score: float
    calibration_score: float
    runtime_minutes: float
    peak_memory_gb: float
    compute_proxy: float
    energy_proxy: float
    regressions: Tuple[str, ...]
    catastrophic_forgetting_detected: bool
    decision: str
    decision_reason: str
    temporary_data_removed: bool
    deletion_record_id: str | None
    previous_entry_hash: str | None = None

    def __post_init__(self) -> None:
        if self.decision not in {
            "retain_experimental",
            "shadow_validate",
            "promote_candidate",
            "reject",
            "rollback",
        }:
            raise ValueError("invalid training decision")
        if not self.dataset_hashes:
            raise ValueError("dataset hashes are required")
        if self.temporary_data_removed and not self.deletion_record_id:
            raise ValueError("deletion record required when temporary data are removed")

    def canonical_payload(self) -> str:
        payload = asdict(self)
        payload["created_at"] = self.created_at.isoformat()
        return json.dumps(payload, sort_keys=True, separators=(",", ":"), default=str)

    @property
    def entry_hash(self) -> str:
        return hashlib.sha256(self.canonical_payload().encode("utf-8")).hexdigest()


def verify_log_chain(entries: Tuple[TrainingLogEntry, ...]) -> bool:
    previous_hash = None
    for entry in entries:
        if entry.previous_entry_hash != previous_hash:
            return False
        previous_hash = entry.entry_hash
    return True
