"""Titans and MIRAS test-time adaptive memory track for PACC and PFRAMOS.

Titans is treated as a candidate adaptive memory architecture that can sit
above or beside efficient sequence backbones such as Mamba. MIRAS supplies the
broader design framework used to compare memory structures, learning biases,
retention mechanisms and test-time update algorithms.

This module does not replace Mamba, TorchTitan or AWS Neuron, and it does not
perform parameter updates by itself.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class TitansVariant:
    variant_id: str
    memory_integration: str
    description: str


@dataclass(frozen=True)
class MIRASVariant:
    variant_id: str
    objective_family: str
    retention_family: str
    intended_property: str


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


MIRAS_DESIGN_AXES = (
    "memory_architecture",
    "attentional_bias",
    "retention_gate",
    "memory_update_algorithm",
)


MIRAS_VARIANTS = (
    MIRASVariant(
        variant_id="yaad",
        objective_family="robust_huber_like_bias",
        retention_family="robust_regularisation",
        intended_property="reduced_sensitivity_to_outliers_and_single_event_noise",
    ),
    MIRASVariant(
        variant_id="moneta",
        objective_family="generalised_norm_bias",
        retention_family="generalised_norm_regularisation",
        intended_property="stronger_control_of_memory_update_geometry",
    ),
    MIRASVariant(
        variant_id="memora",
        objective_family="probability_constrained_associative_memory",
        retention_family="stability_constrained_regularisation",
        intended_property="balanced_and_stable_memory_updates",
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
    "Treat the MIRAS retention gate as the formal memory-regularisation interface.",
    "Route robust MIRAS objectives through PFRAMOS validation before activation.",
)


MODEL_COMPARISON_ARMS = (
    "transformer_sliding_window_baseline",
    "mamba2_baseline",
    "mamba3_siso_baseline",
    "mamba3_mimo_baseline",
    "titans_memory_as_context",
    "titans_memory_as_layer",
    "titans_gated_memory_branch",
    "miras_yaad",
    "miras_moneta",
    "miras_memora",
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
    "outlier_robust_memory_update",
    "memory_stability_under_conflicting_streams",
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
    "mse_bias_versus_robust_bias",
    "standard_weight_decay_versus_miras_retention_gate",
    "yaad_versus_moneta_versus_memora",
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
    "outlier_recovery_time",
    "memory_drift_under_conflicting_updates",
)


RESEARCH_SEQUENCE = (
    "implement a tiny linear neural memory baseline",
    "add surprise-weighted test-time updates",
    "add surprise momentum",
    "add adaptive forgetting",
    "compare shallow and deep memory",
    "test the three Titans memory-integration variants",
    "implement the four MIRAS design axes explicitly",
    "compare MSE, robust and generalised-norm memory objectives",
    "compare YAAD, MONETA and MEMORA under matched controls",
    "add PFRAMOS coherence gating and PIMF persistence filtering",
    "combine the strongest memory branch with Mamba-3",
    "scale through TorchTitan after single-device numerical validation",
    "compare NVIDIA, AMD and AWS Neuron routes where supported",
)
