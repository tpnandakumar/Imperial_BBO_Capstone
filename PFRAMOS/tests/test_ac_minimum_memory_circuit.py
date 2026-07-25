from PFRAMOS.architecture.ac_minimum_memory_circuit import (
    MemoryInput,
    assess_recall,
)


def _assess(item: MemoryInput, **overrides):
    values = dict(
        elapsed_time=1.0,
        forgetting_rate=0.1,
        reactivation=0.4,
        consolidation_efficiency=0.7,
        cue_similarity=0.8,
        semantic_route_quality=0.8,
        contextual_match=0.8,
        retrieval_competition=0.1,
    )
    values.update(overrides)
    return assess_recall(item, **values)


def test_poor_attention_is_not_mislabelled_as_storage_failure() -> None:
    trace = _assess(
        MemoryInput(
            item_id="a",
            attention=0.1,
            semantic_fit=0.9,
            context_coherence=0.9,
            interference=0.0,
            novelty=0.5,
            prior_knowledge=0.8,
        )
    )
    assert trace.dominant_failure_mode == "attention"


def test_weak_semantic_structure_reduces_encoding() -> None:
    weak = _assess(
        MemoryInput(
            item_id="weak",
            attention=0.9,
            semantic_fit=0.1,
            context_coherence=0.1,
            interference=0.0,
            novelty=0.5,
            prior_knowledge=0.1,
        )
    )
    strong = _assess(
        MemoryInput(
            item_id="strong",
            attention=0.9,
            semantic_fit=0.9,
            context_coherence=0.9,
            interference=0.0,
            novelty=0.5,
            prior_knowledge=0.9,
        )
    )
    assert weak.encoding_strength < strong.encoding_strength


def test_high_forgetting_rate_reduces_retention() -> None:
    item = MemoryInput(
        item_id="retention",
        attention=0.9,
        semantic_fit=0.9,
        context_coherence=0.9,
        interference=0.0,
        novelty=0.5,
        prior_knowledge=0.9,
    )
    low_decay = _assess(item, elapsed_time=5.0, forgetting_rate=0.05)
    high_decay = _assess(item, elapsed_time=5.0, forgetting_rate=0.8)
    assert high_decay.retention_strength < low_decay.retention_strength


def test_retrieval_failure_can_occur_despite_good_retention() -> None:
    item = MemoryInput(
        item_id="retrieval",
        attention=0.9,
        semantic_fit=0.9,
        context_coherence=0.9,
        interference=0.0,
        novelty=0.5,
        prior_knowledge=0.9,
    )
    trace = _assess(
        item,
        cue_similarity=0.1,
        semantic_route_quality=0.1,
        contextual_match=0.1,
        retrieval_competition=0.9,
    )
    assert trace.retention_strength > trace.retrieval_accessibility
    assert trace.dominant_failure_mode == "retrieval"


def test_recall_is_output_of_full_circuit() -> None:
    item = MemoryInput(
        item_id="complete",
        attention=0.9,
        semantic_fit=0.9,
        context_coherence=0.9,
        interference=0.05,
        novelty=0.6,
        prior_knowledge=0.8,
    )
    trace = _assess(item)
    assert 0.0 <= trace.recall_probability <= 1.0
    assert len(trace.component_scores) == 5
