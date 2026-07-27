from PFRAMOS.architecture.purpose_priority_memory_distribution import (
    MemoryRequest,
    distribute_memory,
    reclaim_completed_memory,
)


def test_active_protected_function_outranks_queued_task() -> None:
    protected = MemoryRequest(
        request_id="r1",
        task_id="critical",
        purpose="protected-test inference",
        minimum_units=40,
        preferred_units=60,
        maximum_units=80,
        criticality=1.0,
        expected_value=0.9,
        deadline_pressure=0.9,
        recomputation_cost=0.8,
        active_reference=True,
        queued_only=False,
        protected_function=True,
    )
    queued = MemoryRequest(
        request_id="r2",
        task_id="queued",
        purpose="future dataset scan",
        minimum_units=30,
        preferred_units=70,
        maximum_units=90,
        criticality=0.4,
        expected_value=0.5,
        deadline_pressure=0.2,
        recomputation_cost=0.2,
        active_reference=False,
        queued_only=True,
    )
    plan = distribute_memory((queued, protected), total_capacity=100, reserve_fraction=0.1)
    grants = {grant.task_id: grant for grant in plan.grants}
    assert grants["critical"].granted_units >= protected.minimum_units
    assert grants["queued"].granted_units <= queued.preferred_units * 0.25


def test_request_without_purpose_is_invalid() -> None:
    try:
        MemoryRequest(
            request_id="r3",
            task_id="invalid",
            purpose=" ",
            minimum_units=1,
            preferred_units=1,
            maximum_units=1,
            criticality=0.1,
            expected_value=0.1,
            deadline_pressure=0.1,
            recomputation_cost=0.1,
            active_reference=False,
            queued_only=True,
        )
    except ValueError as exc:
        assert "purpose" in str(exc)
    else:
        raise AssertionError("missing purpose should fail")


def test_completed_task_memory_is_reclaimed() -> None:
    request = MemoryRequest(
        request_id="r4",
        task_id="done",
        purpose="semantic graph construction",
        minimum_units=20,
        preferred_units=30,
        maximum_units=40,
        criticality=0.7,
        expected_value=0.7,
        deadline_pressure=0.5,
        recomputation_cost=0.4,
        active_reference=True,
        queued_only=False,
    )
    plan = distribute_memory((request,), total_capacity=100)
    reclaimed = reclaim_completed_memory(plan.grants, ("done",))
    assert reclaimed[0].state == "reclaimed"
    assert reclaimed[0].granted_units == 0.0


def test_total_grants_do_not_exceed_usable_capacity() -> None:
    requests = tuple(
        MemoryRequest(
            request_id=f"r{i}",
            task_id=f"t{i}",
            purpose="parallel cognitive computation",
            minimum_units=20,
            preferred_units=50,
            maximum_units=60,
            criticality=0.5,
            expected_value=0.5,
            deadline_pressure=0.5,
            recomputation_cost=0.5,
            active_reference=True,
            queued_only=False,
        )
        for i in range(5)
    )
    plan = distribute_memory(requests, total_capacity=100, reserve_fraction=0.1)
    assert plan.granted_units <= 90.0
