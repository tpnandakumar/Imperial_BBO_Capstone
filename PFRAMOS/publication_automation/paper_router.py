"""Automatic evidence routing for the PFRAMOS paper series.

The router classifies validated training results, assigns one primary paper,
records permissible secondary papers and blocks publication when evidence is
incomplete. It never fabricates manuscript results or auto-submits papers.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Tuple


PAPER_TRACKS = {
    "PFRAMOS-P1": "core_optimisation_architecture",
    "PFRAMOS-P2": "p_c4_cost_conscious_computation",
    "PFRAMOS-P3": "concurrent_multi_source_schooling",
    "PFRAMOS-P4": "bias_vector_modulation",
    "PFRAMOS-P5": "emergent_behaviour_and_laminar_conduits",
    "PFRAMOS-P6": "technology_mouldability_and_pisharamisation",
    "PFRAMOS-P7": "data_form_specific_learning",
    "PFRAMOS-P8": "publishing_and_manuscript_intelligence",
}


@dataclass(frozen=True)
class EvidenceRecord:
    result_id: str
    training_lane: str
    data_form: str
    source_ids: Tuple[str, ...]
    metrics: Mapping[str, float]
    has_dataset_manifest: bool
    has_training_log_hash: bool
    has_protected_test: bool
    reproducible: bool
    regressions_present: bool
    publication_eligible: bool
    tags: Tuple[str, ...] = ()


@dataclass(frozen=True)
class PaperAssignment:
    result_id: str
    primary_paper: str
    secondary_papers: Tuple[str, ...]
    state: str
    blocking_reasons: Tuple[str, ...]


def _primary_from_lane(record: EvidenceRecord) -> str:
    lane_map = {
        "optimisation": "PFRAMOS-P1",
        "efficiency": "PFRAMOS-P2",
        "concurrent_schooling": "PFRAMOS-P3",
        "bias": "PFRAMOS-P4",
        "emergence": "PFRAMOS-P5",
        "mouldability": "PFRAMOS-P6",
        "data_form": "PFRAMOS-P7",
        "publishing": "PFRAMOS-P8",
        "reasoning": "PFRAMOS-P3",
    }
    return lane_map.get(record.training_lane, "PFRAMOS-P7")


def _secondary_tracks(record: EvidenceRecord, primary: str) -> Tuple[str, ...]:
    candidates = set()
    if "compute" in record.metrics or "energy_proxy" in record.metrics:
        candidates.add("PFRAMOS-P2")
    if record.data_form in {"research_paper", "software_repository", "reproducibility_artifact"}:
        candidates.add("PFRAMOS-P7")
    if any(tag in record.tags for tag in ("bias", "fairness", "representation")):
        candidates.add("PFRAMOS-P4")
    if any(tag in record.tags for tag in ("emergence", "route", "laminar", "synergy")):
        candidates.add("PFRAMOS-P5")
    if any(tag in record.tags for tag in ("mouldability", "pisharamised", "technology_candidate")):
        candidates.add("PFRAMOS-P6")
    if "honeycomb_publications" in record.source_ids:
        candidates.add("PFRAMOS-P8")
    candidates.discard(primary)
    return tuple(sorted(candidates))


def route_evidence(record: EvidenceRecord) -> PaperAssignment:
    blockers = []
    if not record.has_dataset_manifest:
        blockers.append("missing_dataset_manifest")
    if not record.has_training_log_hash:
        blockers.append("missing_training_log_hash")
    if not record.has_protected_test:
        blockers.append("missing_protected_test")
    if not record.reproducible:
        blockers.append("not_reproducible")
    if record.regressions_present:
        blockers.append("unresolved_regressions")
    if not record.publication_eligible:
        blockers.append("result_not_publication_eligible")

    primary = _primary_from_lane(record)
    secondary = _secondary_tracks(record, primary)
    state = "evidence_ready" if not blockers else "evidence_incomplete"
    return PaperAssignment(
        result_id=record.result_id,
        primary_paper=primary,
        secondary_papers=secondary,
        state=state,
        blocking_reasons=tuple(blockers),
    )


def manuscript_state(assignments: Tuple[PaperAssignment, ...]) -> str:
    if not assignments:
        return "no_evidence"
    if any(item.state != "evidence_ready" for item in assignments):
        return "candidate"
    primary_tracks = {item.primary_paper for item in assignments}
    if len(primary_tracks) != 1:
        return "manual_scope_review"
    return "under_internal_review"
