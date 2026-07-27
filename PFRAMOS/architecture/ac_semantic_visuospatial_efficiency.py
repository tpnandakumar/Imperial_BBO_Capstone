"""Computational semantic state, visuospatial configuration and retrieval efficiency.

The module extends Artificial Cognition beyond generic memory. It represents
meaning as a weighted concept network, spatial cognition as an object-relation
configuration, and recall as a measurable outcome of storage and retrieval.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import sqrt
from typing import Mapping, Tuple


def _clip(value: float) -> float:
    return max(0.0, min(1.0, value))


@dataclass(frozen=True)
class SemanticNode:
    concept_id: str
    activation: float
    confidence: float
    contextual_fit: float
    source_reliability: float

    def __post_init__(self) -> None:
        for name in ("activation", "confidence", "contextual_fit", "source_reliability"):
            value = getattr(self, name)
            if not 0.0 <= value <= 1.0:
                raise ValueError(f"{name} must be between 0 and 1")


@dataclass(frozen=True)
class SemanticRelation:
    source_id: str
    target_id: str
    relation_type: str
    strength: float
    direction_confidence: float
    contradiction: float

    def __post_init__(self) -> None:
        for name in ("strength", "direction_confidence", "contradiction"):
            value = getattr(self, name)
            if not 0.0 <= value <= 1.0:
                raise ValueError(f"{name} must be between 0 and 1")


@dataclass(frozen=True)
class SemanticState:
    nodes: Tuple[SemanticNode, ...]
    relations: Tuple[SemanticRelation, ...]

    @property
    def coherence(self) -> float:
        if not self.relations:
            return 0.0
        weighted = [
            relation.strength
            * relation.direction_confidence
            * (1.0 - relation.contradiction)
            for relation in self.relations
        ]
        return _clip(sum(weighted) / len(weighted))

    @property
    def semantic_integrity(self) -> float:
        if not self.nodes:
            return 0.0
        node_quality = sum(
            node.activation
            * node.confidence
            * node.contextual_fit
            * node.source_reliability
            for node in self.nodes
        ) / len(self.nodes)
        return _clip(0.65 * node_quality + 0.35 * self.coherence)

    def retrieval_route_score(self, cue_weights: Mapping[str, float]) -> float:
        if not cue_weights or not self.nodes:
            return 0.0
        node_map = {node.concept_id: node for node in self.nodes}
        numerator = 0.0
        denominator = 0.0
        for concept_id, cue_weight in cue_weights.items():
            if cue_weight < 0:
                raise ValueError("cue weights cannot be negative")
            denominator += cue_weight
            node = node_map.get(concept_id)
            if node is not None:
                numerator += cue_weight * node.activation * node.contextual_fit * node.confidence
        if denominator == 0:
            return 0.0
        return _clip(numerator / denominator)


@dataclass(frozen=True)
class SpatialObject:
    object_id: str
    x: float
    y: float
    z: float
    orientation_radians: float
    scale: float
    identity_confidence: float

    def __post_init__(self) -> None:
        if self.scale <= 0:
            raise ValueError("scale must be positive")
        if not 0.0 <= self.identity_confidence <= 1.0:
            raise ValueError("identity_confidence must be between 0 and 1")


@dataclass(frozen=True)
class SpatialRelation:
    source_id: str
    target_id: str
    expected_distance: float
    tolerance: float
    relation_confidence: float

    def __post_init__(self) -> None:
        if self.expected_distance < 0 or self.tolerance < 0:
            raise ValueError("distance and tolerance cannot be negative")
        if not 0.0 <= self.relation_confidence <= 1.0:
            raise ValueError("relation_confidence must be between 0 and 1")


@dataclass(frozen=True)
class VisuospatialConfiguration:
    objects: Tuple[SpatialObject, ...]
    relations: Tuple[SpatialRelation, ...]

    def _object_map(self) -> Mapping[str, SpatialObject]:
        return {obj.object_id: obj for obj in self.objects}

    @property
    def configuration_coherence(self) -> float:
        if not self.relations:
            return 0.0
        object_map = self._object_map()
        scores = []
        for relation in self.relations:
            source = object_map.get(relation.source_id)
            target = object_map.get(relation.target_id)
            if source is None or target is None:
                scores.append(0.0)
                continue
            actual = sqrt(
                (source.x - target.x) ** 2
                + (source.y - target.y) ** 2
                + (source.z - target.z) ** 2
            )
            error = abs(actual - relation.expected_distance)
            if relation.tolerance == 0:
                distance_score = 1.0 if error == 0 else 0.0
            else:
                distance_score = _clip(1.0 - error / relation.tolerance)
            scores.append(distance_score * relation.relation_confidence)
        return _clip(sum(scores) / len(scores))

    def transform_object(
        self,
        object_id: str,
        rotation_radians: float,
        translation: Tuple[float, float, float],
        scale_multiplier: float = 1.0,
    ) -> SpatialObject:
        if scale_multiplier <= 0:
            raise ValueError("scale_multiplier must be positive")
        obj = self._object_map().get(object_id)
        if obj is None:
            raise ValueError(f"unknown object: {object_id}")
        dx, dy, dz = translation
        return SpatialObject(
            object_id=obj.object_id,
            x=obj.x + dx,
            y=obj.y + dy,
            z=obj.z + dz,
            orientation_radians=obj.orientation_radians + rotation_radians,
            scale=obj.scale * scale_multiplier,
            identity_confidence=obj.identity_confidence,
        )


@dataclass(frozen=True)
class RetrievalEfficiency:
    retained_information: float
    retrieved_information: float
    correct_information: float
    retrieval_latency: float
    retrieval_cost: float
    cue_count: int
    false_retrievals: int

    def __post_init__(self) -> None:
        for name in ("retained_information", "retrieved_information", "correct_information"):
            value = getattr(self, name)
            if value < 0:
                raise ValueError(f"{name} cannot be negative")
        if self.retrieval_latency < 0 or self.retrieval_cost < 0:
            raise ValueError("latency and cost cannot be negative")
        if self.cue_count < 0 or self.false_retrievals < 0:
            raise ValueError("counts cannot be negative")

    @property
    def recall_efficiency(self) -> float:
        if self.retained_information == 0:
            return 0.0
        return _clip(self.correct_information / self.retained_information)

    @property
    def retrieval_precision(self) -> float:
        if self.retrieved_information == 0:
            return 0.0
        return _clip(self.correct_information / self.retrieved_information)

    @property
    def retrieval_yield(self) -> float:
        denominator = 1.0 + self.retrieval_latency + self.retrieval_cost + self.cue_count + self.false_retrievals
        return _clip((self.correct_information * self.retrieval_precision) / denominator)

    @property
    def integrated_efficiency(self) -> float:
        return _clip(
            0.45 * self.recall_efficiency
            + 0.35 * self.retrieval_precision
            + 0.20 * self.retrieval_yield
        )
