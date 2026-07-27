"""Signed coherence modelling for PFRAMOS.

The PHCS coherence index lies in [-1, +1]. Positive values indicate
coherence, negative values indicate conflict, and values near zero indicate
balance, weak evidence or unresolved structure.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import sqrt
from typing import Dict, Iterable, List, Mapping, Sequence, Tuple


@dataclass(frozen=True)
class CoherenceEvidence:
    source_id: str
    support: float
    conflict: float
    confidence: float
    independence: float
    lineage: Tuple[str, ...] = ()

    def __post_init__(self) -> None:
        for name in ("support", "conflict", "confidence", "independence"):
            value = getattr(self, name)
            if not 0.0 <= value <= 1.0:
                raise ValueError(f"{name} must be between 0 and 1")


@dataclass(frozen=True)
class CoherenceScore:
    index: float
    support_strength: float
    conflict_strength: float
    evidence_volume: int
    independence_score: float
    unresolved_issue_count: int


@dataclass(frozen=True)
class InterNodalCoherence:
    source_node: str
    target_node: str
    score: CoherenceScore


@dataclass(frozen=True)
class PathwayEnvelope:
    geometry: str
    centreline_nodes: Tuple[str, ...]
    radius: float
    inner_radius: float
    outer_radius: float
    layer_count: int
    coherence_floor: float


def signed_coherence(
    evidence: Sequence[CoherenceEvidence],
    *,
    unresolved_issue_count: int = 0,
    epsilon: float = 1e-12,
) -> CoherenceScore:
    if not evidence:
        return CoherenceScore(0.0, 0.0, 0.0, 0, 0.0, unresolved_issue_count)

    lineage_counts: Dict[Tuple[str, ...], int] = {}
    for item in evidence:
        key = tuple(sorted(item.lineage))
        lineage_counts[key] = lineage_counts.get(key, 0) + 1

    support = 0.0
    conflict = 0.0
    independence_total = 0.0

    for item in evidence:
        key = tuple(sorted(item.lineage))
        dependency_discount = 1.0 / lineage_counts[key]
        weight = item.confidence * item.independence * dependency_discount
        support += item.support * weight
        conflict += item.conflict * weight
        independence_total += item.independence

    index = (support - conflict) / (support + conflict + epsilon)
    index = max(-1.0, min(1.0, index))

    return CoherenceScore(
        index=index,
        support_strength=support,
        conflict_strength=conflict,
        evidence_volume=len(evidence),
        independence_score=independence_total / len(evidence),
        unresolved_issue_count=unresolved_issue_count,
    )


def engine_coherence(
    nodal_scores: Mapping[str, CoherenceScore],
    internodal_scores: Sequence[InterNodalCoherence],
    *,
    data_coherence: CoherenceScore,
) -> CoherenceScore:
    evidence: List[CoherenceEvidence] = []

    evidence.append(
        CoherenceEvidence(
            source_id="data",
            support=max(0.0, data_coherence.index),
            conflict=max(0.0, -data_coherence.index),
            confidence=min(1.0, data_coherence.evidence_volume / 10.0),
            independence=max(0.1, data_coherence.independence_score),
            lineage=("data",),
        )
    )

    for node_id, score in nodal_scores.items():
        evidence.append(
            CoherenceEvidence(
                source_id=f"node:{node_id}",
                support=max(0.0, score.index),
                conflict=max(0.0, -score.index),
                confidence=min(1.0, score.evidence_volume / 5.0),
                independence=max(0.1, score.independence_score),
                lineage=("node", node_id),
            )
        )

    for edge in internodal_scores:
        evidence.append(
            CoherenceEvidence(
                source_id=f"edge:{edge.source_node}->{edge.target_node}",
                support=max(0.0, edge.score.index),
                conflict=max(0.0, -edge.score.index),
                confidence=min(1.0, edge.score.evidence_volume / 5.0),
                independence=max(0.1, edge.score.independence_score),
                lineage=("edge", edge.source_node, edge.target_node),
            )
        )

    unresolved = data_coherence.unresolved_issue_count + sum(
        score.unresolved_issue_count for score in nodal_scores.values()
    ) + sum(edge.score.unresolved_issue_count for edge in internodal_scores)

    return signed_coherence(evidence, unresolved_issue_count=unresolved)


def augmentation_gain(index: float, *, threshold: float = 0.40, maximum_gain: float = 0.35) -> float:
    """Return coherence-stimulated activity gain without allowing runaway feedback."""

    if index <= threshold:
        return 0.0
    scaled = (index - threshold) / (1.0 - threshold)
    return min(maximum_gain, maximum_gain * scaled)


def stimulate_activity(base_activity: float, internodal_indices: Iterable[float]) -> float:
    """Augment node activity from coherent connected pathways.

    Negative indices never suppress activity here. Conflict handling remains a
    separate explicit penalty so support and opposition stay auditable.
    """

    gain = sum(augmentation_gain(index) for index in internodal_indices)
    return max(0.0, min(1.0, base_activity * (1.0 + gain)))


def maximum_result_path(
    node_scores: Mapping[str, float],
    links: Mapping[str, Sequence[str]],
    *,
    start_node: str,
) -> Tuple[str, ...]:
    """Greedy auditable centreline through locally maximal connected results."""

    if start_node not in node_scores:
        raise KeyError(start_node)

    path = [start_node]
    visited = {start_node}
    current = start_node

    while True:
        candidates = [node for node in links.get(current, ()) if node not in visited]
        if not candidates:
            break
        next_node = max(candidates, key=lambda node: node_scores.get(node, float("-inf")))
        if node_scores.get(next_node, float("-inf")) < node_scores[current]:
            break
        path.append(next_node)
        visited.add(next_node)
        current = next_node

    return tuple(path)


def build_pathway_envelope(
    centreline_nodes: Sequence[str],
    coherence_indices: Sequence[float],
    *,
    geometry: str = "adaptive",
    layer_count: int = 4,
) -> PathwayEnvelope:
    """Construct a coherence envelope around the maximum-result pathway.

    Geometry meanings:
    - band: ordered or near-planar pathway
    - cylinder: directed multi-step pathway with stable width
    - sphere: radial hub with multidirectional support
    - adaptive: chooses from the pathway structure and coherence dispersion
    """

    if not centreline_nodes:
        raise ValueError("centreline_nodes must not be empty")
    if not coherence_indices:
        raise ValueError("coherence_indices must not be empty")
    if layer_count < 1:
        raise ValueError("layer_count must be positive")

    positive = [max(0.0, value) for value in coherence_indices]
    mean = sum(positive) / len(positive)
    variance = sum((value - mean) ** 2 for value in positive) / len(positive)
    dispersion = sqrt(variance)

    if geometry == "adaptive":
        if len(centreline_nodes) <= 2:
            chosen = "band"
        elif dispersion <= 0.10:
            chosen = "cylinder"
        else:
            chosen = "sphere"
    elif geometry in {"band", "cylinder", "sphere"}:
        chosen = geometry
    else:
        raise ValueError(f"Unsupported geometry: {geometry}")

    outer_radius = max(0.05, 1.0 - mean)
    inner_radius = outer_radius / layer_count
    coherence_floor = min(coherence_indices)

    return PathwayEnvelope(
        geometry=chosen,
        centreline_nodes=tuple(centreline_nodes),
        radius=outer_radius,
        inner_radius=inner_radius,
        outer_radius=outer_radius,
        layer_count=layer_count,
        coherence_floor=coherence_floor,
    )
