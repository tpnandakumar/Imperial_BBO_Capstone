from PGC.experiments.PGC_EXPERIMENT_003.run_experiment import generate_cases, run_experiment


def test_experiment_003_generator_is_balanced() -> None:
    cases = generate_cases(seed=11, per_family=3)

    counts: dict[str, int] = {}
    for case in cases:
        counts[case.family] = counts.get(case.family, 0) + 1

    assert set(counts.values()) == {3}
    assert len(cases) == 18


def test_experiment_003_produces_trial_record() -> None:
    result = run_experiment(seeds=[11, 23], per_family=5)

    assert result["experiment_id"] == "PGC_EXPERIMENT_003"
    assert result["state"] == "completed_trial"
    assert result["trial_evidence"] is True
    assert result["publication_evidence"] is False
    assert result["factual_accuracy_precedence"] is True
    assert "pgc_perception_emotion" in result["aggregate"]
    assert "pgc_without_coherence" in result["aggregate"]
    assert result["total_cases_per_seed"] == 30
