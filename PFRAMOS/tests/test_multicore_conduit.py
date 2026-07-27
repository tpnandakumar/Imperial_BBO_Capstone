from PFRAMOS.core.multicore_conduit import (
    ConduitTask,
    MultiCoreConduitExecutor,
    merge_at_coherence_junction,
)


def _task(payload, cache):
    shared = cache.get_or_compute("shared", lambda: payload["base"] * 2)
    return {"value": shared + payload["offset"]}


def test_independent_conduits_execute_and_reuse_cache() -> None:
    executor = MultiCoreConduitExecutor(max_workers=2)
    tasks = [
        ConduitTask("a", _task, {"base": 3, "offset": 1}, coherence_index=0.8),
        ConduitTask("b", _task, {"base": 3, "offset": 2}, coherence_index=0.7),
    ]

    results = executor.execute(tasks)

    assert results["a"].output["value"] == 7
    assert results["b"].output["value"] == 8
    assert executor.cache.saving_count() >= 1


def test_dependency_ordering_is_respected() -> None:
    executor = MultiCoreConduitExecutor(max_workers=2)
    tasks = [
        ConduitTask("first", _task, {"base": 2, "offset": 1}, coherence_index=0.6),
        ConduitTask(
            "second",
            _task,
            {"base": 2, "offset": 2},
            dependencies=("first",),
            coherence_index=0.7,
        ),
    ]

    results = executor.execute(tasks)
    assert results["second"].source_conduits == ("first",)


def test_coherence_junction_merges_compatible_conduits() -> None:
    executor = MultiCoreConduitExecutor(max_workers=2)
    results = executor.execute(
        [
            ConduitTask("a", _task, {"base": 2, "offset": 1}, coherence_index=0.8),
            ConduitTask("b", _task, {"base": 2, "offset": 3}, coherence_index=0.6),
        ]
    )

    merged = merge_at_coherence_junction(
        "junction",
        [results["a"], results["b"]],
        merge_function=lambda outputs: {"mean": sum(item["value"] for item in outputs) / len(outputs)},
        cache=executor.cache,
    )

    assert merged.contributing_conduits == ("a", "b")
    assert merged.merged_output["mean"] == 6.0
    assert merged.merged_coherence_index == 0.7


def test_low_coherence_blocks_merge() -> None:
    executor = MultiCoreConduitExecutor(max_workers=1)
    results = executor.execute(
        [ConduitTask("a", _task, {"base": 1, "offset": 0}, coherence_index=0.1)]
    )

    try:
        merge_at_coherence_junction(
            "junction",
            [results["a"]],
            merge_function=lambda outputs: outputs[0],
            minimum_cross_coherence=0.4,
        )
    except ValueError as error:
        assert "below the merge threshold" in str(error)
    else:
        raise AssertionError("Expected low-coherence merge to be blocked")
