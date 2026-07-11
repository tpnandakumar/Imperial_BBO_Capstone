"""
Week 08 Figure Generation Tool
Imperial BBO Capstone

This script generates analytical figures for the Week 08 README using
the exact objective values recorded during Weeks 01 to 08.

No optimisation values are rounded or truncated in the source data.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


OUTPUT_DIRECTORY = Path(".")
DPI = 300


WEEKLY_RESULTS = {
    "Week 01": {
        "F1": 6.854713532414845e-19,
        "F2": 0.45494185399727516,
        "F3": -0.10183633971746164,
        "F4": -4.359874926582439,
        "F5": 1415.8763939603884,
        "F6": -0.7001549808025808,
        "F7": 1.3199939052019112,
        "F8": 9.58024,
    },
    "Week 02": {
        "F1": 6.659572754640724e-23,
        "F2": 0.41213721316888097,
        "F3": -0.1332555781557258,
        "F4": -23.120154471959825,
        "F5": 2308.1487028593933,
        "F6": -2.0702463923015775,
        "F7": 1.0696579739950232,
        "F8": 9.5241,
    },
    "Week 03": {
        "F1": 0.025559285339829783,
        "F2": 0.14098828808535324,
        "F3": -0.12787021171886992,
        "F4": -14.554028542475695,
        "F5": 2840.9903787629305,
        "F6": -0.648848297397347,
        "F7": 0.8966026942687082,
        "F8": 9.44296,
    },
    "Week 04": {
        "F1": 1.4754580129542488e-07,
        "F2": 0.5228458934672892,
        "F3": -0.06037987403160633,
        "F4": -22.55187651826871,
        "F5": 3238.333368768757,
        "F6": -0.8733671274789931,
        "F7": 1.1968303712356705,
        "F8": 9.539439999999999,
    },
    "Week 05": {
        "F1": 0.012779642669914939,
        "F2": 0.28016822307722516,
        "F3": -0.11392206377710448,
        "F4": -27.44051496086922,
        "F5": 3682.2110623386798,
        "F6": -1.073875453695542,
        "F7": 1.3809299933612855,
        "F8": 9.5113,
    },
    "Week 06": {
        "F1": 2.6752879910742468e-09,
        "F2": 0.5712475315739602,
        "F3": -0.3071823694141529,
        "F4": -31.20347777578016,
        "F5": 3922.7652233497042,
        "F6": -1.3792272680368016,
        "F7": 1.3529491169887171,
        "F8": 9.5148,
    },
    "Week 07": {
        "F1": -1.4546199699251391e-58,
        "F2": 0.2399291698606551,
        "F3": -0.09116928906376276,
        "F4": -10.745961383135121,
        "F5": 4278.816638076986,
        "F6": -1.119713499832813,
        "F7": 1.1543358123792982,
        "F8": 9.49476,
    },
    "Week 08": {
        "F1": -1.4546199699251391e-58,
        "F2": 0.5672775862793291,
        "F3": -0.0991107637427902,
        "F4": -12.305008897187289,
        "F5": 4359.384134322703,
        "F6": -1.1197178425911847,
        "F7": 1.3346391663186332,
        "F8": 9.47621,
    },
}


WEEK_08_STRATEGY = {
    "F1": "Explore",
    "F2": "Refine",
    "F3": "Reassess",
    "F4": "Reassess",
    "F5": "Exploit",
    "F6": "Reassess",
    "F7": "Refine",
    "F8": "Refine",
}


def build_results_dataframe() -> pd.DataFrame:
    """Convert the weekly results dictionary into a long-form DataFrame."""

    rows = []

    for week, function_values in WEEKLY_RESULTS.items():
        week_number = int(week.split()[1])

        for function, output in function_values.items():
            rows.append(
                {
                    "Week": week,
                    "Week_Number": week_number,
                    "Function": function,
                    "Output": output,
                }
            )

    return pd.DataFrame(rows)


def save_figure(filename: str) -> None:
    """Save the current Matplotlib figure and close it."""

    output_path = OUTPUT_DIRECTORY / filename
    plt.tight_layout()
    plt.savefig(output_path, dpi=DPI, bbox_inches="tight")
    plt.close()
    print(f"Created: {output_path}")


def generate_figure_1a(data: pd.DataFrame) -> None:
    """
    Generate Figure 1A.

    Function output evolution across Weeks 01 to 08.
    A symmetric logarithmic scale is used because the functions have
    substantially different magnitudes and include negative values.
    """

    plt.figure(figsize=(13, 8))

    for function in sorted(data["Function"].unique()):
        subset = data[data["Function"] == function].sort_values("Week_Number")

        plt.plot(
            subset["Week_Number"],
            subset["Output"],
            marker="o",
            linewidth=2,
            label=function,
        )

    plt.axhline(0, linewidth=1)
    plt.yscale("symlog", linthresh=0.01)
    plt.xticks(range(1, 9))
    plt.xlabel("Optimisation round")
    plt.ylabel("Objective value, symmetric logarithmic scale")
    plt.title("Figure 1A. Function Output Evolution, Weeks 01 to 08")
    plt.grid(True, linestyle=":", linewidth=0.7)
    plt.legend(title="Function", ncol=4)

    save_figure(
        "figure_1A_function_output_evolution_weeks_01_to_08.png"
    )


def generate_figure_1b(data: pd.DataFrame) -> None:
    """Generate Figure 1B, the Week 08 performance ranking."""

    week_08 = (
        data[data["Week_Number"] == 8]
        .sort_values("Output", ascending=True)
        .copy()
    )

    plt.figure(figsize=(12, 7))

    bars = plt.barh(
        week_08["Function"],
        week_08["Output"],
    )

    for bar, output in zip(bars, week_08["Output"]):
        x_position = output

        if output >= 0:
            horizontal_alignment = "left"
        else:
            horizontal_alignment = "right"

        plt.text(
            x_position,
            bar.get_y() + bar.get_height() / 2,
            repr(output),
            va="center",
            ha=horizontal_alignment,
            fontsize=8,
        )

    plt.axvline(0, linewidth=1)
    plt.xlabel("Week 08 objective value")
    plt.ylabel("Function")
    plt.title("Figure 1B. Week 08 Function Performance Ranking")
    plt.grid(True, axis="x", linestyle=":", linewidth=0.7)

    save_figure(
        "figure_1B_week_08_function_performance_ranking.png"
    )


def generate_figure_1c(data: pd.DataFrame) -> None:
    """Generate Figure 1C, comparing Week 07 and Week 08."""

    comparison = data[data["Week_Number"].isin([7, 8])].pivot(
        index="Function",
        columns="Week_Number",
        values="Output",
    )

    comparison.columns = ["Week_07", "Week_08"]
    comparison["Change"] = comparison["Week_08"] - comparison["Week_07"]
    comparison = comparison.sort_values("Change", ascending=True)

    plt.figure(figsize=(12, 7))

    bars = plt.barh(
        comparison.index,
        comparison["Change"],
    )

    for bar, change in zip(bars, comparison["Change"]):
        if change >= 0:
            horizontal_alignment = "left"
        else:
            horizontal_alignment = "right"

        plt.text(
            change,
            bar.get_y() + bar.get_height() / 2,
            repr(change),
            va="center",
            ha=horizontal_alignment,
            fontsize=8,
        )

    plt.axvline(0, linewidth=1)
    plt.xlabel("Exact change from Week 07 to Week 08")
    plt.ylabel("Function")
    plt.title("Figure 1C. Week 07 to Week 08 Performance Change")
    plt.grid(True, axis="x", linestyle=":", linewidth=0.7)

    save_figure(
        "figure_1C_week_07_vs_week_08_performance_change.png"
    )


def generate_figure_3a(data: pd.DataFrame) -> None:
    """Generate Figure 3A showing ranking evolution across eight weeks."""

    ranked_data = data.copy()

    ranked_data["Rank"] = ranked_data.groupby("Week_Number")[
        "Output"
    ].rank(
        ascending=False,
        method="min",
    )

    plt.figure(figsize=(13, 8))

    for function in sorted(ranked_data["Function"].unique()):
        subset = ranked_data[
            ranked_data["Function"] == function
        ].sort_values("Week_Number")

        plt.plot(
            subset["Week_Number"],
            subset["Rank"],
            marker="o",
            linewidth=2,
            label=function,
        )

    plt.gca().invert_yaxis()
    plt.xticks(range(1, 9))
    plt.yticks(range(1, 9))
    plt.xlabel("Optimisation round")
    plt.ylabel("Rank, 1 is highest")
    plt.title("Figure 3A. Functional Ranking Evolution, Weeks 01 to 08")
    plt.grid(True, linestyle=":", linewidth=0.7)
    plt.legend(title="Function", ncol=4)

    save_figure(
        "figure_3A_functional_ranking_evolution_weeks_01_to_08.png"
    )


def generate_figure_4(data: pd.DataFrame) -> None:
    """Generate Figure 4 showing Function 5 optimisation progress."""

    function_5 = data[
        data["Function"] == "F5"
    ].sort_values("Week_Number")

    plt.figure(figsize=(12, 7))

    plt.plot(
        function_5["Week_Number"],
        function_5["Output"],
        marker="o",
        linewidth=3,
    )

    for _, row in function_5.iterrows():
        plt.annotate(
            repr(row["Output"]),
            (row["Week_Number"], row["Output"]),
            xytext=(0, 10),
            textcoords="offset points",
            ha="center",
            fontsize=8,
        )

    plt.xticks(range(1, 9))
    plt.xlabel("Optimisation round")
    plt.ylabel("Function 5 objective value")
    plt.title("Figure 4. Function 5 Optimisation Progress, Weeks 01 to 08")
    plt.grid(True, linestyle=":", linewidth=0.7)

    save_figure(
        "figure_4_function_5_optimisation_progress_weeks_01_to_08.png"
    )


def generate_figure_4a(data: pd.DataFrame) -> None:
    """Generate Figure 4A showing Week 08 resource allocation."""

    week_08 = (
        data[data["Week_Number"] == 8]
        .sort_values("Output", ascending=False)
        .copy()
    )

    week_08["Strategy"] = week_08["Function"].map(WEEK_08_STRATEGY)

    strategy_counts = (
        week_08["Strategy"]
        .value_counts()
        .reindex(
            ["Exploit", "Refine", "Reassess", "Explore"],
            fill_value=0,
        )
    )

    plt.figure(figsize=(10, 7))

    bars = plt.bar(
        strategy_counts.index,
        strategy_counts.values,
    )

    for bar, count in zip(bars, strategy_counts.values):
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            count,
            str(count),
            ha="center",
            va="bottom",
        )

    plt.xlabel("Week 08 optimisation strategy")
    plt.ylabel("Number of functions")
    plt.title("Figure 4A. Week 08 Resource Allocation Decision Matrix")
    plt.ylim(0, max(strategy_counts.values) + 1)
    plt.grid(True, axis="y", linestyle=":", linewidth=0.7)

    save_figure(
        "figure_4A_week_08_resource_allocation.png"
    )


def generate_week_08_summary_table(data: pd.DataFrame) -> None:
    """Export a figure-ready Week 08 summary table as a CSV file."""

    week_07 = (
        data[data["Week_Number"] == 7]
        .set_index("Function")["Output"]
    )

    week_08 = (
        data[data["Week_Number"] == 8]
        .set_index("Function")["Output"]
    )

    summary = pd.DataFrame(
        {
            "Function": week_08.index,
            "Week_07_Output": week_07,
            "Week_08_Output": week_08,
        }
    ).reset_index(drop=True)

    summary["Change"] = (
        summary["Week_08_Output"] - summary["Week_07_Output"]
    )

    summary["Rank"] = summary["Week_08_Output"].rank(
        ascending=False,
        method="min",
    ).astype(int)

    summary["Strategy"] = summary["Function"].map(WEEK_08_STRATEGY)

    summary = summary.sort_values("Rank")

    output_path = OUTPUT_DIRECTORY / "week_08_figure_data_summary.csv"
    summary.to_csv(output_path, index=False)

    print(f"Created: {output_path}")


def main() -> None:
    """Generate all Week 08 analytical figures."""

    data = build_results_dataframe()

    generate_figure_1a(data)
    generate_figure_1b(data)
    generate_figure_1c(data)
    generate_figure_3a(data)
    generate_figure_4(data)
    generate_figure_4a(data)
    generate_week_08_summary_table(data)

    print("\nAll Week 08 analytical figures were generated successfully.")


if __name__ == "__main__":
    main()
