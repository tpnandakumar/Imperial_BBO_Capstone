"""Verified Week 12 analysis for the Imperial BBO Capstone.

This script evaluates the Week 12 outcomes and repeats the centred PCA used
in Week 11 with the additional Week 12 observation. PCA describes the
recorded query trajectory. It does not reveal the hidden objective function
and it does not select the Week 13 submission automatically.
"""

from __future__ import annotations

import csv
import importlib.util
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np

CURRENT_DIRECTORY = Path(__file__).resolve().parent
REPOSITORY_ROOT = CURRENT_DIRECTORY.parent
INPUT_FILE = CURRENT_DIRECTORY / "week_12_inputs.csv"
RESULT_FILE = CURRENT_DIRECTORY / "week_12_results.csv"
ANALYSIS_FILE = CURRENT_DIRECTORY / "week_12_analysis_summary.csv"
PCA_FILE = CURRENT_DIRECTORY / "week_12_pca_summary.csv"
WEEK_11_SCRIPT = REPOSITORY_ROOT / "Week_11" / "week_11_analysis.py"

FUNCTIONS = [f"Function {number}" for number in range(1, 9)]
EXPECTED_DIMENSIONS = dict(zip(FUNCTIONS, [2, 2, 3, 4, 4, 5, 6, 8]))

WEEK_12_INPUT_TEXT = {
    "Function 1": ("0.600000", "0.600000"),
    "Function 2": ("0.690000", "0.950000"),
    "Function 3": ("0.850000", "0.150000", "0.850000"),
    "Function 4": ("0.600000", "0.430000", "0.420000", "0.250000"),
    "Function 5": ("0.100000", "0.999000", "1.000000", "1.000000"),
    "Function 6": ("0.700000", "0.200000", "0.700000", "0.700000", "0.200000"),
    "Function 7": ("0.040000", "0.480000", "0.260000", "0.220000", "0.420000", "0.740000"),
    "Function 8": ("0.060000", "0.070000", "0.030000", "0.040000", "0.410000", "0.820000", "0.500000", "0.910000"),
}

WEEK_12_OUTPUT_TEXT = {
    "Function 1": "0.025559285339829783",
    "Function 2": "0.7335252043269003",
    "Function 3": "-0.05985127532683556",
    "Function 4": "-4.359874926582439",
    "Function 5": "4427.343995806448",
    "Function 6": "-0.7078316130911375",
    "Function 7": "1.3809299933612855",
    "Function 8": "9.58024",
}


