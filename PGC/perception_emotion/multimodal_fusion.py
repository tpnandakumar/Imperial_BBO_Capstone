"""Reliability-weighted multimodal fusion for PGC.

Factual and emotional signals remain separate throughout fusion. Emotional
intensity cannot overwrite weak factual evidence.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import sqrt
from typing import Iterable, Tuple

from .modality_registry import modality_by_id


@dataclass(frozen=True)
class PerceptualObservation:
    modality_id: str
    factual_signal: float
    emotional_signal: float
    confidence: float
    reliability: float
    provenance: str


@dataclass(frozen=True)
class FusedPerception:
    factual_estimate: float
    emotional_estimate: float
    factual_conflict: float
    emotional_conflict: float
    evidence_strength: float
    modality_coverage: int
    modality_weights: Tuple[Tuple[str, float], ...]
    excluded_modalities: Tuple[str, ...]


def _bounded(value: float, name: str) -> float:
    if not 0.0 <= value <= 1.0:
        raise ValueError(f"{name} must be within [0, 1]")
    return value


def _weighted_dispersion(values: list[float], weights: list[float], mean: float) -> float:
    total = sum(weights)
    if total <= 0.0:
        return 1.0
    variance = sum(weight * ((value - mean) ** 2) for value, weight in zip(values, weights)) / total
    return min(1.0, sqrt(max(0.0, variance)))


def fuse_observations(observations: Iterable[PerceptualObservation]) -> FusedPerception:
    observation_list = tuple(observations)
    if not observation_list:
        raise ValueError("at least one perceptual observation is required")

    included: list[PerceptualObservation] = []
    excluded: list[str] = []
    for observation in observation_list:
        definition = modality_by_id(observation.modality_id)
        _bounded(observation.factual_signal, "factual_signal")
        _bounded(observation.emotional_signal, "emotional_signal")
        _bounded(observation.confidence, "confidence")
        _bounded(observation.reliability, "reliability")
        if not observation.provenance.strip():
            raise ValueError("provenance is required")
        if observation.reliability < definition.minimum_reliability:
            excluded.append(observation.modality_id)
            continue
        included.append(observation)

    if not included:
        raise ValueError("no observation passed the modality reliability threshold")

    raw_weights = [item.confidence * item.reliability for item in included]
    total_weight = sum(raw_weights)
    if total_weight <= 0.0:
        raise ValueError("included observations have zero total evidential weight")

    weights = [value / total_weight for value in raw_weights]
    factual_values = [item.factual_signal for item in included]
    emotional_values = [item.emotional_signal for item in included]
    factual_mean = sum(value * weight for value, weight in zip(factual_values, weights))
    emotional_mean = sum(value * weight for value, weight in zip(emotional_values, weights))

    evidence_strength = min(
        1.0,
        sum(item.confidence * item.reliability for item in included) / len(included),
    )

    return FusedPerception(
        factual_estimate=factual_mean,
        emotional_estimate=emotional_mean,
        factual_conflict=_weighted_dispersion(factual_values, weights, factual_mean),
        emotional_conflict=_weighted_dispersion(emotional_values, weights, emotional_mean),
        evidence_strength=evidence_strength,
        modality_coverage=len(included),
        modality_weights=tuple((item.modality_id, weight) for item, weight in zip(included, weights)),
        excluded_modalities=tuple(excluded),
    )
