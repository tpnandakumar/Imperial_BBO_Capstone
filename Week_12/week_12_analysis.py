"""Verified Week 12 analysis for the Imperial BBO Capstone.

The script validates the authoritative Week 12 input and result files,
compares the round with the complete verified Weeks 1 to 11 history, and
updates PCA summaries for Functions 3 to 8. Source strings are preserved
exactly. Decimal arithmetic is used for exact comparisons and query movement.
"""

from __future__ import annotations

import csv
import importlib.util
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Dict, List, Sequence, Tuple

import numpy as np

CURRENT_DIRECTORY = Path(__file__).resolve().parent
REPOSITORY_ROOT = CURRENT_DIRECTORY.parent
INPUT_FILE = CURRENT_DIRECTORY / "week_12_inputs.csv"
RESULT_FILE = CURRENT_DIRECTORY / "week_12_results.csv"
ANALYSIS_FILE = CURRENT_DIRECTORY / "week_12_analysis_summary.csv"
FIGURE_DATA_FILE = CURRENT_DIRECTORY / "week_12_figure_data_summary.csv"
WEEK_11_SCRIPT = REPOSITORY_ROOT / "Week_11" / "week_11_analysis.py"

FUNCTIONS = [f"Function {number}" for number in range(1, 9)]
EXPECTED_DIMENSIONS = dict(zip(FUNCTIONS, [2, 2, 3, 4, 4, 5, 6, 8]))

AUTHORITATIVE_WEEK_12_INPUTS: Dict[str, Tuple[str, ...]] = {
    "Function 1": ("0.600000", "0.600000"),
    "Function 2": ("0.690000", "0.950000"),
    "Function 3": ("0.850000", "0.150000", "0.850000"),
    "Function 4": ("0.600000", "0.430000", "0.420000", "0.250000"),
    "Function 5": ("0.100000", "0.999000", "1.000000", "1.000000"),
    "Function 6": ("0.700000", "0.200000", "0.700000", "0.700000", "0.200000"),
    "Function 7": ("0.040000", "0.480000", "0.260000", "0.220000", "0.420000", "0.740000"),
    "Function 8": ("0.060000", "0.070000", "0.030000", "0.040000", "0.410000", "0.820000", "0.500000", "0.910000"),
}

AUTHORITATIVE_WEEK_12_OUTPUTS: Dict[str, str] = {
    "Function 1": "0.025559285339829783",
    "Function 2": "0.7335252043269003",
    "Function 3": "-0.05985127532683556",
    "Function 4": "-4.359874926582439",
    "Function 5": "4427.343995806448",
    "Function 6": "-0.7078316130911375",
    "Function 7": "1.3809299933612855",
    "Function 8": "9.58024",
}

OBSERVED_ACTION = {
    "Function 1": "Repeated the Week 11 coordinate",
    "Function 2": "Small local move from Week 11",
    "Function 3": "Returned to the Week 4 coordinate",
    "Function 4": "Returned to the Week 1 coordinate",
    "Function 5": "Continued a small boundary movement",
    "Function 6": "Returned to the Week 3 coordinate",
    "Function 7": "Returned to the Week 5 coordinate",
    "Function 8": "Repeated the Week 11 coordinate",
}


