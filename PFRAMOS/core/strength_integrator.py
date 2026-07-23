"""Dependency-aware cross-node evidence integration for PFRAMOS."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, List, Sequence, Tuple

from .node_contract import EvidenceSignal


@dataclass(frozen=True)
class IntegratedStrength:
    signal_name: str
    raw_support: float
    dependency_adjusted_support: float
    conflict_penalty: float
    final_strength: float
    contributing_lineages: Tuple[Tuple[str, ...], ...]


def _base_strength(signal: EvidenceSignal) -> float:
    """Combine retained signal dimensions without hiding them in storage."""

    return (
        0.25 * signal.strength
        + 0.20 * signal.confidence
        + 0.20 * signal.stability
        + 0.20 * signal.identifiability
        + 0.15 * signal.independence
    )


def integrate_signals(
    signals: Sequence[EvidenceSignal],
    *,
    conflicts: Iterable[Tuple[str, str]] = (),
) -> List[IntegratedStrength]:
    """Integrate same-named signals while discounting shared evidence lineage.

    Signals with identical lineage are not treated as independent replications.
    Conflicts are supplied as pairs of signal names and reduce both groups.
    """

    grouped: Dict[str, List[EvidenceSignal]] = {}
    for signal in signals:
        grouped.setdefault(signal.name, []).append(signal)

    conflict_names = {name for pair in conflicts for name in pair}
    results: List[IntegratedStrength] = []

    for name, group in sorted(grouped.items()):
        raw_support = sum(_base_strength(signal) for signal in group)

        lineage_counts: Dict[Tuple[str, ...], int] = {}
        for signal in group:
            lineage = tuple(sorted(signal.lineage))
            lineage_counts[lineage] = lineage_counts.get(lineage, 0) + 1

        adjusted = 0.0
        for signal in group:
            lineage = tuple(sorted(signal.lineage))
            adjusted += _base_strength(signal) / lineage_counts[lineage]

        conflict_penalty = 0.15 * adjusted if name in conflict_names else 0.0
        final_strength = max(0.0, min(1.0, adjusted - conflict_penalty))

        results.append(
            IntegratedStrength(
                signal_name=name,
                raw_support=raw_support,
                dependency_adjusted_support=adjusted,
                conflict_penalty=conflict_penalty,
                final_strength=final_strength,
                contributing_lineages=tuple(sorted(lineage_counts)),
            )
        )

    return results
