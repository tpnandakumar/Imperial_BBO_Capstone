from __future__ import annotations

import csv
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WEEK = ROOT / "Week_13"
COMPLETE_EVIDENCE = ROOT / "BBO_Dashboard" / "data" / "complete_internal_evidence.csv"
FUNCTIONS = [f"Function {i}" for i in range(1, 9)]
DIMS = {
    f"Function {i}": dim
    for i, dim in enumerate([2, 2, 3, 4, 4, 5, 6, 8], start=1)
}


def load_early_history() -> tuple[
    dict[int, dict[str, Decimal]],
    dict[int, dict[str, tuple[Decimal, ...]]],
]:
    """Load Weeks 1 to 11 from the canonical committed evidence file."""
    history: dict[int, dict[str, Decimal]] = {
        week: {} for week in range(1, 12)
    }
    inputs: dict[int, dict[str, tuple[Decimal, ...]]] = {
        week: {} for week in range(1, 12)
    }

    with COMPLETE_EVIDENCE.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            source = row["source"]
            if not source.startswith("week_"):
                continue
            week = int(source.removeprefix("week_"))
            if week > 11:
                continue
            function = f"Function {int(row['function'])}"
            dim = DIMS[function]
            coords = tuple(
                Decimal(row[f"x{i}"]) for i in range(1, dim + 1)
            )
            if function in history[week] or function in inputs[week]:
                raise ValueError(
                    f"Duplicate {function} record for Week {week} in "
                    f"{COMPLETE_EVIDENCE}"
                )
            history[week][function] = Decimal(row["output"])
            inputs[week][function] = coords

    return history, inputs


def read_results(week: int) -> dict[str, Decimal]:
    """Read a verified Week 12 or Week 13 result file."""
    path = ROOT / f"Week_{week:02d}" / f"week_{week:02d}_results.csv"
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    results: dict[str, Decimal] = {}
    for row in rows:
        function = row.get("function") or row.get("Function")
        output = row.get("output") or row.get("Output")
        if function is None or output is None:
            raise ValueError(f"Unexpected result layout in {path}")
        if function in results:
            raise ValueError(f"Duplicate result row for {function} in {path}")
        results[function] = Decimal(output)

    missing = set(FUNCTIONS) - set(results)
    unexpected = set(results) - set(FUNCTIONS)
    if missing or unexpected:
        raise ValueError(
            f"Invalid result set in {path}: missing={sorted(missing)}, "
            f"unexpected={sorted(unexpected)}"
        )
    return results


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
        if function in result:
            raise ValueError(f"Duplicate input row for {function} in {path}")

        dim = DIMS[function]
        if "Input" in row and row["Input"]:
            values = [item.strip() for item in row["Input"].split(",")]
            if len(values) != dim:
                raise ValueError(
                    f"{function} in {path} has {len(values)} values, "
                    f"expected {dim}"
                )
            coords = tuple(Decimal(value) for value in values)
        else:
            coords = tuple(
                Decimal(row[f"x{i}"]) for i in range(1, dim + 1)
            )

        if any(value < 0 or value > 1 for value in coords):
            raise ValueError(f"Input outside [0, 1] for {function} in {path}")
        result[function] = coords

    missing = set(FUNCTIONS) - set(result)
    unexpected = set(result) - set(FUNCTIONS)
    if missing or unexpected:
        raise ValueError(
            f"Invalid input set in {path}: missing={sorted(missing)}, "
            f"unexpected={sorted(unexpected)}"
        )
    return result


def load_history() -> tuple[
    dict[int, dict[str, Decimal]],
    dict[int, dict[str, tuple[Decimal, ...]]],
]:
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
                f"Incomplete Week {week}: missing outputs "
                f"{sorted(missing_outputs)}, missing inputs "
                f"{sorted(missing_inputs)}"
            )
    return history, inputs


def decimal_text(value: Decimal) -> str:
    """Return exact decimal text and express exact zero simply as 0."""
    return "0" if value == 0 else str(value)


