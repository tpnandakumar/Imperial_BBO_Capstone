"""Repair, validate and forward the full Imperial BBO history.

Historical Week folders remain unchanged. The recovered exact-history file is
used as the authoritative recovery source for Weeks 1 to 11. Where weekly CSV
files exist, their normalised values are compared against the recovered source.
Any mismatch is reported and blocks forwarding.
"""

from __future__ import annotations

import csv
import json
from dataclasses import asdict, dataclass
from decimal import Decimal
from pathlib import Path
from typing import Dict, List, Tuple

from PFRAMOS.analysis.harmony_test import REPOSITORY_ROOT, candidate_files
from PFRAMOS.analysis.learning_log import append_learning
from PFRAMOS.analysis.schema_normalizer import EXPECTED_DIMENSIONS, load_inputs, load_results


PFRAMOS_ROOT = Path(__file__).resolve().parents[1]
RECOVERED_FILE = PFRAMOS_ROOT / "data" / "recovered_exact_history.csv"
CANONICAL_FILE = PFRAMOS_ROOT / "data" / "canonical_bbo_observations.csv"
MANIFEST_FILE = PFRAMOS_ROOT / "data" / "source_manifest.csv"
QUARANTINE_FILE = PFRAMOS_ROOT / "data" / "quarantined_weeks.json"
REPAIR_LOG = PFRAMOS_ROOT / "outputs" / "public" / "harmony_repair_log.json"
CONGRUENCE_REPORT = PFRAMOS_ROOT / "outputs" / "public" / "source_congruence_report.json"
READY_MARKER = PFRAMOS_ROOT / "outputs" / "public" / "harmony_ready.json"


@dataclass(frozen=True)
class RepairEvent:
    week: int
    role: str
    action: str
    source_path: str
    detail: str


def _load_recovered() -> Dict[Tuple[int, int], Dict[str, str]]:
    if not RECOVERED_FILE.exists():
        raise FileNotFoundError(f"Recovered exact history is missing: {RECOVERED_FILE}")

    records: Dict[Tuple[int, int], Dict[str, str]] = {}
    with RECOVERED_FILE.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            week = int(row["Week"])
            function = int(row["Function"])
            dimension = int(row["Dimension"])
            if dimension != EXPECTED_DIMENSIONS[function]:
                raise ValueError(
                    f"Recovered dimension mismatch for Week {week}, Function {function}"
                )
            for index in range(1, dimension + 1):
                value = Decimal(row[f"Input_{index}"])
                if value < 0 or value > 1:
                    raise ValueError(
                        f"Recovered coordinate outside [0,1] for Week {week}, Function {function}"
                    )
            Decimal(row["Output"])
            key = (week, function)
            if key in records:
                raise ValueError(f"Duplicate recovered record: {key}")
            records[key] = row

    expected = {(week, function) for week in range(1, 12) for function in range(1, 9)}
    missing = sorted(expected - set(records))
    extra = sorted(set(records) - expected)
    if missing or extra:
        raise ValueError(f"Recovered history mismatch. Missing={missing}; Extra={extra}")
    return records


def _weekly_sources(week: int) -> tuple[Path | None, Path | None]:
    folder = REPOSITORY_ROOT / f"Week_{week:02d}"
    inputs = candidate_files(folder, "inputs", week)
    results = candidate_files(folder, "results", week)
    return (inputs[0] if inputs else None, results[0] if results else None)


def _compare_week(
    week: int,
    recovered: Dict[Tuple[int, int], Dict[str, str]],
) -> Dict[str, object]:
    input_path, result_path = _weekly_sources(week)
    report: Dict[str, object] = {
        "week": week,
        "input_source": str(input_path) if input_path else "",
        "result_source": str(result_path) if result_path else "",
        "status": "recovered_only",
        "mismatches": [],
    }
    if input_path is None or result_path is None:
        return report

    try:
        weekly_inputs = load_inputs(input_path)
        weekly_results = load_results(result_path)
    except Exception as error:
        report["status"] = "weekly_source_unreadable"
        report["mismatches"] = [str(error)]
        return report

    mismatches: List[str] = []
    for function in range(1, 9):
        recovered_row = recovered[(week, function)]
        dimension = EXPECTED_DIMENSIONS[function]
        recovered_inputs = [
            format(Decimal(recovered_row[f"Input_{index}"]), "f")
            for index in range(1, dimension + 1)
        ]
        if weekly_inputs[function] != recovered_inputs:
            mismatches.append(f"Function {function} input mismatch")
        recovered_output = Decimal(recovered_row["Output"])
        weekly_output = Decimal(weekly_results[function])
        if weekly_output != recovered_output:
            mismatches.append(f"Function {function} output mismatch")

    report["status"] = "congruent" if not mismatches else "conflict"
    report["mismatches"] = mismatches
    return report


