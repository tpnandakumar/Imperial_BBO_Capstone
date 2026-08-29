"""Matched event atlas, threshold sensitivity and transfer checks for PDHIS flickers."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from generate_pdhis_advanced_analysis import fit_logistic, model_probability
from generate_pdhis_event_locked_flickers import FEATURES, build_cases, holm_adjust, load_weekly


OUT = Path(__file__).resolve().parent
FIG = OUT / "infographics"
RANDOM_SEED = 119
N_PERMUTATIONS = 1000
FEATURE_NAMES = list(FEATURES)


def matched_pairs(cases: pd.DataFrame, target: str) -> pd.DataFrame:
    rows = []
    pair_id = 0
    for function, group in cases.groupby("function"):
        events = group[group[target] == 1].sort_values("event_week")
        controls = group[group[target] == 0].copy()
        for _, event in events.iterrows():
            if controls.empty:
                continue
            control = controls.loc[(controls.event_week - event.event_week).abs().idxmin()]
            pair_id += 1
            for role, item in [("event", event), ("matched non-event", control)]:
                record = {"pair_id": pair_id, "target": target, "role": role,
                          "function": item.function, "event_week": item.event_week}
                record.update({feature: item[feature] for feature in FEATURE_NAMES})
                rows.append(record)
    return pd.DataFrame(rows)


def paired_summary(pairs: pd.DataFrame) -> pd.DataFrame:
    rng = np.random.default_rng(RANDOM_SEED)
    rows = []
    for target, target_pairs in pairs.groupby("target"):
        wide = target_pairs.pivot(index="pair_id", columns="role", values=FEATURE_NAMES)
        for feature in FEATURE_NAMES:
            differences = (wide[(feature, "event")] - wide[(feature, "matched non-event")]).to_numpy(float)
            observed = float(differences.mean())
            difference_scale = float(differences.std(ddof=1)) if len(differences) > 1 else 0.0
            standardised = observed / difference_scale if difference_scale > 0 else 0.0
            null = []
            for _ in range(N_PERMUTATIONS):
                signs = rng.choice([-1, 1], len(differences))
                null.append(float(np.mean(differences * signs)))
            p_value = (1 + sum(abs(value) >= abs(observed) for value in null)) / (N_PERMUTATIONS + 1)
            rows.append({"target": target, "feature": feature, "feature_label": FEATURES[feature],
                         "pairs": len(differences), "event_mean": wide[(feature, "event")].mean(),
                         "matched_mean": wide[(feature, "matched non-event")].mean(),
                         "paired_difference": observed, "paired_standardised_difference": standardised,
                         "sign_flip_p": p_value})
    summary = pd.DataFrame(rows)
    summary["holm_p"] = summary.groupby("target", group_keys=False).sign_flip_p.apply(holm_adjust)
    return summary


def threshold_sensitivity(cases: pd.DataFrame) -> pd.DataFrame:
    rng = np.random.default_rng(RANDOM_SEED + 1)
    rows = []
    scale = cases.large_event_threshold / 1.5
    for multiplier in [1.0, 1.25, 1.5, 1.75, 2.0]:
        outcome = (cases.current_change.abs() > multiplier * scale).astype(int)
        for feature in FEATURE_NAMES:
            event_mean = cases.loc[outcome == 1, feature].mean()
            other_mean = cases.loc[outcome == 0, feature].mean()
            observed = float(event_mean - other_mean)
            null = []
            for _ in range(500):
                shuffled = pd.Series(outcome, index=cases.index).groupby(cases.function).transform(
                    lambda values: rng.permutation(values.to_numpy())
                )
                null.append(cases.loc[shuffled == 1, feature].mean() - cases.loc[shuffled == 0, feature].mean())
            p_value = (1 + sum(abs(value) >= abs(observed) for value in null)) / 501
            rows.append({"threshold_multiplier": multiplier, "feature": feature,
                         "feature_label": FEATURES[feature], "events": int(outcome.sum()),
                         "event_mean": event_mean, "non_event_mean": other_mean,
                         "mean_difference": observed, "permutation_p": p_value})
    return pd.DataFrame(rows)


def balanced_accuracy(y: np.ndarray, prediction: np.ndarray) -> float:
    positive = prediction[y == 1].mean() if np.any(y == 1) else np.nan
    negative = (1 - prediction[y == 0]).mean() if np.any(y == 0) else np.nan
    return float(np.nanmean([positive, negative]))


def roc_auc(y: np.ndarray, probability: np.ndarray) -> float:
    positive = probability[y == 1]
    negative = probability[y == 0]
    if not len(positive) or not len(negative):
        return np.nan
    return float(np.mean([np.mean(value > negative) + .5 * np.mean(value == negative) for value in positive]))


def lofo_new_best(cases: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for held_out in sorted(cases.function.unique()):
        train = cases[cases.function != held_out]
        test = cases[cases.function == held_out]
        x_train = train[FEATURE_NAMES].to_numpy(float)
        x_test = test[FEATURE_NAMES].to_numpy(float)
        model = fit_logistic(x_train, train.new_best_event.to_numpy(int), l2_strength=1.0)
        probability = model_probability(model, x_test)
        baseline = np.repeat(train.new_best_event.mean(), len(test))
        for item, prob, base in zip(test.itertuples(), probability, baseline):
            rows.append({"function": held_out, "event_week": item.event_week,
                         "observed": item.new_best_event, "probability": prob,
                         "baseline_probability": base})
    return pd.DataFrame(rows)


def lofo_metrics(predictions: pd.DataFrame) -> pd.DataFrame:
    y = predictions.observed.to_numpy(int)
    rows = []
    for model, column in [("Flicker fingerprint", "probability"), ("Prevalence baseline", "baseline_probability")]:
        probability = predictions[column].to_numpy(float)
        predicted = (probability >= .5).astype(int)
        rows.append({"model": model, "cases": len(y), "events": int(y.sum()),
                     "balanced_accuracy": balanced_accuracy(y, predicted),
                     "roc_auc": roc_auc(y, probability),
                     "brier_score": float(np.mean((probability - y) ** 2))})
    return pd.DataFrame(rows)


def pre_event_profiles(weekly: pd.DataFrame, cases: pd.DataFrame) -> pd.DataFrame:
    rows = []
    case_lookup = cases.set_index(["function", "event_week"])
    for function, group in weekly.groupby("function"):
        outputs = group.sort_values("week").output.to_numpy(float)
        weeks = group.sort_values("week").week.to_numpy(int)
        for target_index in range(6, len(outputs)):
            event_week = weeks[target_index]
            history = outputs[target_index - 6:target_index]
            scale = case_lookup.loc[(function, event_week), "large_event_threshold"] / 1.5
            d1 = np.diff(history) / scale
            for index, value in enumerate(d1):
                rows.append({"function": function, "event_week": event_week,
                             "lag": index - 5, "scaled_delta1": value,
                             "new_best_event": int(case_lookup.loc[(function, event_week), "new_best_event"])})
    return pd.DataFrame(rows)


def make_figure(paired: pd.DataFrame, sensitivity: pd.DataFrame, metrics: pd.DataFrame) -> None:
    new_best = paired[paired.target == "new_best_event"].sort_values("paired_difference")
    peak = sensitivity[sensitivity.feature == "peak_spacing"]
    fig, axes = plt.subplots(1, 3, figsize=(15.5, 6.2), gridspec_kw={"width_ratios": [1.25, 1, .8]})
    axes[0].barh(new_best.feature_label, new_best.paired_standardised_difference,
                 color=np.where(new_best.paired_standardised_difference >= 0, "#ca6f7b", "#72a7c4"))
    axes[0].axvline(0, color="#475569", linewidth=1)
    axes[0].set_title("New-best matched pairs", weight="bold")
    axes[0].set_xlabel("Standardised paired difference")
    axes[1].plot(peak.threshold_multiplier, peak.mean_difference, marker="o", color="#7c67ad", linewidth=2.5)
    axes[1].axhline(0, color="#475569", linewidth=1)
    for row in peak.itertuples():
        axes[1].annotate(f"n={row.events}", (row.threshold_multiplier, row.mean_difference), xytext=(0, 8), textcoords="offset points", ha="center", fontsize=8)
    axes[1].set_title("Large-event threshold sensitivity", weight="bold")
    axes[1].set_xlabel("Threshold multiplier")
    axes[1].set_ylabel("Peak-spacing difference")
    axes[1].grid(alpha=.2)
    axes[2].bar(metrics.model, metrics.balanced_accuracy, color=["#4f9d96", "#cbd5e1"])
    axes[2].axhline(.5, color="#d4a72c", linestyle="--")
    axes[2].set_ylim(0, 1)
    axes[2].set_ylabel("Balanced accuracy")
    axes[2].set_title("Held-out function", weight="bold")
    axes[2].tick_params(axis="x", rotation=20)
    fig.suptitle("PDHIS matched event atlas and stability checks", fontsize=18, weight="bold", color="#14213d")
    fig.text(.5, .015, "Matched comparisons remain retrospective. Held-out-function performance tests transfer, not prospective deployment.", ha="center", fontsize=10)
    fig.tight_layout(rect=[0, .045, 1, .93])
    fig.savefig(FIG / "PDHIS-23_matched_event_atlas.jpg", dpi=180, bbox_inches="tight")
    plt.close(fig)


def write_findings(paired: pd.DataFrame, sensitivity: pd.DataFrame, metrics: pd.DataFrame) -> None:
    best = paired.loc[paired.sign_flip_p.idxmin()]
    model = metrics[metrics.model == "Flicker fingerprint"].iloc[0]
    baseline = metrics[metrics.model == "Prevalence baseline"].iloc[0]
    peak = sensitivity[sensitivity.feature == "peak_spacing"]
    stable_direction = bool((np.sign(peak.mean_difference.dropna()) == np.sign(peak.mean_difference.dropna().iloc[0])).all())
    text = f"""# PDHIS matched event atlas and stability analysis

