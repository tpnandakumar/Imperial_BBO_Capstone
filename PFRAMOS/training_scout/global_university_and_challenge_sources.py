"""Global university, professional society and optimisation challenge sources.

The Scout may discover papers, courses, repositories, benchmarks, challenge
archives and explicitly licensed datasets. Discovery does not grant permission
to train. Each artefact must pass licence, provenance, privacy, contamination
and protected-test checks before use.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class GlobalScoutSource:
    source_id: str
    organisation: str
    category: str
    official_url: str
    active_for_discovery: bool
    permitted_uses: Tuple[str, ...]
    required_gates: Tuple[str, ...]
    notes: str


SOURCES = (
    GlobalScoutSource(
        source_id="imperial_college_london",
        organisation="Imperial College London",
        category="university",
        official_url="https://www.imperial.ac.uk/",
        active_for_discovery=True,
        permitted_uses=("paper_discovery", "course_discovery", "repository_discovery", "benchmark_discovery"),
        required_gates=("source_provenance", "licence_if_artifact_used", "version_pin", "contamination"),
        notes="Priority source for optimisation, machine learning, engineering and computational research.",
    ),
    GlobalScoutSource(
        source_id="harvard_university",
        organisation="Harvard University",
        category="university",
        official_url="https://www.harvard.edu/",
        active_for_discovery=True,
        permitted_uses=("paper_discovery", "course_discovery", "repository_discovery", "dataset_discovery"),
        required_gates=("source_provenance", "dataset_or_repository_licence", "privacy", "contamination"),
        notes="Priority source for authoritative research and educational material.",
    ),
    GlobalScoutSource(
        source_id="university_of_cambridge",
        organisation="University of Cambridge",
        category="university",
        official_url="https://www.cam.ac.uk/",
        active_for_discovery=True,
        permitted_uses=("paper_discovery", "course_discovery", "repository_discovery", "dataset_discovery"),
        required_gates=("source_provenance", "dataset_or_repository_licence", "privacy", "contamination"),
        notes="Priority source for cognition, machine learning, mathematics and optimisation research.",
    ),
    GlobalScoutSource(
        source_id="university_of_oxford",
        organisation="University of Oxford",
        category="university",
        official_url="https://www.ox.ac.uk/",
        active_for_discovery=True,
        permitted_uses=("paper_discovery", "course_discovery", "repository_discovery", "dataset_discovery"),
        required_gates=("source_provenance", "dataset_or_repository_licence", "privacy", "contamination"),
        notes="Priority source for machine learning, cognition, statistics and optimisation research.",
    ),
    GlobalScoutSource(
        source_id="acm_digital_library",
        organisation="Association for Computing Machinery",
        category="professional_society",
        official_url="https://dl.acm.org/",
        active_for_discovery=True,
        permitted_uses=("paper_discovery", "artifact_badge_discovery", "reproducibility_review", "challenge_discovery"),
        required_gates=("publication_access_terms", "artifact_licence", "version_pin", "contamination"),
        notes="Use ACM papers and artefact records as evidence sources. Copyrighted paper text is not a training corpus by default.",
    ),
    GlobalScoutSource(
        source_id="kaggle",
        organisation="Kaggle",
        category="competition_platform",
        official_url="https://www.kaggle.com/",
        active_for_discovery=True,
        permitted_uses=("competition_discovery", "dataset_discovery", "benchmark_discovery", "notebook_pattern_review"),
        required_gates=("competition_rules", "dataset_licence", "account_or_api_access", "privacy", "contamination", "protected_test"),
        notes="Competition data and notebooks remain subject to each competition's rules and dataset licence.",
    ),
    GlobalScoutSource(
        source_id="drivendata",
        organisation="DrivenData",
        category="competition_platform",
        official_url="https://www.drivendata.org/",
        active_for_discovery=True,
        permitted_uses=("competition_discovery", "dataset_discovery", "benchmark_discovery"),
        required_gates=("competition_rules", "dataset_licence", "access_terms", "privacy", "protected_test"),
        notes="Useful for real-world machine learning and optimisation challenge discovery.",
    ),
    GlobalScoutSource(
        source_id="zindi",
        organisation="Zindi",
        category="competition_platform",
        official_url="https://zindi.africa/",
        active_for_discovery=True,
        permitted_uses=("competition_discovery", "dataset_discovery", "benchmark_discovery"),
        required_gates=("competition_rules", "dataset_licence", "access_terms", "privacy", "protected_test"),
        notes="Use only where challenge and data terms explicitly permit the intended research use.",
    ),
    GlobalScoutSource(
        source_id="aicrowd",
        organisation="AIcrowd",
        category="competition_platform",
        official_url="https://www.aicrowd.com/",
        active_for_discovery=True,
        permitted_uses=("competition_discovery", "benchmark_discovery", "dataset_discovery"),
        required_gates=("competition_rules", "dataset_licence", "access_terms", "protected_test"),
        notes="Useful for active and archived AI challenge discovery.",
    ),
    GlobalScoutSource(
        source_id="codalab_competitions",
        organisation="CodaLab Competitions",
        category="competition_platform",
        official_url="https://codalab.lisn.upsaclay.fr/",
        active_for_discovery=True,
        permitted_uses=("competition_discovery", "benchmark_discovery", "dataset_discovery"),
        required_gates=("competition_rules", "dataset_licence", "access_terms", "protected_test"),
        notes="Archived and current competitions must be screened individually.",
    ),
    GlobalScoutSource(
        source_id="bbob_coco",
        organisation="COCO Platform",
        category="optimisation_benchmark",
        official_url="https://numbbo.github.io/coco/",
        active_for_discovery=True,
        permitted_uses=("black_box_optimisation_benchmark", "historical_challenge_review", "reproducibility_testing"),
        required_gates=("benchmark_licence", "version_pin", "test_protocol_lock", "no_test_leakage"),
        notes="Priority source for black-box optimisation benchmark functions and evaluation methodology.",
    ),
    GlobalScoutSource(
        source_id="nevergrad",
        organisation="Meta AI",
        category="optimisation_repository",
        official_url="https://github.com/facebookresearch/nevergrad",
        active_for_discovery=True,
        permitted_uses=("optimiser_discovery", "benchmark_discovery", "reproducibility_review"),
        required_gates=("repository_licence", "version_pin", "benchmark_separation", "contamination"),
        notes="Candidate source for derivative-free optimisation algorithms and benchmarks.",
    ),
    GlobalScoutSource(
        source_id="openml",
        organisation="OpenML",
        category="open_dataset_and_benchmark_platform",
        official_url="https://www.openml.org/",
        active_for_discovery=True,
        permitted_uses=("dataset_discovery", "benchmark_discovery", "task_discovery", "reproducibility_testing"),
        required_gates=("dataset_specific_licence", "provenance", "privacy", "contamination", "protected_test"),
        notes="OpenML hosts datasets and benchmark tasks with dataset-specific conditions.",
    ),
    GlobalScoutSource(
        source_id="awesome_public_datasets",
        organisation="Awesome Data",
        category="dataset_discovery_index",
        official_url="https://github.com/awesomedata/awesome-public-datasets",
        active_for_discovery=True,
        permitted_uses=("dataset_discovery", "source_comparison", "domain_coverage_review", "alternative_source_search"),
        required_gates=("linked_dataset_licence", "linked_dataset_provenance", "privacy", "access_terms", "contamination", "protected_test"),
        notes="Use as a discovery catalogue only. Every linked dataset must be verified at its original source before acquisition or training.",
    ),
)


def active_sources() -> Tuple[GlobalScoutSource, ...]:
    return tuple(source for source in SOURCES if source.active_for_discovery)


def sources_by_category(category: str) -> Tuple[GlobalScoutSource, ...]:
    return tuple(source for source in SOURCES if source.category == category)
