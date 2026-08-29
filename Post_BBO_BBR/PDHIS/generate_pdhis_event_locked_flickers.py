"""Event-locked retrospective characterisation of pre-event Delta flickers."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
FIG = OUT / "infographics"
DATA = ROOT / "BBO_Dashboard" / "data" / "complete_internal_evidence.csv"
WINDOW_OUTPUTS = 6
RANDOM_SEED = 83
N_PERMUTATIONS = 500

FEATURES = {
    "amplitude": "Peak amplitude",
    "energy": "Oscillation energy",
    "temporal_dispersion": "Temporal dispersion",
    "sign_change_rate": "Sign-change frequency",
    "peak_spacing": "Peak spacing",
    "persistence": "Directional persistence",
    "amplification": "Late amplification",
    "delta2_energy": "Delta 2 energy",
    "flicker_density": "Flicker density",
}


def load_weekly() -> pd.DataFrame:
    frame = pd.read_csv(DATA)
    frame = frame[frame.source.str.fullmatch(r"week_\d{2}", na=False)].copy()
    frame["week"] = frame.source.str.extract(r"(\d+)").astype(int)
    frame = frame.sort_values(["function", "week"])
    if len(frame) != 104 or not (frame.groupby("function").size() == 13).all():
        raise ValueError("Expected eight functions with thirteen weekly outputs each.")
    return frame[["function", "week", "output"]]


def safe_scale(values: np.ndarray) -> float:
    nonzero = np.abs(values[np.abs(values) > 1e-12])
    return float(np.median(nonzero)) if len(nonzero) else 1.0


def longest_sign_run(values: np.ndarray) -> int:
    signs = np.sign(values)
    best = current = 1
    for index in range(1, len(signs)):
        current = current + 1 if signs[index] == signs[index - 1] else 1
        best = max(best, current)
    return best


def behaviour_label(d1: np.ndarray, amplification: float, sign_change_rate: float) -> str:
    if sign_change_rate >= 0.75:
        return "Amplifying oscillation" if amplification > 0.25 else "Damped oscillation" if amplification < -0.25 else "Stable oscillation"
    if sign_change_rate >= 0.5:
        return "Intermittent oscillation"
    if longest_sign_run(d1) >= 4:
        return "Directed movement"
    return "Irregular flicker"


def fingerprint(history: np.ndarray, scale: float) -> dict[str, object]:
    d1 = np.diff(history) / scale
    d2 = np.diff(d1)
    positions = np.arange(1, len(d1) + 1, dtype=float)
    weights = d1 ** 2
    weight_sum = weights.sum()
    centre = float(np.average(positions, weights=weights)) if weight_sum else positions.mean()
    dispersion = float(np.sqrt(np.average((positions - centre) ** 2, weights=weights))) if weight_sum else 0.0
    switches = np.flatnonzero(d1[1:] * d1[:-1] < 0) + 1
    sign_change_rate = float(len(switches) / max(1, len(d1) - 1))
    peak_spacing = float(np.diff(switches).mean()) if len(switches) >= 2 else float(len(d1))
    early = float(np.mean(np.abs(d1[:2])))
    late = float(np.mean(np.abs(d1[-2:])))
    amplification = float(np.log2((late + 0.1) / (early + 0.1)))
    threshold = 1.5
    flickers = np.flatnonzero(np.abs(d1) > threshold)
    return {
        "amplitude": float(np.max(np.abs(d1))),
        "energy": float(np.mean(d1 ** 2)),
        "temporal_dispersion": dispersion,
        "sign_change_rate": sign_change_rate,
        "peak_spacing": peak_spacing,
        "persistence": longest_sign_run(d1) / len(d1),
        "amplification": amplification,
        "delta2_energy": float(np.mean(d2 ** 2)),
        "flicker_density": len(flickers) / len(d1),
        "first_flicker_lag": int(flickers[0] - len(d1)) if len(flickers) else np.nan,
        "behaviour": behaviour_label(d1, amplification, sign_change_rate),
    }


def build_cases(weekly: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for function, group in weekly.groupby("function"):
        group = group.sort_values("week")
        outputs = group.output.to_numpy(float)
        weeks = group.week.to_numpy(int)
        for target_index in range(WINDOW_OUTPUTS, len(outputs)):
            prior_outputs = outputs[target_index - WINDOW_OUTPUTS:target_index]
            prior_d1 = np.diff(outputs[:target_index])
            scale = safe_scale(prior_d1)
            current_change = outputs[target_index] - outputs[target_index - 1]
            large_threshold = 1.5 * scale
            record = {
                "function": function,
                "event_week": weeks[target_index],
                "current_change": current_change,
                "positive_event": int(current_change > 0),
                "large_event": int(abs(current_change) > large_threshold),
                "new_best_event": int(outputs[target_index] > np.max(outputs[:target_index])),
                "large_event_threshold": large_threshold,
            }
            record.update(fingerprint(prior_outputs, scale))
            rows.append(record)
    cases = pd.DataFrame(rows)
    if len(cases) != 56:
        raise ValueError("Expected 56 event-locked windows.")
    return cases


def holm_adjust(p_values: pd.Series) -> pd.Series:
    order = np.argsort(p_values.to_numpy())
    adjusted = np.empty(len(p_values), dtype=float)
    running = 0.0
    for rank, index in enumerate(order):
        candidate = min(1.0, (len(p_values) - rank) * p_values.iloc[index])
        running = max(running, candidate)
        adjusted[index] = running
    return pd.Series(adjusted, index=p_values.index)


def association_summary(cases: pd.DataFrame) -> pd.DataFrame:
    rng = np.random.default_rng(RANDOM_SEED)
    rows: list[dict[str, object]] = []
    for target in ["positive_event", "large_event", "new_best_event"]:
        for feature, label in FEATURES.items():
            event = cases[cases[target] == 1][feature].to_numpy(float)
            non_event = cases[cases[target] == 0][feature].to_numpy(float)
            observed = float(event.mean() - non_event.mean())
            pooled = float(cases[feature].std(ddof=1))
            standardised = observed / pooled if pooled > 0 else 0.0
            null = []
            for _ in range(N_PERMUTATIONS):
                shuffled = cases.groupby("function")[target].transform(
                    lambda values: rng.permutation(values.to_numpy())
                )
                null.append(cases.loc[shuffled == 1, feature].mean() - cases.loc[shuffled == 0, feature].mean())
            p_value = (1 + sum(abs(value) >= abs(observed) for value in null)) / (N_PERMUTATIONS + 1)
            rows.append({
                "target": target,
                "feature": feature,
                "feature_label": label,
                "cases": len(cases),
                "events": int(cases[target].sum()),
                "event_mean": event.mean(),
                "non_event_mean": non_event.mean(),
                "mean_difference": observed,
                "standardised_difference": standardised,
                "permutation_p": p_value,
            })
    summary = pd.DataFrame(rows)
    summary["holm_p"] = summary.groupby("target", group_keys=False).permutation_p.apply(holm_adjust)
    return summary


def behaviour_summary(cases: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for behaviour, group in cases.groupby("behaviour"):
        rows.append({
            "behaviour": behaviour,
            "windows": len(group),
            "positive_event_rate": group.positive_event.mean(),
            "large_event_rate": group.large_event.mean(),
            "new_best_event_rate": group.new_best_event.mean(),
        })
    return pd.DataFrame(rows).sort_values("windows", ascending=False)


def make_figure(summary: pd.DataFrame, behaviours: pd.DataFrame) -> None:
    target_labels = {"positive_event": "Any improvement", "large_event": "Large change", "new_best_event": "New best"}
    pivot = summary.pivot(index="feature_label", columns="target", values="standardised_difference")
    pivot = pivot[["positive_event", "large_event", "new_best_event"]]
    fig, axes = plt.subplots(1, 2, figsize=(14, 6.5), gridspec_kw={"width_ratios": [1.35, 1]})
    image = axes[0].imshow(pivot.to_numpy(), cmap="RdBu_r", vmin=-1, vmax=1, aspect="auto")
    axes[0].set_xticks(range(3), [target_labels[column] for column in pivot.columns])
    axes[0].set_yticks(range(len(pivot)), pivot.index)
    axes[0].set_title("Pre-event flicker characteristics", weight="bold")
    for row in range(len(pivot)):
        for col in range(3):
            axes[0].text(col, row, f"{pivot.iloc[row, col]:.2f}", ha="center", va="center", fontsize=9)
    fig.colorbar(image, ax=axes[0], fraction=0.035, pad=0.03, label="Standardised event minus non-event difference")

    ordered = behaviours.sort_values("large_event_rate")
    axes[1].barh(ordered.behaviour, ordered.large_event_rate, color="#6f9d8b")
    for row, (_, item) in enumerate(ordered.iterrows()):
        axes[1].text(item.large_event_rate + 0.015, row, f"n={int(item.windows)}", va="center", fontsize=9)
    axes[1].set_xlim(0, 1)
    axes[1].set_xlabel("Large-event rate")
    axes[1].set_title("Behavioural shape before large events", weight="bold")
    axes[1].grid(axis="x", alpha=0.2)
    fig.suptitle("PDHIS event-locked flicker characterisation", fontsize=18, weight="bold", color="#14213d")
    fig.text(0.5, 0.015, "Each case uses six observations before the target week. Associations are retrospective and exploratory.", ha="center", fontsize=10)
    fig.tight_layout(rect=[0, 0.045, 1, 0.93])
    FIG.mkdir(exist_ok=True)
    fig.savefig(FIG / "PDHIS-22_event_locked_flicker_characterisation.jpg", dpi=180, bbox_inches="tight")
    plt.close(fig)


def write_findings(cases: pd.DataFrame, summary: pd.DataFrame, behaviours: pd.DataFrame) -> None:
    best = summary.loc[summary.permutation_p.idxmin()]
    event_counts = {target: int(cases[target].sum()) for target in ["positive_event", "large_event", "new_best_event"]}
    behaviour_lines = ["| Pre-event behaviour | Windows | Improvement rate | Large-event rate | New-best rate |", "| --- | ---: | ---: | ---: | ---: |"]
    for row in behaviours.itertuples():
        behaviour_lines.append(f"| {row.behaviour} | {row.windows} | {row.positive_event_rate:.3f} | {row.large_event_rate:.3f} | {row.new_best_event_rate:.3f} |")
    text = [
        "# PDHIS event-locked flicker characterisation",
        "",
        "## Question",
        "",
        "Looking backwards from a known event, did the preceding six observations contain a flicker with a characteristic temporal fingerprint?",
        "",
        "## Design",
        "",
        f"The analysis contains {len(cases)} event-locked windows across eight functions. The targets are known outcomes: {event_counts['positive_event']} improvements, {event_counts['large_event']} large function-adjusted changes and {event_counts['new_best_event']} new best outputs. Each target week is compared with the six observations immediately before it.",
        "",
        "The fingerprint measures peak amplitude, oscillation energy, temporal dispersion, sign-change frequency, peak spacing, directional persistence, late amplification, Delta 2 energy and flicker density. Scaling uses only observations available before the target week.",
        "",
        "## Main result",
        "",
        f"The smallest exploratory within-function permutation p value was {best.permutation_p:.3f} for {best.feature_label.lower()} against {best.target.replace('_', ' ')}. Its Holm-adjusted p value was {best.holm_p:.3f}. No characteristic should be treated as confirmed unless its adjusted result remains below the defined threshold and it is reproduced prospectively.",
        "",
        "## Behavioural shapes",
        "",
        *behaviour_lines,
        "",
        "## Interpretation",
        "",
        "This is an event-locked retrospective analysis. It characterises what was present before outcomes already known to have happened or not happened. It does not allow a later event to enter the flicker calculation. The analysis can identify candidate signatures, but the same locked fingerprint must predict untouched later events before it can be described as an early warning signal.",
        "",
        "Weekly sampling and thirteen observations per function limit frequency resolution. Sign-change rate and peak spacing are therefore used instead of a conventional frequency spectrum.",
        "",
        "## Reproducibility",
        "",
        "Run `python Post_BBO_BBR/PDHIS/generate_pdhis_event_locked_flickers.py` from the repository root.",
        "",
    ]
    (OUT / "PDHIS_EVENT_LOCKED_FLICKERS.md").write_text("\n".join(text), encoding="utf-8")


def main() -> None:
    cases = build_cases(load_weekly())
    summary = association_summary(cases)
    behaviours = behaviour_summary(cases)
    cases.to_csv(OUT / "PDHIS_EVENT_LOCKED_FLICKER_CASES.csv", index=False)
    summary.to_csv(OUT / "PDHIS_EVENT_LOCKED_FLICKER_ASSOCIATIONS.csv", index=False)
    behaviours.to_csv(OUT / "PDHIS_EVENT_LOCKED_FLICKER_BEHAVIOURS.csv", index=False)
    make_figure(summary, behaviours)
    write_findings(cases, summary, behaviours)
    print(summary.sort_values("permutation_p").head(10).to_string(index=False))


if __name__ == "__main__":
    main()
