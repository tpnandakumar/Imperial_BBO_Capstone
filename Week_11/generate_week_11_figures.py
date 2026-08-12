"""
Week 11 figure generation script for the Imperial BBO Capstone.

The figures evaluate the returned Week 11 outcomes and add an exploratory
PCA view for Week 12 preparation. Clustering remains anchored to Week 10,
where it was used to choose the Week 11 queries.

Verified output values are retained as exact strings in the source tables.
Values are converted to floating point numbers only for plotting.
"""

from __future__ import annotations

import csv
from decimal import Decimal
from pathlib import Path
from typing import Dict, List

import matplotlib.pyplot as plt


CURRENT_DIRECTORY = Path(__file__).resolve().parent
ANALYSIS_SUMMARY_FILE = CURRENT_DIRECTORY / "week_11_analysis_summary.csv"
FIGURE_DATA_SUMMARY_FILE = CURRENT_DIRECTORY / "week_11_figure_data_summary.csv"
OUTPUT_DIRECTORY = CURRENT_DIRECTORY
DPI = 300
FUNCTIONS = [f"Function {number}" for number in range(1, 9)]

WEEKLY_OUTPUT_TEXT: Dict[int, List[str]] = {
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

FIGURE_DATA_FIELDS = [
    "Function",
    "Week_10_Output",
    "Week_11_Output",
    "Exact_Change",
    "Direction",
    "Week_10_Clustering_Informed_Action",
    "Clustering_Outcome",
    "Prior_Best_Week",
    "Prior_Best_Output",
    "Exact_Squared_Distance_To_Prior_Best_Input",
    "Week_11_Best_Status",
    "PCA_Status",
    "PCA_PC1_Explained_Variance_Ratio",
    "PCA_PC1_PC2_Cumulative_Ratio",
    "PCA_Components_To_Reach_90pct",
]


def read_analysis_summary() -> List[Dict[str, str]]:
    if not ANALYSIS_SUMMARY_FILE.exists():
        raise FileNotFoundError(
            "Run week_11_analysis.py before generate_week_11_figures.py"
        )

    with ANALYSIS_SUMMARY_FILE.open("r", encoding="utf-8-sig", newline="") as csv_file:
        rows = list(csv.DictReader(csv_file))

    if len(rows) != 8:
        raise ValueError("week_11_analysis_summary.csv must contain eight function rows")
    return rows


def write_figure_data_summary(rows: List[Dict[str, str]]) -> None:
    with FIGURE_DATA_SUMMARY_FILE.open("w", encoding="utf-8", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=FIGURE_DATA_FIELDS)
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    "Function": row["Function"],
                    "Week_10_Output": row["Week_10_Output"],
                    "Week_11_Output": row["Week_11_Output"],
                    "Exact_Change": row["Exact_Change"],
                    "Direction": row["Direction"],
                    "Week_10_Clustering_Informed_Action": row[
                        "Week_10_Clustering_Informed_Action"
                    ],
                    "Clustering_Outcome": row["Clustering_Outcome"],
                    "Prior_Best_Week": row["Prior_Best_Week"],
                    "Prior_Best_Output": row["Prior_Best_Output"],
                    "Exact_Squared_Distance_To_Prior_Best_Input": row[
                        "Exact_Squared_Distance_To_Prior_Best_Input"
                    ],
                    "Week_11_Best_Status": row["Week_11_Best_Status"],
                    "PCA_Status": row["PCA_Status"],
                    "PCA_PC1_Explained_Variance_Ratio": row[
                        "PCA_PC1_Explained_Variance_Ratio"
                    ],
                    "PCA_PC1_PC2_Cumulative_Ratio": row[
                        "PCA_PC1_PC2_Cumulative_Ratio"
                    ],
                    "PCA_Components_To_Reach_90pct": row[
                        "PCA_Components_To_Reach_90pct"
                    ],
                }
            )


def add_caption(text: str) -> None:
    plt.figtext(0.05, 0.015, text, ha="left", va="bottom", wrap=True, fontsize=9)


def save_figure(filename: str) -> None:
    output_path = OUTPUT_DIRECTORY / filename
    plt.tight_layout(rect=(0, 0.08, 1, 1))
    plt.savefig(output_path, dpi=DPI, bbox_inches="tight")
    plt.close()
    print(f"Created: {output_path.name}")


def generate_output_evolution() -> None:
    weeks = list(range(1, 12))
    plt.figure(figsize=(14, 9))
    for function_index, function_name in enumerate(FUNCTIONS):
        values = [
            float(Decimal(WEEKLY_OUTPUT_TEXT[week][function_index]))
            for week in weeks
        ]
        plt.plot(weeks, values, marker="o", linewidth=1.8, label=function_name)

    plt.yscale("symlog", linthresh=1e-12)
    plt.xticks(weeks)
    plt.xlabel("Optimisation round")
    plt.ylabel("Objective output on a symmetric logarithmic scale")
    plt.title("Figure 1. Function Output Evolution Across Weeks 1 to 11")
    plt.grid(True, which="both", linestyle=":", linewidth=0.6)
    plt.legend(loc="best", fontsize=8)
    add_caption(
        "Figure 1. Verified outputs across all eleven rounds. Week 11 improved "
        "on Week 10 for every function, although the functions operate on "
        "different numerical scales."
    )
    save_figure("week_11_figure_1_output_evolution.png")


