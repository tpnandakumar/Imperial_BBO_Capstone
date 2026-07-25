"""Contextual emotional appraisal for PGC.

The appraisal describes probable significance and response needs. It does not
claim access to another person's internal emotional state.
"""

from __future__ import annotations

from dataclasses import dataclass

from .multimodal_fusion import FusedPerception


@dataclass(frozen=True)
class EmotionalAppraisal:
    valence: float
    arousal: float
    urgency: float
    threat: float
    trust: float
    empathy_need: float
    uncertainty: float
    factual_support: float


def _bounded(value: float, name: str) -> float:
    if not 0.0 <= value <= 1.0:
        raise ValueError(f"{name} must be within [0, 1]")
    return value


def interpret_emotional_signal(
    perception: FusedPerception,
    *,
    social_significance: float = 0.5,
    stated_distress: float = 0.0,
    trust_signal: float = 0.5,
    negative_valence_signal: float | None = None,
) -> EmotionalAppraisal:
    social = _bounded(social_significance, "social_significance")
    distress = _bounded(stated_distress, "stated_distress")
    trust_value = _bounded(trust_signal, "trust_signal")
    negative_valence = (
        perception.emotional_estimate
        if negative_valence_signal is None
        else _bounded(negative_valence_signal, "negative_valence_signal")
    )

    factual_support = min(1.0, perception.factual_estimate * perception.evidence_strength)
    conflict_penalty = min(1.0, perception.factual_conflict + perception.emotional_conflict)
    uncertainty = min(1.0, (1.0 - perception.evidence_strength) + 0.5 * conflict_penalty)

    threat = min(
        1.0,
        0.65 * factual_support + 0.25 * perception.emotional_estimate + 0.10 * distress,
    )
    urgency = min(
        1.0,
        0.55 * threat + 0.25 * distress + 0.20 * perception.emotional_estimate,
    )
    arousal = min(1.0, 0.55 * perception.emotional_estimate + 0.30 * distress + 0.15 * social)
    empathy_need = min(1.0, 0.50 * distress + 0.30 * social + 0.20 * perception.emotional_estimate)
    valence = max(-1.0, min(1.0, 1.0 - 2.0 * negative_valence))

    return EmotionalAppraisal(
        valence=valence,
        arousal=arousal,
        urgency=urgency,
        threat=threat,
        trust=trust_value,
        empathy_need=empathy_need,
        uncertainty=uncertainty,
        factual_support=factual_support,
    )
