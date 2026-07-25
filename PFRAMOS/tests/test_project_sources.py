from PFRAMOS.schooling.project_sources import active_project_sources, get_project_source


def test_current_bbo_source_is_active() -> None:
    source = get_project_source("imperial_bbo_current")
    assert source.ready_for_ingestion
    assert source.temporal_order_required
    assert "unsubmitted private candidate coordinates" in source.excluded_content


def test_honeycomb_requires_verified_connector() -> None:
    source = get_project_source("honeycomb_publications")
    assert source.authorised
    assert not source.ready_for_ingestion
    assert source.ingestion_status == "authorised_pending_connector"


def test_only_bbo_is_currently_active() -> None:
    active_ids = {source.source_id for source in active_project_sources()}
    assert active_ids == {"imperial_bbo_current"}