def input_movement(
    week_12: tuple[Decimal, ...],
    week_13: tuple[Decimal, ...],
) -> tuple[Decimal, Decimal]:
    """Return exact L1 and squared Euclidean movement."""
    deltas = [new - old for old, new in zip(week_12, week_13)]
    l1 = sum((abs(delta) for delta in deltas), Decimal("0"))
    squared = sum((delta * delta for delta in deltas), Decimal("0"))
    return l1, squared


def repeated_input_variability(
    history: dict[int, dict[str, Decimal]],
    inputs: dict[int, dict[str, tuple[Decimal, ...]]],
) -> list[tuple[str, tuple[Decimal, ...], list[tuple[int, Decimal]]]]:
    """Find repeated coordinates that returned non-identical outputs."""
    findings = []
    for function in FUNCTIONS:
        groups: dict[tuple[Decimal, ...], list[tuple[int, Decimal]]] = {}
        for week in range(1, 14):
            groups.setdefault(inputs[week][function], []).append(
                (week, history[week][function])
            )
        for coords, observations in groups.items():
            outputs = {value for _, value in observations}
            if len(observations) > 1 and len(outputs) > 1:
                findings.append((function, coords, observations))
    return findings


def build_summary(
    history: dict[int, dict[str, Decimal]],
    inputs: dict[int, dict[str, tuple[Decimal, ...]]],
) -> list[dict[str, str]]:
    """Build the final exact Week 13 analytical summary."""
    variability_functions = {
        function
        for function, _, _ in repeated_input_variability(history, inputs)
    }
    summary_rows: list[dict[str, str]] = []

    for function in FUNCTIONS:
        week_12_output = history[12][function]
        week_13_output = history[13][function]
        change = week_13_output - week_12_output
        week_12_input = inputs[12][function]
        week_13_input = inputs[13][function]
        l1, squared = input_movement(week_12_input, week_13_input)
        identical_input = week_12_input == week_13_input

        values = [history[week][function] for week in range(1, 14)]
        best = max(values)
        best_weeks = [
            str(week)
            for week in range(1, 14)
            if history[week][function] == best
        ]

        if week_13_output == best and week_12_output == best:
            final_status = "Best retained"
        elif week_13_output == best:
            final_status = "New overall best"
        elif change < 0:
            final_status = "Declined from Week 12 best"
        else:
            final_status = "Improved but below historical best"

        if identical_input and week_13_output == week_12_output:
            repeatability_result = "Identical input, identical output"
        elif identical_input:
            repeatability_result = "Identical input, different output"
        else:
            repeatability_result = "Input changed"

        summary_rows.append(
            {
                "function": function,
                "week_12_output": str(week_12_output),
                "week_13_output": str(week_13_output),
                "exact_change": decimal_text(change),
                "l1_input_movement": decimal_text(l1),
                "squared_euclidean_movement": decimal_text(squared),
                "identical_input": "Yes" if identical_input else "No",
                "repeatability_result": repeatability_result,
                "historical_repeated_input_variability": (
                    "Yes" if function in variability_functions else "No"
                ),
                "final_status": final_status,
                "best_output": str(best),
                "best_week_or_weeks": ";".join(best_weeks),
            }
        )
    return summary_rows


def write_summary(summary_rows: list[dict[str, str]]) -> Path:
    out_path = WEEK / "week_13_analysis_summary.csv"
    with out_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=summary_rows[0].keys(),
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(summary_rows)
    return out_path


def main() -> None:
    history, inputs = load_history()
    summary_rows = build_summary(history, inputs)
    out_path = write_summary(summary_rows)

    print("Week 13 final analysis")
    for row in summary_rows:
        print(row)

    print("\nRepeated input variability checks")
    findings = repeated_input_variability(history, inputs)
    if not findings:
        print("No repeated coordinate returned a different output.")
    else:
        for function, coords, observations in findings:
            print(function, coords, observations)

    print(f"\nWrote {out_path}")


if __name__ == "__main__":
    main()
