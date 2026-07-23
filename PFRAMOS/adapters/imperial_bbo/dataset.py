"""Load and validate Imperial BBO weekly input and output files."""

from __future__ import annotations

import csv
from dataclasses import dataclass
from decimal import Decimal
from pathlib import Path
from typing import Dict, List, Tuple


DIMENSIONS = {
    1: 2,
    2: 2,
    3: 3,
    4: 4,
    5: 4,
    6: 5,
    7: 6,
    8: 8,
}


@dataclass(frozen=True)
class Observation:
    week: int
    function: int
    coordinates: Tuple[Decimal, ...]
    output: Decimal


def _normalise_function(value: str) -> int:
    cleaned = value.strip().lower().replace("function", "").replace("f", "")
    number = int(cleaned.strip())
    if number not in DIMENSIONS:
        raise ValueError(f"Unsupported function: {value}")
    return number


def _parse_coordinates(value: str, expected: int) -> Tuple[Decimal, ...]:
    separator = "," if "," in value else "-"
    coordinates = tuple(Decimal(item.strip()) for item in value.split(separator))
    if len(coordinates) != expected:
        raise ValueError(f"Expected {expected} coordinates, received {len(coordinates)}")
    if any(value < 0 or value > 1 for value in coordinates):
        raise ValueError("All coordinates must be in [0, 1]")
    return coordinates


def load_week(repository_root: Path, week: int) -> List[Observation]:
    folder = repository_root / f"Week_{week:02d}"
    inputs_path = folder / f"week_{week:02d}_inputs.csv"
    results_path = folder / f"week_{week:02d}_results.csv"

    with inputs_path.open("r", encoding="utf-8-sig", newline="") as handle:
        inputs = {
            _normalise_function(row["Function"]): row["Input"]
            for row in csv.DictReader(handle)
        }

    with results_path.open("r", encoding="utf-8-sig", newline="") as handle:
        outputs = {
            _normalise_function(row["Function"]): Decimal(row["Output"].strip())
            for row in csv.DictReader(handle)
        }

    if inputs.keys() != outputs.keys() or set(inputs) != set(DIMENSIONS):
        raise ValueError(f"Week {week:02d} does not contain a complete matched dataset")

    return [
        Observation(
            week=week,
            function=function,
            coordinates=_parse_coordinates(inputs[function], DIMENSIONS[function]),
            output=outputs[function],
        )
        for function in sorted(inputs)
    ]


def load_history(repository_root: Path, start_week: int = 1, end_week: int = 11) -> Dict[int, List[Observation]]:
    history: Dict[int, List[Observation]] = {function: [] for function in DIMENSIONS}
    for week in range(start_week, end_week + 1):
        for observation in load_week(repository_root, week):
            history[observation.function].append(observation)
    return history
