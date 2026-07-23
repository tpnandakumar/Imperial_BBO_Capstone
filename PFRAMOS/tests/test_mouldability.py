from PFRAMOS.tech_sweep.mouldability import MouldabilityAssessment, rescue_priority


def test_weak_candidate_with_strong_latent_potential_enters_modulation_lab() -> None:
    assessment = MouldabilityAssessment(
        candidate_id="candidate-a",
        core_idea_strength=0.90,
        modularity=0.85,
        decomposability=0.85,
        constraint_responsiveness=0.80,
        recombination_potential=0.85,
        role_reassignment_potential=0.80,
        repair_cost=0.30,
        residual_risk=0.20,
        proposed_modulations=("partial adoption", "role reassignment"),
    )
    assert assessment.disposition == "send_to_modulation_lab"
    assert rescue_priority(0.40, assessment) > 0.0


def test_high_residual_risk_is_rejected() -> None:
    assessment = MouldabilityAssessment(
        candidate_id="candidate-b",
        core_idea_strength=0.95,
        modularity=0.90,
        decomposability=0.90,
        constraint_responsiveness=0.90,
        recombination_potential=0.90,
        role_reassignment_potential=0.90,
        repair_cost=0.20,
        residual_risk=0.85,
        proposed_modulations=("constraint",),
    )
    assert assessment.disposition == "reject_despite_mouldability"


def test_low_mouldability_candidate_is_archived() -> None:
    assessment = MouldabilityAssessment(
        candidate_id="candidate-c",
        core_idea_strength=0.30,
        modularity=0.25,
        decomposability=0.20,
        constraint_responsiveness=0.20,
        recombination_potential=0.25,
        role_reassignment_potential=0.20,
        repair_cost=0.80,
        residual_risk=0.50,
        proposed_modulations=(),
    )
    assert assessment.disposition == "archive_low_mouldability"
