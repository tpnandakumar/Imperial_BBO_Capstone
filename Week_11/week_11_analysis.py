"""Week 11 analysis for the Imperial BBO Capstone.

Clustering belongs to Week 10, where it informed the Week 11 queries.
This script evaluates those outcomes and adds exploratory PCA as preparation
for the later Week 12 decision. Verified source values remain as strings or
Decimal values wherever exact arithmetic is possible.
"""

from __future__ import annotations

import csv
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Dict, List, Sequence, Tuple

import numpy as np

CURRENT_DIRECTORY = Path(__file__).resolve().parent
WEEK_11_INPUTS_FILE = CURRENT_DIRECTORY / "week_11_inputs.csv"
WEEK_11_RESULTS_FILE = CURRENT_DIRECTORY / "week_11_results.csv"
WEEK_11_SUMMARY_FILE = CURRENT_DIRECTORY / "week_11_analysis_summary.csv"
WEEK_10_RESULTS_FILE = CURRENT_DIRECTORY.parent / "Week_10" / "week_10_results.csv"

FUNCTIONS = [f"Function {number}" for number in range(1, 9)]
EXPECTED_DIMENSIONS = dict(zip(FUNCTIONS, [2, 2, 3, 4, 4, 5, 6, 8]))

WEEK_11_ACTION = {
    "Function 1": "Recover confirmed narrow peak",
    "Function 2": "Local cluster refinement",
    "Function 3": "Recovery towards stronger historical region",
    "Function 4": "Recovery towards stronger historical region",
    "Function 5": "Boundary cluster refinement",
    "Function 6": "Recovery towards stronger historical basin",
    "Function 7": "Compact positive cluster refinement",
    "Function 8": "Recover confirmed historical best",
}

CLUSTERING_OUTCOME = {
    "Function 1": "Repeatability confirmed at the prior best point",
    "Function 2": "Emerging positive local region strengthened",
    "Function 3": "Recovery towards the stronger historical region was supported",
    "Function 4": "Recovery towards the stronger historical region was supported",
    "Function 5": "Boundary region strengthened and produced a new best",
    "Function 6": "Recovery towards the stronger historical basin was supported",
    "Function 7": "Compact positive region remained productive",
    "Function 8": "Repeatability confirmed at the prior best point",
}

