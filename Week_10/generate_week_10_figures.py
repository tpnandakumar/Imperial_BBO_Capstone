"""
Week 10 Figure Generation Script
Imperial BBO Capstone

This script generates reproducible analytical figures for Week 10 and
writes week_10_figure_data_summary.csv in the same folder. Numerical
source values are stored as exact strings. Decimal arithmetic is used
for comparisons before values are converted to floats for plotting.
"""

from __future__ import annotations

import csv
from decimal import Decimal
from pathlib import Path
from typing import Dict, List

import matplotlib.pyplot as plt
import pandas as pd


CURRENT_DIRECTORY = Path(__file__).resolve().parent
OUTPUT_DIRECTORY = CURRENT_DIRECTORY
DPI = 300

FUNCTIONS = [f"Function {number}" for number in range(1, 9)]

WEEKLY_OUTPUT_TEXT: Dict[int, List[str]] = {
    1: [
        "6.854713532414845e-19",
        "0.45494185399727516",
        "-0.10183633971746164",
        "-4.359874926582439",
        "1415.8763939603884",
        "-0.7001549808025808",
        "1.3199939052019112",
        "9.58024",
    ],
    2: [
        "6.659572754640724e-23",
        "0.41213721316888097",
        "-0.1332555781557258",
        "-23.120154471959825",
        "2308.1487028593933",
        "-2.0702463923015775",
        "1.0696579739950232",
        "9.5241",
    ],
    3: [
        "0.025559285339829783",
        "0.14098828808535324",
        "-0.12787021171886992",
        "-14.554028542475695",
        "2840.9903787629305",
        "-0.648848297397347",
        "0.8966026942687082",
        "9.44296",
    ],
    4: [
        "1.4754580129542488e-07",
        "0.5228458934672892",
        "-0.06037987403160633",
        "-22.55187651826871",
        "3238.333368768757",
        "-0.8733671274789931",
        "1.1968303712356705",
        "9.539439999999999",
    ],
    5: [
        "0.012779642669914939",
        "0.28016822307722516",
        "-0.11392206377710448",
        "-27.44051496086922",
        "3682.2110623386798",
        "-1.073875453695542",
        "1.3809299933612855",
        "9.5113",
    ],
    6: [
        "2.6752879910742468e-09",
        "0.5712475315739602",
        "-0.3071823694141529",
        "-31.20347777578016",
        "3922.7652233497042",
        "-1.3792272680368016",
        "1.3529491169887171",
        "9.5148",
    ],
    7: [
        "-1.4546199699251391e-58",
        "0.2399291698606551",
        "-0.09116928906376276",
        "-10.745961383135121",
        "4278.816638076986",
        "-1.119713499832813",
        "1.1543358123792982",
        "9.49476",
    ],
    8: [
        "-1.4546199699251391e-58",
        "0.5672775862793291",
        "-0.0991107637427902",
        "-12.305008897187289",
        "4359.384134322703",
        "-1.1197178425911847",
        "1.3346391663186332",
        "9.47621",
    ],
    9: [
        "-1.4546199699251391e-58",
        "0.47297842839949866",
        "-0.1156707106126581",
        "-11.788939969158545",
        "4394.868042481448",
        "-1.1733030029888645",
        "1.314307996450604",
        "9.4709436",
    ],
    10: [
        "2.8950706668499033e-23",
        "0.5311818841205426",
        "-0.08697581687486715",
        "-13.483642655031158",
        "4394.868042481448",
        "-1.2283806967341901",
        "1.285160161342515",
        "9.4646525",
    ],
}

WEEK_10_STRATEGY = {
    "Function 1": "Explore",
    "Function 2": "Refine",
    "Function 3": "Refine",
    "Function 4": "Reassess",
    "Function 5": "Exploit",
    "Function 6": "Reassess",
    "Function 7": "Refine",
    "Function 8": "Refine",
}


