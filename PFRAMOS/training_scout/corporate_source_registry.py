"""Official corporate and institutional data-source registry for Training Scout.

A listed organisation may be approved for discovery while individual datasets
remain subject to licence, provenance, privacy, contamination and relevance
checks. Absence of a verified catalogue keeps a company in watchlist status.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class CorporateDataSource:
    source_id: str
    organisation: str
    official_domain: str
    source_class: str
    catalogue_url: str | None
    discovery_priority: float
    supports_direct_dataset_access: bool
    supports_version_pinning: bool
    notes: Tuple[str, ...]

    def __post_init__(self) -> None:
        allowed = {
            "official_dataset_catalogue",
            "official_reference_kits",
            "official_model_and_data_releases",
            "official_dataset_search_service",
            "monitored_watchlist",
        }
        if self.source_class not in allowed:
            raise ValueError("Invalid source_class")
        if not 0.0 <= self.discovery_priority <= 1.0:
            raise ValueError("discovery_priority must be between 0 and 1")

    @property
    def approved_for_automated_discovery(self) -> bool:
        return self.source_class != "monitored_watchlist"

    @property
    def download_requires_dataset_level_validation(self) -> bool:
        return True


OFFICIAL_CORPORATE_SOURCES = {
    "google_research": CorporateDataSource(
        source_id="google_research",
        organisation="Google Research",
        official_domain="research.google",
        source_class="official_dataset_catalogue",
        catalogue_url="https://research.google/resources/datasets/",
        discovery_priority=0.95,
        supports_direct_dataset_access=True,
        supports_version_pinning=True,
        notes=("Broad official research dataset catalogue", "Check licence per dataset"),
    ),
    "google_dataset_search": CorporateDataSource(
        source_id="google_dataset_search",
        organisation="Google Dataset Search",
        official_domain="datasetsearch.research.google.com",
        source_class="official_dataset_search_service",
        catalogue_url="https://datasetsearch.research.google.com/",
        discovery_priority=0.85,
        supports_direct_dataset_access=False,
        supports_version_pinning=False,
        notes=("Discovery index only", "Trust and licence derive from the hosting source"),
    ),
    "meta_ai": CorporateDataSource(
        source_id="meta_ai",
        organisation="Meta AI",
        official_domain="ai.meta.com",
        source_class="official_dataset_catalogue",
        catalogue_url="https://ai.meta.com/datasets/",
        discovery_priority=0.95,
        supports_direct_dataset_access=True,
        supports_version_pinning=True,
        notes=("AI training and benchmark datasets", "Dataset-specific terms apply"),
    ),
    "meta_data_for_good": CorporateDataSource(
        source_id="meta_data_for_good",
        organisation="Meta Data for Good",
        official_domain="dataforgood.facebook.com",
        source_class="official_dataset_catalogue",
        catalogue_url="https://dataforgood.facebook.com/",
        discovery_priority=0.85,
        supports_direct_dataset_access=True,
        supports_version_pinning=False,
        notes=("Research and public-interest datasets", "Access conditions vary"),
    ),
    "amd_open_ai": CorporateDataSource(
        source_id="amd_open_ai",
        organisation="AMD",
        official_domain="amd.com",
        source_class="official_model_and_data_releases",
        catalogue_url="https://www.amd.com/en/developer/resources/open-source-models.html",
        discovery_priority=0.80,
        supports_direct_dataset_access=True,
        supports_version_pinning=True,
        notes=("Open models, data and training configurations", "Verify linked repositories"),
    ),
    "intel_ai_reference_kits": CorporateDataSource(
        source_id="intel_ai_reference_kits",
        organisation="Intel",
        official_domain="intel.com",
        source_class="official_reference_kits",
        catalogue_url="https://www.intel.com/content/www/us/en/developer/topic-technology/artificial-intelligence/reference-kits.html",
        discovery_priority=0.80,
        supports_direct_dataset_access=True,
        supports_version_pinning=True,
        notes=("Reference kits may include training data", "Third-party dataset rights must be checked separately"),
    ),
    "nvidia_developer": CorporateDataSource(
        source_id="nvidia_developer",
        organisation="NVIDIA",
        official_domain="developer.nvidia.com",
        source_class="official_model_and_data_releases",
        catalogue_url="https://developer.nvidia.com/",
        discovery_priority=0.75,
        supports_direct_dataset_access=False,
        supports_version_pinning=True,
        notes=("Useful for synthetic data, simulation and model-linked datasets", "No single universal dataset catalogue assumed"),
    ),
    "coca_cola": CorporateDataSource(
        source_id="coca_cola",
        organisation="The Coca-Cola Company",
        official_domain="coca-colacompany.com",
        source_class="monitored_watchlist",
        catalogue_url=None,
        discovery_priority=0.30,
        supports_direct_dataset_access=False,
        supports_version_pinning=False,
        notes=("No verified official public AI dataset catalogue found", "Monitor competitions, research partnerships and official releases"),
    ),
}


def get_corporate_source(source_id: str) -> CorporateDataSource:
    try:
        return OFFICIAL_CORPORATE_SOURCES[source_id]
    except KeyError as exc:
        raise ValueError(f"Unknown corporate source: {source_id}") from exc


def automated_discovery_sources() -> Tuple[CorporateDataSource, ...]:
    return tuple(
        source
        for source in OFFICIAL_CORPORATE_SOURCES.values()
        if source.approved_for_automated_discovery
    )
