"""Data contracts and recruitment scoring for technology sweep candidates."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class ResearchCandidate:
    candidate_id: str
    title: str
    source: str
    source_url: str
    published_at: str
    abstract: str
    categories: Tuple[str, ...]
    relevance: float
    novelty: float
    maturity: float
    reproducibility: float
    evidence_quality: float
    transferability: float
    compute_efficiency: float
    energy_efficiency: float
    safety: float
    non_duplication: float

    def __post_init__(self) -> None:
        for field_name in (
            "relevance",
            "novelty",
            "maturity",
            "reproducibility",
            "evidence_quality",
            "transferability",
            "compute_efficiency",
            "energy_efficiency",
            "safety",
            "non_duplication",
        ):
            value = getattr(self, field_name)
            if not 0.0 <= value <= 1.0:
                raise ValueError(f"{field_name} must be between 0 and 1")

    @property
    def recruitment_score(self) -> float:
        positive = (
            0.20 * self.relevance
            + 0.10 * self.novelty
            + 0.10 * self.maturity
            + 0.12 * self.reproducibility
            + 0.15 * self.evidence_quality
            + 0.12 * self.transferability
            + 0.06 * self.compute_efficiency
            + 0.05 * self.energy_efficiency
            + 0.05 * self.safety
            + 0.05 * self.non_duplication
        )
        return max(0.0, min(1.0, positive))

    @property
    def recruitment_state(self) -> str:
        if self.evidence_quality < 0.40 or self.safety < 0.40:
            return "rejected"
        if self.recruitment_score >= 0.78 and self.reproducibility >= 0.60:
            return "experimental_node_candidate"
        if self.recruitment_score >= 0.60:
            return "quarantined_candidate"
        return "screened_only"