# Complete verified history supplied with the Week 11 package.
INPUT_ROWS: Dict[int, List[str]] = {
    1: ["0.74,0.74", "0.72,0.94", "0.53,0.64,0.25", "0.6,0.43,0.42,0.25", "0.21,0.87,0.9,0.9", "0.75,0.18,0.7,0.72,0.04", "0.05,0.5,0.25,0.22,0.42,0.74", "0.06,0.07,0.03,0.04,0.41,0.82,0.5,0.91"],
    2: ["0.3,0.3", "0.76,0.9", "0.75,0.25,0.75", "0.2,0.8,0.8,0.8", "0.18,0.9,0.95,0.95", "0.25,0.75,0.3,0.3,0.8", "0.08,0.55,0.3,0.25,0.45,0.78", "0.08,0.08,0.05,0.05,0.45,0.85,0.55,0.95"],
    3: ["0.6,0.6", "0.8,0.92", "0.2,0.8,0.2", "0.8,0.2,0.2,0.2", "0.17,0.92,0.97,0.97", "0.7,0.2,0.7,0.7,0.2", "0.1,0.58,0.32,0.27,0.47,0.8", "0.04,0.04,0.04,0.04,0.47,0.88,0.58,0.97"],
    4: ["0.7,0.7", "0.68,0.96", "0.85,0.15,0.85", "0.9,0.1,0.1,0.1", "0.16,0.94,0.98,0.98", "0.8,0.15,0.8,0.8,0.15", "0.06,0.52,0.28,0.24,0.44,0.76", "0.07,0.07,0.05,0.05,0.44,0.84,0.54,0.94"],
    5: ["0.45,0.45", "0.64,0.98", "0.9,0.1,0.9", "0.95,0.05,0.05,0.05", "0.15,0.96,0.99,0.99", "0.9,0.1,0.9,0.9,0.1", "0.04,0.48,0.26,0.22,0.42,0.74", "0.06,0.06,0.05,0.05,0.43,0.85,0.55,0.95"],
    6: ["0.5,0.5", "0.7,0.95", "0.95,0.05,0.95", "0.98,0.02,0.02,0.02", "0.14,0.97,0.995,0.995", "0.95,0.05,0.95,0.95,0.05", "0.05,0.5,0.25,0.2,0.4,0.75", "0.05,0.05,0.05,0.05,0.45,0.85,0.55,0.95"],
    7: ["0.35,0.7", "0.76,0.985", "0.25,0.85,0.3", "0.3,0.7,0.65,0.25", "0.12,0.99,0.999,0.999", "0.25,0.75,0.25,0.8,0.3", "0.05,0.52,0.24,0.18,0.41,0.77", "0.05,0.05,0.05,0.05,0.46,0.86,0.56,0.98"],
    8: ["0.35,0.7", "0.72,0.94", "0.26,0.86,0.29", "0.32,0.72,0.68,0.22", "0.12,0.995,0.9995,0.9995", "0.24,0.76,0.24,0.82,0.28", "0.06,0.5,0.25,0.22,0.42,0.74", "0.05,0.05,0.05,0.05,0.47,0.87,0.57,0.98"],
    9: ["0.35,0.7", "0.725,0.945", "0.255,0.855,0.295", "0.31,0.71,0.67,0.23", "0.12,0.997,0.9998,0.9998", "0.24,0.76,0.24,0.82,0.28", "0.058,0.495,0.248,0.218,0.425,0.742", "0.05,0.05,0.05,0.05,0.468,0.872,0.572,0.982"],
    10: ["0.45,0.65", "0.7,0.955", "0.28,0.875,0.315", "0.29,0.73,0.69,0.21", "0.12,0.997,0.9998,0.9998", "0.26,0.78,0.26,0.84,0.3", "0.06,0.5,0.25,0.22,0.43,0.74", "0.05,0.05,0.05,0.05,0.47,0.875,0.575,0.985"],
    11: ["0.6,0.6", "0.695,0.95", "0.84,0.16,0.84", "0.62,0.42,0.44,0.25", "0.11,0.998,0.9999,0.9999", "0.72,0.19,0.7,0.71,0.15", "0.045,0.485,0.255,0.22,0.42,0.745", "0.06,0.07,0.03,0.04,0.41,0.82,0.5,0.91"],
}

OUTPUT_ROWS: Dict[int, List[str]] = {
    1: ["6.854713532414845e-19", "0.45494185399727516", "-0.10183633971746164", "-4.359874926582439", "1415.8763939603884", "-0.7001549808025808", "1.3199939052019112", "9.58024"],
    2: ["6.659572754640724e-23", "0.41213721316888097", "-0.1332555781557258", "-23.120154471959825", "2308.1487028593933", "-2.0702463923015775", "1.0696579739950232", "9.5241"],
    3: ["0.025559285339829783", "0.14098828808535324", "-0.12787021171886992", "-14.554028542475695", "2840.9903787629305", "-0.648848297397347", "0.8966026942687082", "9.44296"],
    4: ["1.4754580129542488e-07", "0.5228458934672892", "-0.06037987403160633", "-22.55187651826871", "3238.333368768757", "-0.8733671274789931", "1.1968303712356705", "9.539439999999999"],
    5: ["0.012779642669914939", "0.28016822307722516", "-0.11392206377710448", "-27.44051496086922", "3682.2110623386798", "-1.073875453695542", "1.3809299933612855", "9.5113"],
    6: ["2.6752879910742468e-09", "0.5712475315739602", "-0.3071823694141529", "-31.20347777578016", "3922.7652233497042", "-1.3792272680368016", "1.3529491169887171", "9.5148"],
    7: ["-1.4546199699251391e-58", "0.2399291698606551", "-0.09116928906376276", "-10.745961383135121", "4278.816638076986", "-1.119713499832813", "1.1543358123792982", "9.49476"],
    8: ["-1.4546199699251391e-58", "0.5672775862793291", "-0.0991107637427902", "-12.305008897187289", "4359.384134322703", "-1.1197178425911847", "1.3346391663186332", "9.47621"],
    9: ["-1.4546199699251391e-58", "0.47297842839949866", "-0.1156707106126581", "-11.788939969158545", "4394.868042481448", "-1.1733030029888645", "1.314307996450604", "9.4709436"],
    10: ["2.8950706668499033e-23", "0.5311818841205426", "-0.08697581687486715", "-13.483642655031158", "4394.868042481448", "-1.2283806967341901", "1.285160161342515", "9.4646525"],
    11: ["0.025559285339829783", "0.5848554940277205", "-0.06542982421105416", "-4.868852987697114", "4411.0387356061765", "-0.7268715077444687", "1.3579108517237013", "9.58024"],
}

