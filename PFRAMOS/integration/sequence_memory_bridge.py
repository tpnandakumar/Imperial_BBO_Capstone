"""Auditable bridge between PFRAMOS, PIMF and the BBO engine.

Responsibilities remain separated:

* PIMF diagnoses influence, persistence and higher-order change.
* PFRAMOS selects, regulates and routes candidate memory actions.
* The BBO engine applies approved state retention and forgetting policies.

No architecture candidate is activated automatically.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Tuple


@dataclass(frozen=True)
class SequenceMemorySignal:
    signal_id: str
    source_architecture: str
    current_value: float
    delta_d: float
    delta2_d: float
    delta3_d: float
    persistence: float
    surprise: float
    coherence: float
    uncertainty: float
    contamination_risk: float

    def __post_init__(self) -> None:
        for name in (
            "persistence",
            "surprise",
            "coherence",
            "uncertainty",
            "contamination_risk",
        ):
            value = getattr(self, name)
            if not 0.0 <= value <= 1.0:
                raise ValueError(f"{name} must be between 0 and 1")


@dataclass(frozen=True)
class PIMFMemoryDiagnosis:
    signal_id: str
    influence_state: str
    directional_signature: str
    persistence_score: float
    reversal_risk: float
    recommendation: str


@dataclass(frozen=True)
class PFRAMOSMemoryDecision:
    signal_id: str
    action: str
    selected_conduit: str
    retention_weight: float
    forgetting_weight: float
    shadow_only: bool
    rationale: Tuple[str, ...]


@dataclass(frozen=True)
class BBOStateUpdate:
    signal_id: str
    function_id: str
    memory_slot: str
    retained_features: Mapping[str, float]
    forgetting_weight: float
    approved: bool
    audit_reference: str


def diagnose_with_pimf(signal: SequenceMemorySignal) -> PIMFMemoryDiagnosis:
    if signal.contamination_risk >= 0.70:
        state = "Boundary"
        recommendation = "quarantine"
    elif signal.delta_d * signal.delta2_d < 0 and abs(signal.delta3_d) > 0.20:
        state = "Reversal"
        recommendation = "retain_for_reversal_analysis"
    elif signal.persistence >= 0.75 and signal.coherence >= 0.70:
        state = "MaxInflu"
        recommendation = "eligible_for_selective_retention"
    elif signal.surprise >= 0.75 and signal.coherence >= 0.55:
        state = "Emerging"
        recommendation = "shadow_memory_candidate"
    elif abs(signal.delta_d) < 0.05 and abs(signal.delta2_d) < 0.05:
        state = "Plateau"
        recommendation = "increase_forgetting_or_exploration"
    else:
        state = "Oscillation"
        recommendation = "observe_and_stabilise"

    if signal.delta_d > 0 and signal.delta2_d > 0:
        direction = "accelerating_positive"
    elif signal.delta_d < 0 and signal.delta2_d < 0:
        direction = "accelerating_negative"
    elif signal.delta_d * signal.delta2_d < 0:
        direction = "directional_conflict"
    else:
        direction = "weak_or_stable"

    reversal_risk = min(1.0, abs(signal.delta2_d - signal.delta_d) + signal.uncertainty)
    return PIMFMemoryDiagnosis(
        signal_id=signal.signal_id,
        influence_state=state,
        directional_signature=direction,
        persistence_score=signal.persistence,
        reversal_risk=reversal_risk,
        recommendation=recommendation,
    )


def regulate_with_pframos(
    signal: SequenceMemorySignal,
    diagnosis: PIMFMemoryDiagnosis,
) -> PFRAMOSMemoryDecision:
    reasons = [diagnosis.influence_state, diagnosis.recommendation]

    if diagnosis.recommendation == "quarantine":
        return PFRAMOSMemoryDecision(
            signal_id=signal.signal_id,
            action="quarantine",
            selected_conduit="none",
            retention_weight=0.0,
            forgetting_weight=1.0,
            shadow_only=True,
            rationale=tuple(reasons),
        )

    retention = (
        0.35 * signal.persistence
        + 0.30 * signal.coherence
        + 0.20 * signal.surprise
        + 0.15 * (1.0 - signal.uncertainty)
    )
    retention *= 1.0 - signal.contamination_risk
    retention = max(0.0, min(1.0, retention))
    forgetting = max(0.0, min(1.0, 1.0 - retention))

    if diagnosis.influence_state == "MaxInflu" and retention >= 0.65:
        action = "selective_retain"
        conduit = "maximum_coherence_memory_conduit"
        shadow = True
    elif diagnosis.influence_state == "Emerging":
        action = "surprise_weighted_shadow_update"
        conduit = "emergent_memory_conduit"
        shadow = True
    elif diagnosis.influence_state == "Plateau":
        action = "adaptive_forgetting"
        conduit = "exploration_recovery_conduit"
        shadow = True
    else:
        action = "observe_without_update"
        conduit = "diagnostic_conduit"
        shadow = True

    return PFRAMOSMemoryDecision(
        signal_id=signal.signal_id,
        action=action,
        selected_conduit=conduit,
        retention_weight=retention,
        forgetting_weight=forgetting,
        shadow_only=shadow,
        rationale=tuple(reasons),
    )


def prepare_bbo_state_update(
    function_id: str,
    signal: SequenceMemorySignal,
    diagnosis: PIMFMemoryDiagnosis,
    decision: PFRAMOSMemoryDecision,
    audit_reference: str,
) -> BBOStateUpdate:
    approved = (
        decision.action in {"selective_retain", "adaptive_forgetting"}
        and not decision.shadow_only
        and signal.contamination_risk < 0.30
        and diagnosis.reversal_risk < 0.60
    )

    features = {
        "current_value": signal.current_value,
        "delta_d": signal.delta_d,
        "delta2_d": signal.delta2_d,
        "delta3_d": signal.delta3_d,
        "persistence": signal.persistence,
        "surprise": signal.surprise,
        "coherence": signal.coherence,
        "retention_weight": decision.retention_weight,
    }

    return BBOStateUpdate(
        signal_id=signal.signal_id,
        function_id=function_id,
        memory_slot=f"{function_id}:{signal.source_architecture}",
        retained_features=features,
        forgetting_weight=decision.forgetting_weight,
        approved=approved,
        audit_reference=audit_reference,
    )
