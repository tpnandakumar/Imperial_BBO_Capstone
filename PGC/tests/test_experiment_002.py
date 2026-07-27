from PGC.experiments.PGC_EXPERIMENT_002.run_experiment import run_experiment


def test_experiment_002_preserves_protected_test_boundary() -> None:
    result = run_experiment([11], bootstrap_resamples=10)

    assert result["experiment_id"] == "PGC_EXPERIMENT_002"
    assert result["state"] == "completed_trial"
    assert result["dataset"]["uci_id"] == 53
    assert result["dataset"]["licence"] == "CC BY 4.0"
    assert result["protected_test_used_for_routing"] is False
    assert result["publication_evidence"] is False
    assert result["trial_evidence"] is True
    assert "pgc_evidence_router" in result["aggregate"]
    assert "confidence_only_router" in result["aggregate"]
    assert "oracle_router" in result["aggregate"]
