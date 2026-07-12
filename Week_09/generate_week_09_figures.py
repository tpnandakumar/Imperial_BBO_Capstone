
"""
Week 09 Figure Generation Script
Imperial BBO Capstone

This script generates the analytical figures used in the Week 09 README.

The source values are preserved at full precision. No optimisation
outputs are rounded or truncated in the underlying data.
"""

from __future__ import annotations

from decimal import Decimal
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


CURRENT_DIRECTORY = Path(__file__).resolve().parent
OUTPUT_DIRECTORY = CURRENT_DIRECTORY
DPI = 300


FUNCTIONS = [
    "Function 1",
    "Function 2",
    "Function 3",
    "Function 4",
    "Function 5",
    "Function 6",
    "Function 7",
    "Function 8",
]


WEEKLY_OUTPUT_TEXT = {
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
}


WEEK_09_STRATEGY = {
    "Function 1": "Explore",
    "Function 2": "Refine",
    "Function 3": "Reassess",
    "Function 4": "Refine",
    "Function 5": "Exploit",
    "Function 6": "Reassess",
    "Function 7": "Refine",
    "Function 8": "Refine",
}


INFORMATION_GAIN_SCORE = {
    "Function 1": 10,
    "Function 2": 48,
    "Function 3": 28,
    "Function 4": 40,
    "Function 5": 95,
    "Function 6": 25,
    "Function 7": 58,
    "Function 8": 65,
}


RESOURCE_ALLOCATION = {
    "Function 1": 12,
    "Function 2": 20,
    "Function 3": 3,
    "Function 4": 7,
    "Function 5": 35,
    "Function 6": 3,
    "Function 7": 10,
    "Function 8": 10,
}


def build_dataframe() -> pd.DataFrame:
    """Create a long-form DataFrame containing Weeks 01 to 09."""

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
    """Save the active figure at 300 DPI and close it."""

    output_path = OUTPUT_DIRECTORY / filename
    plt.tight_layout()
    plt.savefig(output_path, dpi=DPI, bbox_inches="tight")
    plt.close()
    print(f"Created: {output_path.name}")


def add_caption(text: str) -> None:
    """Add an embedded caption beneath the chart."""

    plt.figtext(
        0.05,
        0.015,
        text,
        ha="left",
        va="bottom",
        wrap=True,
        fontsize=9,
    )


def generate_figure_1a(data: pd.DataFrame) -> None:
    """Generate Figure 1A, output evolution across Weeks 01 to 09."""

    plt.figure(figsize=(14, 9))

    for function_name in FUNCTIONS:
        subset = data[data["Function"] == function_name]

        plt.plot(
            subset["Week"],
            subset["Output"],
            marker="o",
            linewidth=2,
            label=function_name,
        )

    plt.axhline(0, linewidth=1)
    plt.yscale("symlog", linthresh=0.01)
    plt.xticks(range(1, 10))
    plt.xlabel("Optimisation round")
    plt.ylabel("Objective function output")
    plt.title("Figure 1A. Function Output Evolution, Weeks 01 to 09")
    plt.grid(True, linestyle=":", linewidth=0.7)
    plt.legend(title="Functions", ncol=2)

    add_caption(
        "Caption: This figure tracks the objective function outputs across "
        "nine optimisation rounds. Function 5 continues to dominate and "
        "reaches 4394.868042481448 in Week 09. Functions 8 and 7 remain "
        "stable positive performers, while Function 1 remains effectively "
        "equal to zero."
    )

    plt.subplots_adjust(bottom=0.16)

    save_figure(
        "figure_1A_function_output_evolution_weeks_01_to_09.png"
    )


