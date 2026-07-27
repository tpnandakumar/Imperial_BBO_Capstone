"""ACM Digital Library and artifact resources for PFRAMOS schooling.

ACM papers, datasets, software, models and reproducibility artifacts are
research evidence. Access does not imply unrestricted training rights.
Dataset-level licence and usage checks remain mandatory.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class ACMResourceClass:
    resource_id: str
    display_name: str
    learning_forms: Tuple[str, ...]
    evidence_weight: float
    direct_training_default: bool
    required_checks: Tuple[str, ...]

    def __post_init__(self) -> None:
        if not 0.0 <= self.evidence_weight <= 1.0:
            raise ValueError("evidence_weight must be between 0 and 1")
        if not self.learning_forms:
            raise ValueError("learning_forms cannot be empty")


ACM_RESOURCE_CLASSES = {
    "paper": ACMResourceClass(
        resource_id="paper",
        display_name="ACM research paper",
        learning_forms=("concept extraction", "method comparison", "citation graph", "hypothesis generation"),
        evidence_weight=0.85,
        direct_training_default=False,
        required_checks=("access rights", "citation preservation", "method and result separation"),
    ),
    "artifact_available": ACMResourceClass(
        resource_id="artifact_available",
        display_name="ACM artifact available",
        learning_forms=("artifact inspection", "schema learning", "reproducibility review"),
        evidence_weight=0.80,
        direct_training_default=False,
        required_checks=("artifact licence", "persistent identifier", "integrity hash"),
    ),
    "artifact_functional": ACMResourceClass(
        resource_id="artifact_functional",
        display_name="ACM artifact evaluated functional",
        learning_forms=("execution learning", "workflow reconstruction", "result reproduction"),
        evidence_weight=0.90,
        direct_training_default=False,
        required_checks=("blank-environment execution", "dependency review", "resource logging"),
    ),
    "artifact_reusable": ACMResourceClass(
        resource_id="artifact_reusable",
        display_name="ACM artifact evaluated reusable",
        learning_forms=("repurposing", "modular extraction", "Pisharamisation candidate review"),
        evidence_weight=0.95,
        direct_training_default=False,
        required_checks=("reuse licence", "modularity review", "lineage preservation"),
    ),
    "results_reproduced": ACMResourceClass(
        resource_id="results_reproduced",
        display_name="ACM results reproduced",
        learning_forms=("high-confidence validation", "benchmark calibration", "independent evidence weighting"),
        evidence_weight=1.00,
        direct_training_default=False,
        required_checks=("reproduction report", "dataset identity", "environment equivalence"),
    ),
}


def get_acm_resource(resource_id: str) -> ACMResourceClass:
    try:
        return ACM_RESOURCE_CLASSES[resource_id]
    except KeyError as exc:
        raise ValueError(f"unknown ACM resource class: {resource_id}") from exc
