"""Functional cognitive network validation scout for PACC.

The scout discovers open datasets that can test computational cognitive-domain
models. Discovery does not authorise training. Each dataset must pass licence,
provenance, privacy, contamination, representativeness and protected-test
checks before use.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple


COGNITIVE_DOMAIN_TAXONOMY = (
    "orientation_and_context",
    "attention",
    "working_memory",
    "episodic_memory",
    "semantic_memory",
    "retrieval_and_recall",
    "verbal_fluency",
    "language",
    "executive_control",
    "abstraction",
    "visuospatial_cognition",
    "naming_and_object_knowledge",
    "praxis",
    "calculation",
    "social_cognition",
    "emotion_recognition",
    "behaviour_and_motivation",
    "metacognition",
)

VALIDATION_PROTOCOLS = {
    "orientation_and_context": ("context_binding", "temporal_order", "state_consistency"),
    "attention": ("selection_accuracy", "sustained_performance", "distractor_resistance"),
    "working_memory": ("capacity", "manipulation_accuracy", "interference_resistance"),
    "episodic_memory": ("encoding", "retention", "recognition", "source_memory"),
    "semantic_memory": ("concept_integrity", "relation_coherence", "category_generalisation"),
    "retrieval_and_recall": ("recall_efficiency", "retrieval_precision", "cue_benefit"),
    "verbal_fluency": ("generation_rate", "switching", "clustering", "perseveration"),
    "language": ("comprehension", "production", "syntax", "semantics", "pragmatics"),
    "executive_control": ("planning", "inhibition", "switching", "monitoring"),
    "abstraction": ("analogy", "rule_induction", "category_formation"),
    "visuospatial_cognition": ("spatial_relation", "rotation", "construction", "navigation"),
    "naming_and_object_knowledge": ("perceptual_identification", "lexical_access", "semantic_access"),
    "praxis": ("action_sequence", "tool_knowledge", "gesture_transformation"),
    "calculation": ("symbolic_processing", "magnitude", "operation_accuracy"),
    "social_cognition": ("theory_of_mind", "intent_inference", "social_rule_use"),
    "emotion_recognition": ("facial_affect", "vocal_affect", "contextual_emotion"),
    "behaviour_and_motivation": ("goal_persistence", "reward_sensitivity", "behavioural_regulation"),
    "metacognition": ("confidence_calibration", "error_awareness", "strategy_revision"),
}


@dataclass(frozen=True)
class CognitiveValidationDataset:
    dataset_id: str
    display_name: str
    source_platform: str
    cognitive_domains: Tuple[str, ...]
    data_forms: Tuple[str, ...]
    validation_targets: Tuple[str, ...]
    access_state: str
    licence_state: str
    privacy_risk: float
    contamination_risk: float
    clinical_claims_allowed: bool = False

    def __post_init__(self) -> None:
        if not self.cognitive_domains:
            raise ValueError("at least one cognitive domain is required")
        if not self.data_forms:
            raise ValueError("at least one data form is required")
        for name in ("privacy_risk", "contamination_risk"):
            value = getattr(self, name)
            if not 0.0 <= value <= 1.0:
                raise ValueError(f"{name} must be between 0 and 1")

    @property
    def discovery_eligible(self) -> bool:
        return self.access_state in {"open", "open_registration", "request_access"}

    @property
    def training_eligible(self) -> bool:
        return (
            self.access_state in {"open", "open_registration"}
            and self.licence_state == "approved"
            and self.privacy_risk < 0.50
            and self.contamination_risk < 0.50
        )


def protocol_for_domain(domain: str) -> Tuple[str, ...]:
    try:
        return VALIDATION_PROTOCOLS[domain]
    except KeyError as exc:
        raise ValueError(f"unsupported cognitive domain: {domain}") from exc


def validate_dataset_mapping(dataset: CognitiveValidationDataset) -> Tuple[str, ...]:
    issues = []
    unknown = sorted(set(dataset.cognitive_domains) - set(COGNITIVE_DOMAIN_TAXONOMY))
    if unknown:
        issues.append("unknown_domains:" + ",".join(unknown))
    if dataset.licence_state not in {"approved", "unclear", "restricted", "prohibited"}:
        issues.append("invalid_licence_state")
    if dataset.privacy_risk >= 0.70:
        issues.append("high_privacy_risk")
    if dataset.contamination_risk >= 0.70:
        issues.append("high_contamination_risk")
    if dataset.clinical_claims_allowed:
        issues.append("clinical_claims_require_separate_governance")
    return tuple(issues)
