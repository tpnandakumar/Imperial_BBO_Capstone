"""
Week 11 Analysis Tool
Imperial BBO Capstone

This script validates the Week 11 input and result files, compares the
Week 11 outputs with Week 10, ranks all eight objective functions and
exports week_11_analysis_summary.csv.

Numerical source values are retained as strings and Decimal values so
that no rounding or truncation is introduced during the analysis.
"""

from __future__ import annotations

import csv
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Dict, List


CURRENT_DIRECTORY = Path(__file__).resolve().parent

WEEK_11_INPUTS_FILE = CURRENT_DIRECTORY / "week_11_inputs.csv"
WEEK_11_RESULTS_FILE = CURRENT_DIRECTORY / "week_11_results.csv"
WEEK_11_SUMMARY_FILE = CURRENT_DIRECTORY / "week_11_analysis_summary.csv"
WEEK_10_RESULTS_FILE = (
    CURRENT_DIRECTORY.parent / "Week_10" / "week_10_results.csv"
)

STRATEGY = {
    "Function 1": "Exploit confirmed narrow peak",
    "Function 2": "Local trust region probe",
    "Function 3": "Local refinement",
    "Function 4": "Local recovery probe",
    "Function 5": "Boundary directed probe",
    "Function 6": "Best basin recovery",
    "Function 7": "Tight trust region refinement",
    "Function 8": "Exploit confirmed best",
}

NEAR_ZERO_THRESHOLD = Decimal("1e-12")
EXPECTED_DIMENSIONS = {
    "Function 1": 2,
    "Function 2": 2,
    "Function 3": 3,
    "Function 4": 4,
    "Function 5": 4,
    "Function 6": 5,
    "Function 7": 6,
    "Function 8": 8,
}


def normalise_function_name(value: str) -> str:
    """Convert labels such as F1 or Function 1 into Function 1."""

    cleaned = value.strip()

    if cleaned.lower().startswith("function"):
        number = cleaned.lower().replace("function", "").strip()
        return f"Function {number}"

    if cleaned.upper().startswith("F"):
        number = cleaned[1:].strip()
        return f"Function {number}"

    raise ValueError(f"Unrecognised function label: {value}")


def validate_function_set(
    values: Dict[str, Dict[str, object]],
    source_name: str,
) -> None:
    """Confirm that all eight functions are present exactly once."""

    expected_functions = {f"Function {number}" for number in range(1, 9)}
    actual_functions = set(values)

    missing_functions = expected_functions.difference(actual_functions)
    unexpected_functions = actual_functions.difference(expected_functions)

    if missing_functions:
        missing = ", ".join(sorted(missing_functions))
        raise ValueError(f"{source_name} is missing: {missing}")

    if unexpected_functions:
        unexpected = ", ".join(sorted(unexpected_functions))
        raise ValueError(f"{source_name} contains unexpected rows: {unexpected}")


def read_results(file_path: Path) -> Dict[str, Dict[str, object]]:
    """Read a results CSV while preserving the original output strings."""

    if not file_path.exists():
        raise FileNotFoundError(f"Results file not found: {file_path}")

    results: Dict[str, Dict[str, object]] = {}

    with file_path.open("r", encoding="utf-8-sig", newline="") as csv_file:
        reader = csv.DictReader(csv_file)

        if reader.fieldnames is None:
            raise ValueError(f"No CSV header found in {file_path.name}")

        required_columns = {"Function", "Output"}
        if not required_columns.issubset(set(reader.fieldnames)):
            raise ValueError(
                f"{file_path.name} must contain the columns "
                "'Function' and 'Output'."
            )

        for row in reader:
            function_name = normalise_function_name(row["Function"])
            output_text = row["Output"].strip()

            try:
                output_decimal = Decimal(output_text)
            except InvalidOperation as error:
                raise ValueError(
                    f"Invalid output for {function_name}: {output_text}"
                ) from error

            if function_name in results:
                raise ValueError(
                    f"Duplicate result row for {function_name} in {file_path.name}"
                )

            results[function_name] = {
                "output_text": output_text,
                "output_decimal": output_decimal,
            }

    validate_function_set(results, file_path.name)
    return results


