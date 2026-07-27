"""Governed cross-modal and emotional memory interfaces for PGC."""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from typing import Iterable, Tuple


@dataclass(frozen=True)
class MemoryWriteProposal:
    source: str
    modality_ids: Tuple[str, ...]
    purpose: str
    factual_summary: str
    emotional_significance: float
    factual_support: float
    phcs_coherence: float
    pimf_persistence: float
    sensitive: bool
    expiry_epoch: int | None


@dataclass(frozen=True)
class MemoryRecord:
    record_id: str
    source: str
    modality_ids: Tuple[str, ...]
    purpose: str
    factual_summary_hash: str
    emotional_significance: float
    factual_support: float
    phcs_coherence: float
    pimf_persistence: float
    sensitive: bool
    expiry_epoch: int | None


@dataclass(frozen=True)
class MemoryWriteDecision:
    accepted: bool
    record: MemoryRecord | None
    reasons: Tuple[str, ...]


def _bounded(value: float, name: str) -> float:
    if not 0.0 <= value <= 1.0:
        raise ValueError(f"{name} must be within [0, 1]")
    return value


def evaluate_memory_write(
    proposal: MemoryWriteProposal,
    *,
    permit_sensitive: bool = False,
    minimum_factual_support: float = 0.60,
    minimum_coherence: float = 0.55,
    minimum_persistence: float = 0.50,
) -> MemoryWriteDecision:
    emotional = _bounded(proposal.emotional_significance, "emotional_significance")
    factual = _bounded(proposal.factual_support, "factual_support")
    coherence = _bounded(proposal.phcs_coherence, "phcs_coherence")
    persistence = _bounded(proposal.pimf_persistence, "pimf_persistence")

    reasons: list[str] = []
    if not proposal.source.strip():
        reasons.append("missing_source")
    if not proposal.purpose.strip():
        reasons.append("missing_purpose")
    if not proposal.factual_summary.strip():
        reasons.append("missing_factual_summary")
    if not proposal.modality_ids:
        reasons.append("missing_modality")
    if factual < minimum_factual_support:
        reasons.append("factual_support_below_threshold")
    if coherence < minimum_coherence:
        reasons.append("coherence_below_threshold")
    if persistence < minimum_persistence:
        reasons.append("persistence_below_threshold")
    if proposal.sensitive and not permit_sensitive:
        reasons.append("sensitive_memory_not_permitted")

    if reasons:
        return MemoryWriteDecision(False, None, tuple(reasons))

    digest = sha256(
        "|".join(
            (
                proposal.source,
                ",".join(sorted(proposal.modality_ids)),
                proposal.purpose,
                proposal.factual_summary,
            )
        ).encode("utf-8")
    ).hexdigest()
    record = MemoryRecord(
        record_id=digest[:20],
        source=proposal.source,
        modality_ids=tuple(sorted(set(proposal.modality_ids))),
        purpose=proposal.purpose,
        factual_summary_hash=sha256(proposal.factual_summary.encode("utf-8")).hexdigest(),
        emotional_significance=emotional,
        factual_support=factual,
        phcs_coherence=coherence,
        pimf_persistence=persistence,
        sensitive=proposal.sensitive,
        expiry_epoch=proposal.expiry_epoch,
    )
    return MemoryWriteDecision(True, record, ())


class CrossModalEmotionalMemory:
    def __init__(self) -> None:
        self._records: dict[str, MemoryRecord] = {}

    def write(self, decision: MemoryWriteDecision) -> None:
        if not decision.accepted or decision.record is None:
            raise ValueError("only accepted memory decisions may be written")
        self._records[decision.record.record_id] = decision.record

    def retrieve(
        self,
        *,
        modality_id: str | None = None,
        minimum_coherence: float = 0.0,
    ) -> Tuple[MemoryRecord, ...]:
        _bounded(minimum_coherence, "minimum_coherence")
        records: Iterable[MemoryRecord] = self._records.values()
        if modality_id is not None:
            records = (record for record in records if modality_id in record.modality_ids)
        return tuple(
            sorted(
                (record for record in records if record.phcs_coherence >= minimum_coherence),
                key=lambda record: (record.pimf_persistence, record.phcs_coherence),
                reverse=True,
            )
        )

    def delete(self, record_id: str) -> bool:
        return self._records.pop(record_id, None) is not None

    def clear(self) -> None:
        self._records.clear()
