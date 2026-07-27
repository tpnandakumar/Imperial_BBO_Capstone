from PFRAMOS.training_scout.corporate_source_registry import (
    automated_discovery_sources,
    get_corporate_source,
)


def test_google_research_is_approved_for_automated_discovery() -> None:
    source = get_corporate_source("google_research")
    assert source.approved_for_automated_discovery
    assert source.supports_direct_dataset_access


def test_meta_ai_is_high_priority_official_catalogue() -> None:
    source = get_corporate_source("meta_ai")
    assert source.source_class == "official_dataset_catalogue"
    assert source.discovery_priority >= 0.9


def test_coca_cola_remains_watchlist_only() -> None:
    source = get_corporate_source("coca_cola")
    assert not source.approved_for_automated_discovery
    assert source.catalogue_url is None


def test_every_download_requires_dataset_level_validation() -> None:
    for source in automated_discovery_sources():
        assert source.download_requires_dataset_level_validation