def load_week_11_module():
    spec = importlib.util.spec_from_file_location("week_11_analysis", WEEK_11_SCRIPT)
    if spec is None or spec.loader is None:
        raise ImportError("Unable to load Week_11/week_11_analysis.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def normalise_label(value: str) -> str:
    cleaned = value.strip()
    if cleaned.lower().startswith("function"):
        return f"Function {cleaned.lower().replace('function', '').strip()}"
    if cleaned.upper().startswith("F"):
        return f"Function {cleaned[1:].strip()}"
    raise ValueError(f"Unrecognised function label: {value}")


def read_csv_case_insensitive(path: Path) -> List[Dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            raise ValueError(f"{path.name} has no header")
        return [{key.lower(): value for key, value in row.items()} for row in reader]


def validate_source_files() -> None:
    inputs = read_csv_case_insensitive(INPUT_FILE)
    results = read_csv_case_insensitive(RESULT_FILE)
    if len(inputs) != 8 or len(results) != 8:
        raise ValueError("Week 12 input and result files must each contain eight rows")

    seen_inputs: Dict[str, Tuple[str, ...]] = {}
    for row in inputs:
        function = normalise_label(row["function"])
        values = tuple(value.strip() for value in row["input"].split(","))
        if len(values) != EXPECTED_DIMENSIONS[function]:
            raise ValueError(f"Incorrect dimension for {function}")
        for value in values:
            try:
                number = Decimal(value)
            except InvalidOperation as error:
                raise ValueError(f"Invalid coordinate for {function}: {value}") from error
            if not Decimal("0") <= number <= Decimal("1"):
                raise ValueError(f"Coordinate outside [0, 1] for {function}")
        seen_inputs[function] = values

    seen_results = {
        normalise_label(row["function"]): row["output"].strip() for row in results
    }
    for function in FUNCTIONS:
        if tuple(map(Decimal, seen_inputs[function])) != tuple(
            map(Decimal, WEEK_12_INPUT_TEXT[function])
        ):
            raise ValueError(f"Week 12 input mismatch for {function}")
        if Decimal(seen_results[function]) != Decimal(WEEK_12_OUTPUT_TEXT[function]):
            raise ValueError(f"Week 12 output mismatch for {function}")


def pca_for_matrix(matrix: np.ndarray):
    centred = matrix - matrix.mean(axis=0)
    _, singular_values, right_vectors = np.linalg.svd(centred, full_matrices=False)
    variances = singular_values ** 2 / (matrix.shape[0] - 1)
    ratios = variances / variances.sum()
    cumulative = np.cumsum(ratios)
    components_90 = int(np.searchsorted(cumulative, 0.90) + 1)
    return ratios, cumulative, right_vectors, components_90


def pairwise_coordinate_correlation(matrix: np.ndarray) -> float:
    correlations = np.corrcoef(matrix, rowvar=False)
    upper = np.abs(correlations[np.triu_indices_from(correlations, k=1)])
    finite = upper[np.isfinite(upper)]
    return float(finite.max()) if finite.size else 0.0


def build_outputs(week_11):
    analysis_rows: List[Dict[str, str]] = []
    pca_rows: List[Dict[str, str]] = []

    for function in FUNCTIONS:
        week_11_output = Decimal(week_11.WEEKLY_OUTPUT_TEXT[11][function])
        week_12_output = Decimal(WEEK_12_OUTPUT_TEXT[function])
        change = week_12_output - week_11_output
        historical_outputs = [
            Decimal(week_11.WEEKLY_OUTPUT_TEXT[week][function])
            for week in range(1, 12)
        ]
        previous_best = max(historical_outputs)
        status = (
            "New verified best" if week_12_output > previous_best
            else "Matched prior verified best" if week_12_output == previous_best
            else "Below prior verified best"
        )
        analysis_rows.append({
            "Function": function,
            "Week_11_Output": str(week_11_output),
            "Week_12_Output": str(week_12_output),
            "Exact_Change": str(change),
            "Direction": "Improved" if change > 0 else "Declined" if change < 0 else "Unchanged",
            "Previous_Best_Output": str(previous_best),
            "Week_12_Best_Status": status,
            "Week_13_Status": "Not selected pending new course strategy",
        })

        if EXPECTED_DIMENSIONS[function] <= 2:
            continue

        matrix_11 = np.array([
            [float(Decimal(value)) for value in week_11.WEEKLY_INPUT_TEXT[week][function]]
            for week in range(1, 12)
        ])
        matrix_12 = np.vstack([
            matrix_11,
            np.array([float(Decimal(value)) for value in WEEK_12_INPUT_TEXT[function]])
        ])
        ratios_11, cumulative_11, _, components_11 = pca_for_matrix(matrix_11)
        ratios_12, cumulative_12, vectors_12, components_12 = pca_for_matrix(matrix_12)
        loadings = vectors_12[0]
        dominant_coordinate = int(np.argmax(np.abs(loadings))) + 1
        pca_rows.append({
            "Function": function,
            "Observations": "12",
            "Dimensions": str(EXPECTED_DIMENSIONS[function]),
            "Week_11_PC1_Ratio": repr(float(ratios_11[0])),
            "Week_12_PC1_Ratio": repr(float(ratios_12[0])),
            "Week_12_PC1_PC2_Cumulative": repr(float(cumulative_12[1])),
            "Week_11_Components_90pct": str(components_11),
            "Week_12_Components_90pct": str(components_12),
            "Dominant_PC1_Coordinate": f"x{dominant_coordinate}",
            "Dominant_PC1_Loading": repr(float(loadings[dominant_coordinate - 1])),
            "Maximum_Absolute_Coordinate_Correlation": repr(
                pairwise_coordinate_correlation(matrix_12)
            ),
            "Interpretation_Limit": "Query trajectory only, not hidden objective dimensionality",
        })

    return analysis_rows, pca_rows


def write_csv(path: Path, rows: List[Dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    validate_source_files()
    week_11 = load_week_11_module()
    analysis_rows, pca_rows = build_outputs(week_11)
    write_csv(ANALYSIS_FILE, analysis_rows)
    write_csv(PCA_FILE, pca_rows)
    print("Week 12 validation and PCA analysis complete")
    print("Week 13 remains unselected pending the next course strategy")


if __name__ == "__main__":
    main()
