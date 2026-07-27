from PFRAMOS.architecture.cognitive_enhancement import (
    CognitiveState,
    build_cognitive_plan,
)


def test_high_risk_task_requires_human_review() -> None:
    plan = build_cognitive_plan(
        CognitiveState(
            task_id="t1",
            attention_load=0.7,
            working_memory_load=0.8,
            uncertainty=0.7,
            conflict=0.5,
            novelty=0.6,
            evidence_quality=0.6,
            time_pressure=0.5,
            risk=0.9,
        )
    )
    assert plan.human_review_required
    assert plan.counterfactual_depth == 3
    assert "request_human_review" in plan.allowed_actions


def test_weak_evidence_triggers_retrieval() -> None:
    plan = build_cognitive_plan(
        CognitiveState(
            task_id="t2",
            attention_load=0.4,
            working_memory_load=0.4,
            uncertainty=0.5,
            conflict=0.2,
            novelty=0.4,
            evidence_quality=0.3,
            time_pressure=0.2,
            risk=0.3,
        )
    )
    assert plan.retrieval_required
    assert "weak_evidence" in plan.rationale


def test_novel_uncertain_task_expands_hypothesis_search() -> None:
    plan = build_cognitive_plan(
        CognitiveState(
            task_id="t3",
            attention_load=0.5,
            working_memory_load=0.5,
            uncertainty=0.8,
            conflict=0.3,
            novelty=0.8,
            evidence_quality=0.7,
            time_pressure=0.2,
            risk=0.4,
        )
    )
    assert plan.hypothesis_count == 5
    assert plan.contradiction_scan
