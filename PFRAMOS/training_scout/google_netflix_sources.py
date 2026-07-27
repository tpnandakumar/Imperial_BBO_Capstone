"""Google, Netflix and NVIDIA source registry for the PACC Scout programme.

Google Research is an active dataset-discovery source. Netflix Open Source and
NVIDIA GitHub are active code, artifact and publication-discovery sources. A
resource is treated as a training dataset only when the specific data release
has an explicit compatible licence and accessible provenance record.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class ScoutSource:
    source_id: str
    organisation: str
    source_type: str
    official_url: str
    active_for_discovery: bool
    direct_training_default: bool
    permitted_uses: Tuple[str, ...]
    required_gates: Tuple[str, ...]
    notes: str


SOURCES = (
    ScoutSource(
        source_id="google_research_datasets",
        organisation="Google Research",
        source_type="dataset_catalogue",
        official_url="https://research.google/resources/datasets/",
        active_for_discovery=True,
        direct_training_default=False,
        permitted_uses=(
            "dataset_discovery",
            "benchmark_discovery",
            "cognitive_domain_mapping",
            "licence_screening",
            "shadow_validation_planning",
        ),
        required_gates=(
            "dataset_specific_licence",
            "access_terms",
            "provenance",
            "privacy",
            "ethics_if_applicable",
            "contamination",
            "protected_test",
        ),
        notes="Google Research publishes a broad official dataset catalogue. Each dataset remains subject to its own terms.",
    ),
    ScoutSource(
        source_id="google_dataset_search",
        organisation="Google",
        source_type="dataset_search_engine",
        official_url="https://datasetsearch.research.google.com/",
        active_for_discovery=True,
        direct_training_default=False,
        permitted_uses=(
            "dataset_discovery",
            "source_comparison",
            "provenance_follow_up",
        ),
        required_gates=(
            "host_dataset_licence",
            "host_access_terms",
            "provenance",
            "privacy",
            "contamination",
        ),
        notes="Dataset Search indexes third-party datasets. Google indexing does not grant training permission.",
    ),
    ScoutSource(
        source_id="netflix_open_source",
        organisation="Netflix",
        source_type="code_and_artifact_registry",
        official_url="https://github.com/Netflix",
        active_for_discovery=True,
        direct_training_default=False,
        permitted_uses=(
            "repository_discovery",
            "reproducibility_artifact_review",
            "systems_efficiency_learning",
            "workflow_pattern_review",
            "explicitly_licensed_dataset_discovery",
        ),
        required_gates=(
            "repository_licence",
            "dataset_specific_licence_if_data_present",
            "version_pin",
            "provenance",
            "contamination",
        ),
        notes="Public Netflix code does not imply access to Netflix production or user data.",
    ),
    ScoutSource(
        source_id="nvidia_github",
        organisation="NVIDIA",
        source_type="code_artifact_and_benchmark_registry",
        official_url="https://github.com/NVIDIA",
        active_for_discovery=True,
        direct_training_default=False,
        permitted_uses=(
            "gpu_kernel_discovery",
            "cuda_optimisation_review",
            "parallel_scan_review",
            "memory_efficiency_learning",
            "inference_optimisation_review",
            "reproducibility_artifact_review",
            "explicitly_licensed_dataset_discovery",
        ),
        required_gates=(
            "repository_licence",
            "dataset_specific_licence_if_data_present",
            "version_pin",
            "hardware_compatibility",
            "provenance",
            "contamination",
            "protected_test",
        ),
        notes="NVIDIA repositories may provide code, kernels, models, benchmarks and examples. Each repository and dataset must be checked separately before use.",
    ),
    ScoutSource(
        source_id="nvidia_research",
        organisation="NVIDIA Research",
        source_type="research_and_artifact_source",
        official_url="https://research.nvidia.com/",
        active_for_discovery=True,
        direct_training_default=False,
        permitted_uses=(
            "paper_discovery",
            "architecture_review",
            "benchmark_discovery",
            "artifact_discovery",
            "efficiency_method_review",
        ),
        required_gates=(
            "paper_or_artifact_provenance",
            "repository_licence_if_code_used",
            "dataset_specific_licence_if_data_used",
            "version_pin",
            "contamination",
        ),
        notes="Research publications guide candidate discovery. Papers alone do not grant permission to use associated code, models or data.",
    ),
)


def active_sources() -> Tuple[ScoutSource, ...]:
    return tuple(source for source in SOURCES if source.active_for_discovery)


def source_by_id(source_id: str) -> ScoutSource:
    for source in SOURCES:
        if source.source_id == source_id:
            return source
    raise ValueError(f"unknown Scout source: {source_id}")
