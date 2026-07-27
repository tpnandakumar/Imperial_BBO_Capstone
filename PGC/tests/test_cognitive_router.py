from PGC.architecture.cognitive_router import CandidateConfiguration, route, score


def candidate(candidate_id: str, **overrides: float | bool) -> CandidateConfiguration:
    values: dict[str, float | bool | str] = {
        "candidate_id": candidate_id,
        "task_fitness": 0.80,
        "evidence_validity": 0.80,
        "coherence": 0.80,
        "robustness": 0.80,
        "uncertainty": 0.20,
        "safety": 0.90,
        "efficiency": 0.70,
        "hard_block": False,
    }
    values.update(overrides)
    return CandidateConfiguration(**values)  # type: ignore[arg-type]


def test_router_selects_strongest_eligible_candidate() -> None:
    weaker = candidate("weaker", task_fitness=0.65, evidence_validity=0.70)
    stronger = candidate("stronger", task_fitness=0.90, evidence_validity=0.90)

    decision = route((weaker, stronger))

    assert decision.abstained is False
    assert decision.selected_candidate_id == "stronger"
    assert decision.ranked_candidate_ids[0] == "stronger"


def test_router_rejects_hard_blocked_candidate() -> None:
    blocked = candidate("blocked", hard_block=True, task_fitness=1.0)
    eligible = candidate("eligible")

    decision = route((blocked, eligible))

    assert decision.selected_candidate_id == "eligible"
    assert "blocked" not in decision.ranked_candidate_ids


def test_router_abstains_when_quality_gate_fails() -> None:
    unsafe = candidate("unsafe", safety=0.30)
    weak_evidence = candidate("weak_evidence", evidence_validity=0.40)

    decision = route((unsafe, weak_evidence))

    assert decision.abstained is True
    assert decision.selected_candidate_id is None


def test_efficiency_cannot_overcome_failed_quality_gate() -> None:
    low_quality = candidate(
        "low_quality",
        task_fitness=0.49,
        efficiency=1.0,
    )

    assert score(low_quality) == float("-inf")


def test_out_of_range_values_raise_error() -> None:
    invalid = candidate("invalid", coherence=1.20)

    try:
        score(invalid)
    except ValueError as error:
        assert "coherence" in str(error)
    else:
        raise AssertionError("expected ValueError")
