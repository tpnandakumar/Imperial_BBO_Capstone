"""Minimum computational memory circuit for Artificial Cognition.

Recall is treated as the output of a larger cognitive process. At minimum,
successful recall depends on attention, semantic processing, encoding,
retention and retrieval. The model separates these components so a failure can
be localised rather than labelled as generic memory failure.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import exp
from typing import Tuple


@dataclass(frozen=True)
class MemoryInput:
    item_id: str
    attention: float
    semantic_fit: float
    context_coherence: float
    interference: float
    novelty: float
    prior_knowledge: float

    def __post_init__(self) -> None:
        for name in (
            "attention",
            "semantic_fit",
            "context_coherence",
            "interference",
            "novelty",
            "prior_knowledge",
        ):
            value = getattr(self, name)
            if not 0.0 <= value <= 1.0:
                raise ValueError(f"{name} must be between 0 and 1")


@dataclass(frozen=True)
class MemoryTrace:
    item_id: str
    encoding_strength: float
    semantic_strength: float
    retention_strength: float
    retrieval_accessibility: float
    recall_probability: float
    dominant_failure_mode: str
    component_scores: Tuple[Tuple[str, float], ...]


def _clip(value: float) -> float:
    return max(0.0, min(1.0, value))


def encode_memory(item: MemoryInput) -> Tuple[float, float]:
    """Return semantic organisation and encoding strength."""
    semantic_strength = _clip(
        0.45 * item.semantic_fit
        + 0.30 * item.context_coherence
        + 0.25 * item.prior_knowledge
    )
    encoding_strength = _clip(
        item.attention
        * semantic_strength
        * (1.0 - item.interference)
        * (0.85 + 0.15 * item.novelty)
    )
    return semantic_strength, encoding_strength


def retain_memory(
    encoding_strength: float,
    elapsed_time: float,
    forgetting_rate: float,
    reactivation: float,
    consolidation_efficiency: float,
) -> float:
    if elapsed_time < 0:
        raise ValueError("elapsed_time cannot be negative")
    for value in (forgetting_rate, reactivation, consolidation_efficiency):
        if not 0.0 <= value <= 1.0:
            raise ValueError("retention inputs must be between 0 and 1")

    decayed = encoding_strength * exp(-forgetting_rate * elapsed_time)
    consolidated = consolidation_efficiency * reactivation * (1.0 - decayed)
    return _clip(decayed + consolidated)


def retrieve_memory(
    retention_strength: float,
    cue_similarity: float,
    semantic_route_quality: float,
    contextual_match: float,
    retrieval_competition: float,
) -> float:
    for value in (
        cue_similarity,
        semantic_route_quality,
        contextual_match,
        retrieval_competition,
    ):
        if not 0.0 <= value <= 1.0:
            raise ValueError("retrieval inputs must be between 0 and 1")
    retrieval_accessibility = (
        retention_strength
        * (0.40 * cue_similarity + 0.35 * semantic_route_quality + 0.25 * contextual_match)
        * (1.0 - retrieval_competition)
    )
    return _clip(retrieval_accessibility)


def _relative_stage_quality(output: float, upstream: float) -> float:
    """Measure a stage without blaming it for an upstream bottleneck.

    Raw downstream values naturally shrink when an earlier stage is weak. Using
    the raw minimum therefore mislabels poor attention as an encoding failure.
    Relative stage quality isolates the loss introduced at each stage.
    """
    if upstream <= 1e-12:
        return 1.0
    return _clip(output / upstream)


def assess_recall(
    item: MemoryInput,
    elapsed_time: float,
    forgetting_rate: float,
    reactivation: float,
    consolidation_efficiency: float,
    cue_similarity: float,
    semantic_route_quality: float,
    contextual_match: float,
    retrieval_competition: float,
) -> MemoryTrace:
    semantic_strength, encoding_strength = encode_memory(item)
    retention_strength = retain_memory(
        encoding_strength=encoding_strength,
        elapsed_time=elapsed_time,
        forgetting_rate=forgetting_rate,
        reactivation=reactivation,
        consolidation_efficiency=consolidation_efficiency,
    )
    retrieval_accessibility = retrieve_memory(
        retention_strength=retention_strength,
        cue_similarity=cue_similarity,
        semantic_route_quality=semantic_route_quality,
        contextual_match=contextual_match,
        retrieval_competition=retrieval_competition,
    )

    recall_probability = _clip(
        retrieval_accessibility
        * (0.55 + 0.25 * item.attention + 0.20 * semantic_strength)
    )

    encoding_upstream = item.attention * semantic_strength
    diagnostic_components = {
        "attention": item.attention,
        "semantic": semantic_strength,
        "encoding": _relative_stage_quality(encoding_strength, encoding_upstream),
        "retention": _relative_stage_quality(retention_strength, encoding_strength),
        "retrieval": _relative_stage_quality(retrieval_accessibility, retention_strength),
    }
    dominant_failure_mode = min(diagnostic_components, key=diagnostic_components.get)

    return MemoryTrace(
        item_id=item.item_id,
        encoding_strength=encoding_strength,
        semantic_strength=semantic_strength,
        retention_strength=retention_strength,
        retrieval_accessibility=retrieval_accessibility,
        recall_probability=recall_probability,
        dominant_failure_mode=dominant_failure_mode,
        component_scores=tuple(diagnostic_components.items()),
    )
