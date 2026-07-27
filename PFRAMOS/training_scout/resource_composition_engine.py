"""Compose open resources into purpose-built PACC and PFRAMOS validation bundles.

The engine combines only resources whose individual licences, provenance and
access terms have been cleared. It preserves source boundaries and records the
role played by each component. It does not merge incompatible licences or
silently convert papers, code or indexed pages into training data.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class ResourceCandidate:
    resource_id: str
    organisation: str
    resource_type: str
    official_source: str
    intended_role: str
    licence_status: str
    provenance_status: str
    access_status: str
    privacy_status: str
    contamination_status: str
    version_pin: str
    cognitive_domains: Tuple[str, ...] = ()
    optimisation_roles: Tuple[str, ...] = ()

    @property
    def cleared(self) -> bool:
        approved = {"approved", "not_applicable"}
        return (
            self.licence_status in approved
            and self.provenance_status in approved
            and self.access_status in approved
            and self.privacy_status in approved
            and self.contamination_status in approved
            and bool(self.version_pin.strip())
        )


@dataclass(frozen=True)
class ResourceBundle:
    bundle_id: str
    purpose: str
    resources: Tuple[ResourceCandidate, ...]
    state: str
    blockers: Tuple[str, ...]
    publication_tracks: Tuple[str, ...]


def compose_bundle(
    bundle_id: str,
    purpose: str,
    resources: Tuple[ResourceCandidate, ...],
    publication_tracks: Tuple[str, ...],
) -> ResourceBundle:
    blockers = []
    if not purpose.strip():
        blockers.append("missing_purpose")
    if not resources:
        blockers.append("no_resources")

    for resource in resources:
        if not resource.cleared:
            blockers.append(f"resource_not_cleared:{resource.resource_id}")

    state = "ready_for_trial" if not blockers else "discovery_only"
    return ResourceBundle(
        bundle_id=bundle_id,
        purpose=purpose,
        resources=resources,
        state=state,
        blockers=tuple(sorted(set(blockers))),
        publication_tracks=publication_tracks,
    )


BUNDLE_BLUEPRINTS = {
    "PACC-CGN-001": {
        "purpose": "functional cognitive network validation",
        "roles": (
            "semantic_relation_data",
            "language_and_retrieval_tasks",
            "visuospatial_tasks",
            "executive_and_abstraction_tasks",
            "social_and_metacognitive_tasks",
        ),
        "publication_tracks": ("PACC-P1", "PACC-P3", "PACC-P4", "PACC-P8"),
    },
    "PFRAMOS-OPT-001": {
        "purpose": "black-box optimisation stress testing",
        "roles": (
            "COCO_BBOB_functions",
            "OpenML_benchmark_suites",
            "competition_archives",
            "historical_BBO_traces",
        ),
        "publication_tracks": ("PFRAMOS-P1", "PFRAMOS-P2", "PACC-P8"),
    },
    "PCECE-MEM-001": {
        "purpose": "cost energy and memory efficiency validation",
        "roles": (
            "NVIDIA_CUDA_samples",
            "NVIDIA_nvbench",
            "NVIDIA_nvCOMP",
            "memory_pressure_simulations",
            "RaR_DMACCE_ablation",
        ),
        "publication_tracks": ("PFRAMOS-P2", "PACC-P7", "PACC-P8"),
    },
    "PACC-XDOMAIN-001": {
        "purpose": "cross-domain acquired cognition and transfer testing",
        "roles": (
            "Google_Research_datasets",
            "OpenML_tasks",
            "university_reproducibility_artifacts",
            "Kaggle_or_similar_open_competitions",
        ),
        "publication_tracks": ("PACC-P7", "PACC-P8"),
    },
}
