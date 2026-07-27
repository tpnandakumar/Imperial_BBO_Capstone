"""Controlled PACC training pilot.

The pilot prepares domain-specific training lanes, validates dataset readiness,
assigns dynamic priority, applies memory controls and emits a shadow-training
plan. It does not download data or update model parameters by itself.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

from PFRAMOS.architecture.dynamic_function_priority import (
    FunctionPriority,
    PriorityContext,
    reprioritise,
)
from PFRAMOS.training_scout.cognitive_network_validation import (
    CognitiveValidationDataset,
    validate_dataset_mapping,
)


PACC_TRAINING_LANES = (
    "attention_and_working_memory",
    "episodic_and_retrieval",
    "semantic_and_language",
    "executive_and_abstraction",
    "visuospatial_and_praxis",
    "social_and_metacognitive",
)


@dataclass(frozen=True)
class PACCTrainingCandidate:
    candidate_id: str
    dataset: CognitiveValidationDataset
    lane: str
    model_version: str
    protected_test_defined: bool
    dataset_manifest_present: bool
    privacy_review_complete: bool
    contamination_review_complete: bool
    initial_priority: FunctionPriority

    def __post_init__(self) -> None:
        if self.lane not in PACC_TRAINING_LANES:
            raise ValueError(f"unsupported training lane: {self.lane}")
        if not self.model_version.strip():
            raise ValueError("model_version is required")


@dataclass(frozen=True)
class PACCTrainingPlan:
    candidate_id: str
    lane: str
    state: str
    priority: FunctionPriority
    parameter_updates_allowed: bool
    shadow_evaluation_allowed: bool
    blockers: Tuple[str, ...]
    required_outputs: Tuple[str, ...]


def build_training_plan(candidate: PACCTrainingCandidate) -> PACCTrainingPlan:
    blockers = list(validate_dataset_mapping(candidate.dataset))

    if not candidate.dataset_manifest_present:
        blockers.append("missing_dataset_manifest")
    if not candidate.protected_test_defined:
        blockers.append("missing_protected_test")
    if not candidate.privacy_review_complete:
        blockers.append("privacy_review_incomplete")
    if not candidate.contamination_review_complete:
        blockers.append("contamination_review_incomplete")
    if not candidate.dataset.training_eligible:
        blockers.append("dataset_not_training_eligible")

    priority_change = reprioritise(
        candidate.initial_priority,
        PriorityContext(
            function_id=candidate.candidate_id,
            criticality=0.85,
            urgency=0.55,
            dependency_pressure=0.65,
            expected_value=0.80,
            failure_risk=0.60,
            waiting_pressure=0.20,
            resource_pressure=0.45,
            active=True,
            queued=False,
            completed=False,
            blocked=bool(blockers),
            protected=True,
        ),
    )

    parameter_updates_allowed = not blockers
    shadow_evaluation_allowed = candidate.dataset.discovery_eligible

    if parameter_updates_allowed:
        state = "ready_for_controlled_training"
    elif shadow_evaluation_allowed:
        state = "shadow_validation_only"
    else:
        state = "blocked"

    return PACCTrainingPlan(
        candidate_id=candidate.candidate_id,
        lane=candidate.lane,
        state=state,
        priority=priority_change.current,
        parameter_updates_allowed=parameter_updates_allowed,
        shadow_evaluation_allowed=shadow_evaluation_allowed,
        blockers=tuple(sorted(set(blockers))),
        required_outputs=(
            "dataset_manifest",
            "model_version_record",
            "protected_test_report",
            "pimf_influence_report",
            "pframos_conduit_decision",
            "pcece_efficiency_record",
            "dmacce_memory_record",
            "publication_routing_record",
        ),
    )
