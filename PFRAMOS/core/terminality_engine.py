"""Select a temporary Terminal Active Node from validated activity evidence."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List, Sequence


@dataclass(frozen=True)
class NodeActivity:
    node_id: str
    relevance: float
    evidence_strength: float
    robustness: float
    pathway_support: float
    uncertainty: float
    fragility: float
    dependency_penalty: float

    def __post_init__(self) -> None:
        for name, value in self.__dict__.items():
            if name == "node_id":
                continue
            if not 0.0 <= value <= 1.0:
                raise ValueError(f"{name} must be between 0 and 1")

    @property
    def activity_score(self) -> float:
        positive = (
            0.25 * self.relevance
            + 0.25 * self.evidence_strength
            + 0.20 * self.robustness
            + 0.15 * self.pathway_support
        )
        penalties = (
            0.07 * self.uncertainty
            + 0.05 * self.fragility
            + 0.03 * self.dependency_penalty
        )
        return max(0.0, min(1.0, positive - penalties))


@dataclass(frozen=True)
class TerminalDecision:
    terminal_node_id: str
    terminal_score: float
    supporting_nodes: Sequence[str]
    unresolved: bool
    reason: str


def select_terminal_node(
    activities: Iterable[NodeActivity],
    *,
    minimum_score: float = 0.45,
    minimum_supporting_nodes: int = 2,
    tie_tolerance: float = 0.03,
) -> TerminalDecision:
    ranked: List[NodeActivity] = sorted(
        activities,
        key=lambda item: item.activity_score,
        reverse=True,
    )
    if not ranked:
        raise ValueError("No node activities were supplied")

    winner = ranked[0]
    supporters = [
        item.node_id
        for item in ranked[1:]
        if item.pathway_support >= 0.5 and item.evidence_strength >= 0.5
    ]

    near_tie = len(ranked) > 1 and (
        winner.activity_score - ranked[1].activity_score <= tie_tolerance
    )
    unresolved = (
        winner.activity_score < minimum_score
        or len(supporters) < minimum_supporting_nodes
        or near_tie
    )

    if winner.activity_score < minimum_score:
        reason = "No node reached the minimum terminal authority threshold."
    elif len(supporters) < minimum_supporting_nodes:
        reason = "Terminal candidate lacks sufficient independent pathway support."
    elif near_tie:
        reason = "Two or more nodes retain near-equal terminal authority."
    else:
        reason = "Highest activity survived threshold, support and tie checks."

    return TerminalDecision(
        terminal_node_id=winner.node_id,
        terminal_score=winner.activity_score,
        supporting_nodes=tuple(supporters),
        unresolved=unresolved,
        reason=reason,
    )
