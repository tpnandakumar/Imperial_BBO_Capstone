"""Publication-grade evidence record for PACC training runs."""

from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Mapping, Tuple


@dataclass(frozen=True)
class PACCExperimentRecord:
    experiment_id: str
    timestamp_utc: str
    cognitive_domain: str
    training_lane: str
    research_question: str
    hypothesis: str
    dataset_name: str
    dataset_version: str
    dataset_source: str
    dataset_manifest_hash: str
    licence_status: str
    access_status: str
    privacy_status: str
    ethics_status: str
    contamination_status: str
    representativeness_status: str
    model_version: str
    software_commit: str
    random_seed: int
    hardware_environment: str
    runtime_seconds: float
    parameter_updates_applied: bool
    shadow_only: bool
    baseline_methods: Tuple[str, ...]
    training_parameters: Mapping[str, str]
    training_metrics: Mapping[str, float]
    validation_metrics: Mapping[str, float]
    protected_test_metrics: Mapping[str, float]
    uncertainty_metrics: Mapping[str, float]
    pcece_metrics: Mapping[str, float]
    memory_metrics: Mapping[str, float]
    pimf_states: Tuple[str, ...]
    pframos_decision: str
    negative_results: Tuple[str, ...]
    limitations: Tuple[str, ...]
    primary_paper_track: str
    secondary_paper_tracks: Tuple[str, ...]
    reproducible: bool

    def blockers(self) -> Tuple[str, ...]:
        blockers = []
        required_text = {
            "experiment_id": self.experiment_id,
            "dataset_manifest_hash": self.dataset_manifest_hash,
            "model_version": self.model_version,
            "software_commit": self.software_commit,
            "pframos_decision": self.pframos_decision,
            "primary_paper_track": self.primary_paper_track,
        }
        for name, value in required_text.items():
            if not str(value).strip():
                blockers.append(f"missing_{name}")

        approved_states = {"approved", "not_applicable"}
        if self.licence_status not in approved_states:
            blockers.append("licence_not_approved")
        if self.access_status not in approved_states:
            blockers.append("access_not_approved")
        if self.privacy_status not in approved_states:
            blockers.append("privacy_not_approved")
        if self.ethics_status not in approved_states:
            blockers.append("ethics_not_approved")
        if self.contamination_status not in approved_states:
            blockers.append("contamination_not_approved")
        if not self.protected_test_metrics:
            blockers.append("missing_protected_test_metrics")
        if not self.reproducible:
            blockers.append("not_reproducible")
        return tuple(blockers)

    @property
    def publication_evidence_ready(self) -> bool:
        return not self.blockers()

    def to_dict(self) -> dict:
        return asdict(self)