def build_dataframe() -> pd.DataFrame:
    """Create a long form DataFrame containing Weeks 01 to 10."""

    rows: list[dict[str, object]] = []

    for week_number, output_values in WEEKLY_OUTPUT_TEXT.items():
        for function_name, output_text in zip(FUNCTIONS, output_values):
            rows.append(
                {
                    "Week": week_number,
                    "Function": function_name,
                    "Output_Text": output_text,
                    "Output": float(Decimal(output_text)),
                }
            )

    return pd.DataFrame(rows)


def save_figure(filename: str) -> None:
    """Save the active figure in the Week 10 folder and close it."""

    output_path = OUTPUT_DIRECTORY / filename
    plt.tight_layout()
    plt.savefig(output_path, dpi=DPI, bbox_inches="tight")
    plt.close()
    print(f"Created: {output_path.name}")


def add_caption(text: str) -> None:
    """Add an embedded caption beneath the active chart."""

    plt.figtext(
        0.05,
        0.015,
        text,
        ha="left",
        va="bottom",
        wrap=True,
        fontsize=9,
    )


def exact_change(week_09_text: str, week_10_text: str) -> str:
    """Calculate an exact change using Decimal arithmetic."""

    change = Decimal(week_10_text) - Decimal(week_09_text)
    return "0" if change == 0 else str(change)


def direction_from_change(change_text: str) -> str:
    """Classify a change as Improved, Declined or Unchanged."""

    change = Decimal(change_text)

    if change > 0:
        return "Improved"

    if change < 0:
        return "Declined"

    return "Unchanged"


def week_10_rank_map() -> Dict[str, int]:
    """Return rank positions based on the Week 10 objective outputs."""

    pairs = list(zip(FUNCTIONS, WEEKLY_OUTPUT_TEXT[10]))
    ranked = sorted(pairs, key=lambda item: Decimal(item[1]), reverse=True)
    return {function_name: rank for rank, (function_name, _) in enumerate(ranked, 1)}