def validate_inputs_file() -> None:
    """Validate the Week 11 input vectors and their dimensions."""

    if not WEEK_11_INPUTS_FILE.exists():
        raise FileNotFoundError(f"Input file not found: {WEEK_11_INPUTS_FILE}")

    rows: Dict[str, List[str]] = {}

    with WEEK_11_INPUTS_FILE.open(
        "r",
        encoding="utf-8-sig",
        newline="",
    ) as csv_file:
        reader = csv.DictReader(csv_file)

        if reader.fieldnames is None:
            raise ValueError(
                f"No CSV header found in {WEEK_11_INPUTS_FILE.name}"
            )

        required_columns = {"Function", "Input"}
        if not required_columns.issubset(set(reader.fieldnames)):
            raise ValueError(
                f"{WEEK_11_INPUTS_FILE.name} must contain the columns "
                "'Function' and 'Input'."
            )

        for row in reader:
            function_name = normalise_function_name(row["Function"])
            input_values = [value.strip() for value in row["Input"].split(",")]

            if function_name in rows:
                raise ValueError(
                    f"Duplicate input row for {function_name} in "
                    f"{WEEK_11_INPUTS_FILE.name}"
                )

            rows[function_name] = input_values

    if set(rows) != set(EXPECTED_DIMENSIONS):
        raise ValueError(
            f"{WEEK_11_INPUTS_FILE.name} must contain Functions 1 to 8."
        )

    for function_name, expected_dimension in EXPECTED_DIMENSIONS.items():
        input_values = rows[function_name]

        if len(input_values) != expected_dimension:
            raise ValueError(
                f"{function_name} should contain {expected_dimension} values, "
                f"but contains {len(input_values)}."
            )

        for value_text in input_values:
            try:
                value = Decimal(value_text)
            except InvalidOperation as error:
                raise ValueError(
                    f"Invalid input for {function_name}: {value_text}"
                ) from error

            if value < 0 or value > 1:
                raise ValueError(
                    f"Input outside [0, 1] for {function_name}: {value_text}"
                )


def classify_status(output: Decimal) -> str:
    """Classify an output as Positive, Negative or Near Zero."""

    if abs(output) < NEAR_ZERO_THRESHOLD:
        return "Near Zero"

    if output > 0:
        return "Positive"

    return "Negative"


def classify_direction(change: Decimal) -> str:
    """Classify the exact change relative to Week 10."""

    if change > 0:
        return "Improved"

    if change < 0:
        return "Declined"

    return "Unchanged"


def format_exact_change(change: Decimal) -> str:
    """Return a stable exact text representation for a Decimal change."""

    if change == 0:
        return "0"

    return str(change)


def build_summary(
    week_10_results: Dict[str, Dict[str, object]],
    week_11_results: Dict[str, Dict[str, object]],
) -> List[Dict[str, object]]:
    """Rank Week 11 functions and build the exact comparison summary."""

    ranked_functions = sorted(
        week_11_results.items(),
        key=lambda item: item[1]["output_decimal"],
        reverse=True,
    )

    summary_rows: List[Dict[str, object]] = []

    for rank, (function_name, values) in enumerate(
        ranked_functions,
        start=1,
    ):
        week_10_value = week_10_results[function_name]["output_decimal"]
        week_11_value = values["output_decimal"]
        change = week_11_value - week_10_value

        summary_rows.append(
            {
                "Function": function_name,
                "Output": values["output_text"],
                "Rank": rank,
                "Strategy": STRATEGY[function_name],
                "Status": classify_status(week_11_value),
                "Week_10_Output": week_10_results[function_name][
                    "output_text"
                ],
                "Exact_Change": format_exact_change(change),
                "Direction": classify_direction(change),
            }
        )

    return summary_rows


def write_summary(summary_rows: List[Dict[str, object]]) -> None:
    """Export the Week 11 analysis summary without changing source values."""

    fieldnames = [
        "Function",
        "Output",
        "Rank",
        "Strategy",
        "Status",
        "Week_10_Output",
        "Exact_Change",
        "Direction",
    ]

    with WEEK_11_SUMMARY_FILE.open(
        "w",
        encoding="utf-8",
        newline="",
    ) as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(summary_rows)


def print_summary_report(summary_rows: List[Dict[str, object]]) -> None:
    """Print the Week 11 ranking and strategy report."""

    best = summary_rows[0]
    worst = summary_rows[-1]

    print("\nWeek 11 BBO Analysis Report")
    print("=" * 76)
    print(f"Best function: {best['Function']}")
    print(f"Highest output: {best['Output']}")
    print(f"Lowest ranked function: {worst['Function']}")
    print(f"Lowest output: {worst['Output']}")

    print("\nWeek 11 ranking and comparison")
    print("-" * 76)

    for row in summary_rows:
        print(
            f"Rank {row['Rank']}: {row['Function']} | "
            f"Output = {row['Output']} | "
            f"Change = {row['Exact_Change']} | "
            f"{row['Direction']} | "
            f"Strategy = {row['Strategy']}"
        )

    print(
        f"\nAnalysis summary exported to: "
        f"{WEEK_11_SUMMARY_FILE.name}"
    )


def main() -> None:
    """Run the complete Week 11 analysis."""

    validate_inputs_file()
    week_10_results = read_results(WEEK_10_RESULTS_FILE)
    week_11_results = read_results(WEEK_11_RESULTS_FILE)
    summary_rows = build_summary(week_10_results, week_11_results)
    write_summary(summary_rows)
    print_summary_report(summary_rows)


if __name__ == "__main__":
    main()
