"""Capability and evidence matrix for PGC."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class CapabilityRecord:
    capability_id: str
    domain: str
    implementation_state: str
    evidence_state: str
    required_next_evidence: Tuple[str, ...]


CAPABILITIES = (
    CapabilityRecord(
        "evidence_aware_routing",
        "regulation",
        "scaffolded",
        "unvalidated",
        ("unit_tests", "static_router_baseline", "routing_regret_trial"),
    ),
    CapabilityRecord(
        "state_tracking",
        "sequence_cognition",
        "planned",
        "protocol_defined",
        ("synthetic_generator", "mamba2_baseline", "mamba3_comparison"),
    ),
    CapabilityRecord(
        "test_time_memory",
        "memory",
        "planned",
        "protocol_defined",
        ("tiny_memory_baseline", "titans_variants", "miras_ablations"),
    ),
    CapabilityRecord(
        "coherence_regulation",
        "regulation",
        "existing_component",
        "requires_pgc_integration",
        ("phcs_adapter", "coherence_gate_test", "ungated_ablation"),
    ),
    CapabilityRecord(
        "influence_persistence",
        "regulation",
        "existing_component",
        "requires_pgc_integration",
        ("pimf_adapter", "persistence_filter_test", "false_retention_analysis"),
    ),
    CapabilityRecord(
        "dynamic_memory_allocation",
        "memory",
        "existing_component",
        "requires_consolidation",
        ("single_orchestrator", "legacy_policy_deprecation", "stress_test"),
    ),
    CapabilityRecord(
        "multimodal_perception",
        "perception",
        "source_registry_only",
        "unvalidated",
        ("small_vision_trial", "small_audio_trial", "cross_modal_trial"),
    ),
    CapabilityRecord(
        "distributed_training",
        "execution",
        "backend_plans_defined",
        "not_executed",
        ("torchtitan_smoke_test", "checkpoint_round_trip", "failure_recovery_test"),
    ),
    CapabilityRecord(
        "trainium_state_space_execution",
        "execution",
        "mamba2_backend_identified",
        "not_executed",
        ("aws_credentials", "trainium_instance", "mamba2_dry_run"),
    ),
)


def capability_by_id(capability_id: str) -> CapabilityRecord:
    for capability in CAPABILITIES:
        if capability.capability_id == capability_id:
            return capability
    raise ValueError(f"unknown capability: {capability_id}")
