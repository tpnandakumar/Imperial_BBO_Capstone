"""Parallel execution for PFRAMOS coherence conduits.

Independent conduits may execute concurrently. Shared computations are cached
and reused. Conduits synchronise only at declared coherence junctions, after
which merged results remain fully traceable to their source pathways.
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from threading import Lock
from typing import Any, Callable, Dict, Iterable, Mapping, MutableMapping, Sequence, Tuple


@dataclass(frozen=True)
class ConduitTask:
    conduit_id: str
    function: Callable[[Mapping[str, Any], "SharedComputationCache"], Mapping[str, Any]]
    payload: Mapping[str, Any]
    dependencies: Tuple[str, ...] = ()
    coherence_index: float = 0.0

    def __post_init__(self) -> None:
        if not -1.0 <= self.coherence_index <= 1.0:
            raise ValueError("coherence_index must be between -1 and +1")


@dataclass(frozen=True)
class ConduitResult:
    conduit_id: str
    output: Mapping[str, Any]
    coherence_index: float
    reused_computations: Tuple[str, ...]
    source_conduits: Tuple[str, ...]
    status: str


@dataclass(frozen=True)
class CoherenceJunctionResult:
    junction_id: str
    merged_output: Mapping[str, Any]
    contributing_conduits: Tuple[str, ...]
    merged_coherence_index: float
    computation_saving_count: int
    unresolved_conflicts: Tuple[str, ...]


class SharedComputationCache:
    """Thread-safe cache for reusable deterministic calculations."""

    def __init__(self) -> None:
        self._values: MutableMapping[str, Any] = {}
        self._hits: Dict[str, int] = {}
        self._lock = Lock()

    def get_or_compute(self, key: str, function: Callable[[], Any]) -> Any:
        with self._lock:
            if key in self._values:
                self._hits[key] = self._hits.get(key, 0) + 1
                return self._values[key]

        value = function()

        with self._lock:
            if key not in self._values:
                self._values[key] = value
                self._hits.setdefault(key, 0)
            else:
                self._hits[key] = self._hits.get(key, 0) + 1
                value = self._values[key]
        return value

    def reused_keys(self) -> Tuple[str, ...]:
        with self._lock:
            return tuple(sorted(key for key, hits in self._hits.items() if hits > 0))

    def saving_count(self) -> int:
        with self._lock:
            return sum(self._hits.values())


class MultiCoreConduitExecutor:
    """Execute dependency-ready conduits concurrently and deterministically."""

    def __init__(self, max_workers: int | None = None) -> None:
        self.max_workers = max_workers
        self.cache = SharedComputationCache()

    def execute(self, tasks: Sequence[ConduitTask]) -> Dict[str, ConduitResult]:
        task_map = {task.conduit_id: task for task in tasks}
        if len(task_map) != len(tasks):
            raise ValueError("Conduit IDs must be unique")

        results: Dict[str, ConduitResult] = {}
        pending = set(task_map)

        while pending:
            ready = [
                task_map[conduit_id]
                for conduit_id in sorted(pending)
                if all(dependency in results for dependency in task_map[conduit_id].dependencies)
            ]
            if not ready:
                unresolved = {item: task_map[item].dependencies for item in pending}
                raise RuntimeError(f"Cyclic or unresolved conduit dependencies: {unresolved}")

            with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
                future_map = {
                    executor.submit(task.function, task.payload, self.cache): task
                    for task in ready
                }
                completed: Dict[str, Mapping[str, Any]] = {}
                for future in as_completed(future_map):
                    task = future_map[future]
                    completed[task.conduit_id] = future.result()

            reused = self.cache.reused_keys()
            for task in ready:
                results[task.conduit_id] = ConduitResult(
                    conduit_id=task.conduit_id,
                    output=completed[task.conduit_id],
                    coherence_index=task.coherence_index,
                    reused_computations=reused,
                    source_conduits=task.dependencies,
                    status="completed",
                )
                pending.remove(task.conduit_id)

        return results


def merge_at_coherence_junction(
    junction_id: str,
    results: Sequence[ConduitResult],
    *,
    merge_function: Callable[[Sequence[Mapping[str, Any]]], Mapping[str, Any]],
    minimum_cross_coherence: float = 0.40,
    conflicts: Iterable[str] = (),
    cache: SharedComputationCache | None = None,
) -> CoherenceJunctionResult:
    if not results:
        raise ValueError("At least one conduit result is required")

    conflict_list = tuple(sorted(set(conflicts)))
    mean_coherence = sum(item.coherence_index for item in results) / len(results)
    if mean_coherence < minimum_cross_coherence:
        raise ValueError("Cross-conduit coherence is below the merge threshold")
    if conflict_list:
        raise ValueError("Unresolved conflict prevents conduit merging")

    merged = merge_function([item.output for item in results])
    saving_count = cache.saving_count() if cache is not None else 0

    return CoherenceJunctionResult(
        junction_id=junction_id,
        merged_output=merged,
        contributing_conduits=tuple(sorted(item.conduit_id for item in results)),
        merged_coherence_index=max(-1.0, min(1.0, mean_coherence)),
        computation_saving_count=saving_count,
        unresolved_conflicts=conflict_list,
    )