def write_figure_data_summary() -> None:
    """Write the exact comparison data used by the Week 10 figures."""

    output_path = CURRENT_DIRECTORY / "week_10_figure_data_summary.csv"
    rank_map = week_10_rank_map()
    fieldnames = [
        "Function",
        "Week_09_Output",
        "Week_10_Output",
        "Exact_Change",
        "Direction",
        "Strategy",
        "Week_10_Rank",
    ]

    with output_path.open("w", encoding="utf-8", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for index, function_name in enumerate(FUNCTIONS):
            week_09_text = WEEKLY_OUTPUT_TEXT[9][index]
            week_10_text = WEEKLY_OUTPUT_TEXT[10][index]
            change_text = exact_change(week_09_text, week_10_text)

            writer.writerow(
                {
                    "Function": function_name,
                    "Week_09_Output": week_09_text,
                    "Week_10_Output": week_10_text,
                    "Exact_Change": change_text,
                    "Direction": direction_from_change(change_text),
                    "Strategy": WEEK_10_STRATEGY[function_name],
                    "Week_10_Rank": rank_map[function_name],
                }
            )

    print(f"Created: {output_path.name}")


def generate_output_evolution(data: pd.DataFrame) -> None:
    """Generate output evolution across Weeks 01 to 10."""

    plt.figure(figsize=(14, 9))

    for function_name in FUNCTIONS:
        subset = data[data["Function"] == function_name]
        plt.plot(
            subset["Week"],
            subset["Output"],
            marker="o",
            linewidth=1.8,
            label=function_name,
        )

    plt.yscale("symlog", linthresh=1e-12)
    plt.xticks(range(1, 11), [f"Week {week}" for week in range(1, 11)])
    plt.xlabel("Optimisation round")
    plt.ylabel("Objective output on a symmetric logarithmic scale")
    plt.title("Figure 1. Function Output Evolution Across Weeks 01 to 10")
    plt.grid(True, which="both", linestyle=":", linewidth=0.6)
    plt.legend(loc="best", fontsize=8)
    add_caption(
        "Figure 1. Objective outputs for all eight functions across ten "
        "optimisation rounds. The symmetric logarithmic scale retains "
        "positive, negative and near zero values within one view."
    )
    save_figure("week_10_figure_1_output_evolution.png")


def generate_week_10_ranking() -> None:
    """Generate the Week 10 performance ranking."""

    rank_map = week_10_rank_map()
    ordered_functions = sorted(FUNCTIONS, key=lambda name: rank_map[name])
    output_lookup = {
        function_name: float(Decimal(output_text))
        for function_name, output_text in zip(FUNCTIONS, WEEKLY_OUTPUT_TEXT[10])
    }

    plt.figure(figsize=(11, 7))
    plt.barh(
        ordered_functions[::-1],
        [output_lookup[name] for name in ordered_functions[::-1]],
    )
    plt.xscale("symlog", linthresh=1e-12)
    plt.xlabel("Week 10 objective output")
    plt.ylabel("Objective function")
    plt.title("Figure 2. Week 10 Function Performance Ranking")
    plt.grid(True, axis="x", which="both", linestyle=":", linewidth=0.6)
    add_caption(
        "Figure 2. Functions ranked by the exact Week 10 objective output. "
        "Function 5 remains first, followed by Functions 8, 7 and 2."
    )
    save_figure("week_10_figure_2_performance_ranking.png")


def generate_weekly_change() -> None:
    """Generate the exact Week 09 to Week 10 change comparison."""

    changes = [
        float(Decimal(week_10) - Decimal(week_09))
        for week_09, week_10 in zip(
            WEEKLY_OUTPUT_TEXT[9],
            WEEKLY_OUTPUT_TEXT[10],
        )
    ]

    plt.figure(figsize=(11, 7))
    plt.barh(FUNCTIONS, changes)
    plt.axvline(0, linewidth=1)
    plt.xscale("symlog", linthresh=1e-12)
    plt.xlabel("Exact change in objective output")
    plt.ylabel("Objective function")
    plt.title("Figure 3. Change from Week 09 to Week 10")
    plt.grid(True, axis="x", which="both", linestyle=":", linewidth=0.6)
    add_caption(
        "Figure 3. Week 10 improved Functions 1, 2 and 3, left Function 5 "
        "unchanged and produced lower outputs for Functions 4, 6, 7 and 8."
    )
    save_figure("week_10_figure_3_weekly_change.png")


def generate_strategy_allocation() -> None:
    """Generate a count of the evidence based Week 10 strategies."""

    strategy_order = ["Exploit", "Refine", "Reassess", "Explore"]
    counts = [
        sum(strategy == category for strategy in WEEK_10_STRATEGY.values())
        for category in strategy_order
    ]

    plt.figure(figsize=(9, 6))
    plt.bar(strategy_order, counts)
    plt.xlabel("Strategy")
    plt.ylabel("Number of functions")
    plt.title("Figure 4. Week 10 Strategy Allocation")
    plt.grid(True, axis="y", linestyle=":", linewidth=0.6)
    add_caption(
        "Figure 4. One function remains an exploitation target, four require "
        "refinement, two require reassessment and one remains exploratory."
    )
    save_figure("week_10_figure_4_strategy_allocation.png")


def generate_function_5_progress() -> None:
    """Generate the Function 5 optimisation trajectory."""

    weeks = list(WEEKLY_OUTPUT_TEXT)
    values = [float(Decimal(WEEKLY_OUTPUT_TEXT[week][4])) for week in weeks]

    plt.figure(figsize=(10, 6))
    plt.plot(weeks, values, marker="o", linewidth=2)
    plt.xticks(weeks)
    plt.xlabel("Optimisation round")
    plt.ylabel("Function 5 objective output")
    plt.title("Figure 5. Function 5 Progress Across Weeks 01 to 10")
    plt.grid(True, linestyle=":", linewidth=0.6)
    add_caption(
        "Figure 5. Function 5 increased strongly across the first nine rounds "
        "and remained exactly unchanged at 4394.868042481448 in Week 10."
    )
    save_figure("week_10_figure_5_function_5_progress.png")


def main() -> None:
    """Generate all Week 10 figures and their exact summary data."""

    data = build_dataframe()
    write_figure_data_summary()
    generate_output_evolution(data)
    generate_week_10_ranking()
    generate_weekly_change()
    generate_strategy_allocation()
    generate_function_5_progress()


if __name__ == "__main__":
    main()
