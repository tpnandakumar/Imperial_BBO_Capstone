"""Emergent behaviour synthesis, bias-vector modulation and laminar route discovery.

This module treats unexpected behaviour as evidence that may reveal latent
capability, hidden node coupling or a more efficient conduit. It does not
promote emergent behaviour automatically.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import sqrt
from typing import Tuple


@dataclass(frozen=True)
class BehaviourVector:
    behaviour_id: str
    magnitude: float
    direction: Tuple[float, ...]
    confidence: float
    coherence: float
    persistence: float
    risk: float
    compute_cost: float
    variance: float

    def __post_init__(self) -> None:
        if not self.direction:
            raise ValueError("direction cannot be empty")
        for name in (
            "magnitude",
            "confidence",
            "coherence",
            "persistence",
            "risk",
            "compute_cost",
            "variance",
        ):
            value = getattr(self, name)
            if not 0.0 <= value <= 1.0:
                raise ValueError(f"{name} must be between 0 and 1")

    @property
    def norm(self) -> float:
        return sqrt(sum(component * component for component in self.direction))


@dataclass(frozen=True)
class BiasVectorAssessment:
    vector: BehaviourVector
    bias_class: str
    harmful_distortion: float
    productive_potential: float
    contextuality: float
    modulations: Tuple[str, ...]

    def __post_init__(self) -> None:
        allowed = {
            "data_bias",
            "representation_bias",
            "measurement_bias",
            "selection_bias",
            "confirmation_bias",
            "routing_bias",
            "optimisation_bias",
            "emergent_bias",
            "productive_inductive_bias",
            "contextual_bias",
        }
        if self.bias_class not in allowed:
            raise ValueError("invalid bias_class")
        for name in ("harmful_distortion", "productive_potential", "contextuality"):
            value = getattr(self, name)
            if not 0.0 <= value <= 1.0:
                raise ValueError(f"{name} must be between 0 and 1")

    @property
    def action(self) -> str:
        if self.vector.risk >= 0.80 or self.harmful_distortion >= 0.80:
            return "suppress_or_quarantine"
        if self.productive_potential >= 0.70 and self.contextuality >= 0.50:
            return "repurpose_conditionally"
        if self.productive_potential >= 0.60:
            return "redirect_and_validate"
        if self.harmful_distortion >= 0.50:
            return "counterbalance"
        return "observe"


@dataclass(frozen=True)
class EmergentCombination:
    combination_id: str
    vectors: Tuple[BehaviourVector, ...]
    compatibility: float
    synergy: float
    stabilisation: float
    novelty: float
    routing_gain: float
    residual_risk: float

    def __post_init__(self) -> None:
        if len(self.vectors) < 2:
            raise ValueError("at least two behaviour vectors are required")
        dimensions = {len(vector.direction) for vector in self.vectors}
        if len(dimensions) != 1:
            raise ValueError("all behaviour vectors must have equal dimensions")
        for name in (
            "compatibility",
            "synergy",
            "stabilisation",
            "novelty",
            "routing_gain",
            "residual_risk",
        ):
            value = getattr(self, name)
            if not 0.0 <= value <= 1.0:
                raise ValueError(f"{name} must be between 0 and 1")

    @property
    def compound_capability_score(self) -> float:
        positive = (
            0.24 * self.compatibility
            + 0.24 * self.synergy
            + 0.16 * self.stabilisation
            + 0.16 * self.novelty
            + 0.20 * self.routing_gain
        )
        penalty = 0.25 * self.residual_risk
        return max(0.0, min(1.0, positive - penalty))

    @property
    def disposition(self) -> str:
        if self.residual_risk >= 0.80:
            return "quarantine_combination"
        if self.compound_capability_score >= 0.72:
            return "build_candidate_conduit"
        if self.compound_capability_score >= 0.55:
            return "retain_for_modulation"
        return "archive_combination"


@dataclass(frozen=True)
class LaminarConduitAssessment:
    conduit_id: str
    validated_capability_gain: float
    coherence: float
    robustness: float
    compute_cost: float
    routing_friction: float
    variance: float
    reproducibility: float
    residual_risk: float

    def __post_init__(self) -> None:
        for name, value in self.__dict__.items():
            if name == "conduit_id":
                continue
            if not 0.0 <= value <= 1.0:
                raise ValueError(f"{name} must be between 0 and 1")

    @property
    def laminar_efficiency(self) -> float:
        numerator = (
            self.validated_capability_gain
            * self.coherence
            * self.robustness
            * self.reproducibility
        )
        denominator = 1.0 + self.compute_cost + self.routing_friction + self.variance
        risk_penalty = 1.0 - self.residual_risk
        return max(0.0, min(1.0, (numerator / denominator) * risk_penalty))

    @property
    def promotion_state(self) -> str:
        if self.residual_risk >= 0.75:
            return "reject"
        if self.laminar_efficiency >= 0.35:
            return "shadow_validate"
        if self.laminar_efficiency >= 0.20:
            return "experimental_only"
        return "insufficient_gain"


def exploration_randomness_budget(
    uncertainty: float,
    stagnation: float,
    disagreement: float,
    novelty_deficit: float,
    risk: float,
    decision_proximity: float,
) -> float:
    """Return a bounded stochastic exploration budget between 0 and 1."""
    for value in (
        uncertainty,
        stagnation,
        disagreement,
        novelty_deficit,
        risk,
        decision_proximity,
    ):
        if not 0.0 <= value <= 1.0:
            raise ValueError("all inputs must be between 0 and 1")

    exploration_pressure = (
        0.30 * uncertainty
        + 0.25 * stagnation
        + 0.20 * disagreement
        + 0.25 * novelty_deficit
    )
    suppression = 0.55 * risk + 0.45 * decision_proximity
    return max(0.0, min(1.0, exploration_pressure * (1.0 - suppression)))
