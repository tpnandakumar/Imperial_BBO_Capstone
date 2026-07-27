"""FICO optimisation and explainability Scout integration.

The Scout separates FICO Xpress examples, challenge datasets, published papers
and commercial solver licensing. Public examples may be reviewed and trialled
subject to their own terms. Challenge datasets retain dataset-specific use
conditions. FICO Community pages are treated as discovery pointers rather than
a reliable acquisition endpoint.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class FICOResourceChannel:
    channel_id: str
    name: str
    official_url: str
    resource_type: str
    default_state: str
    permitted_uses: Tuple[str, ...]
    required_checks: Tuple[str, ...]
    notes: str


CHANNELS = (
    FICOResourceChannel(
        channel_id="fico_xpress_examples",
        name="FICO Xpress Optimization Examples Repository",
        official_url="https://examples.xpress.fico.com/",
        resource_type="optimisation_examples_and_model_files",
        default_state="usable_pending_normal_checks",
        permitted_uses=(
            "lp_trial",
            "mip_trial",
            "qp_trial",
            "miqp_trial",
            "qcqp_trial",
            "heuristic_trial",
            "iis_analysis",
            "model_file_parsing",
            "solver_control_review",
            "reproducibility_review",
        ),
        required_checks=(
            "example_specific_terms",
            "solver_licence_or_trial_access",
            "version_pin",
            "data_file_terms",
            "benchmark_separation",
        ),
        notes="Use official examples and downloadable model files where terms permit. Commercial Xpress licensing remains separate from example access.",
    ),
    FICOResourceChannel(
        channel_id="fico_explainable_ml_challenge",
        name="FICO Explainable Machine Learning Challenge",
        official_url="https://community.fico.com/s/explainable-machine-learning-challenge",
        resource_type="challenge_dataset_and_research_benchmark",
        default_state="discovery_and_verification",
        permitted_uses=(
            "explainability_benchmark_review",
            "credit_risk_model_comparison",
            "global_and_local_explanation_validation",
            "fairness_and_calibration_trial",
            "published_solution_review",
        ),
        required_checks=(
            "challenge_dataset_terms",
            "source_provenance",
            "privacy",
            "fairness_review",
            "protected_test",
            "publication_citation",
        ),
        notes="The HELOC challenge is valuable for interpretable modelling, but dataset use must follow challenge-specific conditions.",
    ),
    FICOResourceChannel(
        channel_id="fico_community",
        name="FICO Community",
        official_url="https://community.fico.com/s/",
        resource_type="community_and_discovery_portal",
        default_state="discovery_only",
        permitted_uses=(
            "challenge_discovery",
            "example_discovery",
            "paper_discovery",
            "implementation_discussion_review",
        ),
        required_checks=(
            "follow_original_source",
            "resource_specific_terms",
            "version_pin",
        ),
        notes="The portal can be technically unreliable. Prefer original example repositories, papers and downloadable artefacts for acquisition.",
    ),
)


PRIORITY_TRIALS = (
    "small LP and MIP reproducibility trial",
    "heuristic versus exact optimisation comparison",
    "IIS and infeasibility-diagnosis trial",
    "explainable credit-risk benchmark review",
    "GPU-accelerated optimisation literature follow-up",
)


def active_channels() -> Tuple[FICOResourceChannel, ...]:
    return CHANNELS