WEEKLY_INPUT_TEXT = {
    week: {function: tuple(row.split(",")) for function, row in zip(FUNCTIONS, rows)}
    for week, rows in INPUT_ROWS.items()
}
WEEKLY_OUTPUT_TEXT = {
    week: dict(zip(FUNCTIONS, rows)) for week, rows in OUTPUT_ROWS.items()
}


def normalise_function_name(value: str) -> str:
    cleaned = value.strip()
    if cleaned.lower().startswith("function"):
        return f"Function {cleaned.lower().replace('function', '').strip()}"
    if cleaned.upper().startswith("F"):
        return f"Function {cleaned[1:].strip()}"
    raise ValueError(f"Unrecognised function label: {value}")


def read_inputs(file_path: Path) -> Dict[str, Tuple[str, ...]]:
    inputs: Dict[str, Tuple[str, ...]] = {}
    with file_path.open("r", encoding="utf-8-sig", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        if reader.fieldnames is None or not {"Function", "Input"}.issubset(reader.fieldnames):
            raise ValueError(f"{file_path.name} must contain Function and Input columns")
        for row in reader:
            function = normalise_function_name(row["Function"])
            if function in inputs:
                raise ValueError(f"Duplicate input row for {function}")
            inputs[function] = tuple(value.strip() for value in row["Input"].split(","))

    if set(inputs) != set(FUNCTIONS):
        raise ValueError(f"{file_path.name} must contain Functions 1 to 8")
    for function, values in inputs.items():
        if len(values) != EXPECTED_DIMENSIONS[function]:
            raise ValueError(f"Incorrect dimension for {function}")
        for text in values:
            try:
                value = Decimal(text)
            except InvalidOperation as error:
                raise ValueError(f"Invalid input for {function}: {text}") from error
            if not Decimal("0") <= value <= Decimal("1"):
                raise ValueError(f"Input outside [0, 1] for {function}: {text}")
    return inputs


def read_results(file_path: Path) -> Dict[str, str]:
    results: Dict[str, str] = {}
    with file_path.open("r", encoding="utf-8-sig", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        if reader.fieldnames is None or not {"Function", "Output"}.issubset(reader.fieldnames):
            raise ValueError(f"{file_path.name} must contain Function and Output columns")
        for row in reader:
            function = normalise_function_name(row["Function"])
            if function in results:
                raise ValueError(f"Duplicate result row for {function}")
            text = row["Output"].strip()
            try:
                Decimal(text)
            except InvalidOperation as error:
                raise ValueError(f"Invalid output for {function}: {text}") from error
            results[function] = text
    if set(results) != set(FUNCTIONS):
        raise ValueError(f"{file_path.name} must contain Functions 1 to 8")
    return results


def validate_week_11(inputs: Dict[str, Tuple[str, ...]], results: Dict[str, str]) -> None:
    for function in FUNCTIONS:
        stored_input = tuple(Decimal(value) for value in inputs[function])
        verified_input = tuple(Decimal(value) for value in WEEKLY_INPUT_TEXT[11][function])
        if stored_input != verified_input:
            raise ValueError(f"Week 11 input mismatch for {function}")
        if Decimal(results[function]) != Decimal(WEEKLY_OUTPUT_TEXT[11][function]):
            raise ValueError(f"Week 11 output mismatch for {function}")


def prior_best(function: str) -> Tuple[int, str, Tuple[str, ...]]:
    week = max(range(1, 11), key=lambda number: Decimal(WEEKLY_OUTPUT_TEXT[number][function]))
    return week, WEEKLY_OUTPUT_TEXT[week][function], WEEKLY_INPUT_TEXT[week][function]


def squared_distance_exact(first: Sequence[str], second: Sequence[str]) -> str:
    total = sum((Decimal(a) - Decimal(b)) ** 2 for a, b in zip(first, second))
    return str(total)


def pca_metrics(function: str) -> Tuple[str, str, str, str]:
    if EXPECTED_DIMENSIONS[function] <= 2:
        return "Not applied, direct two dimensional geometry retained", "", "", ""

    matrix = np.array([
        [float(Decimal(value)) for value in WEEKLY_INPUT_TEXT[week][function]]
        for week in range(1, 12)
    ])
    centred = matrix - matrix.mean(axis=0)
    _, singular_values, _ = np.linalg.svd(centred, full_matrices=False)
    explained = (singular_values ** 2) / (matrix.shape[0] - 1)
    ratio = explained / explained.sum()
    cumulative = np.cumsum(ratio)
    components_90 = int(np.searchsorted(cumulative, 0.90) + 1)
    return (
        "Exploratory centred PCA on Weeks 1 to 11 inputs",
        repr(float(ratio[0])),
        repr(float(cumulative[1])),
        str(components_90),
    )


def build_summary(week_10_results: Dict[str, str]) -> List[Dict[str, str]]:
    ranked = sorted(FUNCTIONS, key=lambda name: Decimal(WEEKLY_OUTPUT_TEXT[11][name]), reverse=True)
    rank = {function: index for index, function in enumerate(ranked, start=1)}
    rows: List[Dict[str, str]] = []

    for function in FUNCTIONS:
        week_10 = week_10_results[function]
        week_11 = WEEKLY_OUTPUT_TEXT[11][function]
        change = Decimal(week_11) - Decimal(week_10)
        best_week, best_output, best_input = prior_best(function)
        current = Decimal(week_11)
        previous = Decimal(best_output)
        best_status = (
            "New verified best" if current > previous
            else "Matched prior verified best" if current == previous
            else "Below prior verified best"
        )
        pca_status, pc1, pc12, components_90 = pca_metrics(function)
        rows.append({
            "Function": function,
            "Week_11_Output": week_11,
            "Week_11_Rank": str(rank[function]),
            "Week_10_Output": week_10,
            "Exact_Change": str(change),
            "Direction": "Improved" if change > 0 else "Declined" if change < 0 else "Unchanged",
            "Week_10_Clustering_Informed_Action": WEEK_11_ACTION[function],
            "Clustering_Outcome": CLUSTERING_OUTCOME[function],
            "Prior_Best_Week": str(best_week),
            "Prior_Best_Output": best_output,
            "Exact_Squared_Distance_To_Prior_Best_Input": squared_distance_exact(WEEKLY_INPUT_TEXT[11][function], best_input),
            "Week_11_Best_Status": best_status,
            "PCA_Status": pca_status,
            "PCA_PC1_Explained_Variance_Ratio": pc1,
            "PCA_PC1_PC2_Cumulative_Ratio": pc12,
            "PCA_Components_To_Reach_90pct": components_90,
        })
    return rows


def main() -> None:
    week_11_inputs = read_inputs(WEEK_11_INPUTS_FILE)
    week_11_results = read_results(WEEK_11_RESULTS_FILE)
    week_10_results = read_results(WEEK_10_RESULTS_FILE)
    validate_week_11(week_11_inputs, week_11_results)
    rows = build_summary(week_10_results)

    with WEEK_11_SUMMARY_FILE.open("w", encoding="utf-8", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    print("Week 11 analysis complete")
    print("PCA is exploratory preparation only and did not guide the Week 11 queries")


if __name__ == "__main__":
    main()
