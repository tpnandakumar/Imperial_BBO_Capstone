"""Emotional cognitive coherence assessment for PGC."""

from __future__ import annotations

from dataclasses import dataclass
from statistics import fmean
from typing import Tuple


@dataclass(frozen=True)
class EmotionalCognitiveState:
    perceived_significance: float
    appraisal_intensity: float
    reasoning_intensity: float
    memory_intensity: float
    expression_intensity: float
    action_intensity: float
    factual_accuracy: float
    safety: float
    proportionality: float
    uncertainty_awareness: float


@dataclass(frozen=True)
class CoherenceAssessment:
    coherence_index: float
    agreement: float
    gate_score: float
    passed: bool
    conflicts: Tuple[str, ...]


def _bounded(value: float, name: str) -> float:
    if not 0.0 <= value <= 1.0:
        raise ValueError(f"{name} must be within [0, 1]")
    return value


def assess_coherence(
    state: EmotionalCognitiveState,
    *,
    minimum_factual_accuracy: float = 0.60,
    minimum_safety: float = 0.70,
    minimum_proportionality: float = 0.55,
) -> CoherenceAssessment:
    values = {
        field: _bounded(getattr(state, field), field)
        for field in (
            "perceived_significance",
            "appraisal_intensity",
            "reasoning_intensity",
            "memory_intensity",
            "expression_intensity",
            "action_intensity",
            "factual_accuracy",
            "safety",
            "proportionality",
            "uncertainty_awareness",
        )
    }

    cognitive_values = [
        values["perceived_significance"],
        values["appraisal_intensity"],
        values["reasoning_intensity"],
        values["memory_intensity"],
        values["expression_intensity"],
        values["action_intensity"],
    ]
    centre = fmean(cognitive_values)
    mean_absolute_deviation = fmean(abs(value - centre) for value in cognitive_values)
    agreement = max(0.0, 1.0 - 2.0 * mean_absolute_deviation)

    gate_score = min(
        values["factual_accuracy"],
        values["safety"],
        values["proportionality"],
        values["uncertainty_awareness"],
    )
    coherence_index = max(-1.0, min(1.0, 2.0 * (0.65 * agreement + 0.35 * gate_score) - 1.0))

    conflicts: list[str] = []
    if values["factual_accuracy"] < minimum_factual_accuracy:
        conflicts.append("factual_accuracy_below_gate")
    if values["safety"] < minimum_safety:
        conflicts.append("safety_below_gate")
    if values["proportionality"] < minimum_proportionality:
        conflicts.append("proportionality_below_gate")
    if abs(values["appraisal_intensity"] - values["action_intensity"]) > 0.40:
        conflicts.append("appraisal_action_mismatch")
    if abs(values["reasoning_intensity"] - values["action_intensity"]) > 0.35:
        conflicts.append("reasoning_action_mismatch")
    if values["uncertainty_awareness"] < 0.40:
        conflicts.append("uncertainty_underrepresented")

    passed = not conflicts and coherence_index >= 0.20
    return CoherenceAssessment(
        coherence_index=coherence_index,
        agreement=agreement,
        gate_score=gate_score,
        passed=passed,
        conflicts=tuple(conflicts),
    )
