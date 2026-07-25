from PFRAMOS.architecture.dynamic_function_priority import (
    FunctionPriority,
    PriorityContext,
    calculate_target_priority,
    reprioritise,
)


def test_priority_levels_and_sublevels_are_bounded() -> None:
    assert FunctionPriority(1, 0).rank < FunctionPriority(15, 99).rank


def test_high_urgency_active_function_is_promoted() -> None:
    current = FunctionPriority(5, 20)
    change = reprioritise(
        current,
        PriorityContext(
            function_id="f1",
            criticality=0.9,
            urgency=0.95,
            dependency_pressure=0.8,
            expected_value=0.9,
            failure_risk=0.7,
            waiting_pressure=0.4,
            resource_pressure=0.2,
            active=True,
            queued=False,
            completed=False,
            blocked=False,
            protected=True,
        ),
    )
    assert change.direction == "promoted"
    assert change.current.level <= current.level + 2


def test_blocked_low_value_function_can_be_demoted() -> None:
    current = FunctionPriority(10, 50)
    change = reprioritise(
        current,
        PriorityContext(
            function_id="f2",
            criticality=0.2,
            urgency=0.1,
            dependency_pressure=0.1,
            expected_value=0.2,
            failure_risk=0.2,
            waiting_pressure=0.1,
            resource_pressure=0.9,
            active=False,
            queued=True,
            completed=False,
            blocked=True,
        ),
    )
    assert change.direction == "demoted"


def test_waiting_pressure_supports_starvation_prevention() -> None:
    low_wait = calculate_target_priority(
        PriorityContext(
            function_id="f3",
            criticality=0.4,
            urgency=0.4,
            dependency_pressure=0.4,
            expected_value=0.4,
            failure_risk=0.3,
            waiting_pressure=0.0,
            resource_pressure=0.4,
            active=False,
            queued=True,
            completed=False,
            blocked=False,
        )
    )
    high_wait = calculate_target_priority(
        PriorityContext(
            function_id="f3",
            criticality=0.4,
            urgency=0.4,
            dependency_pressure=0.4,
            expected_value=0.4,
            failure_risk=0.3,
            waiting_pressure=1.0,
            resource_pressure=0.4,
            active=False,
            queued=True,
            completed=False,
            blocked=False,
        )
    )
    assert high_wait.rank > low_wait.rank


def test_completion_immediately_demotes_to_lowest_priority() -> None:
    change = reprioritise(
        FunctionPriority(15, 99),
        PriorityContext(
            function_id="f4",
            criticality=1.0,
            urgency=1.0,
            dependency_pressure=1.0,
            expected_value=1.0,
            failure_risk=1.0,
            waiting_pressure=1.0,
            resource_pressure=0.0,
            active=False,
            queued=False,
            completed=True,
            blocked=False,
            protected=True,
        ),
    )
    assert change.current == FunctionPriority(1, 0)
    assert change.direction == "demoted"