def generate_figure_1b(data: pd.DataFrame) -> None:
    """Generate Figure 1B, Week 09 function performance ranking."""

    week_09 = (
        data[data["Week"] == 9]
        .sort_values("Output", ascending=True)
        .copy()
    )

    plt.figure(figsize=(13, 8))

    bars = plt.barh(
        week_09["Function"],
        week_09["Output"],
    )

    for bar, output_text, output in zip(
        bars,
        week_09["Output_Text"],
        week_09["Output"],
    ):
        if output >= 0:
            alignment = "left"
        else:
            alignment = "right"

        plt.text(
            output,
            bar.get_y() + bar.get_height() / 2,
            output_text,
            va="center",
            ha=alignment,
            fontsize=8,
        )

    plt.axvline(0, linewidth=1)
    plt.xlabel("Week 09 objective output")
    plt.ylabel("Function")
    plt.title("Figure 1B. Week 09 Function Performance Ranking")
    plt.grid(True, axis="x", linestyle=":", linewidth=0.7)

    add_caption(
        "Caption: This figure ranks the eight objective functions using "
        "their exact Week 09 outputs. Function 5 remains first with "
        "4394.868042481448, followed by Functions 8, 7 and 2. Function 1 "
        "remains effectively zero, while Functions 3, 6 and 4 remain "
        "within negative regions."
    )

    plt.subplots_adjust(bottom=0.17)

    save_figure(
        "figure_1B_week_09_function_performance_ranking.png"
    )


def generate_figure_1c(data: pd.DataFrame) -> None:
    """Generate Figure 1C, exact Week 08 to Week 09 changes."""

    week_08 = (
        data[data["Week"] == 8]
        .set_index("Function")
        .loc[FUNCTIONS]
    )

    week_09 = (
        data[data["Week"] == 9]
        .set_index("Function")
        .loc[FUNCTIONS]
    )

    comparison = pd.DataFrame(index=FUNCTIONS)
    comparison["Week_08"] = week_08["Output"]
    comparison["Week_09"] = week_09["Output"]
    comparison["Change"] = (
        comparison["Week_09"] - comparison["Week_08"]
    )

    exact_changes = {
        function_name: str(
            Decimal(
                week_09.loc[function_name, "Output_Text"]
            )
            - Decimal(
                week_08.loc[function_name, "Output_Text"]
            )
        )
        for function_name in FUNCTIONS
    }

    comparison = comparison.sort_values("Change")

    plt.figure(figsize=(13, 8))

    bars = plt.barh(
        comparison.index,
        comparison["Change"],
    )

    for bar, function_name, change in zip(
        bars,
        comparison.index,
        comparison["Change"],
    ):
        alignment = "left" if change >= 0 else "right"

        plt.text(
            change,
            bar.get_y() + bar.get_height() / 2,
            exact_changes[function_name],
            va="center",
            ha=alignment,
            fontsize=8,
        )

    plt.axvline(0, linewidth=1)
    plt.xlabel("Exact change from Week 08 to Week 09")
    plt.ylabel("Function")
    plt.title("Figure 1C. Week 08 vs Week 09 Performance Change")
    plt.grid(True, axis="x", linestyle=":", linewidth=0.7)

    add_caption(
        "Caption: This figure compares the Week 08 and Week 09 results. "
        "Function 5 increased by 35.483908158745 and Function 4 improved "
        "by 0.516068928028744. Functions 2, 3, 6, 7 and 8 declined, while "
        "Function 1 remained unchanged."
    )

    plt.subplots_adjust(bottom=0.17)

    save_figure(
        "figure_1C_week_08_vs_week_09_performance_change.png"
    )


