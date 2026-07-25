"""Governed modality registry for coordinated PGC perception and emotion."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class ModalityDefinition:
    modality_id: str
    signal_types: Tuple[str, ...]
    minimum_reliability: float
    privacy_risk: str
    temporal: bool
    emotional_relevance: Tuple[str, ...]
    required_controls: Tuple[str, ...]


MODALITIES = (
    ModalityDefinition(
        modality_id="language",
        signal_types=("semantic_content", "intent", "ambiguity", "emotion_expression"),
        minimum_reliability=0.55,
        privacy_risk="medium",
        temporal=True,
        emotional_relevance=("valence", "urgency", "trust", "distress"),
        required_controls=("source_provenance", "negation_check", "sarcasm_uncertainty", "language_context"),
    ),
    ModalityDefinition(
        modality_id="vision",
        signal_types=("object", "scene", "spatial_relation", "facial_or_postural_cue"),
        minimum_reliability=0.60,
        privacy_risk="high",
        temporal=False,
        emotional_relevance=("threat", "social_significance", "distress_cue"),
        required_controls=("consent_or_lawful_basis", "occlusion_check", "demographic_bias_test", "scene_context"),
    ),
    ModalityDefinition(
        modality_id="audio",
        signal_types=("speech_prosody", "environmental_event", "rhythm", "intensity"),
        minimum_reliability=0.55,
        privacy_risk="high",
        temporal=True,
        emotional_relevance=("arousal", "urgency", "distress", "confidence"),
        required_controls=("noise_estimate", "speaker_uncertainty", "consent_or_lawful_basis", "event_context"),
    ),
    ModalityDefinition(
        modality_id="video",
        signal_types=("motion", "action", "continuity", "interaction"),
        minimum_reliability=0.60,
        privacy_risk="high",
        temporal=True,
        emotional_relevance=("threat_trajectory", "social_interaction", "distress_progression"),
        required_controls=("frame_continuity", "identity_minimisation", "scene_context", "temporal_bias_test"),
    ),
    ModalityDefinition(
        modality_id="spatial",
        signal_types=("distance", "orientation", "proximity", "navigation_state"),
        minimum_reliability=0.65,
        privacy_risk="medium",
        temporal=True,
        emotional_relevance=("personal_space", "approach_or_avoidance", "environmental_threat"),
        required_controls=("coordinate_uncertainty", "sensor_calibration", "location_minimisation"),
    ),
    ModalityDefinition(
        modality_id="temporal",
        signal_types=("sequence", "duration", "rhythm", "change_rate"),
        minimum_reliability=0.60,
        privacy_risk="low",
        temporal=True,
        emotional_relevance=("persistence", "escalation", "recovery", "instability"),
        required_controls=("clock_alignment", "missing_interval_check", "change_point_validation"),
    ),
    ModalityDefinition(
        modality_id="social",
        signal_types=("interaction", "role", "trust_signal", "conflict_signal"),
        minimum_reliability=0.55,
        privacy_risk="high",
        temporal=True,
        emotional_relevance=("empathy_need", "trust", "conflict", "attachment"),
        required_controls=("cultural_uncertainty", "role_uncertainty", "stereotype_guard", "consent_or_lawful_basis"),
    ),
    ModalityDefinition(
        modality_id="internal_state",
        signal_types=("confidence", "uncertainty", "memory_load", "goal_conflict"),
        minimum_reliability=0.50,
        privacy_risk="low",
        temporal=True,
        emotional_relevance=("cognitive_tension", "overconfidence", "instability", "fatigue_proxy"),
        required_controls=("calibration", "self_report_as_inference", "no_consciousness_claim"),
    ),
)


def modality_by_id(modality_id: str) -> ModalityDefinition:
    for modality in MODALITIES:
        if modality.modality_id == modality_id:
            return modality
    raise ValueError(f"unknown modality: {modality_id}")


def eligible_modalities(reliability: float) -> Tuple[ModalityDefinition, ...]:
    if not 0.0 <= reliability <= 1.0:
        raise ValueError("reliability must be within [0, 1]")
    return tuple(item for item in MODALITIES if reliability >= item.minimum_reliability)
