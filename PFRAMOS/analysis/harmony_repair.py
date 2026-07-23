"""Conservative harmonisation and forwarding gate for PFRAMOS.

Historical Week folders are never edited. Recognised sources are normalised
into a canonical dataset. Missing or unverifiable weeks are quarantined and
reported. Full forwarding is permitted only when all 88 observations exist.
"""

from __future__ import annotations

import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, List

from PFRAMOS.analysis.harmony_test import REPOSITORY_ROOT, candidate_files
from PFRAMOS.analysis.learning_log import append_learning
from PFRAMOS.analysis.schema_normalizer import (
    EXPECTED_DIMENSIONS,
    load_inputs,
    load_results,
)


PFRAMOS_ROOT = Path(__file__).resolve().parents[1]
CANONICAL_FILE = PFRAMOS_ROOT / "data" / "canonical_bbo_observations.csv"
MANIFEST_FILE = PFRAMOS_ROOT / "data" / "source_manifest.csv"
QUARANTINE_FILE = PFRAMOS_ROOT / "data" / "quarantined_weeks.json"
REPAIR_LOG = PFRAMOS_ROOT / "outputs" / "public" / "harmony_repair_log.json"
READY_MARKER = PFRAMOS_ROOT / "outputs" / "public" / "harmony_ready.json"


@dataclass(frozen=True)
class RepairEvent:
    week: int
    role: str
    action: str
    source_path: str
    detail: str


def _select_source(week: int, role: str) -> Path:
    folder = REPOSITORY_ROOT / f"Week_{week:02d}"
    candidates = candidate_files(folder, role, week)
    if not candidates:
        raise FileNotFoundError(f"No {role} CSV found for Week {week:02d}")
    return candidates[0]


def _canonical_row(week: int, function: int, coordinates: List[str], output: str) -> Dict[str, str]:
    row: Dict[str, str] = {
        "Week": str(week),
        "Function": str(function),
        "Dimension": str(EXPECTED_DIMENSIONS[function]),
        "Output": output,
    }
    for index in range(1, 9):
        row[f"Input_{index}"] = coordinates[index - 1] if index <= len(coordinates) else ""
    return row


def main() -> None:
    events: List[RepairEvent] = []
    canonical_rows: List[Dict[str, str]] = []
    manifest_rows: List[Dict[str, str]] = []
    quarantined: List[Dict[str, object]] = []

    for week in range(1, 12):
        try:
            input_path = _select_source(week, "inputs")
            result_path = _select_source(week, "results")
            inputs = load_inputs(input_path)
            results = load_results(result_path)
        except Exception as error:
            quarantined.append({"week": week, "reason": str(error)})
            manifest_rows.append(
                {
                    "Week": str(week),
                    "Input_Source": "",
                    "Result_Source": "",
                    "Status": "quarantined",
                    "Detail": str(error),
                }
            )
            events.append(RepairEvent(week, "both", "quarantined", "", str(error)))
            continue

        for function in sorted(EXPECTED_DIMENSIONS):
            canonical_rows.append(
                _canonical_row(week, function, inputs[function], results[function])
            )

        manifest_rows.append(
            {
                "Week": str(week),
                "Input_Source": str(input_path),
                "Result_Source": str(result_path),
                "Status": "validated",
                "Detail": "Schema normalised without changing source files",
            }
        )
        events.extend(
            [
                RepairEvent(week, "inputs", "normalised_copy", str(input_path), "Packed or split input schema normalised"),
                RepairEvent(week, "results", "normalised_copy", str(result_path), "Header and numeric output schema normalised"),
            ]
        )

    CANONICAL_FILE.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = ["Week", "Function", "Dimension"] + [f"Input_{index}" for index in range(1, 9)] + ["Output"]
    with CANONICAL_FILE.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(canonical_rows)

    with MANIFEST_FILE.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["Week", "Input_Source", "Result_Source", "Status", "Detail"],
        )
        writer.writeheader()
        writer.writerows(manifest_rows)

    QUARANTINE_FILE.write_text(json.dumps(quarantined, indent=2), encoding="utf-8")
    REPAIR_LOG.parent.mkdir(parents=True, exist_ok=True)
    REPAIR_LOG.write_text(json.dumps([asdict(event) for event in events], indent=2), encoding="utf-8")

    expected_rows = 88
    ready = len(canonical_rows) == expected_rows and not quarantined
    READY_MARKER.write_text(
        json.dumps(
            {
                "ready": ready,
                "canonical_rows": len(canonical_rows),
                "expected_rows": expected_rows,
                "validated_weeks": 11 - len(quarantined),
                "quarantined_weeks": [item["week"] for item in quarantined],
            },
            indent=2,
        ),
        encoding="utf-8",
    )

    append_learning(
        stage="harmony_repair",
        finding="Historical weekly schemas were heterogeneous.",
        evidence={
            "canonical_rows": len(canonical_rows),
            "quarantined_weeks": [item["week"] for item in quarantined],
        },
        action_taken="Normalised recognised packed, split-column and leading-blank-line CSV formats; quarantined missing or unverifiable weeks.",
        outcome="Created a traceable partial canonical dataset without inventing data.",
        reusable_rule="Normalise proven schema variants, preserve source files, and quarantine unverified evidence.",
    )

    print(
        f"Harmony repair produced {len(canonical_rows)}/{expected_rows} canonical rows; "
        f"quarantined weeks: {[item['week'] for item in quarantined]}"
    )
    if not ready:
        raise SystemExit("Harmony forwarding remains blocked until all 88 observations are validated")


if __name__ == "__main__":
    main()