def generate_figure_3a(data: pd.DataFrame) -> None:
    """Generate Figure 3A, ranking evolution across nine weeks."""

    ranked = data.copy()

    ranked["Rank"] = ranked.groupby("Week")["Output"].rank(
        ascending=False,
        method="min",
    )

    plt.figure(figsize=(14, 9))

    for function_name in FUNCTIONS:
        subset = ranked[
            ranked["Function"] == function_name
        ].sort_values("Week")

        plt.plot(
            subset["Week"],
            subset["Rank"],
            marker="o",
            linewidth=2,
            label=function_name,
        )

    plt.gca().invert_yaxis()
    plt.xticks(range(1, 10))
    plt.yticks(range(1, 9))
    plt.xlabel("Optimisation round")
    plt.ylabel("Rank, where 1 is highest")
    plt.title(
        "Figure 3A. Functional Ranking Evolution, Weeks 01 to 09"
    )
    plt.grid(True, linestyle=":", linewidth=0.7)
    plt.legend(title="Functions", ncol=2)

    add_caption(
        "Caption: This figure shows the ranking evolution of all eight "
        "objective functions across nine optimisation rounds. Function 5 "
        "remains the highest ranked function, while Functions 8 and 7 "
        "retain second and third positions. Function 1 remains near zero, "
        "and Functions 3, 6 and 4 occupy the lower rankings."
    )

    plt.subplots_adjust(bottom=0.16)

    save_figure(
        "figure_3A_functional_ranking_evolution_weeks_01_to_09.png"
    )


def generate_figure_4(data: pd.DataFrame) -> None:
    """Generate Figure 4, Function 5 optimisation progress."""

    function_5 = data[
        data["Function"] == "Function 5"
    ].sort_values("Week")

    plt.figure(figsize=(13, 8))

    plt.plot(
        function_5["Week"],
        function_5["Output"],
        marker="o",
        linewidth=3,
    )

    for _, row in function_5.iterrows():
        plt.annotate(
            row["Output_Text"],
            (row["Week"], row["Output"]),
            xytext=(0, 10),
            textcoords="offset points",
            ha="center",
            fontsize=8,
        )

    plt.xticks(range(1, 10))
    plt.xlabel("Optimisation round")
    plt.ylabel("Function 5 objective output")
    plt.title(
        "Figure 4. Function 5 Optimisation Progress, Weeks 01 to 09"
    )
    plt.grid(True, linestyle=":", linewidth=0.7)

    add_caption(
        "Caption: This figure illustrates the optimisation progress of "
        "Function 5 across nine rounds. Its objective value increased from "
        "1415.8763939603884 in Week 01 to 4394.868042481448 in Week 09. "
        "The uninterrupted upward trajectory supports continued local "
        "exploitation of the current search region."
    )

    plt.subplots_adjust(bottom=0.17)

    save_figure(
        "figure_4_function_5_optimisation_progress_weeks_01_to_09.png"
    )


def generate_figure_4a() -> None:
    """Generate Figure 4A, Week 10 resource allocation decision."""

    allocation = pd.Series(RESOURCE_ALLOCATION).sort_values()

    plt.figure(figsize=(12, 8))

    bars = plt.barh(
        allocation.index,
        allocation.values,
    )

    for bar, value in zip(bars, allocation.values):
        plt.text(
            value,
            bar.get_y() + bar.get_height() / 2,
            f"{value}%",
            va="center",
            ha="left",
        )

    plt.xlabel("Recommended Week 10 resource allocation")
    plt.ylabel("Function")
    plt.title(
        "Figure 4A. Resource Allocation Decision Matrix, Week 09"
    )
    plt.xlim(0, max(allocation.values) + 5)
    plt.grid(True, axis="x", linestyle=":", linewidth=0.7)

    add_caption(
        "Caption: This figure presents the proposed allocation of the "
        "Week 10 query effort based on Week 09 performance. Function 5 "
        "receives the highest allocation for continued exploitation. "
        "Functions 2, 7 and 8 receive refinement priority, while Function "
        "1 remains the principal exploration target."
    )

    plt.subplots_adjust(bottom=0.17)

    save_figure(
        "figure_4A_week_09_resource_allocation_decision_matrix.png"
    )