## Purpose

This extension exploits the existing event-locked evidence by pairing each event with the nearest non-event window from the same function. It then tests threshold sensitivity and transfer to a function excluded from fitting.

## Matched comparison

The smallest paired sign-flip p value was {best.sign_flip_p:.3f} for {best.feature_label.lower()} against {best.target.replace('_', ' ')} across {int(best.pairs)} pairs. Its Holm-adjusted p value was {best.holm_p:.3f}. Matching controls function identity and favours a nearby comparison week, but it does not create additional independent events.

## Threshold sensitivity

The large-event definition was varied from 1.00 to 2.00 times the function-adjusted historical scale. The direction of the peak-spacing difference was {'stable' if stable_direction else 'not stable'} across the tested thresholds. Event counts and complete feature results are retained in `PDHIS_EVENT_THRESHOLD_SENSITIVITY.csv`.

## Transfer to an unseen function

The complete nine-feature fingerprint was fitted on seven functions and tested on the eighth. Balanced accuracy was {model.balanced_accuracy:.3f}, ROC AUC was {model.roc_auc:.3f} and Brier score was {model.brier_score:.3f}. The prevalence baseline balanced accuracy was {baseline.balanced_accuracy:.3f} with Brier score {baseline.brier_score:.3f}.

## Interpretation

