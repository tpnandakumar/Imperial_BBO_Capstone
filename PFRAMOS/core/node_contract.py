"""Common optimisation-node contract for PFRAMOS.

The contract is deliberately transparent. Every node must expose its evidence,
assumptions, candidate outputs, uncertainty, conflicts and audit information.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Mapping, Protocol, Sequence


class NodeState(str, Enum):
    PROPOSED = "proposed"
    EXPERIMENTAL = "experimental"
    VALIDATED = "validated"
    ELIGIBLE = "eligible"
    PRIMED = "primed"
    ACTIVE = "active"
    TERMINAL = "terminal"
    DORMANT = "dormant"
    DEPRECATED = "deprecated"
    RETIRED = "retired"
    ARCHIVED = "archived"


@dataclass(frozen=True)
class EvidenceSignal:
    name: str
    value: Any
    strength: float
    confidence: float
    stability: float
    identifiability: float
    independence: float
    lineage: Sequence[str] = field(default_factory=tuple)

    def __post_init__(self) -> None:
        for field_name in (
            "strength",
            "confidence",
            "stability",
            "identifiability",
            "independence",
        ):
            value = getattr(self, field_name)
            if not 0.0 <= value <= 1.0:
                raise ValueError(f"{field_name} must be between 0 and 1")


@dataclass(frozen=True)
class NodeContext:
    problem_id: str
    objective: str
    constraints: Mapping[str, Any]
    evidence: Sequence[EvidenceSignal]
    upstream_messages: Sequence[Mapping[str, Any]] = field(default_factory=tuple)


@dataclass(frozen=True)
class NodeResult:
    node_id: str
    local_objective: str
    recommendation: Mapping[str, Any]
    alternatives: Sequence[Mapping[str, Any]]
    signals: Sequence[EvidenceSignal]
    uncertainty: float
    conflicts: Sequence[str]
    feedback_requests: Sequence[Mapping[str, Any]]
    audit_notes: Sequence[str]

    def __post_init__(self) -> None:
        if not 0.0 <= self.uncertainty <= 1.0:
            raise ValueError("uncertainty must be between 0 and 1")


class OptimisationNode(Protocol):
    """Interface implemented by every PFRAMOS optimisation node."""

    node_id: str
    state: NodeState

    def relevance(self, context: NodeContext) -> float:
        """Return problem-specific relevance in the closed interval [0, 1]."""

    def optimise(self, context: NodeContext) -> NodeResult:
        """Optimise the node's local objective and return an auditable result."""

    def receive_feedback(self, messages: Sequence[Mapping[str, Any]]) -> None:
        """Recalibrate the node using bidirectional or lateral feedback."""