def generate_figure_5() -> None:
    """Generate Figure 5, information gain summary."""

    scores = pd.Series(INFORMATION_GAIN_SCORE).sort_values()

    plt.figure(figsize=(12, 8))

    bars = plt.barh(
        scores.index,
        scores.values,
    )

    for bar, value in zip(bars, scores.values):
        plt.text(
            value,
            bar.get_y() + bar.get_height() / 2,
            str(value),
            va="center",
            ha="left",
        )

    plt.xlabel("Information gain score")
    plt.ylabel("Function")
    plt.title("Figure 5. Information Gain Summary, Week 09")
    plt.xlim(0, 105)
    plt.grid(True, axis="x", linestyle=":", linewidth=0.7)

    add_caption(
        "Caption: This figure summarises the information gained from the "
        "Week 09 queries. Function 5 provides the highest information gain "
        "because it combines improved output with low uncertainty. "
        "Functions 8, 7, 2 and 4 provide useful supporting evidence, while "
        "Function 1 remains the least informative and requires broader "
        "exploration."
    )

    plt.subplots_adjust(bottom=0.17)

    save_figure(
        "figure_5_week_09_information_gain_summary.png"
    )


def generate_figure_5a() -> None:
    """Generate a simple computational workflow diagram."""

    steps = [
        "Input CSV files",
        "Validate data",
        "Calculate changes",
        "Rank functions",
        "Assign strategy",
        "Generate outputs",
    ]

    x_positions = np.arange(len(steps))

    plt.figure(figsize=(15, 5))
    plt.scatter(x_positions, np.zeros(len(steps)), s=1800)

    for index, step in enumerate(steps):
        plt.text(
            index,
            0,
            str(index + 1),
            ha="center",
            va="center",
            fontsize=14,
        )
        plt.text(
            index,
            -0.18,
            step,
            ha="center",
            va="top",
            fontsize=10,
        )

        if index < len(steps) - 1:
            plt.annotate(
                "",
                xy=(index + 0.8, 0),
                xytext=(index + 0.2, 0),
                arrowprops={"arrowstyle": "->", "linewidth": 2},
            )

    plt.xlim(-0.5, len(steps) - 0.5)
    plt.ylim(-0.5, 0.4)
    plt.axis("off")
    plt.title("Figure 5A. Python Computational Workflow, Week 09")

    add_caption(
        "Caption: This figure illustrates the Week 09 Python workflow. "
        "Structured CSV files are validated and processed before exact "
        "changes, rankings and optimisation strategies are calculated. "
        "The workflow then generates reproducible summary tables, figures "
        "and documentation."
    )

    plt.subplots_adjust(bottom=0.2)

    save_figure(
        "figure_5A_week_09_python_computational_workflow.png"
    )


def generate_figure_5b() -> None:
    """Generate a simplified Week 09 repository workflow diagram."""

    files = [
        "week_09_inputs.csv",
        "week_09_results.csv",
        "week_09_analysis.py",
        "week_09_analysis_summary.csv",
        "generate_week_09_figures.py",
        "README.md",
    ]

    x_positions = np.arange(len(files))

    plt.figure(figsize=(16, 6))
    plt.scatter(x_positions, np.zeros(len(files)), s=2000)

    for index, filename in enumerate(files):
        plt.text(
            index,
            0,
            str(index + 1),
            ha="center",
            va="center",
            fontsize=14,
        )
        plt.text(
            index,
            -0.18,
            filename,
            ha="center",
            va="top",
            fontsize=9,
            rotation=15,
        )

        if index < len(files) - 1:
            plt.annotate(
                "",
                xy=(index + 0.8, 0),
                xytext=(index + 0.2, 0),
                arrowprops={"arrowstyle": "->", "linewidth": 2},
            )

    plt.xlim(-0.5, len(files) - 0.5)
    plt.ylim(-0.65, 0.4)
    plt.axis("off")
    plt.title("Figure 5B. Week 09 Repository Structure and Workflow")

    add_caption(
        "Caption: This figure shows the Week 09 file workflow. Exact query "
        "inputs and returned outputs are processed by the analysis script, "
        "which produces the summary dataset. The figure generation script "
        "creates the analytical visualisations used in the README. This "
        "structure supports transparency and reproducibility."
    )

    plt.subplots_adjust(bottom=0.23)

    save_figure(
        "figure_5B_week_09_repository_structure_and_workflow.png"
    )


