"""Run the RL-informed policy used to prepare the Week 13 BBO inputs.

The experiment uses only starter and Week 1 to Week 12 evidence to select an
action type for each function. Week 13 outputs are loaded only afterwards to
evaluate the selected policy. This is a deterministic, human-supervised policy
experiment, not a claim that a tabular Q-learning agent was trained.
"""

from __future__ import annotations

from pathlib import Path
import csv

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image


ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "BBO_Dashboard" / "data" / "complete_internal_evidence.csv"
WEEK13_INPUTS = ROOT / "Week_13" / "week_13_inputs.csv"
WEEK13_RESULTS = ROOT / "Week_13" / "week_13_results.csv"
OUT = Path(__file__).resolve().parent / "outputs"

ACTION_LABELS = {
    "retain": "Retain winner",
    "local": "Local refinement",
    "boundary": "Boundary refinement",
    "repeat": "Repeat for uncertainty",
}


def optimise_png(path: Path) -> None:
    """Reduce repository image size without changing its visible content."""
    with Image.open(path) as source:
        reduced = source.convert("P", palette=Image.Palette.ADAPTIVE, colors=128)
        reduced.save(path, optimize=True)


def coordinates(row: pd.Series) -> np.ndarray:
    values = [row[f"x{i}"] for i in range(1, 9) if pd.notna(row[f"x{i}"])]
    return np.asarray(values, dtype=float)


def load_history() -> pd.DataFrame:
    frame = pd.read_csv(DATA)
    weekly = frame[frame.source.str.match(r"week_\d+")].copy()
    weekly["week"] = weekly.source.str.extract(r"(\d+)").astype(int)
    return weekly[weekly.week <= 12].sort_values(["function", "week"])


def repeated_outputs(group: pd.DataFrame, point: np.ndarray) -> list[float]:
    matches = []
    for _, row in group.iterrows():
        candidate = coordinates(row)
        if candidate.shape == point.shape and np.allclose(candidate, point, atol=1e-12):
            matches.append(float(row.output))
    return matches


def state_and_policy(group: pd.DataFrame) -> dict[str, object]:
    group = group.sort_values("week")
    latest = group.iloc[-1]
    latest_point = coordinates(latest)
    outputs = group.output.astype(float).to_numpy()
    best = float(outputs.max())
    latest_is_best = bool(np.isclose(float(latest.output), best, atol=1e-12))
    repeats = repeated_outputs(group, latest_point)
    repeat_count = len(repeats)
    repeat_variable = repeat_count >= 2 and not np.allclose(repeats, repeats[0], atol=1e-12)
    repeat_stable = repeat_count >= 2 and np.allclose(repeats, repeats[0], atol=1e-12)
    recent_gain = float(outputs[-1] - outputs[-2])
    boundary_score = float(np.mean(np.minimum(latest_point, 1.0 - latest_point) <= 0.01))

    # Policy priority mirrors the final decision logic documented in Week 13.
    if repeat_stable and latest_is_best:
        action = "retain"
        reason = "Winning coordinate was reproduced exactly"
    elif latest_is_best and boundary_score >= 0.50 and recent_gain > 0:
        action = "boundary"
        reason = "Recent reward improved along an active boundary direction"
    elif latest_is_best and recent_gain > 0:
        action = "local"
        reason = "New best and recent gain supported controlled refinement"
    elif repeat_variable:
        action = "repeat"
        reason = "Repeated coordinate had not reliably reproduced its reward"
    elif latest_is_best or recent_gain > 0:
        action = "local"
        reason = "Recent local evidence supported a controlled refinement"
    else:
        action = "retain"
        reason = "No sufficiently rewarded direction justified final-round risk"

    return {
        "function": f"F{int(latest.function)}",
        "state_week": 12,
        "latest_reward": float(latest.output),
        "best_reward_to_week12": best,
        "recent_reward_change": recent_gain,
        "latest_is_best": latest_is_best,
        "repeat_count": repeat_count,
        "repeat_stable": repeat_stable,
        "repeat_variable": repeat_variable,
        "boundary_fraction": boundary_score,
        "selected_action": action,
        "selected_action_label": ACTION_LABELS[action],
        "policy_reason": reason,
    }


def load_week13_validation() -> dict[str, float]:
    results = pd.read_csv(WEEK13_RESULTS)
    return {
        f"F{int(str(row.iloc[0]).split()[-1])}": float(row.iloc[1])
        for _, row in results.iterrows()
    }


