"""Assess whether a weak technology candidate can be moulded into a strong node.

A candidate may improve through partial adoption, simplification, constraint,
role reassignment, combination with another node, or decomposition into useful
subcomponents. Mouldability does not authorise integration.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class MouldabilityAssessment:
    candidate_id: str
    core_idea_strength: float
    modularity: float
    decomposability: float
    constraint_responsiveness: float
    recombination_potential: float
    role_reassignment_potential: float
    repair_cost: float
    residual_risk: float
    proposed_modulations: Tuple[str, ...]

    def __post_init__(self) -> None:
        for name, value in self.__dict__.items():
            if name in {"candidate_id", "proposed_modulations"}:
                continue
            if not 0.0 <= value <= 1.0:
                raise ValueError(f"{name} must be between 0 and 1")

    @property
    def mouldability_score(self) -> float:
        positive = (
            0.22 * self.core_idea_strength
            + 0.16 * self.modularity
            + 0.16 * self.decomposability
            + 0.14 * self.constraint_responsiveness
            + 0.14 * self.recombination_potential
            + 0.10 * self.role_reassignment_potential
        )
        penalties = 0.05 * self.repair_cost + 0.03 * self.residual_risk
        return max(0.0, min(1.0, positive - penalties))

    @property
    def disposition(self) -> str:
        if self.residual_risk >= 0.80:
            return "reject_despite_mouldability"
        if self.mouldability_score >= 0.72:
            return "send_to_modulation_lab"
        if self.mouldability_score >= 0.55:
            return "retain_for_recombination"
        return "archive_low_mouldability"


def rescue_priority(current_quality: float, assessment: MouldabilityAssessment) -> float:
    """Prioritise weak candidates with strong latent potential, not already strong ones."""
    latent_gain = max(0.0, assessment.mouldability_score - current_quality)
    return latent_gain * (1.0 - assessment.repair_cost) * (1.0 - assessment.residual_risk)
