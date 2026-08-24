from __future__ import annotations

import csv
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WEEK = ROOT / "Week_13"
EARLY_HISTORY = ROOT / "PFRAMOS" / "data" / "recovered_exact_history.csv"
FUNCTIONS = [f"Function {i}" for i in range(1, 9)]
DIMS = {f"Function {i}": dim for i, dim in enumerate([2, 2, 3, 4, 4, 5, 6, 8], start=1)}


def load_early_history() -> tuple[dict[int, dict[str, Decimal]], dict[int, dict[str, tuple[Decimal, ...]]]]:
    """Load the committed exact Weeks 1 to 11 history without altering values."""
    history: dict[int, dict[str, Decimal]] = {week: {} for week in range(1, 12)}
    inputs: dict[int, dict[str, tuple[Decimal, ...]]] = {week: {} for week in range(1, 12)}

    with EARLY_HISTORY.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            week = int(row["Week"])
            if week > 11:
                continue
            function = f"Function {int(row['Function'])}"
            dim = int(row["Dimension"])
            coords = tuple(Decimal(row[f"Input_{i}"]) for i in range(1, dim + 1))
            history[week][function] = Decimal(row["Output"])
            inputs[week][function] = coords

    return history, inputs


def read_results(week: int) -> dict[str, Decimal]:
    """Read a verified Week 12 or Week 13 result file."""
    path = ROOT / f"Week_{week:02d}" / f"week_{week:02d}_results.csv"
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    return {row["function"]: Decimal(row["output"]) for row in rows}


def read_inputs(week: int) -> dict[str, tuple[Decimal, ...]]:
    """Read the two input-file layouts used in Weeks 12 and 13."""
    path = ROOT / f"Week_{week:02d}" / f"week_{week:02d}_inputs.csv"
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    result: dict[str, tuple[Decimal, ...]] = {}
    for row in rows:
        function = row.get("function") or row.get("Function")
        if function is None:
            raise ValueError(f"Missing function label in {path}")
        dim = DIMS[function]

        if "Input" in row and row["Input"]:
            values = [item.strip() for item in row["Input"].split(",")]
            coords = tuple(Decimal(values[i]) for i in range(dim))
        else:
            coords = tuple(Decimal(row[f"x{i}"]) for i in range(1, dim + 1))

        result[function] = coords
    return result


def load_history() -> tuple[dict[int, dict[str, Decimal]], dict[int, dict[str, tuple[Decimal, ...]]]]:
    """Build the complete thirteen-round history from committed evidence."""
    history, inputs = load_early_history()
    for week in (12, 13):
        history[week] = read_results(week)
        inputs[week] = read_inputs(week)

    for week in range(1, 14):
        missing_outputs = set(FUNCTIONS) - set(history[week])
        missing_inputs = set(FUNCTIONS) - set(inputs[week])
        if missing_outputs or missing_inputs:
            raise ValueError(
                f"Incomplete Week {week}: missing outputs {sorted(missing_outputs)}, "
                f"missing inputs {sorted(missing_inputs)}"
            )
    return history, inputs


def build_summary(history: dict[int, dict[str, Decimal]]) -> list[dict[str, str]]:
    summary_rows: list[dict[str, str]] = []
    for function in FUNCTIONS:
        week12 = history[12][function]
        week13 = history[13][function]
        change = week13 - week12
        values = [history[w][function] for w in range(1, 14)]
        best = max(values)
        best_weeks = [str(w) for w in range(1, 14) if history[w][function] == best]

        if week13 == best and week12 == best:
            status = "Best retained"
        elif week13 == best:
            status = "New overall best"
        elif change < 0:
            status = "Declined from Week 12 best"
        else:
            status = "Improved but below historical best"

        summary_rows.append(
            {
                "function": function,
                "week_12_output": str(week12),
                "week_13_output": str(week13),
                "exact_change": str(change),
                "final_status": status,
                "best_output": str(best),
                "best_week_or_weeks": ";".join(best_weeks),
            }
        )
    return summary_rows


def write_summary(summary_rows: list[dict[str, str]]) -> Path:
    out_path = WEEK / "week_13_analysis_summary.csv"
    with out_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=summary_rows[0].keys())
        writer.writeheader()
        writer.writerows(summary_rows)
    return out_path


def repeated_input_variability(
    history: dict[int, dict[str, Decimal]],
    inputs: dict[int, dict[str, tuple[Decimal, ...]]],
) -> list[tuple[str, tuple[Decimal, ...], list[tuple[int, Decimal]]]]:
    findings = []
    for function in FUNCTIONS:
        groups: dict[tuple[Decimal, ...], list[tuple[int, Decimal]]] = {}
        for week in range(1, 14):
            groups.setdefault(inputs[week][function], []).append((week, history[week][function]))
        for coords, observations in groups.items():
            if len(observations) > 1 and len({value for _, value in observations}) > 1:
                findings.append((function, coords, observations))
    return findings


def main() -> None:
    history, inputs = load_history()
    summary_rows = build_summary(history)
    out_path = write_summary(summary_rows)

    print("Week 13 summary")
    for row in summary_rows:
        print(row)

    print("\nRepeated input checks")
    for finding in repeated_input_variability(history, inputs):
        print(*finding)

    print(f"\nWrote {out_path}")


if __name__ == "__main__":
    main()
