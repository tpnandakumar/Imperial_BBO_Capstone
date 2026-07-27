from PFRAMOS.training_scout.open_dataset_ecosystems import (
    get_open_ecosystem,
    varied_source_rotation,
)


def test_google_research_has_varied_multimodal_coverage() -> None:
    source = get_open_ecosystem("google_research")
    assert "multimodal" in source.domain_coverage
    assert source.default_priority >= 0.9


def test_openml_supports_programmatic_versioned_access() -> None:
    source = get_open_ecosystem("openml")
    assert source.supports_versioning
    assert source.supports_api_or_programmatic_access


def test_common_crawl_requires_heavy_filtering() -> None:
    source = get_open_ecosystem("common_crawl")
    assert "quality filtering" in source.required_checks
    assert "fuzzy deduplication" in source.required_checks


def test_rotation_uses_multiple_independent_sources() -> None:
    rotation = varied_source_rotation()
    assert len(rotation) >= 6
    assert len(rotation) == len(set(rotation))
