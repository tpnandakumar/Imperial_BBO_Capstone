from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
WEEK = ROOT / "Week_13"
FUNCTIONS = [f"Function {i}" for i in range(1, 9)]


def read_week(week: int) -> dict[str, float]:
    path = ROOT / f"Week_{week:02d}" / f"week_{week:02d}_results.csv"
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    return {row["function"]: float(row["output"]) for row in rows}


def save_final_change(history: dict[int, dict[str, float]]) -> None:
    changes = [history[13][f] - history[12][f] for f in FUNCTIONS]
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(FUNCTIONS, changes)
    ax.axhline(0, linewidth=1)
    ax.set_title("Week 12 to Week 13 objective change")
    ax.set_ylabel("Change")
    ax.tick_params(axis="x", rotation=45)
    fig.tight_layout()
    fig.savefig(WEEK / "week_13_figure_1_final_change.png", dpi=200)
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
            scaled = [(v - lo) / (hi - lo) for v in values]
        ax.plot(weeks, scaled, marker="o", label=function)
    ax.set_title("Within function progress across thirteen rounds")
    ax.set_xlabel("Round")
    ax.set_ylabel("Normalised within function performance")
    ax.set_xticks(weeks)
    ax.legend(ncol=2)
    fig.tight_layout()
    fig.savefig(WEEK / "week_13_figure_2_normalised_progress.png", dpi=200)
    plt.close(fig)


def save_function5(history: dict[int, dict[str, float]]) -> None:
    weeks = list(range(1, 14))
    values = [history[w]["Function 5"] for w in weeks]
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(weeks, values, marker="o")
    ax.set_title("Function 5 optimisation trajectory")
    ax.set_xlabel("Round")
    ax.set_ylabel("Objective value")
    ax.set_xticks(weeks)
    fig.tight_layout()
    fig.savefig(WEEK / "week_13_figure_3_function_5_trajectory.png", dpi=200)
    plt.close(fig)


def save_best_week(history: dict[int, dict[str, float]]) -> None:
    best_weeks = []
    for function in FUNCTIONS:
        values = [history[w][function] for w in range(1, 14)]
        best = max(values)
        best_weeks.append(max(w for w in range(1, 14) if history[w][function] == best))
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(FUNCTIONS, best_weeks)
    ax.set_title("Latest round in which each final best was observed")
    ax.set_ylabel("Round")
    ax.set_ylim(0, 13.5)
    ax.tick_params(axis="x", rotation=45)
    fig.tight_layout()
    fig.savefig(WEEK / "week_13_figure_4_latest_best_round.png", dpi=200)
    plt.close(fig)


def main() -> None:
    history = {week: read_week(week) for week in range(1, 14)}
    save_final_change(history)
    save_normalised_progress(history)
    save_function5(history)
    save_best_week(history)


if __name__ == "__main__":
    main()
