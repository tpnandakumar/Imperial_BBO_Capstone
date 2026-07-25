from PFRAMOS.emergence.vector_conduiting import (
    BehaviourVector,
    BiasVectorAssessment,
    EmergentCombination,
    LaminarConduitAssessment,
    exploration_randomness_budget,
)


def _vector(identifier: str, **overrides):
    values = dict(
        behaviour_id=identifier,
        magnitude=0.8,
        direction=(0.6, 0.8),
        confidence=0.8,
        coherence=0.8,
        persistence=0.7,
        risk=0.2,
        compute_cost=0.3,
        variance=0.2,
    )
    values.update(overrides)
    return BehaviourVector(**values)


def test_productive_bias_can_be_redirected() -> None:
    assessment = BiasVectorAssessment(
        vector=_vector("b1"),
        bias_class="productive_inductive_bias",
        harmful_distortion=0.2,
        productive_potential=0.8,
        contextuality=0.4,
        modulations=("redirect",),
    )
    assert assessment.action == "redirect_and_validate"


def test_high_risk_bias_is_quarantined() -> None:
    assessment = BiasVectorAssessment(
        vector=_vector("b2", risk=0.9),
        bias_class="emergent_bias",
        harmful_distortion=0.4,
        productive_potential=0.9,
        contextuality=0.8,
        modulations=("quarantine",),
    )
    assert assessment.action == "suppress_or_quarantine"


def test_synergistic_combination_builds_candidate_conduit() -> None:
    combination = EmergentCombination(
        combination_id="combo-1",
        vectors=(_vector("a"), _vector("b")),
        compatibility=0.9,
        synergy=0.9,
        stabilisation=0.8,
        novelty=0.8,
        routing_gain=0.9,
        residual_risk=0.1,
    )
    assert combination.disposition == "build_candidate_conduit"


def test_laminar_candidate_can_reach_shadow_validation() -> None:
    assessment = LaminarConduitAssessment(
        conduit_id="route-1",
        validated_capability_gain=0.95,
        coherence=0.95,
        robustness=0.95,
        compute_cost=0.05,
        routing_friction=0.05,
        variance=0.05,
        reproducibility=0.95,
        residual_risk=0.05,
    )
    assert assessment.promotion_state == "shadow_validate"


def test_randomness_reduces_near_final_decision() -> None:
    early = exploration_randomness_budget(0.8, 0.8, 0.7, 0.8, 0.1, 0.1)
    late = exploration_randomness_budget(0.8, 0.8, 0.7, 0.8, 0.1, 0.9)
    assert early > late
