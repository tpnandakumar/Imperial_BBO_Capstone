"""Open dataset ecosystems for varied PFRAMOS schooling.

A source registry entry authorises discovery only. Every dataset still
requires licence, provenance, privacy, contamination, duplication and
protected-test checks before training.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class OpenDatasetEcosystem:
    source_id: str
    display_name: str
    official_domain: str
    source_class: str
    supports_versioning: bool
    supports_api_or_programmatic_access: bool
    domain_coverage: Tuple[str, ...]
    default_priority: float
    required_checks: Tuple[str, ...]

    def __post_init__(self) -> None:
        if not 0.0 <= self.default_priority <= 1.0:
            raise ValueError("default_priority must be between 0 and 1")
        if not self.domain_coverage:
            raise ValueError("domain_coverage cannot be empty")


OPEN_DATASET_ECOSYSTEMS = {
    "google_research": OpenDatasetEcosystem(
        source_id="google_research",
        display_name="Google Research Datasets",
        official_domain="research.google",
        source_class="official_research_catalogue",
        supports_versioning=True,
        supports_api_or_programmatic_access=False,
        domain_coverage=("audio", "image", "robotics", "text", "video", "multimodal"),
        default_priority=0.95,
        required_checks=("dataset-specific licence", "version pinning", "benchmark contamination"),
    ),
    "google_dataset_search": OpenDatasetEcosystem(
        source_id="google_dataset_search",
        display_name="Google Dataset Search",
        official_domain="datasetsearch.research.google.com",
        source_class="dataset_discovery_index",
        supports_versioning=False,
        supports_api_or_programmatic_access=False,
        domain_coverage=("cross-domain discovery",),
        default_priority=0.75,
        required_checks=("hosting-source verification", "licence verification", "duplicate-source resolution"),
    ),
    "openml": OpenDatasetEcosystem(
        source_id="openml",
        display_name="OpenML",
        official_domain="openml.org",
        source_class="open_ml_dataset_and_experiment_platform",
        supports_versioning=True,
        supports_api_or_programmatic_access=True,
        domain_coverage=("classification", "regression", "clustering", "benchmarking", "experiment metadata"),
        default_priority=0.90,
        required_checks=("dataset version", "task leakage", "licence", "benchmark contamination"),
    ),
    "uci_ml_repository": OpenDatasetEcosystem(
        source_id="uci_ml_repository",
        display_name="UCI Machine Learning Repository",
        official_domain="archive.ics.uci.edu",
        source_class="academic_dataset_repository",
        supports_versioning=True,
        supports_api_or_programmatic_access=True,
        domain_coverage=("tabular", "time series", "classification", "regression", "clustering"),
        default_priority=0.90,
        required_checks=("dataset citation", "licence or usage terms", "sensitive-feature review", "split integrity"),
    ),
    "huggingface_datasets": OpenDatasetEcosystem(
        source_id="huggingface_datasets",
        display_name="Hugging Face Datasets",
        official_domain="huggingface.co",
        source_class="open_dataset_hub",
        supports_versioning=True,
        supports_api_or_programmatic_access=True,
        domain_coverage=("text", "image", "audio", "video", "multimodal", "code"),
        default_priority=0.90,
        required_checks=("repository revision", "dataset card", "licence", "streaming integrity", "contamination"),
    ),
    "common_crawl": OpenDatasetEcosystem(
        source_id="common_crawl",
        display_name="Common Crawl",
        official_domain="commoncrawl.org",
        source_class="web_scale_raw_corpus",
        supports_versioning=True,
        supports_api_or_programmatic_access=True,
        domain_coverage=("web text", "multilingual", "web metadata"),
        default_priority=0.55,
        required_checks=("quality filtering", "fuzzy deduplication", "privacy", "copyright", "benchmark overlap"),
    ),
    "uk_open_data": OpenDatasetEcosystem(
        source_id="uk_open_data",
        display_name="UK Government Open Data",
        official_domain="data.gov.uk",
        source_class="government_open_data_portal",
        supports_versioning=True,
        supports_api_or_programmatic_access=True,
        domain_coverage=("public services", "transport", "environment", "economy", "health metadata"),
        default_priority=0.80,
        required_checks=("open-government licence", "personal-data exclusion", "temporal consistency"),
    ),
    "world_bank_open_data": OpenDatasetEcosystem(
        source_id="world_bank_open_data",
        display_name="World Bank Open Data",
        official_domain="data.worldbank.org",
        source_class="international_statistical_portal",
        supports_versioning=True,
        supports_api_or_programmatic_access=True,
        domain_coverage=("economics", "development", "population", "education", "environment"),
        default_priority=0.80,
        required_checks=("indicator definition", "revision date", "missingness", "country comparability"),
    ),
}


def get_open_ecosystem(source_id: str) -> OpenDatasetEcosystem:
    try:
        return OPEN_DATASET_ECOSYSTEMS[source_id]
    except KeyError as exc:
        raise ValueError(f"unknown open dataset ecosystem: {source_id}") from exc


def varied_source_rotation() -> Tuple[str, ...]:
    """Return a balanced default rotation rather than repeated single-source use."""
    return (
        "google_research",
        "openml",
        "uci_ml_repository",
        "huggingface_datasets",
        "uk_open_data",
        "world_bank_open_data",
        "common_crawl",
    )
