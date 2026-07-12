"""
Week 09 Analysis Tool
Imperial BBO Capstone

This script reads the Week 09 optimisation results, ranks the eight
objective functions, assigns optimisation strategies, classifies each
result and exports week_09_analysis_summary.csv.

All numerical values are preserved exactly as stored in the CSV files.
No rounding or truncation is applied.
"""

from __future__ import annotations

import csv
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Dict, List


CURRENT_DIRECTORY = Path(__file__).resolve().parent

WEEK_09_INPUTS_FILE = CURRENT_DIRECTORY / "week_09_inputs.csv"
WEEK_09_RESULTS_FILE = CURRENT_DIRECTORY / "week_09_results.csv"
WEEK_09_SUMMARY_FILE = CURRENT_DIRECTORY / "week_09_analysis_summary.csv"

WEEK_08_RESULTS_FILE = (
    CURRENT_DIRECTORY.parent / "Week_08" / "week_08_results.csv"
)


STRATEGY = {
    "Function 1": "Explore",
    "Function 2": "Refine",
    "Function 3": "Reassess",
    "Function 4": "Refine",
    "Function 5": "Exploit",
    "Function 6": "Reassess",
    "Function 7": "Refine",
    "Function 8": "Refine",
}


NEAR_ZERO_THRESHOLD = Decimal("1e-12")


def normalise_function_name(value: str) -> str:
    """
    Convert labels such as F1 or Function 1 into Function 1.
    """

    cleaned = value.strip()

    if cleaned.lower().startswith("function"):
        number = cleaned.lower().replace("function", "").strip()
        return f"Function {number}"

    if cleaned.upper().startswith("F"):
        number = cleaned[1:].strip()
        return f"Function {number}"

    raise ValueError(f"Unrecognised function label: {value}")


def read_results(file_path: Path) -> Dict[str, Dict[str, object]]:
    """
    Read a results CSV while preserving the original output strings.

    Expected columns:
        Function,Output
    """

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
                f"'Function' and 'Output'."
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

            results[function_name] = {
                "output_text": output_text,
                "output_decimal": output_decimal,
            }

    expected_functions = {
        f"Function {number}" for number in range(1, 9)
    }

    missing_functions = expected_functions.difference(results)

    if missing_functions:
        missing = ", ".join(sorted(missing_functions))
        raise ValueError(
            f"{file_path.name} is missing these functions: {missing}"
        )

    return results


def validate_inputs_file() -> None:
    """
    Confirm that the Week 09 inputs file exists and contains eight rows.
    """

    if not WEEK_09_INPUTS_FILE.exists():
        raise FileNotFoundError(
            f"Input file not found: {WEEK_09_INPUTS_FILE}"
        )

    with WEEK_09_INPUTS_FILE.open(
        "r",
        encoding="utf-8-sig",
        newline="",
    ) as csv_file:
        reader = csv.DictReader(csv_file)

        if reader.fieldnames is None:
            raise ValueError(
                f"No CSV header found in {WEEK_09_INPUTS_FILE.name}"
            )

        required_columns = {"Function", "Input"}

        if not required_columns.issubset(set(reader.fieldnames)):
            raise ValueError(
                f"{WEEK_09_INPUTS_FILE.name} must contain the columns "
                f"'Function' and 'Input'."
            )

        rows = list(reader)

    if len(rows) != 8:
        raise ValueError(
            f"{WEEK_09_INPUTS_FILE.name} should contain 8 functions, "
            f"but contains {len(rows)}."
        )


def classify_status(output: Decimal) -> str:
    """
    Classify an output as Positive, Negative or Near Zero.
    """

    if abs(output) < NEAR_ZERO_THRESHOLD:
        return "Near Zero"

    if output > 0:
        return "Positive"

    return "Negative"


def build_summary(
    week_09_results: Dict[str, Dict[str, object]]
) -> List[Dict[str, object]]:
    """
    Rank Week 09 functions and build the summary rows.
    """

    ranked_functions = sorted(
        week_09_results.items(),
        key=lambda item: item[1]["output_decimal"],
        reverse=True,
    )

    summary_rows: List[Dict[str, object]] = []

    for rank, (function_name, values) in enumerate(
        ranked_functions,
        start=1,
    ):
        output_decimal = values["output_decimal"]

        summary_rows.append(
            {
                "Function": function_name,
                "Output": values["output_text"],
                "Rank": rank,
                "Strategy": STRATEGY[function_name],
                "Status": classify_status(output_decimal),
            }
        )

    return summary_rows