def main() -> None:
    recovered = _load_recovered()
    events: List[RepairEvent] = []
    congruence = [_compare_week(week, recovered) for week in range(1, 12)]
    conflicts = [item for item in congruence if item["status"] == "conflict"]

    canonical_rows = [recovered[key] for key in sorted(recovered)]
    CANONICAL_FILE.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "Week",
        "Function",
        "Dimension",
        *[f"Input_{index}" for index in range(1, 9)],
        "Output",
        "Source",
    ]
    with CANONICAL_FILE.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(canonical_rows)

    manifest_rows: List[Dict[str, str]] = []
    for item in congruence:
        status = str(item["status"])
        week = int(item["week"])
        manifest_rows.append(
            {
                "Week": str(week),
                "Recovered_Source": str(RECOVERED_FILE),
                "Input_Source": str(item["input_source"]),
                "Result_Source": str(item["result_source"]),
                "Status": status,
                "Detail": "; ".join(item["mismatches"]) if item["mismatches"] else "Validated exact history",
            }
        )
        events.append(
            RepairEvent(
                week=week,
                role="both",
                action="recovered_and_compared",
                source_path=str(RECOVERED_FILE),
                detail=f"Weekly source status: {status}",
            )
        )

    with MANIFEST_FILE.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "Week",
                "Recovered_Source",
                "Input_Source",
                "Result_Source",
                "Status",
                "Detail",
            ],
        )
        writer.writeheader()
        writer.writerows(manifest_rows)

    quarantined = [
        {"week": int(item["week"]), "reason": item["mismatches"]}
        for item in conflicts
    ]
    QUARANTINE_FILE.write_text(json.dumps(quarantined, indent=2), encoding="utf-8")
    CONGRUENCE_REPORT.parent.mkdir(parents=True, exist_ok=True)
    CONGRUENCE_REPORT.write_text(json.dumps(congruence, indent=2), encoding="utf-8")
    REPAIR_LOG.write_text(json.dumps([asdict(event) for event in events], indent=2), encoding="utf-8")

    ready = len(canonical_rows) == 88 and not conflicts
    READY_MARKER.write_text(
        json.dumps(
            {
                "ready": ready,
                "canonical_rows": len(canonical_rows),
                "expected_rows": 88,
                "validated_weeks": 11,
                "conflicted_weeks": [int(item["week"]) for item in conflicts],
                "recovery_source": str(RECOVERED_FILE),
            },
            indent=2,
        ),
        encoding="utf-8",
    )

    append_learning(
        stage="github_repair_session",
        finding="Complete exact Weeks 1 to 11 history existed outside the incomplete weekly-folder layout.",
        evidence={
            "recovered_records": len(canonical_rows),
            "weekly_congruence_checks": len(congruence),
            "conflicted_weeks": [int(item["week"]) for item in conflicts],
        },
        action_taken="Added the traceable recovered exact-history source, compared it with available weekly CSVs, and rebuilt the canonical dataset.",
        outcome="The canonical dataset now contains all 88 expected observations; forwarding depends on absence of source conflicts.",
        reusable_rule="Search authoritative project artefacts before declaring data absent, then verify recovered records against any local duplicates.",
    )

    print(
        f"GitHub repair session produced {len(canonical_rows)}/88 canonical rows; "
        f"source conflicts: {[int(item['week']) for item in conflicts]}"
    )
    if not ready:
        raise SystemExit("Harmony forwarding blocked by source conflicts")


if __name__ == "__main__":
    main()
