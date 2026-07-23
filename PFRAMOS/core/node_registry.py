"""Lifecycle and eligibility registry for PFRAMOS optimisation nodes."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, List

from .node_contract import NodeState, OptimisationNode


LIVE_STATES = {
    NodeState.VALIDATED,
    NodeState.ELIGIBLE,
    NodeState.PRIMED,
    NodeState.ACTIVE,
    NodeState.TERMINAL,
    NodeState.DORMANT,
}


@dataclass
class RegistryEntry:
    node: OptimisationNode
    independent_value_score: float = 0.0
    robustness_score: float = 0.0
    auditability_score: float = 0.0

    @property
    def admission_score(self) -> float:
        return (
            self.independent_value_score
            + self.robustness_score
            + self.auditability_score
        ) / 3.0


class NodeRegistry:
    """Register, activate, retire and inspect interchangeable nodes."""

    def __init__(self) -> None:
        self._entries: Dict[str, RegistryEntry] = {}

    def register(self, entry: RegistryEntry) -> None:
        node_id = entry.node.node_id
        if node_id in self._entries:
            raise ValueError(f"Node already registered: {node_id}")
        self._entries[node_id] = entry

    def get(self, node_id: str) -> RegistryEntry:
        try:
            return self._entries[node_id]
        except KeyError as error:
            raise KeyError(f"Unknown node: {node_id}") from error

    def eligible_nodes(self, minimum_admission_score: float = 0.5) -> List[OptimisationNode]:
        return [
            entry.node
            for entry in self._entries.values()
            if entry.node.state in LIVE_STATES
            and entry.admission_score >= minimum_admission_score
        ]

    def retire(self, node_id: str) -> None:
        entry = self.get(node_id)
        entry.node.state = NodeState.RETIRED

    def entries(self) -> Iterable[RegistryEntry]:
        return tuple(self._entries.values())
