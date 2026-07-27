"""Evidence-subordinate emotional balance regulation for PGC."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class BalanceInput:
    factual_support: float
    threat: float
    urgency: float
    empathy_need: float
    uncertainty: float
    factual_accuracy: float
    safety: float
    proportionality: float
    phcs_coherence: float


@dataclass(frozen=True)
class BalanceDecision:
    action: str
    response_intensity: float
    empathy_level: float
    balance_score: float
    blocked: bool
    reasons: Tuple[str, ...]


def _bounded(value: float, name: str) -> float:
    if not 0.0 <= value <= 1.0:
        raise ValueError(f"{name} must be within [0, 1]")
    return value


def regulate_balance(balance_input: BalanceInput) -> BalanceDecision:
    values = {
        name: _bounded(getattr(balance_input, name), name)
        for name in (
            "factual_support",
            "threat",
            "urgency",
            "empathy_need",
            "uncertainty",
            "factual_accuracy",
            "safety",
            "proportionality",
            "phcs_coherence",
        )
    }

    reasons: list[str] = []
    if values["factual_accuracy"] < 0.55:
        reasons.append("insufficient_factual_accuracy")
    if values["safety"] < 0.65:
        reasons.append("safety_gate_failed")
    if values["proportionality"] < 0.50:
        reasons.append("proportionality_gate_failed")
    if values["phcs_coherence"] < 0.45:
        reasons.append("phcs_coherence_below_gate")

    blocked = bool(reasons)
    if blocked:
        return BalanceDecision(
            action="abstain_and_review",
            response_intensity=0.0,
            empathy_level=min(0.75, values["empathy_need"]),
            balance_score=0.0,
            blocked=True,
            reasons=tuple(reasons),
        )

    factual = values["factual_support"]
    emotional_pressure = 0.55 * values["threat"] + 0.45 * values["urgency"]
    calibrated_pressure = emotional_pressure * (0.45 + 0.55 * factual)
    response_intensity = min(1.0, calibrated_pressure * (1.0 - 0.35 * values["uncertainty"]))
    empathy_level = min(1.0, values["empathy_need"] * (0.75 + 0.25 * values["phcs_coherence"]))

    if factual >= 0.75 and values["threat"] >= 0.70:
        action = "urgent_response"
    elif factual >= 0.60 and values["threat"] >= 0.45:
        action = "caution"
    elif empathy_level >= 0.60 and factual < 0.60:
        action = "support"
    elif values["uncertainty"] >= 0.45 or (values["threat"] >= 0.60 and factual < 0.50):
        action = "clarify"
    else:
        action = "observe"

    evidence_emotion_alignment = 1.0 - abs(factual - response_intensity)
    balance_score = min(
        1.0,
        0.30 * evidence_emotion_alignment
        + 0.20 * values["proportionality"]
        + 0.20 * values["phcs_coherence"]
        + 0.15 * values["factual_accuracy"]
        + 0.15 * values["safety"],
    )

    return BalanceDecision(
        action=action,
        response_intensity=response_intensity,
        empathy_level=empathy_level,
        balance_score=balance_score,
        blocked=False,
        reasons=(),
    )
