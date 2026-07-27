"""Competition Scout for official machine-learning challenge platforms.

Competition discovery is permitted, but every competition remains governed by
its own rules, licence and data-use restrictions. Hidden test data must never
enter training.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Tuple


@dataclass(frozen=True)
class CompetitionPlatform:
    platform_id: str
    display_name: str
    official_domain: str
    supports_public_rules: bool
    supports_leaderboard: bool
    supports_api_or_cli: bool
    default_trust: float

    def __post_init__(self) -> None:
        if not 0.0 <= self.default_trust <= 1.0:
            raise ValueError("default_trust must be between 0 and 1")


OFFICIAL_PLATFORMS = {
    "kaggle": CompetitionPlatform("kaggle", "Kaggle", "kaggle.com", True, True, True, 0.80),
    "drivendata": CompetitionPlatform("drivendata", "DrivenData", "drivendata.org", True, True, False, 0.80),
    "zindi": CompetitionPlatform("zindi", "Zindi", "zindi.africa", True, True, False, 0.75),
    "aicrowd": CompetitionPlatform("aicrowd", "AIcrowd", "aicrowd.com", True, True, True, 0.75),
    "codalab": CompetitionPlatform("codalab", "CodaLab", "codalab.lisn.upsaclay.fr", True, True, False, 0.70),
}


@dataclass(frozen=True)
class CompetitionCandidate:
    competition_id: str
    platform_id: str
    title: str
    rules_url: str
    discovered_at: datetime
    start_at: datetime | None
    end_at: datetime | None
    dataset_use_class: str
    licence_clear: bool
    external_data_allowed: bool | None
    team_sharing_allowed: bool | None
    submission_automation_allowed: bool | None
    hidden_test_present: bool
    benchmark_value: float
    domain_relevance: float
    reproducibility: float
    documentation_quality: float
    compute_affordability: float
    legal_risk: float
    privacy_risk: float
    contamination_risk: float
    rules_complete: bool

    def __post_init__(self) -> None:
        if self.platform_id not in OFFICIAL_PLATFORMS:
            raise ValueError(f"Unsupported platform: {self.platform_id}")
        allowed_classes = {"open_learning", "competition_only", "restricted", "unclear"}
        if self.dataset_use_class not in allowed_classes:
            raise ValueError("Invalid dataset_use_class")
        for name in (
            "benchmark_value",
            "domain_relevance",
            "reproducibility",
            "documentation_quality",
            "compute_affordability",
            "legal_risk",
            "privacy_risk",
            "contamination_risk",
        ):
            value = getattr(self, name)
            if not 0.0 <= value <= 1.0:
                raise ValueError(f"{name} must be between 0 and 1")

    @property
    def hard_blocks(self) -> Tuple[str, ...]:
        blocks = []
        if not self.rules_complete:
            blocks.append("competition rules incomplete")
        if not self.licence_clear:
            blocks.append("licence or data-use rights unclear")
        if self.dataset_use_class in {"restricted", "unclear"}:
            blocks.append("dataset not approved for schooling")
        if self.legal_risk >= 0.60:
            blocks.append("legal risk too high")
        if self.privacy_risk >= 0.50:
            blocks.append("privacy risk too high")
        if self.contamination_risk >= 0.70:
            blocks.append("benchmark contamination risk too high")
        return tuple(blocks)

    @property
    def suitability_score(self) -> float:
        platform = OFFICIAL_PLATFORMS[self.platform_id]
        positive = (
            0.18 * platform.default_trust
            + 0.24 * self.benchmark_value
            + 0.24 * self.domain_relevance
            + 0.12 * self.reproducibility
            + 0.10 * self.documentation_quality
            + 0.08 * self.compute_affordability
        )
        penalties = 0.02 * self.legal_risk + 0.01 * self.privacy_risk + 0.01 * self.contamination_risk
        return max(0.0, min(1.0, positive - penalties))

    @property
    def schooling_permission(self) -> str:
        if self.hard_blocks:
            return "restricted_or_quarantine"
        if self.dataset_use_class == "open_learning":
            return "eligible_for_schooling_validation"
        if self.dataset_use_class == "competition_only":
            return "competition_sandbox_only"
        return "restricted_or_quarantine"

    @property
    def disposition(self) -> str:
        if self.hard_blocks:
            return "quarantine"
        if self.suitability_score >= 0.72:
            return "priority_external_exam"
        if self.suitability_score >= 0.55:
            return "retain_for_review"
        return "archive_low_value"


@dataclass(frozen=True)
class CompetitionResult:
    competition_id: str
    model_version: str
    submitted_at: datetime
    public_score: float | None
    private_score: float | None
    metric_name: str
    runtime_seconds: float
    peak_memory_mb: float
    estimated_energy_proxy: float
    submission_count: int

    @property
    def leaderboard_gap(self) -> float | None:
        if self.public_score is None or self.private_score is None:
            return None
        return abs(self.public_score - self.private_score)
