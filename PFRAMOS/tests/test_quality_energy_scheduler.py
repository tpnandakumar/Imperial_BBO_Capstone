from PFRAMOS.core.quality_energy_scheduler import (
    ExecutionOption,
    marginal_quality_return,
    select_quality_first,
    should_continue_computation,
)


def test_materially_better_quality_is_never_sacrificed() -> None:
    options = [
        ExecutionOption("best", 0.95, 0.8, 0.8, 0.2, 10.0, 8.0),
        ExecutionOption("cheap", 0.80, 0.9, 0.9, 0.1, 1.0, 1.0),
    ]

    decision = select_quality_first(options, quality_tolerance=0.02)
    assert decision.selected_option_id == "best"


def test_lowest_resource_option_wins_inside_quality_basin() -> None:
    options = [
        ExecutionOption("heavy", 0.95, 0.8, 0.8, 0.2, 10.0, 8.0),
        ExecutionOption("efficient", 0.94, 0.8, 0.8, 0.2, 3.0, 2.0),
    ]

    decision = select_quality_first(options, quality_tolerance=0.02)
    assert decision.selected_option_id == "efficient"
    assert decision.resource_saving > 0.0


def test_low_coherence_option_is_rejected() -> None:
    options = [
        ExecutionOption("coherent", 0.94, 0.8, 0.8, 0.2, 5.0, 4.0),
        ExecutionOption("incoherent", 0.95, 0.1, 0.8, 0.2, 1.0, 1.0),
    ]

    decision = select_quality_first(options, quality_tolerance=0.02)
    assert decision.selected_option_id == "coherent"


def test_marginal_quality_return_controls_stopping() -> None:
    value = marginal_quality_return(0.80, 0.82, 2.0, 1.0)
    assert value > 0.0
    assert should_continue_computation(
        expected_quality_gain=0.02,
        additional_compute=2.0,
        additional_energy=1.0,
        minimum_marginal_return=0.005,
    )
    assert not should_continue_computation(
        expected_quality_gain=0.001,
        additional_compute=2.0,
        additional_energy=1.0,
        minimum_marginal_return=0.005,
    )
