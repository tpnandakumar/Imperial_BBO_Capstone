"""Previously tested technical evidence sources for PFRAMOS schooling.

These sources enter as historical validated evidence candidates, not as raw
unrestricted training corpora. Their prior tests, papers, artefacts and
project interpretations must remain traceable.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class HistoricalTechnologySource:
    source_id: str
    display_name: str
    evidence_class: str
    validation_state: str
    permitted_lanes: Tuple[str, ...]
    retained_material: Tuple[str, ...]
    required_checks: Tuple[str, ...]
    may_train_directly: bool

    def __post_init__(self) -> None:
        if self.validation_state not in {
            "previously_tested",
            "validated_historical",
            "pending_revalidation",
        }:
            raise ValueError("invalid validation_state")
        if not self.permitted_lanes:
            raise ValueError("at least one permitted lane is required")

    @property
    def eligible_for_schooling_review(self) -> bool:
        return self.validation_state in {"previously_tested", "validated_historical"}


HISTORICAL_TECHNOLOGY_SOURCES = {
    "hebo": HistoricalTechnologySource(
        source_id="hebo",
        display_name="HEBO",
        evidence_class="bayesian_optimisation_method",
        validation_state="previously_tested",
        permitted_lanes=("optimisation", "efficiency", "emergence", "reasoning"),
        retained_material=(
            "original paper and repository references",
            "project figures and explanatory analysis",
            "prior validation outcomes",
            "derived PFRAMOS comparisons",
        ),
        required_checks=(
            "version and commit pinning",
            "licence verification",
            "benchmark contamination review",
            "reproduction against frozen datasets",
        ),
        may_train_directly=False,
    ),
    "github": HistoricalTechnologySource(
        source_id="github",
        display_name="GitHub Technical Evidence",
        evidence_class="software_engineering_repositories_and_workflows",
        validation_state="previously_tested",
        permitted_lanes=("reasoning", "efficiency", "optimisation", "emergence"),
        retained_material=(
            "official GitHub documentation",
            "version-pinned public repositories",
            "workflow and CI evidence",
            "project repository history and reproducible commits",
        ),
        required_checks=(
            "repository-owner and source verification",
            "licence verification",
            "commit SHA pinning",
            "malicious code and supply-chain review",
            "dataset and benchmark contamination review",
        ),
        may_train_directly=False,
    ),
    "netflix": HistoricalTechnologySource(
        source_id="netflix",
        display_name="Netflix Technical Evidence",
        evidence_class="recommendation_and_large_scale_ml",
        validation_state="previously_tested",
        permitted_lanes=("reasoning", "efficiency", "bias", "emergence"),
        retained_material=(
            "official technical publications",
            "approved public datasets or benchmark references",
            "previous project analysis",
            "reproducible derived tests",
        ),
        required_checks=(
            "official-source confirmation",
            "dataset-specific licence verification",
            "privacy and user-data exclusion",
            "representation and selection-bias review",
        ),
        may_train_directly=False,
    ),
    "nvidia": HistoricalTechnologySource(
        source_id="nvidia",
        display_name="NVIDIA Technical Evidence",
        evidence_class="accelerated_computing_and_ai",
        validation_state="previously_tested",
        permitted_lanes=("efficiency", "optimisation", "emergence", "reasoning"),
        retained_material=(
            "official papers and technical reports",
            "approved model or dataset documentation",
            "previous project analysis",
            "compute and energy efficiency evidence",
        ),
        required_checks=(
            "official-source confirmation",
            "licence and usage verification",
            "hardware-specific assumption review",
            "independent reproduction where feasible",
        ),
        may_train_directly=False,
    ),
}


def get_historical_source(source_id: str) -> HistoricalTechnologySource:
    try:
        return HISTORICAL_TECHNOLOGY_SOURCES[source_id]
    except KeyError as exc:
        raise ValueError(f"unknown historical source: {source_id}") from exc


def historical_schooling_candidates() -> Tuple[HistoricalTechnologySource, ...]:
    return tuple(
        source
        for source in HISTORICAL_TECHNOLOGY_SOURCES.values()
        if source.eligible_for_schooling_review
    )
