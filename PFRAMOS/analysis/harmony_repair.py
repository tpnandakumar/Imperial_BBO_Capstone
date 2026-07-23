"""Conservative repair and forwarding gate for PFRAMOS historical data.

The repair engine never edits historical Week folders. It reads recognised
variants, normalises them into a canonical dataset, records every repair, and
forwards data only when all 88 observations pass validation.
"""

from __future__ import annotations

import csv
import json
from dataclasses import asdict, dataclass
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Dict, List

from PFRAMOS.analysis.harmony_test import (
    EXPECTED_DIMENSIONS,
    REPOSITORY_ROOT,
    candidate_files,
    find_column,
    normalise_function,
    read_csv,
)


PFRAMOS_ROOT = Path(__file__).resolve().parents[1]
CANONICAL_FILE = PFRAMOS_ROOT / "data" / "canonical_bbo_observations.csv"
MANIFEST_FILE = PFRAMOS_ROOT / "data" / "source_manifest.csv"
REPAIR_LOG = PFRAMOS_ROOT / "outputs" / "public" / "harmony_repair_log.json"
READY_MARKER = PFRAMOS_ROOT / "outputs" / "public" / "harmony_ready.json"


@dataclass(frozen=True)
class RepairEvent:
    week: int
    role: str
    action: str
    source_path: str
    detail: str


def _normalise_coordinates(value: str, expected: int) -> List[str]:
    text = value.strip().strip('"')
    separator = "," if "," in text else "-"
    parts = [part.strip() for part in text.split(separator) if part.strip()]
    if len(parts) != expected:
        raise ValueError(f"Expected {expected} coordinates, found {len(parts)}")
    normalised: List[str] = []
    for part in parts:
        number = Decimal(part)
        if number < 0 or number > 1:
            raise ValueError(f"Coordinate outside [0,1]: {number}")
        normalised.append(format(number, "f"))
    return normalised


def _load_role(week: int, role: str, events: List[RepairEvent]) -> Dict[int, object]:
    folder = REPOSITORY_ROOT / f"Week_{week:02d}"
    candidates = candidate_files(folder, role, week)
    if not candidates:
        raise FileNotFoundError(f"No {role} CSV found for Week {week:02d}")

    path = candidates[0]
    if len(candidates) > 1:
        events.append(RepairEvent(week, role, "resolved_ambiguity", str(path), "Selected preferred or first deterministic candidate"))

    fieldnames, rows = read_csv(path)
    function_column = find_column(fieldnames, ("function", "function_id", "objective"))
    value_column = find_column(
        fieldnames,
        ("input", "query", "coordinates") if role == "inputs" else ("output", "result", "value"),
    )
    if function_column is None or value_column is None:
        raise ValueError(f"Unrecognised schema in {path}: {fieldnames}")

    loaded: Dict[int, object] = {}
    for row in rows:
        function = normalise_function(row.get(function_column, ""))
        if function is None:
            raise ValueError(f"Invalid function label in {path}")
        if function in loaded:
            raise ValueError(f"Duplicate Function {function} in {path}")

        raw_value = row.get(value_column, "")
        if role == "inputs":
            loaded[function] = _normalise_coordinates(raw_value, EXPECTED_DIMENSIONS[function])
        else:
            try:
                loaded[function] = format(Decimal(raw_value.strip()), "f")
            except InvalidOperation as error:
                raise ValueError(f"Invalid output for Function {function} in {path}") from error

    if set(loaded) != set(EXPECTED_DIMENSIONS):
        raise ValueError(f"Incomplete {role} data in {path}")

    events.append(RepairEvent(week, role, "normalised_copy", str(path), "Source preserved; canonical copy created"))
    return loaded


def main() -> None:
    events: List[RepairEvent] = []
    canonical_rows: List[Dict[str, str]] = []
    manifest_rows: List[Dict[str, str]] = []

    for week in range(1, 12):
        inputs = _load_role(week, "inputs", events)
        results = _load_role(week, "results", events)
        for function in sorted(EXPECTED_DIMENSIONS):
            coordinates = inputs[function]
            row: Dict[str, str] = {
                "Week": str(week),
                "Function": str(function),
                "Dimension": str(EXPECTED_DIMENSIONS[function]),
                "Output": str(results[function]),
            }
            for index in range(1, 9):
                row[f"Input_{index}"] = coordinates[index - 1] if index <= len(coordinates) else ""
            canonical_rows.append(row)

        folder = REPOSITORY_ROOT / f"Week_{week:02d}"
        manifest_rows.append(
            {
                "Week": str(week),
                "Input_Source": str(candidate_files(folder, "inputs", week)[0]),
                "Result_Source": str(candidate_files(folder, "results", week)[0]),
                "Status": "validated",
            }
        )

    expected_rows = 88
    if len(canonical_rows) != expected_rows:
        raise RuntimeError(f"Canonical dataset contains {len(canonical_rows)} rows, expected {expected_rows}")

    CANONICAL_FILE.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = ["Week", "Function", "Dimension"] + [f"Input_{index}" for index in range(1, 9)] + ["Output"]
    with CANONICAL_FILE.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(canonical_rows)

    with MANIFEST_FILE.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["Week", "Input_Source", "Result_Source", "Status"])
        writer.writeheader()
        writer.writerows(manifest_rows)

    REPAIR_LOG.parent.mkdir(parents=True, exist_ok=True)
    REPAIR_LOG.write_text(json.dumps([asdict(event) for event in events], indent=2), encoding="utf-8")
    READY_MARKER.write_text(json.dumps({"ready": True, "rows": expected_rows, "weeks": 11, "functions": 8}, indent=2), encoding="utf-8")
    print(f"Harmony repair complete. Canonical dataset written to {CANONICAL_FILE}")


if __name__ == "__main__":
    main()
