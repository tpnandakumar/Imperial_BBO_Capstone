"""Route different data forms to appropriate PFRAMOS learning methods."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class DataFormRoute:
    data_form: str
    primary_learning: str
    secondary_learning: Tuple[str, ...]
    suitable_lanes: Tuple[str, ...]
    default_training_mode: str
    protected_test_required: bool
    special_risks: Tuple[str, ...]


DATA_FORM_ROUTES = {
    "research_paper": DataFormRoute(
        data_form="research_paper",
        primary_learning="concept and method extraction",
        secondary_learning=("citation graphing", "hypothesis generation", "comparative reasoning"),
        suitable_lanes=("reasoning", "emergence", "optimisation", "efficiency"),
        default_training_mode="retrieval_and_structured_evidence",
        protected_test_required=True,
        special_risks=("citation loss", "method-result conflation", "publication bias"),
    ),
    "labelled_tabular": DataFormRoute(
        data_form="labelled_tabular",
        primary_learning="supervised predictive learning",
        secondary_learning=("feature analysis", "calibration", "fairness testing"),
        suitable_lanes=("optimisation", "bias", "reasoning"),
        default_training_mode="supervised_training",
        protected_test_required=True,
        special_risks=("target leakage", "class imbalance", "selection bias"),
    ),
    "unlabelled_text": DataFormRoute(
        data_form="unlabelled_text",
        primary_learning="representation and language-pattern learning",
        secondary_learning=("retrieval indexing", "topic discovery", "style analysis"),
        suitable_lanes=("reasoning", "bias", "emergence"),
        default_training_mode="retrieval_first_then_selective_adaptation",
        protected_test_required=True,
        special_risks=("copyright", "memorisation", "social bias", "contamination"),
    ),
    "time_series": DataFormRoute(
        data_form="time_series",
        primary_learning="temporal and trajectory learning",
        secondary_learning=("drift detection", "change-point analysis", "forecasting"),
        suitable_lanes=("optimisation", "efficiency", "emergence"),
        default_training_mode="time_ordered_walk_forward",
        protected_test_required=True,
        special_risks=("future leakage", "non-stationarity", "seasonality confusion"),
    ),
    "optimisation_trace": DataFormRoute(
        data_form="optimisation_trace",
        primary_learning="search-policy and response-surface learning",
        secondary_learning=("delta analysis", "route discovery", "cost-aware allocation"),
        suitable_lanes=("optimisation", "efficiency", "emergence"),
        default_training_mode="sequential_policy_learning",
        protected_test_required=True,
        special_risks=("adaptive sampling bias", "future-output leakage", "local-optimum overfitting"),
    ),
    "software_repository": DataFormRoute(
        data_form="software_repository",
        primary_learning="structural and executable workflow learning",
        secondary_learning=("dependency analysis", "test-pattern learning", "modular repurposing"),
        suitable_lanes=("efficiency", "reasoning", "emergence"),
        default_training_mode="static_analysis_and_sandbox_execution",
        protected_test_required=True,
        special_risks=("malicious code", "supply-chain risk", "licence incompatibility"),
    ),
    "reproducibility_artifact": DataFormRoute(
        data_form="reproducibility_artifact",
        primary_learning="execution and independent result reproduction",
        secondary_learning=("workflow validation", "resource profiling", "repurposing assessment"),
        suitable_lanes=("reasoning", "efficiency", "optimisation", "emergence"),
        default_training_mode="sandbox_reproduction",
        protected_test_required=True,
        special_risks=("environment mismatch", "hidden dependencies", "dataset substitution"),
    ),
    "image_audio_video": DataFormRoute(
        data_form="image_audio_video",
        primary_learning="multimodal representation learning",
        secondary_learning=("cross-modal alignment", "classification", "generation"),
        suitable_lanes=("reasoning", "bias", "emergence"),
        default_training_mode="modality_specific_or_multimodal_adapter",
        protected_test_required=True,
        special_risks=("identity and privacy", "annotation bias", "distribution shift"),
    ),
    "simulation_trace": DataFormRoute(
        data_form="simulation_trace",
        primary_learning="dynamics and counterfactual learning",
        secondary_learning=("policy testing", "rare-event generation", "robustness analysis"),
        suitable_lanes=("optimisation", "efficiency", "emergence", "reasoning"),
        default_training_mode="simulation_conditioned_learning",
        protected_test_required=True,
        special_risks=("simulator bias", "reality gap", "parameter misspecification"),
    ),
}


def route_data_form(data_form: str) -> DataFormRoute:
    try:
        return DATA_FORM_ROUTES[data_form]
    except KeyError as exc:
        raise ValueError(f"unsupported data form: {data_form}") from exc
