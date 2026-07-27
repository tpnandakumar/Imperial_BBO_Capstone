"""Run the first controlled PFRAMOS experiment suite.

The suite separates architecture experiments from BBO-data experiments.
Architecture experiments always run. Historical experiments run only after the
Harmony Repair Gate creates a validated canonical dataset.
"""

from __future__ import annotations

import csv
import json
import math
import time
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Dict, List, Mapping, Sequence

from PFRAMOS.core.coherence_engine import (
    CoherenceEvidence,
    build_pathway_envelope,
    maximum_result_path,
    signed_coherence,
    stimulate_activity,
)
from PFRAMOS.core.multicore_conduit import (
    ConduitTask,
    MultiCoreConduitExecutor,
    merge_at_coherence_junction,
)
from PFRAMOS.core.quality_energy_scheduler import ExecutionOption, select_quality_first
from PFRAMOS.core.terminality_engine import NodeActivity, select_terminal_node


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "outputs" / "public" / "experiments"
CANONICAL_FILE = ROOT / "data" / "canonical_bbo_observations.csv"


@dataclass(frozen=True)
class ExperimentResult:
    experiment_id: str
    status: str
    metric: str
    value: float | int | str
    passed: bool
    notes: str


def experiment_01_coherence_sign() -> ExperimentResult:
    score = signed_coherence(
        [
            CoherenceEvidence("a", 0.9, 0.1, 0.9, 0.9, ("a",)),
            CoherenceEvidence("b", 0.8, 0.2, 0.8, 0.8, ("b",)),
        ]
    )
    return ExperimentResult(
        "E01",
        "completed",
        "coherence_index",
        score.index,
        score.index > 0.5,
        "Positive support should produce strong positive coherence.",
    )


def experiment_02_conflict_detection() -> ExperimentResult:
    score = signed_coherence(
        [
            CoherenceEvidence("a", 0.1, 0.9, 0.9, 0.9, ("a",)),
            CoherenceEvidence("b", 0.2, 0.8, 0.8, 0.8, ("b",)),
        ]
    )
    return ExperimentResult(
        "E02",
        "completed",
        "coherence_index",
        score.index,
        score.index < -0.5,
        "Strong opposition should produce strong negative coherence.",
    )


def experiment_03_augmentation_bound() -> ExperimentResult:
    value = stimulate_activity(0.6, [0.95, 0.90, 0.85])
    return ExperimentResult(
        "E03",
        "completed",
        "augmented_activity",
        value,
        0.6 < value <= 1.0,
        "High internodal coherence should augment activity without runaway growth.",
    )


def experiment_04_terminal_stability() -> ExperimentResult:
    activities = [
        NodeActivity("trajectory", 0.8, 0.8, 0.8, 0.8, 0.1, 0.1, 0.1),
        NodeActivity("boundary", 0.9, 0.9, 0.9, 0.9, 0.1, 0.1, 0.1),
        NodeActivity("uncertainty", 0.7, 0.7, 0.8, 0.8, 0.2, 0.1, 0.1),
    ]
    decision = select_terminal_node(activities)
    return ExperimentResult(
        "E04",
        "completed",
        "terminal_node",
        decision.terminal_node_id,
        decision.terminal_node_id == "boundary" and not decision.unresolved,
        decision.reason,
    )


def experiment_05_maximum_coherence_conduit() -> ExperimentResult:
    scores = {"data": 0.5, "trajectory": 0.7, "boundary": 0.9, "candidate": 0.95}
    links = {
        "data": ("trajectory",),
        "trajectory": ("data", "boundary"),
        "boundary": ("trajectory", "candidate"),
        "candidate": ("boundary",),
    }
    path = maximum_result_path(scores, links, start_node="data")
    envelope = build_pathway_envelope(path, (0.55, 0.75, 0.88, 0.92))
    passed = path == ("data", "trajectory", "boundary", "candidate") and envelope.outer_radius < 0.5
    return ExperimentResult(
        "E05",
        "completed",
        "conduit_length",
        len(path),
        passed,
        f"Path={path}; geometry={envelope.geometry}; radius={envelope.outer_radius:.4f}",
    )


