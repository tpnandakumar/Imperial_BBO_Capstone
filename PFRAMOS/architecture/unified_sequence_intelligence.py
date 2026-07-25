"""Unified sequence intelligence for PFRAMOS.

This architecture combines selective state, local attention, persistent rules,
surprise-sensitive long-term memory, adaptive forgetting, PIMF diagnosis and
PFRAMOS conduit arbitration. Superiority over external architectures is a
research hypothesis until demonstrated by reproducible benchmarks.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Tuple


@dataclass(frozen=True)
class SequenceContext:
    context_id: str
    token_or_step_count: int
    local_context_pressure: float
    long_range_dependency: float
    novelty: float
    uncertainty: float
    contamination_risk: float
    compute_pressure: float
    memory_pressure: float

    def __post_init__(self) -> None:
        if self.token_or_step_count < 1:
            raise ValueError("token_or_step_count must be positive")
        for name in (
            "local_context_pressure",
            "long_range_dependency",
            "novelty",
            "uncertainty",
            "contamination_risk",
            "compute_pressure",
            "memory_pressure",
        ):
            value = getattr(self, name)
            if not 0.0 <= value <= 1.0:
                raise ValueError(f"{name} must be between 0 and 1")


@dataclass(frozen=True)
class MemoryLayerState:
    persistent_rules: Mapping[str, float]
    short_term_state: Mapping[str, float]
    selective_state: Mapping[str, float]
    long_term_neural_state: Mapping[str, float]
    quarantine_state: Mapping[str, float]


@dataclass(frozen=True)
class SequenceRouteDecision:
    route_id: str
    use_local_attention: bool
    use_selective_state: bool
    use_long_term_memory: bool
    update_long_term_memory: bool
    use_persistent_memory: bool
    forgetting_weight: float
    retention_weight: float
    exploration_weight: float
    shadow_only: bool
    reasons: Tuple[str, ...]


def choose_sequence_route(context: SequenceContext) -> SequenceRouteDecision:
    reasons = []

    use_local_attention = context.local_context_pressure >= 0.45
    if use_local_attention:
        reasons.append("local_precision_required")

    use_selective_state = context.long_range_dependency >= 0.35 or context.memory_pressure >= 0.50
    if use_selective_state:
        reasons.append("compressed_long_range_state_required")

    use_long_term_memory = context.long_range_dependency >= 0.65 or context.novelty >= 0.70
    if use_long_term_memory:
        reasons.append("long_term_memory_relevant")

    safe_to_update = context.contamination_risk < 0.30 and context.uncertainty < 0.65
    update_long_term_memory = use_long_term_memory and context.novelty >= 0.70 and safe_to_update
    if update_long_term_memory:
        reasons.append("surprise_supported_memory_update")

    use_persistent_memory = True
    retention = (
        0.35 * context.long_range_dependency
        + 0.30 * context.novelty
        + 0.20 * (1.0 - context.uncertainty)
        + 0.15 * (1.0 - context.contamination_risk)
    )
    retention = max(0.0, min(1.0, retention))
    forgetting = max(0.0, min(1.0, 1.0 - retention))

    exploration = (
        0.40 * context.novelty
        + 0.30 * context.uncertainty
        + 0.20 * context.long_range_dependency
        + 0.10 * context.memory_pressure
    ) * (1.0 - context.contamination_risk)
    exploration = max(0.0, min(1.0, exploration))

    shadow_only = context.contamination_risk >= 0.20 or context.uncertainty >= 0.50
    if shadow_only:
        reasons.append("shadow_validation_required")

    if context.compute_pressure >= 0.70:
        reasons.append("p_c4_efficiency_pressure")

    route_parts = ["persistent"]
    if use_local_attention:
        route_parts.append("local")
    if use_selective_state:
        route_parts.append("selective")
    if use_long_term_memory:
        route_parts.append("longterm")

    return SequenceRouteDecision(
        route_id="+".join(route_parts),
        use_local_attention=use_local_attention,
        use_selective_state=use_selective_state,
        use_long_term_memory=use_long_term_memory,
        update_long_term_memory=update_long_term_memory,
        use_persistent_memory=use_persistent_memory,
        forgetting_weight=forgetting,
        retention_weight=retention,
        exploration_weight=exploration,
        shadow_only=shadow_only,
        reasons=tuple(reasons),
    )