def load_week_11_module():
    """Load the verified Weeks 1 to 11 history from the Week 11 analysis file."""

    spec = importlib.util.spec_from_file_location("week_11_analysis", WEEK_11_SCRIPT)
    if spec is None or spec.loader is None:
        raise ImportError("Unable to load Week_11/week_11_analysis.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def normalise_label(value: str) -> str:
    """Normalise F1 and Function 1 style labels."""

    cleaned = value.strip()
    if cleaned.lower().startswith("function"):
        number = cleaned.lower().replace("function", "").strip()
        return f"Function {number}"
    if cleaned.upper().startswith("F"):
        return f"Function {cleaned[1:].strip()}"
    raise ValueError(f"Unrecognised function label: {value}")


def read_csv_case_insensitive(path: Path) -> List[Dict[str, str]]:
    """Read a CSV while normalising only the column names."""

    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            raise ValueError(f"{path.name} has no header")
        return [
            {key.lower(): value for key, value in row.items()}
            for row in reader
        ]


def validate_source_files() -> None:
    """Validate all Week 12 source strings, dimensions and bounds."""

    inputs = read_csv_case_insensitive(INPUT_FILE)
    results = read_csv_case_insensitive(RESULT_FILE)

    if len(inputs) != 8 or len(results) != 8:
        raise ValueError("Week 12 input and result files must each contain eight rows")

    input_map: Dict[str, Tuple[str, ...]] = {}
    for row in inputs:
        function = normalise_label(row["function"])
        if function in input_map:
            raise ValueError(f"Duplicate input row for {function}")
        values = tuple(value.strip() for value in row["input"].split(","))
        if len(values) != EXPECTED_DIMENSIONS[function]:
            raise ValueError(f"Incorrect dimension for {function}")
        for value_text in values:
            try:
                value = Decimal(value_text)
            except InvalidOperation as error:
                raise ValueError(f"Invalid coordinate for {function}: {value_text}") from error
            if not Decimal("0") <= value <= Decimal("1"):
                raise ValueError(f"Coordinate outside [0, 1] for {function}: {value_text}")
        input_map[function] = values

    result_map: Dict[str, str] = {}
    for row in results:
        function = normalise_label(row["function"])
        if function in result_map:
            raise ValueError(f"Duplicate result row for {function}")
        output_text = row["output"].strip()
        try:
            Decimal(output_text)
        except InvalidOperation as error:
            raise ValueError(f"Invalid output for {function}: {output_text}") from error
        result_map[function] = output_text

    if set(input_map) != set(FUNCTIONS) or set(result_map) != set(FUNCTIONS):
        raise ValueError("Week 12 source files must contain Functions 1 to 8 exactly once")

    for function in FUNCTIONS:
        if input_map[function] != AUTHORITATIVE_WEEK_12_INPUTS[function]:
            raise ValueError(f"Week 12 input string mismatch for {function}")
        if result_map[function] != AUTHORITATIVE_WEEK_12_OUTPUTS[function]:
            raise ValueError(f"Week 12 output string mismatch for {function}")


def format_decimal(value: Decimal) -> str:
    """Format an exact Decimal while displaying exact zero as 0."""

    return "0" if value == 0 else str(value)


def exact_squared_distance(
    left: Sequence[str],
    right: Sequence[str],
) -> str:
    """Return the exact squared Euclidean distance between two query vectors."""

    if len(left) != len(right):
        raise ValueError("Query vectors have different dimensions")
    distance = sum(
        (Decimal(a) - Decimal(b)) ** 2
        for a, b in zip(left, right)
    )
    return format_decimal(distance)


def pca_for_matrix(matrix: np.ndarray):
    """Return centred PCA metrics using singular value decomposition."""

    centred = matrix - matrix.mean(axis=0)
    _, singular_values, right_vectors = np.linalg.svd(
        centred,
        full_matrices=False,
    )
    variances = singular_values ** 2 / (matrix.shape[0] - 1)
    ratios = variances / variances.sum()
    cumulative = np.cumsum(ratios)
    components_90 = int(np.searchsorted(cumulative, 0.90) + 1)
    return ratios, cumulative, right_vectors, components_90


def maximum_absolute_coordinate_correlation(matrix: np.ndarray) -> float:
    """Return the largest finite absolute pairwise coordinate correlation."""

    correlations = np.corrcoef(matrix, rowvar=False)
    upper = np.abs(correlations[np.triu_indices_from(correlations, k=1)])
    finite = upper[np.isfinite(upper)]
    return float(finite.max()) if finite.size else 0.0


def previous_best_record(week_11, function: str) -> Tuple[str, str]:
    """Return the strongest Weeks 1 to 11 output and every week that matched it."""

    values = [
        Decimal(week_11.WEEKLY_OUTPUT_TEXT[week][function])
        for week in range(1, 12)
    ]
    best = max(values)
    weeks = [
        str(week)
        for week in range(1, 12)
        if Decimal(week_11.WEEKLY_OUTPUT_TEXT[week][function]) == best
    ]
    return str(best), "|".join(weeks)


def best_status(week_12_output: Decimal, previous_best: Decimal) -> str:
    """Classify Week 12 against the verified Weeks 1 to 11 best."""

    if week_12_output > previous_best:
        return "New verified best"
    if week_12_output == previous_best:
        return "Matched prior verified best"
    return "Below prior verified best"


def build_analysis_rows(week_11) -> List[Dict[str, str]]:
    """Build the exact Week 12 outcome summary."""

    rows: List[Dict[str, str]] = []

    for function in FUNCTIONS:
        week_11_input = week_11.WEEKLY_INPUT_TEXT[11][function]
        week_12_input = AUTHORITATIVE_WEEK_12_INPUTS[function]
        week_11_output_text = week_11.WEEKLY_OUTPUT_TEXT[11][function]
        week_12_output_text = AUTHORITATIVE_WEEK_12_OUTPUTS[function]

        week_11_output = Decimal(week_11_output_text)
        week_12_output = Decimal(week_12_output_text)
        change = week_12_output - week_11_output
        previous_best_text, previous_best_weeks = previous_best_record(
            week_11,
            function,
        )
        previous_best = Decimal(previous_best_text)

        rows.append({
            "Function": function,
            "Week_11_Input": ",".join(week_11_input),
            "Week_12_Input": ",".join(week_12_input),
            "Week_11_Output": week_11_output_text,
            "Week_12_Output": week_12_output_text,
            "Exact_Change": format_decimal(change),
            "Direction": (
                "Improved" if change > 0
                else "Declined" if change < 0
                else "Unchanged"
            ),
            "Exact_Squared_Query_Distance": exact_squared_distance(
                week_11_input,
                week_12_input,
            ),
            "Previous_Best_Output": previous_best_text,
            "Previous_Best_Weeks": previous_best_weeks,
            "Week_12_Best_Status": best_status(week_12_output, previous_best),
            "Observed_Action": OBSERVED_ACTION[function],
            "Week_13_Status": "Not selected",
        })

    return rows


def build_figure_rows(week_11, analysis_rows: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """Build plotting data and PCA metrics from the verified query history."""

    analysis_map = {row["Function"]: row for row in analysis_rows}
    rows: List[Dict[str, str]] = []

    for function in FUNCTIONS:
        base = analysis_map[function]
        figure_row = {
            "Function": function,
            "Week_11_Output": base["Week_11_Output"],
            "Week_12_Output": base["Week_12_Output"],
            "Exact_Change": base["Exact_Change"],
            "Exact_Squared_Query_Distance": base["Exact_Squared_Query_Distance"],
            "PC1_Ratio_Weeks_01_to_11": "",
            "PC1_Ratio_Weeks_01_to_12": "",
            "PC1_PC2_Cumulative_Weeks_01_to_12": "",
            "Components_90pct_Weeks_01_to_11": "",
            "Components_90pct_Weeks_01_to_12": "",
            "Dominant_PC1_Coordinate_Weeks_01_to_12": "",
            "Dominant_PC1_Loading_Weeks_01_to_12": "",
            "Maximum_Absolute_Coordinate_Correlation_Weeks_01_to_12": "",
            "Interpretation_Limit": "Direct two dimensional geometry used; PCA not required",
        }

        if EXPECTED_DIMENSIONS[function] > 2:
            matrix_11 = np.array([
                [
                    float(Decimal(value))
                    for value in week_11.WEEKLY_INPUT_TEXT[week][function]
                ]
                for week in range(1, 12)
            ])
            matrix_12 = np.vstack([
                matrix_11,
                np.array([
                    float(Decimal(value))
                    for value in AUTHORITATIVE_WEEK_12_INPUTS[function]
                ]),
            ])

            ratios_11, _, _, components_11 = pca_for_matrix(matrix_11)
            ratios_12, cumulative_12, vectors_12, components_12 = pca_for_matrix(
                matrix_12
            )
            dominant_index = int(np.argmax(np.abs(vectors_12[0])))

            figure_row.update({
                "PC1_Ratio_Weeks_01_to_11": repr(float(ratios_11[0])),
                "PC1_Ratio_Weeks_01_to_12": repr(float(ratios_12[0])),
                "PC1_PC2_Cumulative_Weeks_01_to_12": repr(
                    float(cumulative_12[1])
                ),
                "Components_90pct_Weeks_01_to_11": str(components_11),
                "Components_90pct_Weeks_01_to_12": str(components_12),
                "Dominant_PC1_Coordinate_Weeks_01_to_12": f"x{dominant_index + 1}",
                "Dominant_PC1_Loading_Weeks_01_to_12": repr(
                    float(vectors_12[0][dominant_index])
                ),
                "Maximum_Absolute_Coordinate_Correlation_Weeks_01_to_12": repr(
                    maximum_absolute_coordinate_correlation(matrix_12)
                ),
                "Interpretation_Limit": (
                    "Query trajectory only; not hidden objective dimensionality"
                ),
            })

        rows.append(figure_row)

    return rows


def write_csv(path: Path, rows: List[Dict[str, str]]) -> None:
    """Write a derived CSV using the supplied field order."""

    if not rows:
        raise ValueError(f"No rows available for {path.name}")
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    """Run the complete verified Week 12 analysis."""

    validate_source_files()
    week_11 = load_week_11_module()
    analysis_rows = build_analysis_rows(week_11)
    figure_rows = build_figure_rows(week_11, analysis_rows)
    write_csv(ANALYSIS_FILE, analysis_rows)
    write_csv(FIGURE_DATA_FILE, figure_rows)
    print("Week 12 source validation complete")
    print("Week 12 analysis and figure data summaries updated")
    print("Week 13 remains unselected")


if __name__ == "__main__":
    main()
