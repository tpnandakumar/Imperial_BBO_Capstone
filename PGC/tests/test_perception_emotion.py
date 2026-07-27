from PGC.perception_emotion.emotional_balance_regulator import BalanceInput, regulate_balance
from PGC.perception_emotion.emotional_coherence_controller import (
    EmotionalCognitiveState,
    assess_coherence,
)
from PGC.perception_emotion.memory_interfaces import MemoryWriteProposal, evaluate_memory_write
from PGC.perception_emotion.multimodal_fusion import PerceptualObservation, fuse_observations


def observation(
    modality_id: str,
    factual: float,
    emotional: float,
    reliability: float = 0.90,
) -> PerceptualObservation:
    return PerceptualObservation(
        modality_id=modality_id,
        factual_signal=factual,
        emotional_signal=emotional,
        confidence=0.90,
        reliability=reliability,
        provenance=f"test:{modality_id}",
    )


def test_fusion_keeps_factual_and_emotional_signals_separate() -> None:
    fused = fuse_observations(
        (
            observation("language", factual=0.20, emotional=0.90),
            observation("audio", factual=0.25, emotional=0.85),
        )
    )

    assert fused.factual_estimate < 0.30
    assert fused.emotional_estimate > 0.80


def test_low_reliability_modality_is_excluded() -> None:
    fused = fuse_observations(
        (
            observation("language", factual=0.20, emotional=0.30),
            observation("vision", factual=0.95, emotional=0.95, reliability=0.40),
        )
    )

    assert fused.modality_coverage == 1
    assert fused.excluded_modalities == ("vision",)
    assert fused.factual_estimate == 0.20


def test_emotional_intensity_cannot_force_urgent_response_without_facts() -> None:
    decision = regulate_balance(
        BalanceInput(
            factual_support=0.25,
            threat=0.90,
            urgency=0.90,
            empathy_need=0.30,
            uncertainty=0.65,
            factual_accuracy=0.90,
            safety=0.90,
            proportionality=0.90,
            phcs_coherence=0.80,
        )
    )

    assert decision.action == "clarify"


def test_strong_factual_risk_is_not_ignored_when_emotion_is_low() -> None:
    decision = regulate_balance(
        BalanceInput(
            factual_support=0.70,
            threat=0.55,
            urgency=0.35,
            empathy_need=0.20,
            uncertainty=0.20,
            factual_accuracy=0.90,
            safety=0.90,
            proportionality=0.85,
            phcs_coherence=0.80,
        )
    )

    assert decision.action == "caution"


def test_coherence_cannot_pass_failed_factual_gate() -> None:
    assessment = assess_coherence(
        EmotionalCognitiveState(
            perceived_significance=0.80,
            appraisal_intensity=0.80,
            reasoning_intensity=0.80,
            memory_intensity=0.80,
            expression_intensity=0.80,
            action_intensity=0.80,
            factual_accuracy=0.30,
            safety=0.90,
            proportionality=0.90,
            uncertainty_awareness=0.90,
        )
    )

    assert assessment.passed is False
    assert "factual_accuracy_below_gate" in assessment.conflicts


def test_emotional_significance_alone_cannot_create_memory() -> None:
    decision = evaluate_memory_write(
        MemoryWriteProposal(
            source="test",
            modality_ids=("language", "audio"),
            purpose="controlled_test",
            factual_summary="An emotionally intense but weakly supported event.",
            emotional_significance=0.95,
            factual_support=0.30,
            phcs_coherence=0.90,
            pimf_persistence=0.90,
            sensitive=False,
            expiry_epoch=None,
        )
    )

    assert decision.accepted is False
    assert "factual_support_below_threshold" in decision.reasons
