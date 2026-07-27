"""Load validated Imperial BBO observations from the canonical dataset."""

from __future__ import annotations

import csv
import json
from dataclasses import dataclass
from decimal import Decimal
from pathlib import Path
from typing import Dict, List, Tuple


DIMENSIONS = {1: 2, 2: 2, 3: 3, 4: 4, 5: 4, 6: 5, 7: 6, 8: 8}


@dataclass(frozen=True)
class Observation:
    week: int
    function: int
    coordinates: Tuple[Decimal, ...]
    output: Decimal


def canonical_paths(repository_root: Path) -> tuple[Path, Path]:
    pframos_root = repository_root / "PFRAMOS"
    return (
        pframos_root / "data" / "canonical_bbo_observations.csv",
        pframos_root / "outputs" / "public" / "harmony_ready.json",
    )


def load_history(
    repository_root: Path,
    start_week: int = 1,
    end_week: int = 11,
    *,
    require_complete: bool = True,
) -> Dict[int, List[Observation]]:
    canonical_file, ready_marker = canonical_paths(repository_root)
    if not canonical_file.exists():
        raise FileNotFoundError("Canonical BBO dataset has not been created")

    if require_complete:
        if not ready_marker.exists():
            raise RuntimeError("Harmony readiness marker is missing")
        readiness = json.loads(ready_marker.read_text(encoding="utf-8"))
        if not readiness.get("ready", False):
            raise RuntimeError(
                "Canonical dataset remains incomplete; quarantined weeks must be resolved"
            )

    history: Dict[int, List[Observation]] = {function: [] for function in DIMENSIONS}
    with canonical_file.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            week = int(row["Week"])
            function = int(row["Function"])
            if week < start_week or week > end_week:
                continue
            dimension = DIMENSIONS[function]
            coordinates = tuple(
                Decimal(row[f"Input_{index}"])
                for index in range(1, dimension + 1)
            )
            observation = Observation(
                week=week,
                function=function,
                coordinates=coordinates,
                output=Decimal(row["Output"]),
            )
            history[function].append(observation)

    for observations in history.values():
        observations.sort(key=lambda item: item.week)

    if require_complete:
        expected_count = end_week - start_week + 1
        incomplete = {
            function: len(observations)
            for function, observations in history.items()
            if len(observations) != expected_count
        }
        if incomplete:
            raise RuntimeError(f"Incomplete canonical history: {incomplete}")

    return history