def make_policy_figure(frame: pd.DataFrame) -> None:
    colours = {
        "retain": "#3B82F6",
        "local": "#F59E0B",
        "boundary": "#10B981",
        "repeat": "#8B5CF6",
    }
    fig, ax = plt.subplots(figsize=(14, 7.5))
    ax.axis("off")
    fig.patch.set_facecolor("#F8FAFC")
    ax.text(0.02, 0.95, "Week 13 RL-Informed Decision Experiment", fontsize=23,
            weight="bold", color="#172033", transform=ax.transAxes)
    ax.text(0.02, 0.895,
            "State: verified Week 1-12 history   |   Action: next query policy   |   Reward: black-box output",
            fontsize=12, color="#475569", transform=ax.transAxes)

    y_positions = np.linspace(0.78, 0.12, len(frame))
    for y, (_, row) in zip(y_positions, frame.iterrows()):
        action = row.selected_action
        ax.add_patch(plt.Rectangle((0.02, y - 0.032), 0.075, 0.064,
                                   color=colours[action], transform=ax.transAxes))
        ax.text(0.0575, y, row.function, ha="center", va="center", color="white",
                weight="bold", fontsize=12, transform=ax.transAxes)
        ax.text(0.115, y + 0.014, row.selected_action_label, va="center", weight="bold",
                fontsize=12.5, color="#172033", transform=ax.transAxes)
        ax.text(0.115, y - 0.018, row.policy_reason, va="center", fontsize=10.5,
                color="#475569", transform=ax.transAxes)
        outcome = "New best" if row.week13_new_best else (
            "Best retained" if row.week13_retained_best else "Below Week 12 best"
        )
        outcome_colour = "#047857" if outcome != "Below Week 12 best" else "#B91C1C"
        ax.text(0.82, y + 0.010, outcome, va="center", fontsize=11.5, weight="bold",
                color=outcome_colour, transform=ax.transAxes)
        ax.text(0.82, y - 0.020, f"Week 13 reward: {row.week13_reward:.6g}", va="center",
                fontsize=9.8, color="#64748B", transform=ax.transAxes)

    ax.text(0.02, 0.035,
            "Executed from the Imperial_BBO_Capstone repository. Actions use Weeks 1-12; outcomes shown are the later portal returns.",
            fontsize=9.5, color="#64748B", transform=ax.transAxes)
    path = OUT / "rl_week13_policy_snapshot.png"
    fig.savefig(path, dpi=180, bbox_inches="tight")
    plt.close(fig)
    optimise_png(path)


def make_reward_figure(frame: pd.DataFrame) -> None:
    deltas = frame.week13_reward - frame.latest_reward
    observed_range = frame.reward_range_to_week12.replace(0, np.nan)
    normalised = (deltas / observed_range * 100).fillna(0.0)
    colours = ["#16A34A" if value > 0 else "#64748B" if value == 0 else "#DC2626" for value in normalised]
    fig, ax = plt.subplots(figsize=(12, 6.5), constrained_layout=True)
    fig.patch.set_facecolor("#F8FAFC")
    ax.set_facecolor("#FFFFFF")
    bars = ax.bar(frame.function, normalised, color=colours, width=0.64)
    ax.axhline(0, color="#334155", linewidth=1)
    fig.suptitle("Week 13 Reward Change After RL-Informed Action Selection", x=0.06,
                 ha="left", fontsize=20, weight="bold", color="#172033")
    ax.set_ylabel("Change as % of each function's Week 1-12 observed range")
    ax.grid(axis="y", alpha=0.18)
    ax.spines[["top", "right"]].set_visible(False)
    lower = min(float(normalised.min()), 0.0)
    upper = max(float(normalised.max()), 0.0)
    padding = max((upper - lower) * 0.16, 1.0)
    ax.set_ylim(lower - padding, upper + padding)
    for bar, value, raw in zip(bars, normalised, deltas):
        ax.text(bar.get_x() + bar.get_width() / 2, value,
                f"{value:.2f}%\n({raw:.6g})", ha="center", va="bottom" if value >= 0 else "top",
                fontsize=9.5, weight="bold")
    path = OUT / "rl_week13_reward_snapshot.png"
    fig.savefig(path, dpi=180, bbox_inches="tight")
    plt.close(fig)
    optimise_png(path)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    history = load_history()
    rows = [state_and_policy(group) for _, group in history.groupby("function")]
    frame = pd.DataFrame(rows)
    ranges = history.groupby("function").output.agg(lambda values: float(values.max() - values.min()))
    frame["reward_range_to_week12"] = frame.function.map({f"F{int(k)}": v for k, v in ranges.items()})
    validation = load_week13_validation()
    frame["week13_reward"] = frame.function.map(validation)
    frame["week13_new_best"] = frame.week13_reward > frame.best_reward_to_week12 + 1e-12
    frame["week13_retained_best"] = np.isclose(
        frame.week13_reward, frame.best_reward_to_week12, atol=1e-12
    )
    frame.to_csv(OUT / "rl_week13_policy_results.csv", index=False, quoting=csv.QUOTE_MINIMAL)
    make_policy_figure(frame)
    make_reward_figure(frame)
    print(frame[["function", "selected_action_label", "week13_reward", "week13_new_best"]].to_string(index=False))
    print(f"Outputs written to {OUT}")


if __name__ == "__main__":
    main()
