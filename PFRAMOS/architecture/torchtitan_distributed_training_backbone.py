"""TorchTitan distributed training backbone for PACC and PFRAMOS.

TorchTitan is registered as the general PyTorch-native distributed training
layer for large-scale generative, sequential and state-space experiments. AWS
Neuron remains the Trainium-specific backend. Mamba-3 requires a dedicated
TorchTitan model adapter, parallelisation plan and checkpoint interface before
it can use this backbone.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class TorchTitanBackend:
    backend_id: str
    official_repository: str
    licence: str
    current_state: str
    current_model_support: Tuple[str, ...]
    reusable_capabilities: Tuple[str, ...]
    required_integrations: Tuple[str, ...]
    governance_rules: Tuple[str, ...]


TORCHTITAN = TorchTitanBackend(
    backend_id="torchtitan_distributed_training_backbone",
    official_repository="https://github.com/pytorch/torchtitan",
    licence="BSD-3-Clause",
    current_state="general_backbone_ready_mamba3_adapter_required",
    current_model_support=(
        "llama3_1_out_of_the_box",
        "custom_models_through_extension_points",
    ),
    reusable_capabilities=(
        "fsdp2",
        "tensor_parallelism",
        "pipeline_parallelism",
        "context_parallelism",
        "ddp",
        "hsdp",
        "distributed_checkpointing",
        "asynchronous_checkpointing",
        "checkpointable_data_loading",
        "activation_checkpointing",
        "torch_compile",
        "float8_training",
        "mxfp8_training",
        "supervised_fine_tuning",
        "torchft_fault_tolerance",
        "gradient_accumulation",
        "warmup_stable_decay_scheduler",
        "bf16_optimizer_states",
        "structured_logging",
        "tensorboard_and_wandb_metrics",
        "cpu_gpu_and_memory_profiling",
    ),
    required_integrations=(
        "define_pacc_model_adapter",
        "define_mamba2_model_adapter",
        "define_mamba3_siso_model_adapter",
        "define_mamba3_mimo_model_adapter",
        "map_state_space_layers_to_parallelism",
        "define_distributed_checkpoint_schema",
        "define_dataset_and_sampler_adapter",
        "define_fault_tolerant_resume_tests",
        "define_nvidia_and_amd_backend_profiles",
        "retain_aws_neuron_as_separate_backend",
    ),
    governance_rules=(
        "Pin TorchTitan, PyTorch, CUDA or ROCm and torchao versions.",
        "Do not claim Mamba-3 support until the adapter and kernels are validated.",
        "Record the exact data, tensor, pipeline and context parallel topology.",
        "Use interoperable checkpoints only after round-trip validation.",
        "Run single-device numerical equivalence before distributed scaling.",
        "Keep scale-up evidence separate from model-quality evidence.",
        "Measure throughput, memory, TFLOPs, MFU, restart recovery and cost.",
        "Preserve source-specific licences for all datasets and model assets.",
    ),
)


INTEGRATION_SEQUENCE = (
    "pin a stable TorchTitan release and matching PyTorch stack",
    "run a tiny built-in Llama smoke test to validate infrastructure",
    "add a minimal PACC-compatible custom model through extension points",
    "add Mamba-2 as the first state-space adapter",
    "validate single-device outputs against the authoritative implementation",
    "add FSDP2 and tensor-parallel scaling",
    "add distributed and asynchronous checkpointing",
    "validate fault-tolerant resume with checkpointable data loading",
    "port Mamba-3 SISO and then MIMO after numerical validation",
    "compare TorchTitan NVIDIA or AMD execution against AWS Neuron",
)


EFFICIENCY_AND_RELIABILITY_METRICS = (
    "tokens_per_second",
    "training_step_time_ms",
    "peak_device_memory_bytes",
    "tflops",
    "model_flops_utilisation",
    "checkpoint_write_time_seconds",
    "checkpoint_restore_time_seconds",
    "restart_recovery_steps",
    "failure_recovery_success_rate",
    "cost_per_billion_tokens",
    "energy_if_measurable",
)
