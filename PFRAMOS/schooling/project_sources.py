"""Project-owned schooling source registry.

These sources are approved in principle because they are controlled by the
project owner. Individual records still require integrity, privacy, temporal
and task-suitability checks before training.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class ProjectSchoolingSource:
    source_id: str
    display_name: str
    source_kind: str
    repository: str
    authorised: bool
    ingestion_status: str
    permitted_lanes: Tuple[str, ...]
    excluded_content: Tuple[str, ...]
    temporal_order_required: bool
    protected_test_required: bool

    def __post_init__(self) -> None:
        allowed_status = {
            "active",
            "authorised_pending_connector",
            "quarantined",
            "disabled",
        }
        if self.ingestion_status not in allowed_status:
            raise ValueError("invalid ingestion_status")
        if not self.permitted_lanes:
            raise ValueError("at least one permitted lane is required")

    @property
    def ready_for_ingestion(self) -> bool:
        return self.authorised and self.ingestion_status == "active"


PROJECT_SCHOOLING_SOURCES = {
    "imperial_bbo_current": ProjectSchoolingSource(
        source_id="imperial_bbo_current",
        display_name="Current Imperial BBO Corpus",
        source_kind="sequential_optimisation",
        repository="tpnandakumar/Imperial_BBO_Capstone",
        authorised=True,
        ingestion_status="active",
        permitted_lanes=(
            "optimisation",
            "efficiency",
            "emergence",
            "reasoning",
        ),
        excluded_content=(
            "unsubmitted private candidate coordinates",
            "protected future outputs",
            "live submission secrets",
        ),
        temporal_order_required=True,
        protected_test_required=True,
    ),
    "honeycomb_publications": ProjectSchoolingSource(
        source_id="honeycomb_publications",
        display_name="Honeycomb Publications Corpus",
        source_kind="publishing_and_language",
        repository="tpnandakumar/honeycombpublications-site",
        authorised=True,
        ingestion_status="authorised_pending_connector",
        permitted_lanes=(
            "reasoning",
            "bias",
            "emergence",
        ),
        excluded_content=(
            "unpublished manuscripts without explicit inclusion",
            "personal correspondence",
            "contracts and financial records",
            "third-party copyrighted material without training permission",
            "private medical or personal information",
        ),
        temporal_order_required=False,
        protected_test_required=True,
    ),
}


def get_project_source(source_id: str) -> ProjectSchoolingSource:
    try:
        return PROJECT_SCHOOLING_SOURCES[source_id]
    except KeyError as exc:
        raise ValueError(f"unknown project schooling source: {source_id}") from exc


def active_project_sources() -> Tuple[ProjectSchoolingSource, ...]:
    return tuple(source for source in PROJECT_SCHOOLING_SOURCES.values() if source.ready_for_ingestion)
