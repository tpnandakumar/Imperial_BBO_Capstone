"""Controlled Mamba-3 validation plan for PACC and PFRAMOS.

This module defines a reproducible comparison between Mamba-2, Mamba-3 SISO
and Mamba-3 MIMO. It focuses first on synthetic state tracking, arithmetic and
retrieval before any fine-tuning or pretraining. No model weights are changed
by this module.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class ValidationTask:
    task_id: str
    family: str
    description: str
    primary_metric: str
    controls: Tuple[str, ...]


TASKS = (
    ValidationTask(
        task_id="alternating_state",
        family="synthetic_state_tracking",
        description="Track alternating latent states across variable sequence lengths with distractor tokens.",
        primary_metric="exact_state_accuracy",
        controls=("matched_token_budget", "matched_parameter_budget", "five_random_seeds"),
    ),
    ValidationTask(
        task_id="parity_tracking",
        family="synthetic_state_tracking",
        description="Predict parity of binary sequences under increasing context length.",
        primary_metric="exact_sequence_accuracy",
        controls=("balanced_classes", "unseen_lengths", "chance_baseline"),
    ),
    ValidationTask(
        task_id="modular_arithmetic",
        family="algorithmic_arithmetic",
        description="Maintain and update modular arithmetic state over long token streams.",
        primary_metric="exact_answer_accuracy",
        controls=("held_out_moduli", "held_out_lengths", "no_chain_of_thought_training"),
    ),
    ValidationTask(
        task_id="induction_copy",
        family="induction_and_retrieval",
        description="Retrieve and reproduce a token associated with a repeated key after variable delays.",
        primary_metric="retrieval_accuracy",
        controls=("novel_keys", "variable_delay", "distractor_density"),
    ),
    ValidationTask(
        task_id="multi_register_update",
        family="synthetic_state_tracking",
        description="Update several independent registers and report selected final values.",
        primary_metric="all_registers_exact_accuracy",
        controls=("matched_register_count", "unseen_update_orders", "balanced_queries"),
    ),
    ValidationTask(
        task_id="bbh_selected",
        family="external_reasoning_benchmark",
        description="Run a fixed, contamination-reviewed subset of BBH after synthetic validation.",
        primary_metric="task_macro_accuracy",
        controls=("prompt_lock", "no_training_on_test", "published_scoring_protocol"),
    ),
)


MODEL_ARMS = (
    "mamba2_matched_baseline",
    "mamba3_siso",
    "mamba3_mimo",
)


REQUIRED_ABLATIONS = (
    "mamba3_without_complex_rotation",
    "mamba3_without_exponential_trapezoidal_update",
    "mamba3_siso_versus_mimo",
    "matched_state_size",
    "matched_decode_latency",
    "matched_parameter_count",
)


EFFICIENCY_METRICS = (
    "tokens_per_second",
    "peak_gpu_memory_bytes",
    "decode_latency_ms_per_token",
    "training_step_time_ms",
    "energy_if_measurable",
    "accuracy_per_unit_latency",
)


GOVERNANCE_RULES = (
    "Synthetic datasets are generated from versioned scripts and seeds.",
    "BBH remains evaluation-only and is never used for parameter updates.",
    "Trial outputs remain separate from publication evidence until replicated.",
    "No claim of Mamba-3 superiority is made without matched controls.",
    "Exact package, repository commit, GPU, CUDA and kernel versions are recorded.",
    "LoRA target modules are discovered from the instantiated model and never guessed.",
)


def validation_order() -> Tuple[str, ...]:
    return tuple(task.task_id for task in TASKS)
