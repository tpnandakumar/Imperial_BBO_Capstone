from datetime import datetime, timezone

from PFRAMOS.training_scout.scout import DatasetCandidate, build_manifest


NOW = datetime(2026, 7, 23, 21, 0, tzinfo=timezone.utc)


def _candidate(**overrides):
    values = dict(
        candidate_id="dataset-1",
        repository="example/repo",
        file_path="data/train.csv",
        source_commit_sha="abc123",
        discovered_at=NOW,
        licence_id="MIT",
        source_authority=0.90,
        relevance=0.90,
        documentation_quality=0.85,
        reproducibility=0.85,
        independence=0.80,
        maintenance_recency=0.80,
        schema_accessibility=0.90,
        expected_training_value=0.90,
        estimated_download_cost=0.20,
        privacy_risk=0.10,
        poisoning_risk=0.10,
        benchmark_contamination_risk=0.10,
    )
    values.update(overrides)
    return DatasetCandidate(**values)


def test_high_quality_candidate_enters_schooling_quarantine() -> None:
    candidate = _candidate()
    assert candidate.disposition == "download_to_schooling_quarantine"
    assert not candidate.hard_blocks


def test_unclear_licence_blocks_download() -> None:
    candidate = _candidate(licence_id=None)
    assert candidate.disposition == "reject_or_quarantine"
    assert "licence not approved or unclear" in candidate.hard_blocks


def test_executable_content_blocks_download() -> None:
    candidate = _candidate(file_path="data/train.zip", contains_executable_content=True)
    assert candidate.disposition == "reject_or_quarantine"
    assert "executable content detected" in candidate.hard_blocks


def test_benchmark_contamination_blocks_candidate() -> None:
    candidate = _candidate(benchmark_contamination_risk=0.80)
    assert candidate.disposition == "reject_or_quarantine"


def test_manifest_preserves_source_commit_and_score() -> None:
    candidate = _candidate()
    manifest = build_manifest(candidate)
    assert manifest.source_commit_sha == "abc123"
    assert manifest.discovery_score == candidate.discovery_score
    assert manifest.disposition == candidate.disposition