def write_summary(summary_rows: List[Dict[str, object]]) -> None:
    """
    Export the Week 09 analysis summary without altering output values.
    """

    fieldnames = [
        "Function",
        "Output",
        "Rank",
        "Strategy",
        "Status",
    ]

    with WEEK_09_SUMMARY_FILE.open(
        "w",
        encoding="utf-8",
        newline="",
    ) as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(summary_rows)


def calculate_weekly_changes(
    week_08_results: Dict[str, Dict[str, object]],
    week_09_results: Dict[str, Dict[str, object]],
) -> List[Dict[str, object]]:
    """
    Calculate exact Week 08 to Week 09 changes using Decimal arithmetic.
    """

    comparison_rows: List[Dict[str, object]] = []

    for number in range(1, 9):
        function_name = f"Function {number}"

        week_08_value = week_08_results[function_name][
            "output_decimal"
        ]
        week_09_value = week_09_results[function_name][
            "output_decimal"
        ]

        change = week_09_value - week_08_value

        if change > 0:
            direction = "Improved"
        elif change < 0:
            direction = "Declined"
        else:
            direction = "Unchanged"

        comparison_rows.append(
            {
                "Function": function_name,
                "Week_08_Output": week_08_results[function_name][
                    "output_text"
                ],
                "Week_09_Output": week_09_results[function_name][
                    "output_text"
                ],
                "Exact_Change": str(change),
                "Direction": direction,
            }
        )

    return comparison_rows


def print_summary_report(
    summary_rows: List[Dict[str, object]],
    comparison_rows: List[Dict[str, object]] | None,
) -> None:
    """
    Print the Week 09 ranking and strategy report.
    """

    best = summary_rows[0]
    worst = summary_rows[-1]

    print("\nWeek 09 BBO Analysis Report")
    print("=" * 72)

    print(f"Best function: {best['Function']}")
    print(f"Highest output: {best['Output']}")
    print(f"Worst function: {worst['Function']}")
    print(f"Lowest output: {worst['Output']}")

    print("\nWeek 09 ranking")
    print("-" * 72)

    for row in summary_rows:
        print(
            f"Rank {row['Rank']}: "
            f"{row['Function']} | "
            f"Output = {row['Output']} | "
            f"Strategy = {row['Strategy']} | "
            f"Status = {row['Status']}"
        )

    print("\nStrategy allocation")
    print("-" * 72)
    print("Exploit: Function 5")
    print("Refine: Functions 2, 4, 7 and 8")
    print("Reassess: Functions 3 and 6")
    print("Explore: Function 1")

    if comparison_rows is not None:
        print("\nWeek 08 to Week 09 comparison")
        print("-" * 72)

        for row in comparison_rows:
            print(
                f"{row['Function']}: "
                f"{row['Week_08_Output']} to "
                f"{row['Week_09_Output']} | "
                f"Change = {row['Exact_Change']} | "
                f"{row['Direction']}"
            )

    print(
        f"\nAnalysis summary exported to: "
        f"{WEEK_09_SUMMARY_FILE.name}"
    )


def main() -> None:
    """
    Run the complete Week 09 analysis.
    """

    validate_inputs_file()

    week_09_results = read_results(WEEK_09_RESULTS_FILE)
    summary_rows = build_summary(week_09_results)
    write_summary(summary_rows)

    comparison_rows = None

    if WEEK_08_RESULTS_FILE.exists():
        week_08_results = read_results(WEEK_08_RESULTS_FILE)
        comparison_rows = calculate_weekly_changes(
            week_08_results,
            week_09_results,
        )
    else:
        print(
            f"Warning: {WEEK_08_RESULTS_FILE} was not found. "
            "The Week 08 to Week 09 comparison was skipped."
        )

    print_summary_report(summary_rows, comparison_rows)


if __name__ == "__main__":
    main()
