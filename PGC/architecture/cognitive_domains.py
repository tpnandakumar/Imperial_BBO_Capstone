"""Cognitive-domain registry for PGC.

The registry describes available capability families without claiming that any
particular implementation has already passed validation.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class CognitiveDomain:
    domain_id: str
    modalities: Tuple[str, ...]
    candidate_engines: Tuple[str, ...]
    required_metrics: Tuple[str, ...]
    default_priority: int
    publication_ready: bool = False


DOMAINS = (
    CognitiveDomain(
        domain_id="language_dialogue",
        modalities=("text", "dialogue"),
        candidate_engines=("transformer_control", "mamba2", "mamba3", "titans_miras_memory"),
        required_metrics=("task_accuracy", "calibration", "consistency", "safety", "latency"),
        default_priority=5,
    ),
    CognitiveDomain(
        domain_id="code_reasoning",
        modalities=("source_code", "repository_structure"),
        candidate_engines=("code_model_control", "mamba3", "retrieval_memory"),
        required_metrics=("pass_rate", "licence_traceability", "security", "latency"),
        default_priority=6,
    ),
    CognitiveDomain(
        domain_id="vision",
        modalities=("image",),
        candidate_engines=("vision_transformer", "cnn_control", "multimodal_router"),
        required_metrics=("accuracy", "robustness", "calibration", "memory_cost"),
        default_priority=6,
    ),
    CognitiveDomain(
        domain_id="temporal_vision",
        modalities=("video", "tracking"),
        candidate_engines=("temporal_encoder", "mamba3", "tracking_memory"),
        required_metrics=("action_accuracy", "tracking_continuity", "frame_loss_robustness", "latency"),
        default_priority=7,
    ),
    CognitiveDomain(
        domain_id="speech_audio",
        modalities=("speech", "environmental_audio"),
        candidate_engines=("asr_control", "audio_encoder", "temporal_memory"),
        required_metrics=("word_error_rate", "event_map", "accent_robustness", "noise_robustness"),
        default_priority=6,
    ),
    CognitiveDomain(
        domain_id="time_series",
        modalities=("univariate_series", "multivariate_series"),
        candidate_engines=("time_series_library", "mamba2", "mamba3", "titans_memory"),
        required_metrics=("forecast_error", "anomaly_f1", "imputation_error", "stability"),
        default_priority=7,
    ),
    CognitiveDomain(
        domain_id="optimisation",
        modalities=("objective_function", "constraints", "observations"),
        candidate_engines=("pframos", "coco_bbob", "nevergrad_control", "fico_control"),
        required_metrics=("best_value", "evaluation_budget", "robustness", "coherence", "cost"),
        default_priority=3,
    ),
    CognitiveDomain(
        domain_id="clinical_research",
        modalities=("tabular", "time_series", "text", "signals"),
        candidate_engines=("clinical_control", "pimf", "time_series_engine", "language_engine"),
        required_metrics=("sensitivity", "specificity", "calibration", "privacy", "clinical_validity"),
        default_priority=2,
    ),
    CognitiveDomain(
        domain_id="cross_modal_reasoning",
        modalities=("multimodal",),
        candidate_engines=("pgc_router", "shared_memory", "pframos", "phcs"),
        required_metrics=("cross_modal_consistency", "task_success", "coherence", "uncertainty"),
        default_priority=4,
    ),
)


def domain_by_id(domain_id: str) -> CognitiveDomain:
    for domain in DOMAINS:
        if domain.domain_id == domain_id:
            return domain
    raise ValueError(f"unknown cognitive domain: {domain_id}")


def active_domains() -> Tuple[CognitiveDomain, ...]:
    return DOMAINS
