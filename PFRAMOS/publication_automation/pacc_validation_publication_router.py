"""Route PACC cognitive-network validation evidence into paper publications."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple


PACC_PAPER_TRACKS = {
    "PACC-P1": "foundations_and_mathematical_state_model",
    "PACC-P2": "computational_memory_circuit",
    "PACC-P3": "computational_semantic_cognition",
    "PACC-P4": "computational_visuospatial_cognition",
    "PACC-P5": "executive_control_abstraction_and_flexibility",
    "PACC-P6": "social_behavioural_and_metacognitive_cognition",
    "PACC-P7": "acquired_cognitive_development",
    "PACC-P8": "integrated_functional_cognitive_network_validation",
}


@dataclass(frozen=True)
class CognitiveValidationResult:
    result_id: str
    dataset_id: str
    cognitive_domains: Tuple[str, ...]
    validation_protocols: Tuple[str, ...]
    data_forms: Tuple[str, ...]
    has_dataset_manifest: bool
    has_model_version: bool
    has_protected_test: bool
    has_pimf_analysis: bool
    has_pframos_decision: bool
    reproducible: bool
    clinical_claim: bool = False


@dataclass(frozen=True)
class CognitivePaperAssignment:
    result_id: str
    primary_paper: str
    secondary_papers: Tuple[str, ...]
    state: str
    blockers: Tuple[str, ...]


def _domain_owner(domain: str) -> str:
    if domain in {"attention", "working_memory", "episodic_memory", "retrieval_and_recall"}:
        return "PACC-P2"
    if domain in {"semantic_memory", "naming_and_object_knowledge", "language", "verbal_fluency"}:
        return "PACC-P3"
    if domain in {"visuospatial_cognition", "praxis", "calculation"}:
        return "PACC-P4"
    if domain in {"executive_control", "abstraction", "orientation_and_context"}:
        return "PACC-P5"
    if domain in {"social_cognition", "emotion_recognition", "behaviour_and_motivation", "metacognition"}:
        return "PACC-P6"
    return "PACC-P8"


def route_cognitive_validation(result: CognitiveValidationResult) -> CognitivePaperAssignment:
    blockers = []
    if not result.has_dataset_manifest:
        blockers.append("missing_dataset_manifest")
    if not result.has_model_version:
        blockers.append("missing_model_version")
    if not result.has_protected_test:
        blockers.append("missing_protected_test")
    if not result.has_pimf_analysis:
        blockers.append("missing_pimf_analysis")
    if not result.has_pframos_decision:
        blockers.append("missing_pframos_decision")
    if not result.reproducible:
        blockers.append("not_reproducible")
    if result.clinical_claim:
        blockers.append("clinical_claim_requires_separate_validation")

    owners = tuple(sorted({_domain_owner(domain) for domain in result.cognitive_domains}))
    if len(owners) == 1:
        primary = owners[0]
        secondary = ("PACC-P8",) if primary != "PACC-P8" else ()
    else:
        primary = "PACC-P8"
        secondary = owners

    state = "evidence_ready" if not blockers else "evidence_incomplete"
    return CognitivePaperAssignment(
        result_id=result.result_id,
        primary_paper=primary,
        secondary_papers=secondary,
        state=state,
        blockers=tuple(blockers),
    )
