"""PFRAMOS Training Scout candidate assessment.

The scout evaluates GitHub-hosted dataset candidates before any download or
schooling activity. Discovery never grants training approval.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Tuple


APPROVED_DATA_EXTENSIONS = (
    ".csv",
    ".json",
    ".jsonl",
    ".parquet",
    ".zip",
    ".tar.gz",
)

APPROVED_LICENCES = {
    "apache-2.0",
    "mit",
    "bsd-2-clause",
    "bsd-3-clause",
    "cc-by-4.0",
    "cc0-1.0",
    "odc-by-1.0",
    "odbl-1.0",
}


@dataclass(frozen=True)
class DatasetCandidate:
    candidate_id: str
    repository: str
    file_path: str
    source_commit_sha: str
    discovered_at: datetime
    licence_id: str | None
    source_authority: float
    relevance: float
    documentation_quality: float
    reproducibility: float
    independence: float
    maintenance_recency: float
    schema_accessibility: float
    expected_training_value: float
    estimated_download_cost: float
    privacy_risk: float
    poisoning_risk: float
    benchmark_contamination_risk: float
    contains_executable_content: bool = False
    provenance_complete: bool = True

    def __post_init__(self) -> None:
        for name, value in self.__dict__.items():
            if name in {
                "candidate_id",
                "repository",
                "file_path",
                "source_commit_sha",
                "discovered_at",
                "licence_id",
                "contains_executable_content",
                "provenance_complete",
            }:
                continue
            if not 0.0 <= value <= 1.0:
                raise ValueError(f"{name} must be between 0 and 1")

    @property
    def extension_supported(self) -> bool:
        path = self.file_path.lower()
        return any(path.endswith(ext) for ext in APPROVED_DATA_EXTENSIONS)

    @property
    def licence_approved(self) -> bool:
        return bool(self.licence_id and self.licence_id.lower() in APPROVED_LICENCES)

    @property
    def discovery_score(self) -> float:
        positive = (
            0.16 * self.source_authority
            + 0.18 * self.relevance
            + 0.10 * self.documentation_quality
            + 0.10 * self.reproducibility
            + 0.10 * self.independence
            + 0.08 * self.maintenance_recency
            + 0.08 * self.schema_accessibility
            + 0.14 * self.expected_training_value
        )
        penalties = (
            0.02 * self.estimated_download_cost
            + 0.02 * self.privacy_risk
            + 0.01 * self.poisoning_risk
            + 0.01 * self.benchmark_contamination_risk
        )
        return max(0.0, min(1.0, positive - penalties))

    @property
    def hard_blocks(self) -> Tuple[str, ...]:
        blocks = []
        if not self.extension_supported:
            blocks.append("unsupported dataset format")
        if not self.licence_approved:
            blocks.append("licence not approved or unclear")
        if not self.provenance_complete:
            blocks.append("incomplete provenance")
        if self.contains_executable_content:
            blocks.append("executable content detected")
        if self.privacy_risk >= 0.50:
            blocks.append("privacy risk too high")
        if self.poisoning_risk >= 0.70:
            blocks.append("poisoning risk too high")
        if self.benchmark_contamination_risk >= 0.70:
            blocks.append("benchmark contamination risk too high")
        return tuple(blocks)

    @property
    def disposition(self) -> str:
        if self.hard_blocks:
            return "reject_or_quarantine"
        if self.discovery_score >= 0.72:
            return "download_to_schooling_quarantine"
        if self.discovery_score >= 0.55:
            return "retain_for_manual_review"
        return "archive_low_value"


@dataclass(frozen=True)
class DatasetManifest:
    candidate_id: str
    repository: str
    file_path: str
    source_commit_sha: str
    licence_id: str
    discovered_at: datetime
    discovery_score: float
    disposition: str
    hard_blocks: Tuple[str, ...]


def build_manifest(candidate: DatasetCandidate) -> DatasetManifest:
    return DatasetManifest(
        candidate_id=candidate.candidate_id,
        repository=candidate.repository,
        file_path=candidate.file_path,
        source_commit_sha=candidate.source_commit_sha,
        licence_id=candidate.licence_id or "unknown",
        discovered_at=candidate.discovered_at,
        discovery_score=candidate.discovery_score,
        disposition=candidate.disposition,
        hard_blocks=candidate.hard_blocks,
    )
