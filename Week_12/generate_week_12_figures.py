"""Generate reproducible Week 12 analytical figures.

Run week_12_analysis.py first. Images are derived from verified CSV records.
No figure selects or recommends a Week 13 query.
"""

from __future__ import annotations

import csv
from decimal import Decimal
from pathlib import Path

import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
ANALYSIS_FILE = HERE / "week_12_analysis_summary.csv"
PCA_FILE = HERE / "week_12_pca_summary.csv"
FIGURE_DATA_FILE = HERE / "week_12_figure_data_summary.csv"
DPI = 300


def read_rows(path: Path):
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def caption(text: str) -> None:
    plt.figtext(0.05, 0.015, text, ha="left", va="bottom", wrap=True, fontsize=9)


def save(name: str) -> None:
    plt.tight_layout(rect=(0, 0.09, 1, 1))
    plt.savefig(HERE / name, dpi=DPI, bbox_inches="tight")
    plt.close()


def weekly_change(rows):
    labels = [row["Function"] for row in rows]
    values = [float(Decimal(row["Exact_Change"])) for row in rows]
    plt.figure(figsize=(11, 7))
    plt.barh(labels, values, color="#2471A3")
    plt.axvline(0, color="#1B2631", linewidth=1)
    plt.xscale("symlog", linthresh=1e-12)
    plt.xlabel("Exact change in objective output")
    plt.title("Figure 1. Week 11 to Week 12 Outcome Change")
    plt.grid(True, axis="x", linestyle=":", linewidth=0.6)
    caption("Figure 1. Every function improved or remained unchanged. Values are compared only within each function because the objectives use different numerical scales.")
    save("week_12_figure_1_weekly_change.png")


def pca_variance(rows):
    labels = [row["Function"] for row in rows]
    pc1 = [float(row["Week_12_PC1_Ratio"]) for row in rows]
    pc12 = [float(row["Week_12_PC1_PC2_Cumulative"]) for row in rows]
    x = list(range(len(labels)))
    width = 0.35
    plt.figure(figsize=(11, 7))
    plt.bar([v - width / 2 for v in x], pc1, width, label="PC1", color="#17A589")
    plt.bar([v + width / 2 for v in x], pc12, width, label="PC1 plus PC2", color="#F4D03F")
    plt.xticks(x, labels)
    plt.ylim(0, 1.05)
    plt.ylabel("Explained variance ratio")
    plt.title("Figure 2. PCA of Query Trajectories Through Week 12")
    plt.legend()
    plt.grid(True, axis="y", linestyle=":", linewidth=0.6)
    caption("Figure 2. PCA describes concentration in the submitted query paths. It does not establish the dimensionality of the hidden objective functions.")
    save("week_12_figure_2_pca_variance.png")


def pca_change(rows):
    labels = [row["Function"] for row in rows]
    change = [
        float(row["Week_12_PC1_Ratio"]) - float(row["Week_11_PC1_Ratio"])
        for row in rows
    ]
    colours = ["#7D3C98" if value >= 0 else "#CA6F1E" for value in change]
    plt.figure(figsize=(11, 7))
    plt.barh(labels, change, color=colours)
    plt.axvline(0, color="#1B2631", linewidth=1)
    plt.xlabel("Change in PC1 explained variance ratio")
    plt.title("Figure 3. Effect of the Week 12 Observation on PCA Concentration")
    plt.grid(True, axis="x", linestyle=":", linewidth=0.6)
    caption("Figure 3. The difference between the Weeks 1 to 11 PCA and the Weeks 1 to 12 PCA shows how one additional query altered the recorded variance structure.")
    save("week_12_figure_3_pca_change.png")


def correlation(rows):
    labels = [row["Function"] for row in rows]
    values = [float(row["Maximum_Absolute_Coordinate_Correlation"]) for row in rows]
    plt.figure(figsize=(11, 7))
    plt.bar(labels, values, color="#C0392B")
    plt.ylim(0, 1.05)
    plt.ylabel("Maximum absolute coordinate correlation")
    plt.title("Figure 4. Coordinate Correlation and Possible Redundancy")
    plt.grid(True, axis="y", linestyle=":", linewidth=0.6)
    caption("Figure 4. High correlation identifies coordinates that moved together in the observed queries. It is evidence of trajectory redundancy, not proof that a coordinate is irrelevant.")
    save("week_12_figure_4_coordinate_correlation.png")


def main() -> None:
    analysis = read_rows(ANALYSIS_FILE)
    pca = read_rows(PCA_FILE)
    if len(analysis) != 8 or len(pca) != 6:
        raise ValueError("Run week_12_analysis.py and verify the generated summaries")
    with FIGURE_DATA_FILE.open("w", encoding="utf-8", newline="") as handle:
        fields = list(pca[0].keys())
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(pca)
    weekly_change(analysis)
    pca_variance(pca)
    pca_change(pca)
    correlation(pca)
    print("Week 12 figure generation complete")


if __name__ == "__main__":
    main()
