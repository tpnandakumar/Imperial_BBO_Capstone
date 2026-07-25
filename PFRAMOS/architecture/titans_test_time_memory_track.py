"""Titans-inspired test-time adaptive memory track for PACC and PFRAMOS.

This module registers Titans as a candidate adaptive memory architecture that
can sit above or beside efficient sequence backbones such as Mamba. It does not
replace Mamba, TorchTitan or AWS Neuron. Instead, it defines a research track
for test-time long-term neural memory, surprise-driven updates, adaptive
forgetting and persistent task memory.

The design follows the paper's separation of:

1. short-term memory for current-context processing,
2. long-term neural memory updated during inference,
3. persistent memory for task-level knowledge.

No model weights are updated by this module.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class TitansVariant:
    variant_id: str
    memory_integration: str
    description: str


VARIANTS = (
    TitansVariant(
        variant_id="memory_as_context",
        memory_integration="prepend_or_merge_retrieved_memory_with_current_context",
        description="Retrieved long-term memory is exposed to the current-context processor as additional context.",
    ),
    TitansVariant(
        variant_id="memory_as_layer",
        memory_integration="dedicated_long_term_memory_layer_in_sequence_stack",
        description="The neural memory becomes a distinct processing layer.",
    ),
    TitansVariant(
        variant_id="gated_memory_branch",
        memory_integration="parallel_memory_branch_with_learned_gate",
        description="Current processing and long-term memory run in parallel and are combined by a learned gate.",
    ),
)


MEMORY_COMPONENTS = (
    "short_term_current_context_processor",
    "test_time_neural_long_term_memory",
    "persistent_task_memory",
    "surprise_estimator",
    "surprise_momentum_state",
    "adaptive_forgetting_gate",
    "memory_read_interface",
    "memory_write_interface",
    "memory_capacity_controller",
)


PFRAMOS_ALIGNMENT = (
    "Map surprise magnitude to dynamic function priority.",
    "Map adaptive forgetting to RaR and memory-return policies.",
    "Use PIMF influence diagnostics to decide whether surprising events are persistent or transient.",
    "Use PHCS coherence to suppress incoherent test-time memory writes.",
    "Use the common memory pool for temporary working state.",
    "Return inactive memory to the shared pool when no longer justified.",
    "Keep persistent task memory separate from trial-specific adaptive memory.",
)


MODEL_COMPARISON_ARMS = (
    "transformer_sliding_window_baseline",
    "mamba2_baseline",
    "mamba3_siso_baseline",
    "mamba3_mimo_baseline",
    "titans_memory_as_context",
    "titans_memory_as_layer",
    "titans_gated_memory_branch",
    "mamba3_with_titans_gated_memory",
)


VALIDATION_TASKS = (
    "needle_in_haystack_by_position_and_context_length",
    "babilong_reasoning",
    "synthetic_state_tracking",
    "continual_context_switching",
    "surprise_event_retention",
    "controlled_forgetting",
    "time_series_forecasting",
    "dna_sequence_modelling",
    "dialogue_memory_consistency",
    "retrieval_after_long_distractor_intervals",
)


REQUIRED_ABLATIONS = (
    "without_surprise_momentum",
    "without_adaptive_forgetting",
    "linear_memory_versus_deep_memory",
    "without_persistent_memory",
    "without_short_term_attention",
    "memory_as_context_versus_layer_versus_gated_branch",
    "fixed_write_rate_versus_surprise_weighted_write",
    "coherence_gated_write_versus_ungated_write",
    "pimf_persistence_filter_on_versus_off",
)


SAFETY_AND_PRIVACY_RULES = (
    "Do not permit unrestricted memorisation of personal or sensitive data.",
    "Every test-time write must retain source, purpose and expiry metadata.",
    "Support deletion, rollback and memory reset.",
    "Separate persistent task memory from user-specific or session-specific memory.",
    "Do not promote adaptive memory into publication evidence without reproducible replay.",
    "Record what was written, forgotten, retrieved and retained.",
)


EFFICIENCY_METRICS = (
    "memory_update_time_ms",
    "memory_read_time_ms",
    "tokens_per_second",
    "peak_device_memory_bytes",
    "test_time_update_flops",
    "retrieval_accuracy_per_memory_byte",
    "accuracy_per_unit_latency",
    "forgetting_precision",
    "retention_recall",
    "coherence_after_memory_update",
)


RESEARCH_SEQUENCE = (
    "implement a tiny linear neural memory baseline",
    "add surprise-weighted test-time updates",
    "add surprise momentum",
    "add adaptive forgetting",
    "compare shallow and deep memory",
    "test the three memory-integration variants",
    "add PFRAMOS coherence gating and PIMF persistence filtering",
    "combine the strongest memory branch with Mamba-3",
    "scale through TorchTitan after single-device numerical validation",
    "compare NVIDIA, AMD and AWS Neuron routes where supported",
)
