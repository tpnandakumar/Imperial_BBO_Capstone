from PFRAMOS.architecture.pcece_dmacce import MemoryAllocation
from PFRAMOS.architecture.rar_guided_dmacce import (
    ReferenceAwareRetentionState,
    rar_guided_dmacce_decide,
)


def _allocation(**overrides):
    values = dict(
        allocation_id="m1",
        owner_task_id="task",
        size_units=100.0,
        priority=0.5,
        recomputation_cost=0.3,
        compression_ratio=0.2,
        persistent=False,
        active_references=frozenset(),
        queued_references=frozenset(),
        dependent_references=frozenset(),
        last_used_tick=0,
        location="active",
    )
    values.update(overrides)
    return MemoryAllocation(**values)


def _state(**overrides):
    values = dict(
        active_references=frozenset(),
        queued_references=frozenset(),
        dependent_references=frozenset(),
        anticipated_references=frozenset(),
        reference_strength=0.1,
        recent_activity=0.1,
        current_relevance=0.1,
        anticipated_relevance=0.1,
        recomputation_risk=0.1,
    )
    values.update(overrides)
    return ReferenceAwareRetentionState(**values)


def test_live_reference_prevents_release() -> None:
    decision = rar_guided_dmacce_decide(
        _allocation(),
        _state(active_references=frozenset({"job-a"})),
        current_tick=10,
        memory_pressure=1.0,
        energy_pressure=1.0,
    )
    assert decision.action == "retain_active"
    assert decision.released_units == 0.0


def test_anticipated_reference_retains_compressed_copy() -> None:
    decision = rar_guided_dmacce_decide(
        _allocation(),
        _state(
            anticipated_references=frozenset({"job-next"}),
            reference_strength=0.5,
            anticipated_relevance=0.9,
            recomputation_risk=0.8,
        ),
        current_tick=10,
        memory_pressure=0.8,
        energy_pressure=0.4,
    )
    assert decision.action == "retain_compressed"
    assert decision.retained_units > 0.0


def test_unreferenced_low_value_memory_can_be_released() -> None:
    decision = rar_guided_dmacce_decide(
        _allocation(),
        _state(),
        current_tick=10,
        memory_pressure=0.9,
        energy_pressure=0.9,
    )
    assert decision.action == "release"
    assert decision.retained_units == 0.0


def test_persistent_memory_is_not_released() -> None:
    decision = rar_guided_dmacce_decide(
        _allocation(persistent=True),
        _state(),
        current_tick=10,
        memory_pressure=0.9,
        energy_pressure=0.9,
    )
    assert decision.action == "compress_persistent"
    assert decision.retained_units > 0.0
