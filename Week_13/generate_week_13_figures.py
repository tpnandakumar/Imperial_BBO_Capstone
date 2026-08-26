from __future__ import annotations

import csv
from decimal import Decimal
from pathlib import Path

import matplotlib.pyplot as plt

from week_13_analysis import (
    FUNCTIONS,
    build_summary,
    load_history,
)

WEEK = Path(__file__).resolve().parent


def as_float_history(
    history: dict[int, dict[str, Decimal]],
) -> dict[int, dict[str, float]]:
    """Convert exact Decimals to floats only for plotting."""
    return {
        week: {function: float(value) for function, value in values.items()}
        for week, values in history.items()
    }


def write_figure_data_summary(summary_rows: list[dict[str, str]]) -> Path:
    """Write exact source data used by the Week 13 figures."""
    path = WEEK / "week_13_figure_data_summary.csv"
    fieldnames = [
        "function",
        "week_12_output",
        "week_13_output",
        "exact_change",
        "l1_input_movement",
        "squared_euclidean_movement",
        "identical_input",
        "repeatability_result",
        "best_output",
        "latest_best_round",
    ]

    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in summary_rows:
            best_weeks = [
                int(value) for value in row["best_week_or_weeks"].split(";")
            ]
            writer.writerow(
                {
                    "function": row["function"],
                    "week_12_output": row["week_12_output"],
                    "week_13_output": row["week_13_output"],
                    "exact_change": row["exact_change"],
                    "l1_input_movement": row["l1_input_movement"],
                    "squared_euclidean_movement": row[
                        "squared_euclidean_movement"
                    ],
                    "identical_input": row["identical_input"],
                    "repeatability_result": row["repeatability_result"],
                    "best_output": row["best_output"],
                    "latest_best_round": max(best_weeks),
                }
            )
    return path


def save_final_change(history: dict[int, dict[str, float]]) -> None:
    changes = [history[13][f] - history[12][f] for f in FUNCTIONS]
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(FUNCTIONS, changes)
    ax.axhline(0, linewidth=1)
    ax.set_title("Week 12 to Week 13 objective change")
    ax.set_ylabel("Change in objective output")
    ax.tick_params(axis="x", rotation=45)
    fig.tight_layout()
    fig.savefig(WEEK / "week_13_figure_1_final_change.png", dpi=300)
    plt.close(fig)


def save_normalised_progress(history: dict[int, dict[str, float]]) -> None:
    fig, ax = plt.subplots(figsize=(11, 6))
    weeks = list(range(1, 14))
    for function in FUNCTIONS:
        values = [history[w][function] for w in weeks]
        lo, hi = min(values), max(values)
        if hi == lo:
            scaled = [0.0 for _ in values]
        else:
            scaled = [(value - lo) / (hi - lo) for value in values]
        ax.plot(weeks, scaled, marker="o", label=function)
    ax.set_title("Within function progress across thirteen rounds")
    ax.set_xlabel("Round")
    ax.set_ylabel("Normalised within function performance")
    ax.set_xticks(weeks)
    ax.legend(ncol=2)
    fig.tight_layout()
    fig.savefig(WEEK / "week_13_figure_2_normalised_progress.png", dpi=300)
    plt.close(fig)


def save_function5(history: dict[int, dict[str, float]]) -> None:
    weeks = list(range(1, 14))
    values = [history[w]["Function 5"] for w in weeks]
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(weeks, values, marker="o")
    ax.set_title("Function 5 optimisation trajectory")
    ax.set_xlabel("Round")
    ax.set_ylabel("Objective output")
    ax.set_xticks(weeks)
    fig.tight_layout()
    fig.savefig(WEEK / "week_13_figure_3_function_5_trajectory.png", dpi=300)
    plt.close(fig)


def save_best_week(summary_rows: list[dict[str, str]]) -> None:
    latest_best = [
        max(int(value) for value in row["best_week_or_weeks"].split(";"))
        for row in summary_rows
    ]
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(FUNCTIONS, latest_best)
    ax.set_title("Latest round in which each final best was observed")
    ax.set_ylabel("Round")
    ax.set_ylim(0, 13.5)
    ax.tick_params(axis="x", rotation=45)
    fig.tight_layout()
    fig.savefig(WEEK / "week_13_figure_4_latest_best_round.png", dpi=300)
    plt.close(fig)


def save_movement_against_change(summary_rows: list[dict[str, str]]) -> None:
    movement = [
        float(Decimal(row["l1_input_movement"])) for row in summary_rows
    ]
    output_change = [
        float(Decimal(row["exact_change"])) for row in summary_rows
    ]

    fig, ax = plt.subplots(figsize=(9, 6))
    ax.scatter(movement, output_change)
    ax.axhline(0, linewidth=1)
    for row, x_value, y_value in zip(summary_rows, movement, output_change):
        ax.annotate(
            row["function"].replace("Function ", "F"),
            (x_value, y_value),
        )
    ax.set_title("Final query movement against objective change")
    ax.set_xlabel("L1 input movement from Week 12")
    ax.set_ylabel("Week 13 minus Week 12 objective output")
    fig.tight_layout()
    fig.savefig(WEEK / "week_13_figure_5_movement_vs_change.png", dpi=300)
    plt.close(fig)


def main() -> None:
    decimal_history, inputs = load_history()
    summary_rows = build_summary(decimal_history, inputs)
    figure_data_path = write_figure_data_summary(summary_rows)
    history = as_float_history(decimal_history)

    save_final_change(history)
    save_normalised_progress(history)
    save_function5(history)
    save_best_week(summary_rows)
    save_movement_against_change(summary_rows)

    print(f"Wrote {figure_data_path}")
    print(f"Wrote Week 13 figures to {WEEK}")


if __name__ == "__main__":
    main()
