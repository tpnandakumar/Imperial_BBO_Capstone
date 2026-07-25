from PFRAMOS.training.pacc_publication_record import PACCExperimentRecord


def _record(**overrides):
    values = dict(
        experiment_id="PACC-EXP-001",
        timestamp_utc="2026-07-25T12:00:00Z",
        cognitive_domain="semantic_memory",
        training_lane="semantic_and_language",
        research_question="Can the model preserve semantic relations under perturbation?",
        hypothesis="Validated semantic structure will improve protected-test coherence.",
        dataset_name="open-semantic-example",
        dataset_version="1.0",
        dataset_source="approved-open-source",
        dataset_manifest_hash="abc123",
        licence_status="approved",
        access_status="approved",
        privacy_status="not_applicable",
        ethics_status="not_applicable",
        contamination_status="approved",
        representativeness_status="approved",
        model_version="pacc-semantic-v0.1",
        software_commit="deadbeef",
        random_seed=42,
        hardware_environment="cpu-test",
        runtime_seconds=10.0,
        parameter_updates_applied=False,
        shadow_only=True,
        baseline_methods=("baseline-a",),
        training_parameters={"mode": "shadow"},
        training_metrics={"loss": 0.5},
        validation_metrics={"coherence": 0.7},
        protected_test_metrics={"coherence": 0.68},
        uncertainty_metrics={"calibration_error": 0.1},
        pcece_metrics={"score": 0.4},
        memory_metrics={"returned_units": 64.0},
        pimf_states=("Emerging",),
        pframos_decision="retain_shadow_only",
        negative_results=(),
        limitations=("small pilot",),
        primary_paper_track="PACC-P3",
        secondary_paper_tracks=("PACC-P8",),
        reproducible=True,
    )
    values.update(overrides)
    return PACCExperimentRecord(**values)


def test_complete_record_is_publication_evidence_ready() -> None:
    record = _record()
    assert record.publication_evidence_ready
    assert record.blockers() == ()


def test_missing_protected_test_blocks_publication() -> None:
    record = _record(protected_test_metrics={})
    assert not record.publication_evidence_ready
    assert "missing_protected_test_metrics" in record.blockers()


def test_unapproved_licence_blocks_publication() -> None:
    record = _record(licence_status="pending")
    assert "licence_not_approved" in record.blockers()


def test_nonreproducible_run_is_blocked() -> None:
    record = _record(reproducible=False)
    assert "not_reproducible" in record.blockers()
