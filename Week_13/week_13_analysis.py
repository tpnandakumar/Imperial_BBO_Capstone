from __future__ import annotations

import csv
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WEEK = ROOT / "Week_13"
FUNCTIONS = [f"Function {i}" for i in range(1, 9)]
DIMS = [2, 2, 3, 4, 4, 5, 6, 8]


def read_results(week: int) -> dict[str, Decimal]:
    path = ROOT / f"Week_{week:02d}" / f"week_{week:02d}_results.csv"
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    return {row["function"]: Decimal(row["output"]) for row in rows}


def read_inputs(week: int) -> dict[str, tuple[Decimal, ...]]:
    path = ROOT / f"Week_{week:02d}" / f"week_{week:02d}_inputs.csv"
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    result = {}
    for row, dim in zip(rows, DIMS):
        coords = tuple(Decimal(row[f"x{i}"]) for i in range(1, dim + 1))
        result[row["function"]] = coords
    return result


def main() -> None:
    history = {week: read_results(week) for week in range(1, 14)}
    inputs = {week: read_inputs(week) for week in range(1, 14)}

    summary_rows = []
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

    out_path = WEEK / "week_13_analysis_summary.csv"
    with out_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=summary_rows[0].keys())
        writer.writeheader()
        writer.writerows(summary_rows)

    print("Week 13 summary")
    for row in summary_rows:
        print(row)

    print("\nRepeated input checks")
    for function in FUNCTIONS:
        groups: dict[tuple[Decimal, ...], list[tuple[int, Decimal]]] = {}
        for week in range(1, 14):
            groups.setdefault(inputs[week][function], []).append((week, history[week][function]))
        for coords, observations in groups.items():
            if len(observations) > 1:
                unique_outputs = {value for _, value in observations}
                if len(unique_outputs) > 1:
                    print(function, coords, observations)


if __name__ == "__main__":
    main()