def generate_figure_5c(data: pd.DataFrame) -> None:
    """Generate Figure 5C, Week 09 conclusions dashboard."""

    week_09 = (
        data[data["Week"] == 9]
        .sort_values("Output", ascending=True)
        .copy()
    )

    plt.figure(figsize=(13, 8))

    bars = plt.barh(
        week_09["Function"],
        week_09["Output"],
    )

    for bar, output_text, output in zip(
        bars,
        week_09["Output_Text"],
        week_09["Output"],
    ):
        alignment = "left" if output >= 0 else "right"

        plt.text(
            output,
            bar.get_y() + bar.get_height() / 2,
            output_text,
            va="center",
            ha=alignment,
            fontsize=8,
        )

    plt.axvline(0, linewidth=1)
    plt.xlabel("Week 09 objective output")
    plt.ylabel("Function")
    plt.title("Figure 5C. Week 09 Conclusions and Strategic Outlook")
    plt.grid(True, axis="x", linestyle=":", linewidth=0.7)

    add_caption(
        "Caption: This figure summarises the Week 09 position. Function 5 "
        "remains the strongest exploitation target. Functions 8 and 7 "
        "remain stable positive performers, while Function 2 requires "
        "careful refinement. Function 4 is improving within a negative "
        "region, Functions 3 and 6 require reassessment, and Function 1 "
        "remains the main exploration priority."
    )

    plt.subplots_adjust(bottom=0.18)

    save_figure(
        "figure_5C_week_09_conclusions_and_strategic_outlook.png"
    )


def export_figure_data(data: pd.DataFrame) -> None:
    """Export the exact data used by the Week 09 figures."""

    week_08 = (
        data[data["Week"] == 8]
        .set_index("Function")
        .loc[FUNCTIONS]
    )

    week_09 = (
        data[data["Week"] == 9]
        .set_index("Function")
        .loc[FUNCTIONS]
    )

    rows: list[dict[str, object]] = []

    for function_name in FUNCTIONS:
        week_08_text = week_08.loc[
            function_name,
            "Output_Text",
        ]
        week_09_text = week_09.loc[
            function_name,
            "Output_Text",
        ]

        change = (
            Decimal(week_09_text)
            - Decimal(week_08_text)
        )

        rows.append(
            {
                "Function": function_name,
                "Week_08_Output": week_08_text,
                "Week_09_Output": week_09_text,
                "Exact_Change": str(change),
                "Strategy": WEEK_09_STRATEGY[function_name],
                "Information_Gain_Score": INFORMATION_GAIN_SCORE[
                    function_name
                ],
                "Resource_Allocation_Percent": RESOURCE_ALLOCATION[
                    function_name
                ],
            }
        )

    output_path = (
        OUTPUT_DIRECTORY / "week_09_figure_data_summary.csv"
    )

    pd.DataFrame(rows).to_csv(output_path, index=False)

    print(f"Created: {output_path.name}")


def main() -> None:
    """Generate every Week 09 analytical figure."""

    data = build_dataframe()

    generate_figure_1a(data)
    generate_figure_1b(data)
    generate_figure_1c(data)
    generate_figure_3a(data)
    generate_figure_4(data)
    generate_figure_4a()
    generate_figure_5()
    generate_figure_5a()
    generate_figure_5b()
    generate_figure_5c(data)
    export_figure_data(data)

    print()
    print("All Week 09 figures were generated successfully.")


if __name__ == "__main__":
    main()
