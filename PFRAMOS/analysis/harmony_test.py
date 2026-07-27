"""Repository harmony test for Imperial BBO historical data.

The module inspects weekly folders without rewriting historical source files.
It reports naming, file-presence, schema, dimensional, formatting and
completeness disharmony before any optimisation analysis is permitted to run.
"""

from __future__ import annotations

import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, List, Sequence


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
OUTPUT_FILE = Path(__file__).resolve().parents[1] / "outputs" / "public" / "harmony_report.json"
EXPECTED_DIMENSIONS = {1: 2, 2: 2, 3: 3, 4: 4, 5: 4, 6: 5, 7: 6, 8: 8}


@dataclass(frozen=True)
class HarmonyIssue:
    week: int
    category: str
    severity: str
    detail: str
    path: str = ""


def candidate_files(folder: Path, role: str, week: int) -> List[Path]:
    tokens = ("input", "query") if role == "inputs" else ("result", "output")
    candidates = [
        path
        for path in folder.rglob("*.csv")
        if any(token in path.name.lower() for token in tokens)
    ]
    preferred = folder / f"week_{week:02d}_{role}.csv"
    if preferred.exists():
        return [preferred] + [item for item in candidates if item != preferred]
    return sorted(candidates)


def read_csv(path: Path) -> tuple[Sequence[str], List[Dict[str, str]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        return tuple(reader.fieldnames or ()), list(reader)


def find_column(fieldnames: Sequence[str], options: Sequence[str]) -> str | None:
    mapping = {name.lower().strip(): name for name in fieldnames}
    for option in options:
        if option in mapping:
            return mapping[option]
    return None


def normalise_function(value: str) -> int | None:
    cleaned = value.lower().replace("function", "").replace("f", "").strip()
    try:
        number = int(cleaned)
    except ValueError:
        return None
    return number if number in EXPECTED_DIMENSIONS else None


def coordinate_count(value: str) -> int:
    text = value.strip().strip('"')
    separator = "," if "," in text else "-"
    return len([part for part in text.split(separator) if part.strip()])


def inspect_week(week: int) -> List[HarmonyIssue]:
    issues: List[HarmonyIssue] = []
    folder = REPOSITORY_ROOT / f"Week_{week:02d}"
    if not folder.exists():
        return [HarmonyIssue(week, "folder", "critical", "Weekly folder is missing", str(folder))]

    for role in ("inputs", "results"):
        candidates = candidate_files(folder, role, week)
        if not candidates:
            issues.append(HarmonyIssue(week, "file_presence", "critical", f"No {role} CSV found", str(folder)))
            continue
        if len(candidates) > 1:
            issues.append(HarmonyIssue(week, "file_ambiguity", "warning", f"Multiple possible {role} CSV files found", ", ".join(str(item) for item in candidates)))

        path = candidates[0]
        try:
            fieldnames, rows = read_csv(path)
        except Exception as error:
            issues.append(HarmonyIssue(week, "csv_read", "critical", f"Could not read CSV: {error}", str(path)))
            continue

        function_column = find_column(fieldnames, ("function", "function_id", "objective"))
        value_column = find_column(
            fieldnames,
            ("input", "query", "coordinates") if role == "inputs" else ("output", "result", "value"),
        )
        if function_column is None or value_column is None:
            issues.append(HarmonyIssue(week, "schema", "critical", f"Unrecognised columns: {fieldnames}", str(path)))
            continue

        if len(rows) != 8:
            issues.append(HarmonyIssue(week, "row_count", "critical", f"Expected 8 rows, found {len(rows)}", str(path)))

        seen: set[int] = set()
        for row in rows:
            function = normalise_function(row.get(function_column, ""))
            if function is None:
                issues.append(HarmonyIssue(week, "function_label", "critical", f"Invalid function label: {row.get(function_column, '')}", str(path)))
                continue
            if function in seen:
                issues.append(HarmonyIssue(week, "duplicate_function", "critical", f"Duplicate Function {function}", str(path)))
            seen.add(function)

            if role == "inputs":
                count = coordinate_count(row.get(value_column, ""))
                expected = EXPECTED_DIMENSIONS[function]
                if count != expected:
                    issues.append(HarmonyIssue(week, "dimension", "critical", f"Function {function} has {count} coordinates, expected {expected}", str(path)))

        missing = sorted(set(EXPECTED_DIMENSIONS) - seen)
        if missing:
            issues.append(HarmonyIssue(week, "missing_functions", "critical", f"Missing functions: {missing}", str(path)))

    return issues


def main() -> None:
    issues = [issue for week in range(1, 12) for issue in inspect_week(week)]
    critical = sum(issue.severity == "critical" for issue in issues)
    warnings = sum(issue.severity == "warning" for issue in issues)
    report = {
        "weeks_checked": list(range(1, 12)),
        "critical_issue_count": critical,
        "warning_count": warnings,
        "harmonious": critical == 0,
        "issues": [asdict(issue) for issue in issues],
    }
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"Harmony report written to {OUTPUT_FILE}")
    if critical:
        raise SystemExit(f"Harmony gate blocked forwarding: {critical} critical issue(s)")


if __name__ == "__main__":
    main()
