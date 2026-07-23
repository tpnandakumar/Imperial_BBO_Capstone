from PFRAMOS.tech_sweep.models import ResearchCandidate


def _candidate(**overrides):
    values = dict(
        candidate_id="x",
        title="Test",
        source="arXiv",
        source_url="https://example.com",
        published_at="2026-07-23T00:00:00Z",
        abstract="Test abstract",
        categories=("cs.LG",),
        relevance=0.9,
        novelty=0.85,
        maturity=0.85,
        reproducibility=0.85,
        evidence_quality=0.9,
        transferability=0.9,
        compute_efficiency=0.8,
        energy_efficiency=0.8,
        safety=0.9,
        non_duplication=0.9,
    )
    values.update(overrides)
    return ResearchCandidate(**values)


def test_high_quality_candidate_reaches_experimental_state() -> None:
    candidate = _candidate()
    assert candidate.recruitment_score >= 0.78
    assert candidate.recruitment_state == "experimental_node_candidate"


def test_low_evidence_candidate_is_rejected() -> None:
    candidate = _candidate(evidence_quality=0.2)
    assert candidate.recruitment_state == "rejected"


def test_midrange_candidate_remains_quarantined() -> None:
    candidate = _candidate(
        relevance=0.65,
        novelty=0.55,
        maturity=0.55,
        reproducibility=0.55,
        evidence_quality=0.60,
        transferability=0.60,
        compute_efficiency=0.55,
        energy_efficiency=0.50,
        safety=0.65,
        non_duplication=0.60,
    )
    assert candidate.recruitment_state in {"quarantined_candidate", "screened_only"}
