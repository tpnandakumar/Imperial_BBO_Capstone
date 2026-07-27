"""Approved source registry for PFRAMOS Training Scout.

Source approval allows discovery only. Individual datasets still require
licence, provenance, privacy, contamination and quality validation.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class TrainingSource:
    source_id: str
    display_name: str
    discovery_method: str
    authentication_required: bool
    supports_version_pinning: bool
    supports_partial_download: bool
    default_trust: float
    permitted_uses: Tuple[str, ...]

    def __post_init__(self) -> None:
        if not 0.0 <= self.default_trust <= 1.0:
            raise ValueError("default_trust must be between 0 and 1")


APPROVED_SOURCES = {
    "github": TrainingSource(
        source_id="github",
        display_name="GitHub",
        discovery_method="repository and file search",
        authentication_required=False,
        supports_version_pinning=True,
        supports_partial_download=True,
        default_trust=0.55,
        permitted_uses=("discovery", "metadata", "approved_dataset_download"),
    ),
    "kaggle": TrainingSource(
        source_id="kaggle",
        display_name="Kaggle",
        discovery_method="official Kaggle CLI",
        authentication_required=True,
        supports_version_pinning=True,
        supports_partial_download=True,
        default_trust=0.65,
        permitted_uses=("discovery", "metadata", "approved_dataset_download"),
    ),
    "huggingface": TrainingSource(
        source_id="huggingface",
        display_name="Hugging Face Datasets",
        discovery_method="Hub API and datasets library",
        authentication_required=False,
        supports_version_pinning=True,
        supports_partial_download=True,
        default_trust=0.65,
        permitted_uses=("discovery", "metadata", "streaming", "approved_dataset_download"),
    ),
}


def get_source(source_id: str) -> TrainingSource:
    try:
        return APPROVED_SOURCES[source_id.lower()]
    except KeyError as exc:
        raise ValueError(f"Unapproved training source: {source_id}") from exc


def source_eligible_for_download(source_id: str) -> bool:
    source = get_source(source_id)
    return "approved_dataset_download" in source.permitted_uses