def _shared_task(payload: Mapping[str, Any], cache) -> Mapping[str, Any]:
    shared = cache.get_or_compute("feature_matrix", lambda: sum(payload["values"]))
    return {"score": shared * payload["weight"]}


def experiment_06_multicore_cache() -> ExperimentResult:
    executor = MultiCoreConduitExecutor(max_workers=4)
    tasks = [
        ConduitTask("c1", _shared_task, {"values": [1, 2, 3], "weight": 1.0}, coherence_index=0.8),
        ConduitTask("c2", _shared_task, {"values": [1, 2, 3], "weight": 2.0}, coherence_index=0.8),
        ConduitTask("c3", _shared_task, {"values": [1, 2, 3], "weight": 3.0}, coherence_index=0.8),
    ]
    started = time.perf_counter()
    results = executor.execute(tasks)
    elapsed = time.perf_counter() - started
    merged = merge_at_coherence_junction(
        "j1",
        list(results.values()),
        merge_function=lambda outputs: {"max_score": max(item["score"] for item in outputs)},
        cache=executor.cache,
    )
    return ExperimentResult(
        "E06",
        "completed",
        "cache_savings",
        merged.computation_saving_count,
        merged.computation_saving_count >= 2 and merged.merged_output["max_score"] == 18.0,
        f"elapsed_seconds={elapsed:.6f}",
    )


def experiment_07_quality_energy_priority() -> ExperimentResult:
    options = [
        ExecutionOption("high_quality", 0.95, 0.85, 0.85, 0.15, 10.0, 8.0),
        ExecutionOption("efficient_equal", 0.94, 0.85, 0.85, 0.15, 3.0, 2.0),
        ExecutionOption("cheap_lower", 0.80, 0.95, 0.95, 0.10, 1.0, 1.0),
    ]
    decision = select_quality_first(options, quality_tolerance=0.02)
    return ExperimentResult(
        "E07",
        "completed",
        "selected_option",
        decision.selected_option_id,
        decision.selected_option_id == "efficient_equal",
        decision.reason,
    )


def experiment_08_historical_readiness() -> ExperimentResult:
    if not CANONICAL_FILE.exists():
        return ExperimentResult(
            "E08",
            "blocked",
            "canonical_rows",
            0,
            False,
            "Canonical BBO dataset is not yet available; historical experiment remains gated.",
        )

    with CANONICAL_FILE.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    return ExperimentResult(
        "E08",
        "completed",
        "canonical_rows",
        len(rows),
        len(rows) == 88,
        "Historical experiment requires exactly 88 validated observations.",
    )


def run_suite() -> List[ExperimentResult]:
    experiments = [
        experiment_01_coherence_sign,
        experiment_02_conflict_detection,
        experiment_03_augmentation_bound,
        experiment_04_terminal_stability,
        experiment_05_maximum_coherence_conduit,
        experiment_06_multicore_cache,
        experiment_07_quality_energy_priority,
        experiment_08_historical_readiness,
    ]
    return [experiment() for experiment in experiments]


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    results = run_suite()
    summary = {
        "experiment_count": len(results),
        "passed": sum(item.passed for item in results),
        "failed": sum(item.status == "completed" and not item.passed for item in results),
        "blocked": sum(item.status == "blocked" for item in results),
        "results": [asdict(item) for item in results],
    }
    (OUTPUT_DIR / "experiment_suite_summary.json").write_text(
        json.dumps(summary, indent=2), encoding="utf-8"
    )

    with (OUTPUT_DIR / "experiment_suite_results.csv").open(
        "w", encoding="utf-8", newline=""
    ) as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["experiment_id", "status", "metric", "value", "passed", "notes"],
        )
        writer.writeheader()
        writer.writerows(asdict(item) for item in results)

    for result in results:
        print(
            f"{result.experiment_id}: status={result.status} "
            f"passed={result.passed} {result.metric}={result.value}"
        )

    completed_failures = [
        result for result in results if result.status == "completed" and not result.passed
    ]
    if completed_failures:
        raise SystemExit(f"{len(completed_failures)} completed experiment(s) failed")


if __name__ == "__main__":
    main()
