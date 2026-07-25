from PFRAMOS.schooling.data_form_router import route_data_form
from PFRAMOS.training_scout.acm_resources import get_acm_resource


def test_acm_reproduced_results_have_highest_evidence_weight() -> None:
    reproduced = get_acm_resource("results_reproduced")
    reusable = get_acm_resource("artifact_reusable")
    assert reproduced.evidence_weight > reusable.evidence_weight


def test_research_papers_use_evidence_learning_not_direct_training() -> None:
    route = route_data_form("research_paper")
    assert route.default_training_mode == "retrieval_and_structured_evidence"


def test_time_series_requires_walk_forward_learning() -> None:
    route = route_data_form("time_series")
    assert route.default_training_mode == "time_ordered_walk_forward"
    assert "future leakage" in route.special_risks


def test_software_repositories_are_sandboxed() -> None:
    route = route_data_form("software_repository")
    assert route.default_training_mode == "static_analysis_and_sandbox_execution"
    assert "malicious code" in route.special_risks


def test_simulation_and_real_data_are_not_treated_as_equivalent() -> None:
    route = route_data_form("simulation_trace")
    assert "reality gap" in route.special_risks
