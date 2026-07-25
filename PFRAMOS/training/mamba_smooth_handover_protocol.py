"""Mamba smooth-handover training protocol for PACC and PFRAMOS.

This protocol adapts published Mamba training lessons into a controlled,
reproducible programme. It treats Warmup-Stable-Decay scheduling, checkpoint
handover, positional loss weighting, decay-phase data refinement and rollback
from loss spikes as hypotheses to validate, not universal truths.

No training is launched by this module.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class TrainingArm:
    arm_id: str
    scheduler: str
    positional_loss_weighting: bool
    decay_phase_data_upgrade: bool
    description: str


TRAINING_ARMS = (
    TrainingArm(
        arm_id="cosine_baseline",
        scheduler="linear_warmup_then_cosine_decay",
        positional_loss_weighting=False,
        decay_phase_data_upgrade=False,
        description="Conventional matched-control baseline.",
    ),
    TrainingArm(
        arm_id="wsd_baseline",
        scheduler="warmup_stable_decay",
        positional_loss_weighting=False,
        decay_phase_data_upgrade=False,
        description="Tests resumable pre-decay checkpoints and stable-phase continuation.",
    ),
    TrainingArm(
        arm_id="wsd_positional_weighting",
        scheduler="warmup_stable_decay",
        positional_loss_weighting=True,
        decay_phase_data_upgrade=False,
        description="Tests down-weighting of early-token loss as an explicit ablation.",
    ),
    TrainingArm(
        arm_id="wsd_quality_decay",
        scheduler="warmup_stable_decay",
        positional_loss_weighting=False,
        decay_phase_data_upgrade=True,
        description="Introduces higher-quality or instruction data only during decay.",
    ),
    TrainingArm(
        arm_id="wsd_quality_decay_positional",
        scheduler="warmup_stable_decay",
        positional_loss_weighting=True,
        decay_phase_data_upgrade=True,
        description="Combined handover arm, retained only if individual ablations justify it.",
    ),
)


HANDOVER_CHECKPOINTS = (
    "post_warmup_checkpoint",
    "stable_phase_25_percent_checkpoint",
    "stable_phase_50_percent_checkpoint",
    "stable_phase_75_percent_checkpoint",
    "pre_decay_checkpoint",
    "mid_decay_checkpoint",
    "final_decay_checkpoint",
)


SMOOTH_HANDOVER_TESTS = (
    "resume_from_each_stable_phase_checkpoint_without learning-rate collapse",
    "continue with the same data mix",
    "continue with a higher-quality data mix",
    "continue with instruction data introduced only at decay",
    "measure transient loss increase after restart",
    "measure steps required to recover pre-restart validation quality",
    "measure final quality against uninterrupted training",
    "verify optimiser-state and scheduler-state restoration",
)


LOSS_SPIKE_POLICY = (
    "Record the exact batch identifiers and source shards associated with every spike.",
    "Checkpoint before and after each detected spike window.",
    "Do not silently skip data without preserving an audit record.",
    "Repeat the suspect batch where safe to distinguish data effects from optimisation noise.",
    "Rollback only when predefined loss, gradient or numerical thresholds are exceeded.",
    "Keep rollback trials separate from the uninterrupted control arm.",
)


THROUGHPUT_CONTROLS = (
    "matched model parameter count",
    "matched sequence length",
    "matched global token batch",
    "matched precision",
    "matched activation recomputation policy",
    "matched FSDP wrapping policy",
    "matched hardware and software versions",
    "matched data-order seed",
)


EVALUATION_METRICS = (
    "validation_perplexity",
    "top_1_accuracy",
    "top_3_accuracy",
    "top_10_accuracy",
    "exact_state_tracking_accuracy",
    "needle_retrieval_accuracy_by_position_and_context_length",
    "training_tokens_per_second",
    "model_flops_utilisation_with_method_recorded",
    "peak_device_memory",
    "restart_recovery_steps",
    "accuracy_per_compute_cost",
)


GOVERNANCE_RULES = (
    "WSD is treated as a testable scheduling hypothesis.",
    "Positional loss weighting is never enabled without a matched unweighted arm.",
    "A decay-phase data upgrade must preserve source, licence and mixture records.",
    "Pre-decay checkpoints are preserved for reproducible continuation studies.",
    "Long-context tests must report retrieval position as well as context length.",
    "Benchmark contamination is reviewed before external evaluation.",
    "Trial findings do not become publication claims until replicated.",
)


def arm_ids() -> Tuple[str, ...]:
    return tuple(arm.arm_id for arm in TRAINING_ARMS)
