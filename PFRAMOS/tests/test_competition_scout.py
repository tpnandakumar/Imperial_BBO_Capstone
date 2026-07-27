from datetime import datetime, timezone

from PFRAMOS.training_scout.competition_scout import CompetitionCandidate, CompetitionResult


NOW = datetime(2026, 7, 23, 21, 30, tzinfo=timezone.utc)


def _candidate(**overrides):
    values = dict(
        competition_id="comp-1",
        platform_id="kaggle",
        title="Example Competition",
        rules_url="https://www.kaggle.com/competitions/example/rules",
        discovered_at=NOW,
        start_at=None,
        end_at=None,
        dataset_use_class="open_learning",
        licence_clear=True,
        external_data_allowed=True,
        team_sharing_allowed=False,
        submission_automation_allowed=False,
        hidden_test_present=True,
        benchmark_value=0.90,
        domain_relevance=0.90,
        reproducibility=0.85,
        documentation_quality=0.85,
        compute_affordability=0.80,
        legal_risk=0.10,
        privacy_risk=0.10,
        contamination_risk=0.10,
        rules_complete=True,
    )
    values.update(overrides)
    return CompetitionCandidate(**values)


def test_open_learning_competition_can_enter_schooling_validation() -> None:
    candidate = _candidate()
    assert candidate.schooling_permission == "eligible_for_schooling_validation"
    assert candidate.disposition == "priority_external_exam"


def test_competition_only_data_remains_in_sandbox() -> None:
    candidate = _candidate(dataset_use_class="competition_only")
    assert candidate.schooling_permission == "competition_sandbox_only"


def test_unclear_rules_force_quarantine() -> None:
    candidate = _candidate(rules_complete=False, licence_clear=False)
    assert candidate.disposition == "quarantine"
    assert candidate.hard_blocks


def test_high_contamination_risk_blocks_candidate() -> None:
    candidate = _candidate(contamination_risk=0.80)
    assert candidate.schooling_permission == "restricted_or_quarantine"


def test_leaderboard_gap_is_recorded() -> None:
    result = CompetitionResult(
        competition_id="comp-1",
        model_version="pframos-0.1",
        submitted_at=NOW,
        public_score=0.90,
        private_score=0.82,
        metric_name="accuracy",
        runtime_seconds=10.0,
        peak_memory_mb=512.0,
        estimated_energy_proxy=1.0,
        submission_count=1,
    )
    assert abs(result.leaderboard_gap - 0.08) < 1e-12
