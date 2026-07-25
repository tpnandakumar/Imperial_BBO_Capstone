from PFRAMOS.publication_automation.paper_router import (
    EvidenceRecord,
    manuscript_state,
    route_evidence,
)


def _record(**overrides):
    values = dict(
        result_id="R-001",
        training_lane="optimisation",
        data_form="optimisation_trace",
        source_ids=("imperial_bbo_current",),
        metrics={"quality": 0.8},
        has_dataset_manifest=True,
        has_training_log_hash=True,
        has_protected_test=True,
        reproducible=True,
        regressions_present=False,
        publication_eligible=True,
        tags=(),
    )
    values.update(overrides)
    return EvidenceRecord(**values)


def test_optimisation_result_routes_to_paper_one() -> None:
    assignment = route_evidence(_record())
    assert assignment.primary_paper == "PFRAMOS-P1"
    assert assignment.state == "evidence_ready"


def test_honeycomb_result_routes_to_publishing_paper() -> None:
    assignment = route_evidence(
        _record(
            training_lane="publishing",
            data_form="unlabelled_text",
            source_ids=("honeycomb_publications",),
        )
    )
    assert assignment.primary_paper == "PFRAMOS-P8"


def test_cross_cutting_emergence_is_secondary_not_duplicate_owner() -> None:
    assignment = route_evidence(_record(tags=("emergence", "laminar")))
    assert assignment.primary_paper == "PFRAMOS-P1"
    assert "PFRAMOS-P5" in assignment.secondary_papers


def test_incomplete_evidence_is_blocked() -> None:
    assignment = route_evidence(_record(has_protected_test=False))
    assert assignment.state == "evidence_incomplete"
    assert "missing_protected_test" in assignment.blocking_reasons


def test_manuscript_does_not_advance_with_mixed_primary_tracks() -> None:
    first = route_evidence(_record())
    second = route_evidence(_record(result_id="R-002", training_lane="efficiency"))
    assert manuscript_state((first, second)) == "manual_scope_review"