These checks ask whether the candidate fingerprint survives closer controls, alternative event thresholds and a held-out function. They do not turn retrospective discovery into prospective confirmation. A characteristic should be locked only if its direction is stable, its adjusted evidence is credible and its transfer performance improves on the simple baseline.

## Reproducibility

Run `python Post_BBO_BBR/PDHIS/generate_pdhis_matched_event_atlas.py` from the repository root.
"""
    (OUT / "PDHIS_MATCHED_EVENT_ATLAS.md").write_text(text, encoding="utf-8")


def main() -> None:
    weekly = load_weekly()
    cases = build_cases(weekly)
    pairs = pd.concat([matched_pairs(cases, target) for target in ["positive_event", "large_event", "new_best_event"]], ignore_index=True)
    paired = paired_summary(pairs)
    sensitivity = threshold_sensitivity(cases)
    predictions = lofo_new_best(cases)
    metrics = lofo_metrics(predictions)
    profiles = pre_event_profiles(weekly, cases)
    pairs.to_csv(OUT / "PDHIS_MATCHED_EVENT_PAIRS.csv", index=False)
    paired.to_csv(OUT / "PDHIS_MATCHED_EVENT_RESULTS.csv", index=False)
    sensitivity.to_csv(OUT / "PDHIS_EVENT_THRESHOLD_SENSITIVITY.csv", index=False)
    predictions.to_csv(OUT / "PDHIS_FLICKER_LOFO_PREDICTIONS.csv", index=False)
    metrics.to_csv(OUT / "PDHIS_FLICKER_LOFO_METRICS.csv", index=False)
    profiles.to_csv(OUT / "PDHIS_PRE_EVENT_PROFILES.csv", index=False)
    make_figure(paired, sensitivity, metrics)
    write_findings(paired, sensitivity, metrics)
    print(paired.sort_values("sign_flip_p").head(8).to_string(index=False))
    print(metrics.to_string(index=False))


if __name__ == "__main__":
    main()
