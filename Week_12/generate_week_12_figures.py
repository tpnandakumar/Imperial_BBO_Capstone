"""Generate reproducible Week 12 analytical figures.

Run week_12_analysis.py first. Every plotted source value comes from the
verified Week 12 analysis and figure data summaries. Images are written
straight into the Week 12 folder. No separate figures directory is created.
"""

from __future__ import annotations

import csv
from decimal import Decimal
from pathlib import Path

import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
ANALYSIS_FILE = HERE / "week_12_analysis_summary.csv"
FIGURE_DATA_FILE = HERE / "week_12_figure_data_summary.csv"
DPI = 300


def read_rows(path: Path):
    """Read a CSV as a list of dictionaries."""

    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def add_caption(text: str) -> None:
    """Embed a caption beneath the active figure."""

    plt.figtext(
        0.05,
        0.015,
        text,
        ha="left",
        va="bottom",
        wrap=True,
        fontsize=9,
    )


def save(name: str) -> None:
    """Save the active figure directly in Week_12 and close it."""

    plt.tight_layout(rect=(0, 0.09, 1, 1))
    plt.savefig(HERE / name, dpi=DPI, bbox_inches="tight")
    plt.close()


def generate_weekly_change(rows) -> None:
    labels = [row["Function"] for row in rows]
    values = [float(Decimal(row["Exact_Change"])) for row in rows]

    plt.figure(figsize=(11, 7))
    plt.barh(labels, values)
    plt.axvline(0, linewidth=1)
    plt.xscale("symlog", linthresh=1e-12)
    plt.xlabel("Exact change in objective output")
    plt.ylabel("Objective function")
    plt.title("Figure 1. Week 11 to Week 12 Outcome Change")
    plt.grid(True, axis="x", linestyle=":", linewidth=0.6)
    add_caption(
        "Figure 1. Every Week 12 output improved or remained unchanged relative "
        "to Week 11. Objective scales differ, so the bar lengths should only be "
        "interpreted within the context of each function."
    )
    save("week_12_figure_1_weekly_change.png")


def generate_query_movement(rows) -> None:
    labels = [row["Function"] for row in rows]
    values = [
        float(Decimal(row["Exact_Squared_Query_Distance"]))
        for row in rows
    ]

    plt.figure(figsize=(11, 7))
    plt.barh(labels, values)
    plt.xscale("symlog", linthresh=1e-12)
    plt.xlabel("Exact squared Euclidean movement from Week 11")
    plt.ylabel("Objective function")
    plt.title("Figure 2. Week 12 Query Movement")
    plt.grid(True, axis="x", linestyle=":", linewidth=0.6)
    add_caption(
        "Figure 2. Query movement was small or zero for every function. Function "
        "6 made the largest recorded squared movement in this round."
    )
    save("week_12_figure_2_query_movement.png")


def pca_rows(rows):
    """Return only functions for which PCA was calculated."""

    return [row for row in rows if row["PC1_Ratio_Weeks_01_to_12"]]


def generate_pca_variance(rows) -> None:
    selected = pca_rows(rows)
    labels = [row["Function"] for row in selected]
    pc1 = [float(row["PC1_Ratio_Weeks_01_to_12"]) for row in selected]
    pc12 = [
        float(row["PC1_PC2_Cumulative_Weeks_01_to_12"])
        for row in selected
    ]
    x = list(range(len(labels)))
    width = 0.35

    plt.figure(figsize=(11, 7))
    plt.bar([value - width / 2 for value in x], pc1, width, label="PC1")
    plt.bar(
        [value + width / 2 for value in x],
        pc12,
        width,
        label="PC1 plus PC2",
    )
    plt.xticks(x, labels)
    plt.ylim(0, 1.05)
    plt.ylabel("Explained variance ratio")
    plt.title("Figure 3. PCA of Query Trajectories Through Week 12")
    plt.legend()
    plt.grid(True, axis="y", linestyle=":", linewidth=0.6)
    add_caption(
        "Figure 3. PCA summarises concentration in the submitted query paths for "
        "Functions 3 to 8. It does not establish hidden objective dimensionality."
    )
    save("week_12_figure_3_pca_variance.png")


def generate_pca_change(rows) -> None:
    selected = pca_rows(rows)
    labels = [row["Function"] for row in selected]
    values = [
        float(row["PC1_Ratio_Weeks_01_to_12"])
        - float(row["PC1_Ratio_Weeks_01_to_11"])
        for row in selected
    ]

    plt.figure(figsize=(11, 7))
    plt.barh(labels, values)
    plt.axvline(0, linewidth=1)
    plt.xlabel("Change in PC1 explained variance ratio")
    plt.ylabel("Objective function")
    plt.title("Figure 4. Effect of the Week 12 Query on PCA Concentration")
    plt.grid(True, axis="x", linestyle=":", linewidth=0.6)
    add_caption(
        "Figure 4. The added Week 12 observation increased PC1 concentration for "
        "Functions 3 and 8 and reduced it slightly for Functions 4, 5, 6 and 7."
    )
    save("week_12_figure_4_pca_change.png")


def generate_coordinate_correlation(rows) -> None:
    selected = pca_rows(rows)
    labels = [row["Function"] for row in selected]
    values = [
        float(row["Maximum_Absolute_Coordinate_Correlation_Weeks_01_to_12"])
        for row in selected
    ]

    plt.figure(figsize=(11, 7))
    plt.bar(labels, values)
    plt.ylim(0, 1.05)
    plt.ylabel("Maximum absolute coordinate correlation")
    plt.title("Figure 5. Coordinate Correlation in the Recorded Query Path")
    plt.grid(True, axis="y", linestyle=":", linewidth=0.6)
    add_caption(
        "Figure 5. High correlation shows that some submitted coordinates moved "
        "together. It is evidence about the query trajectory, not proof that a "
        "coordinate is redundant in the hidden objective."
    )
    save("week_12_figure_5_coordinate_correlation.png")


def main() -> None:
    """Generate all Week 12 figures from the verified summaries."""

    analysis = read_rows(ANALYSIS_FILE)
    figure_data = read_rows(FIGURE_DATA_FILE)

    if len(analysis) != 8 or len(figure_data) != 8:
        raise ValueError("Run week_12_analysis.py and verify the generated summaries")
    if len(pca_rows(figure_data)) != 6:
        raise ValueError("PCA data should be available for Functions 3 to 8")

    generate_weekly_change(analysis)
    generate_query_movement(analysis)
    generate_pca_variance(figure_data)
    generate_pca_change(figure_data)
    generate_coordinate_correlation(figure_data)
    print("Week 12 figure generation complete")


if __name__ == "__main__":
    main()
