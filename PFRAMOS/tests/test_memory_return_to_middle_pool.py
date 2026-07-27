from PFRAMOS.architecture.memory_return_to_middle_pool import (
    ReclaimableMemoryState,
    decide_middle_pool_return,
)


def _state(**overrides):
    values = dict(
        allocation_id="m1",
        allocated_units=64.0,
        active_reference_count=0,
        queued_reference_count=0,
        dependent_reference_count=0,
        anticipated_reference_count=0,
        anticipated_reference_justified=False,
        checkpoint_required=False,
        checkpoint_complete=False,
        computation_complete=True,
    )
    values.update(overrides)
    return ReclaimableMemoryState(**values)


def test_unused_memory_returns_to_middle_pool() -> None:
    decision = decide_middle_pool_return(_state())
    assert decision.action == "return_to_middle_pool"
    assert decision.returned_units == 64.0
    assert decision.target_pool == "dynamic_middle_pool"


def test_live_reference_prevents_return() -> None:
    decision = decide_middle_pool_return(_state(active_reference_count=1))
    assert decision.action == "retain_for_live_reference"
    assert decision.returned_units == 0.0


def test_checkpoint_must_complete_before_return() -> None:
    decision = decide_middle_pool_return(
        _state(checkpoint_required=True, checkpoint_complete=False)
    )
    assert decision.action == "checkpoint_before_return"


def test_persistent_information_can_return_after_checkpoint() -> None:
    decision = decide_middle_pool_return(
        _state(checkpoint_required=True, checkpoint_complete=True)
    )
    assert decision.action == "return_to_middle_pool"
    assert decision.remaining_allocated_units == 0.0


def test_unjustified_anticipated_reference_does_not_block_return() -> None:
    decision = decide_middle_pool_return(
        _state(
            anticipated_reference_count=1,
            anticipated_reference_justified=False,
        )
    )
    assert decision.action == "return_to_middle_pool"
