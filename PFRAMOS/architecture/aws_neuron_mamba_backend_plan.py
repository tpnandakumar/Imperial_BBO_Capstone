"""AWS Neuron backend plan for the PACC and PFRAMOS state-space programme.

The current awslabs/state-space-models-neuron repository provides a working
Mamba-2 and hybrid Mamba-2 implementation for AWS Trainium. It does not yet
provide Mamba-3. This module therefore registers AWS Neuron as:

1. an immediate Mamba-2 training and inference backend,
2. a matched-hardware comparison route against NVIDIA CUDA,
3. a reference implementation for a future Mamba-3 Neuron port.

No claim of Mamba-3 support is made until complex-valued recurrence,
exponential-trapezoidal discretisation, MIMO updates and associated kernels are
implemented and validated on Neuron.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class NeuronBackend:
    backend_id: str
    official_repository: str
    current_model_support: Tuple[str, ...]
    current_capabilities: Tuple[str, ...]
    required_environment: Tuple[str, ...]
    current_state: str
    notes: str


AWS_NEURON_BACKEND = NeuronBackend(
    backend_id="aws_neuron_state_space_backend",
    official_repository="https://github.com/awslabs/state-space-models-neuron",
    current_model_support=(
        "mamba2",
        "mamba2_hybrid_attention",
    ),
    current_capabilities=(
        "aws_trainium_training",
        "nki_custom_forward_backward_kernels",
        "autoregressive_inference_kernel",
        "tensor_parallelism",
        "sequence_parallelism",
        "zero1_optimizer",
        "gradient_accumulation",
        "mixed_precision",
        "multi_instance_training",
        "huggingface_mamba2_checkpoint_conversion",
    ),
    required_environment=(
        "aws_trainium_or_compatible_neuron_instance",
        "torch_neuronx",
        "neuronx_cc",
        "neuronx_distributed",
        "nki",
        "version_pinned_deep_learning_ami",
    ),
    current_state="mamba2_ready_mamba3_port_required",
    notes="Use as the immediate Trainium baseline and as the engineering template for a future Mamba-3 Neuron implementation.",
)


MAMBA3_PORT_REQUIREMENTS = (
    "Implement exponential-trapezoidal state update in NKI.",
    "Implement complex-valued or equivalent paired-real state representation.",
    "Implement data-dependent rotary state transition.",
    "Implement Mamba-3 SISO kernels.",
    "Implement Mamba-3 MIMO kernels.",
    "Implement forward, backward and autoregressive inference kernels.",
    "Define tensor-parallel partitioning for new projections and state groups.",
    "Provide checkpoint conversion from the authoritative Mamba-3 implementation.",
    "Validate numerical agreement against an NVIDIA reference implementation.",
    "Run matched accuracy, throughput, latency, memory and energy comparisons.",
)


VALIDATION_SEQUENCE = (
    "reproduce a small Mamba-2 synthetic state-tracking baseline on Trainium",
    "verify checkpoint conversion and numerical equivalence",
    "measure Mamba-2 Trainium throughput, latency and memory",
    "port the smallest Mamba-3 SISO kernel",
    "validate recurrence numerics against the authoritative implementation",
    "add Mamba-3 MIMO support",
    "run the controlled Mamba-2 versus Mamba-3 validation suite",
    "compare Trainium and NVIDIA under matched model and token budgets",
)


GOVERNANCE_RULES = (
    "Pin the awslabs repository commit and Neuron software versions.",
    "Do not label the current repository as Mamba-3 compatible.",
    "Keep trial results separate from publication evidence until replicated.",
    "Record cloud instance type, chip count, compiler flags and compile cache state.",
    "Measure cost and energy alongside accuracy and throughput where possible.",
    "Retain an NVIDIA reference implementation for cross-backend correctness checks.",
)