def generate_week_10_to_11_change(rows: List[Dict[str, str]]) -> None:
    changes = [float(Decimal(row["Exact_Change"])) for row in rows]
    labels = [row["Function"] for row in rows]

    plt.figure(figsize=(11, 7))
    plt.barh(labels, changes)
    plt.axvline(0, linewidth=1)
    plt.xscale("symlog", linthresh=1e-12)
    plt.xlabel("Change in objective output")
    plt.ylabel("Objective function")
    plt.title("Figure 2. Week 10 to Week 11 Outcome Change")
    plt.grid(True, axis="x", which="both", linestyle=":", linewidth=0.6)
    add_caption(
        "Figure 2. Every Week 11 result improved on Week 10. The chart records "
        "the outcome of the clustering informed decisions made in Week 10."
    )
    save_figure("week_11_figure_2_weekly_change.png")


def generate_function_5_progress() -> None:
    weeks = list(range(1, 12))
    values = [float(Decimal(WEEKLY_OUTPUT_TEXT[week][4])) for week in weeks]

    plt.figure(figsize=(10, 6))
    plt.plot(weeks, values, marker="o", linewidth=2)
    plt.xticks(weeks)
    plt.xlabel("Optimisation round")
    plt.ylabel("Function 5 objective output")
    plt.title("Figure 3. Function 5 Progress Across Weeks 1 to 11")
    plt.grid(True, linestyle=":", linewidth=0.6)
    add_caption(
        "Figure 3. Function 5 moved from a Week 10 plateau at "
        "4394.868042481448 to a new Week 11 best of 4411.0387356061765 "
        "after the boundary cluster refinement."
    )
    save_figure("week_11_figure_3_function_5_progress.png")


def generate_prior_best_distance(rows: List[Dict[str, str]]) -> None:
    labels = [row["Function"] for row in rows]
    values = [
        float(Decimal(row["Exact_Squared_Distance_To_Prior_Best_Input"]))
        for row in rows
    ]

    plt.figure(figsize=(11, 7))
    plt.barh(labels, values)
    plt.xlabel("Exact squared Euclidean distance to the prior best input")
    plt.ylabel("Objective function")
    plt.title("Figure 4. Week 11 Proximity to the Prior Best Input")
    plt.grid(True, axis="x", linestyle=":", linewidth=0.6)
    add_caption(
        "Figure 4. The Week 11 choices were deliberately close to confirmed "
        "strong regions for several functions. Squared distance is used so the "
        "stored distance measure remains exact for decimal input coordinates."
    )
    save_figure("week_11_figure_4_prior_best_distance.png")


def pca_rows(rows: List[Dict[str, str]]) -> List[Dict[str, str]]:
    return [
        row
        for row in rows
        if row["PCA_PC1_Explained_Variance_Ratio"].strip()
    ]


def generate_pca_variance(rows: List[Dict[str, str]]) -> None:
    selected = pca_rows(rows)
    labels = [row["Function"] for row in selected]
    pc1 = [float(row["PCA_PC1_Explained_Variance_Ratio"]) for row in selected]
    pc12 = [float(row["PCA_PC1_PC2_Cumulative_Ratio"]) for row in selected]
    x = list(range(len(labels)))
    width = 0.35

    plt.figure(figsize=(11, 7))
    plt.bar([value - width / 2 for value in x], pc1, width=width, label="PC1")
    plt.bar([value + width / 2 for value in x], pc12, width=width, label="PC1 plus PC2")
    plt.xticks(x, labels)
    plt.ylim(0, 1.05)
    plt.xlabel("Objective function")
    plt.ylabel("Explained variance ratio")
    plt.title("Figure 5. Exploratory PCA of the Recorded Query Trajectories")
    plt.grid(True, axis="y", linestyle=":", linewidth=0.6)
    plt.legend()
    add_caption(
        "Figure 5. Centred PCA is applied only to Functions 3 to 8 as a "
        "forward looking description of the query trajectories. It does not "
        "identify the hidden objective surface or an optimum."
    )
    save_figure("week_11_figure_5_pca_variance.png")


def generate_pca_components_90(rows: List[Dict[str, str]]) -> None:
    selected = pca_rows(rows)
    labels = [row["Function"] for row in selected]
    components = [int(row["PCA_Components_To_Reach_90pct"]) for row in selected]

    plt.figure(figsize=(10, 6))
    plt.bar(labels, components)
    plt.xlabel("Objective function")
    plt.ylabel("Principal components required for at least 90 percent variance")
    plt.title("Figure 6. Exploratory PCA Dimensional Concentration")
    plt.grid(True, axis="y", linestyle=":", linewidth=0.6)
    add_caption(
        "Figure 6. Most recorded query variation is concentrated in one or two "
        "principal directions. This reflects the search path chosen so far and "
        "must not be interpreted as the true dimensionality of the objective."
    )
    save_figure("week_11_figure_6_pca_components_90.png")


def main() -> None:
    rows = read_analysis_summary()
    write_figure_data_summary(rows)
    generate_output_evolution()
    generate_week_10_to_11_change(rows)
    generate_function_5_progress()
    generate_prior_best_distance(rows)
    generate_pca_variance(rows)
    generate_pca_components_90(rows)
    print(f"Created: {FIGURE_DATA_SUMMARY_FILE.name}")


if __name__ == "__main__":
    main()
