"""Advanced chronological analysis of the PDHIS Delta signature.

The analysis asks whether Delta information available at the end of one week
helps classify improvement in the following week. All feature scaling is based
only on observations available by the prediction week. The script compares
regularised logistic models with a prevalence baseline, uses leave-one-function-
out and expanding-week validation, and adds permutation and cluster-bootstrap
stability checks.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
FIG = OUT / "infographics"
DATA = ROOT / "BBO_Dashboard" / "data" / "complete_internal_evidence.csv"
RANDOM_SEED = 42
N_PERMUTATIONS = 100
N_BOOTSTRAPS = 250

DELTA_FEATURES = [f"delta{i}_scaled" for i in range(1, 6)]
SIGNATURE_FEATURES = DELTA_FEATURES + ["delta1_sign_switch", "delta1_persistence", "cross_level_coherence"]
MODEL_FEATURES = {
    "Delta 1 only": ["delta1_scaled"],
    "Delta 1 to Delta 2": ["delta1_scaled", "delta2_scaled"],
    "Delta signature": SIGNATURE_FEATURES,
}


def load_weekly() -> pd.DataFrame:
    frame = pd.read_csv(DATA)
    frame = frame[frame.source.str.fullmatch(r"week_\d{2}", na=False)].copy()
    frame["week"] = frame.source.str.extract(r"(\d+)").astype(int)
    frame = frame.sort_values(["function", "week"])
    counts = frame.groupby("function").size()
    if len(frame) != 104 or len(counts) != 8 or not (counts == 13).all():
        raise ValueError("Expected thirteen weekly outputs for each of eight functions.")
    return frame[["function", "week", "output"]]


def scaled_last_delta(history: np.ndarray, order: int) -> tuple[float, np.ndarray]:
    values = np.asarray(history, dtype=float)
    for _ in range(order):
        values = np.diff(values)
    scale = np.max(np.abs(values)) if len(values) else 0.0
    scaled = values / scale if scale > 0 else np.zeros_like(values)
    return float(scaled[-1]), scaled


def build_cases(weekly: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, float | int | str]] = []
    for function, group in weekly.groupby("function"):
        group = group.sort_values("week")
        outputs = group.output.to_numpy(float)
        for end_week in range(6, 13):
            history = outputs[:end_week]
            features: dict[str, float] = {}
            scaled_sequences: dict[int, np.ndarray] = {}
            for order in range(1, 6):
                latest, sequence = scaled_last_delta(history, order)
                features[f"delta{order}_scaled"] = latest
                scaled_sequences[order] = sequence

            delta1 = scaled_sequences[1]
            recent_signs = np.sign(delta1[-min(3, len(delta1)):])
            active_signs = recent_signs[recent_signs != 0]
            persistence = abs(float(np.mean(active_signs))) if len(active_signs) else 0.0
            sign_switch = int(len(delta1) >= 2 and delta1[-1] * delta1[-2] < 0)
            level_signs = np.sign([features[f"delta{i}_scaled"] for i in range(1, 6)])
            active_levels = level_signs[level_signs != 0]
            coherence = abs(float(np.mean(active_levels))) if len(active_levels) else 0.0

            next_change = outputs[end_week] - outputs[end_week - 1]
            d1 = features["delta1_scaled"]
            if abs(d1) <= 0.05:
                state = "Plateau"
            elif sign_switch:
                state = "Reversal"
            elif persistence >= 2 / 3 and d1 > 0:
                state = "Directed improvement"
            elif persistence >= 2 / 3 and d1 < 0:
                state = "Directed decline"
            else:
                state = "Irregular or oscillating"

            rows.append({
                "function": int(function),
                "end_week": end_week,
                **features,
                "delta1_sign_switch": sign_switch,
                "delta1_persistence": persistence,
                "cross_level_coherence": coherence,
                "influence_state": state,
                "next_change": next_change,
                "next_improved": int(next_change > 0),
            })
    cases = pd.DataFrame(rows)
    if len(cases) != 56 or cases.next_improved.nunique() != 2:
        raise ValueError("Advanced analysis requires 56 balanced forward cases.")
    return cases


def sigmoid(values: np.ndarray) -> np.ndarray:
    values = np.clip(values, -35, 35)
    return 1.0 / (1.0 + np.exp(-values))


def fit_logistic(x: np.ndarray, y: np.ndarray, l2_strength: float = 1.0) -> dict[str, np.ndarray]:
    """Fit an L2-regularised logistic model using batch gradient descent."""
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    mean = x.mean(axis=0)
    scale = x.std(axis=0)
    scale[scale == 0] = 1.0
    standardised = (x - mean) / scale
    design = np.column_stack([np.ones(len(standardised)), standardised])
    weights = np.zeros(design.shape[1])
    learning_rate = 0.08
    previous_loss = np.inf
    for _ in range(1000):
        probability = sigmoid(design @ weights)
        gradient = design.T @ (probability - y) / len(y)
        gradient[1:] += l2_strength * weights[1:] / len(y)
        weights -= learning_rate * gradient
        probability = np.clip(sigmoid(design @ weights), 1e-12, 1 - 1e-12)
        loss = -np.mean(y * np.log(probability) + (1 - y) * np.log(1 - probability))
        loss += l2_strength * np.sum(weights[1:] ** 2) / (2 * len(y))
        if abs(previous_loss - loss) < 1e-9:
            break
        previous_loss = loss
    return {"mean": mean, "scale": scale, "weights": weights}


def model_probability(model: dict[str, np.ndarray], x: np.ndarray) -> np.ndarray:
    standardised = (np.asarray(x, dtype=float) - model["mean"]) / model["scale"]
    design = np.column_stack([np.ones(len(standardised)), standardised])
    return sigmoid(design @ model["weights"])


def predict_fold(train: pd.DataFrame, test: pd.DataFrame, features: list[str]) -> np.ndarray:
    y_train = train.next_improved.to_numpy(int)
    if len(np.unique(y_train)) < 2:
        return np.repeat(float(np.mean(y_train)), len(test))
    model = fit_logistic(train[features].to_numpy(float), y_train)
    return model_probability(model, test[features].to_numpy(float))


def balanced_accuracy(y: np.ndarray, prediction: np.ndarray) -> float:
    recalls = []
    for label in (0, 1):
        active = y == label
        if active.any():
            recalls.append(np.mean(prediction[active] == label))
    return float(np.mean(recalls))


def roc_auc(y: np.ndarray, probability: np.ndarray) -> float:
    positive = probability[y == 1]
    negative = probability[y == 0]
    if not len(positive) or not len(negative):
        return np.nan
    comparisons = positive[:, None] - negative[None, :]
    return float(np.mean(comparisons > 0) + 0.5 * np.mean(comparisons == 0))


def validation_predictions(cases: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for model_name, features in MODEL_FEATURES.items():
        for held_out in sorted(cases.function.unique()):
            train = cases[cases.function != held_out]
            test = cases[cases.function == held_out]
            probabilities = predict_fold(train, test, features)
            baseline = np.repeat(train.next_improved.mean(), len(test))
            for row, probability, base_probability in zip(test.itertuples(), probabilities, baseline):
                rows.append({"validation": "Leave one function out", "model": model_name,
                             "function": row.function, "end_week": row.end_week,
                             "observed": row.next_improved, "probability": probability,
                             "baseline_probability": base_probability})

        for week in range(7, 13):
            train = cases[cases.end_week < week]
            test = cases[cases.end_week == week]
            probabilities = predict_fold(train, test, features)
            baseline = np.repeat(train.next_improved.mean(), len(test))
            for row, probability, base_probability in zip(test.itertuples(), probabilities, baseline):
                rows.append({"validation": "Expanding week", "model": model_name,
                             "function": row.function, "end_week": row.end_week,
                             "observed": row.next_improved, "probability": probability,
                             "baseline_probability": base_probability})
    return pd.DataFrame(rows)


def metric_row(group: pd.DataFrame, probability_column: str, label: str) -> dict[str, float | int | str]:
    y = group.observed.to_numpy(int)
    probability = np.clip(group[probability_column].to_numpy(float), 1e-6, 1 - 1e-6)
    prediction = (probability >= 0.5).astype(int)
    return {
        "validation": group.validation.iloc[0],
        "model": group.model.iloc[0],
        "prediction": label,
        "n": len(group),
        "accuracy": float(np.mean(y == prediction)),
        "balanced_accuracy": balanced_accuracy(y, prediction),
        "roc_auc": roc_auc(y, probability),
        "brier_score": float(np.mean((probability - y) ** 2)),
        "log_loss": float(-np.mean(y * np.log(probability) + (1 - y) * np.log(1 - probability))),
        "mean_predicted_probability": probability.mean(),
        "observed_improvement_rate": y.mean(),
    }


def validation_metrics(predictions: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for _, group in predictions.groupby(["validation", "model"], sort=False):
        rows.append(metric_row(group, "probability", "Regularised logistic"))
        rows.append(metric_row(group, "baseline_probability", "Prevalence baseline"))
    return pd.DataFrame(rows)


def lofo_balanced_accuracy(cases: pd.DataFrame, features: list[str], outcome: np.ndarray) -> float:
    working = cases.copy()
    working["next_improved"] = outcome
    observed, predicted = [], []
    for held_out in sorted(working.function.unique()):
        train = working[working.function != held_out]
        test = working[working.function == held_out]
        probability = predict_fold(train, test, features)
        observed.extend(test.next_improved.astype(int))
        predicted.extend((probability >= 0.5).astype(int))
    return balanced_accuracy(np.asarray(observed), np.asarray(predicted))


def permutation_test(cases: pd.DataFrame) -> pd.DataFrame:
    rng = np.random.default_rng(RANDOM_SEED)
    observed_y = cases.next_improved.to_numpy(int)
    observed_score = lofo_balanced_accuracy(cases, SIGNATURE_FEATURES, observed_y)
    null_scores = []
    for _ in range(N_PERMUTATIONS):
        shuffled = cases.groupby("function", group_keys=False).next_improved.transform(
            lambda values: rng.permutation(values.to_numpy())
        ).to_numpy(int)
        null_scores.append(lofo_balanced_accuracy(cases, SIGNATURE_FEATURES, shuffled))
    null_scores = np.asarray(null_scores)
    p_value = (1 + np.sum(null_scores >= observed_score)) / (N_PERMUTATIONS + 1)
    return pd.DataFrame([{
        "test": "Within-function outcome permutation",
        "permutations": N_PERMUTATIONS,
        "observed_lofo_balanced_accuracy": observed_score,
        "null_mean": null_scores.mean(),
        "null_95_low": np.quantile(null_scores, 0.025),
        "null_95_high": np.quantile(null_scores, 0.975),
        "permutation_p": p_value,
    }])


def fit_coefficients(frame: pd.DataFrame) -> np.ndarray:
    model = fit_logistic(frame[SIGNATURE_FEATURES].to_numpy(float), frame.next_improved.to_numpy(int))
    return model["weights"][1:]


def coefficient_stability(cases: pd.DataFrame) -> pd.DataFrame:
    rng = np.random.default_rng(RANDOM_SEED)
    point = fit_coefficients(cases)
    functions = np.sort(cases.function.unique())
    estimates = []
    for _ in range(N_BOOTSTRAPS):
        sampled = rng.choice(functions, size=len(functions), replace=True)
        blocks = []
        for block_id, function in enumerate(sampled):
            block = cases[cases.function == function].copy()
            block["bootstrap_block"] = block_id
            blocks.append(block)
        sample = pd.concat(blocks, ignore_index=True)
        if sample.next_improved.nunique() == 2:
            estimates.append(fit_coefficients(sample))
    estimates = np.asarray(estimates)
    rows = []
    for index, feature in enumerate(SIGNATURE_FEATURES):
        same_sign = np.mean(np.sign(estimates[:, index]) == np.sign(point[index]))
        rows.append({"feature": feature, "standardised_coefficient": point[index],
                     "bootstrap_95_low": np.quantile(estimates[:, index], 0.025),
                     "bootstrap_95_high": np.quantile(estimates[:, index], 0.975),
                     "same_sign_stability": same_sign,
                     "bootstrap_samples": len(estimates)})
    return pd.DataFrame(rows)


def state_summary(cases: pd.DataFrame) -> pd.DataFrame:
    return cases.groupby("influence_state").agg(
        cases=("next_improved", "size"),
        next_improvements=("next_improved", "sum"),
        next_improvement_rate=("next_improved", "mean"),
        median_next_change=("next_change", "median"),
    ).reset_index().sort_values("cases", ascending=False)


def make_figure(metrics: pd.DataFrame, coefficients: pd.DataFrame) -> None:
    FIG.mkdir(parents=True, exist_ok=True)
    logistic = metrics[metrics.prediction == "Regularised logistic"].copy()
    logistic["label"] = logistic.model + "\n" + logistic.validation
    fig, axes = plt.subplots(1, 2, figsize=(14, 6.4))
    colours = ["#4f9d96", "#7c67ad", "#d4a72c", "#4f9d96", "#7c67ad", "#d4a72c"]
    axes[0].barh(logistic.label, logistic.balanced_accuracy, color=colours[:len(logistic)])
    axes[0].axvline(0.5, color="#94a3b8", linestyle="--", linewidth=1)
    axes[0].set_xlim(0, 1)
    axes[0].set_xlabel("Balanced accuracy")
    axes[0].set_title("Out-of-sample classification")
    ordered = coefficients.sort_values("standardised_coefficient")
    axes[1].errorbar(ordered.standardised_coefficient, ordered.feature,
                     xerr=[ordered.standardised_coefficient - ordered.bootstrap_95_low,
                           ordered.bootstrap_95_high - ordered.standardised_coefficient],
                     fmt="o", color="#4f9d96", ecolor="#9bc7c2", capsize=3)
    axes[1].axvline(0, color="#94a3b8", linewidth=1)
    axes[1].set_xlabel("Standardised logistic coefficient")
    axes[1].set_title("Coefficient direction and cluster-bootstrap interval")
    fig.suptitle("Advanced PDHIS next-week improvement analysis", fontsize=18, weight="bold", color="#14213d")
    fig.text(0.5, 0.015, "Models use information available by the prediction week. Intervals describe stability across resampled functions, not causal effects.",
             ha="center", fontsize=9, color="#475569")
    fig.tight_layout(rect=(0, 0.045, 1, 0.94))
    fig.savefig(FIG / "PDHIS-21_advanced_logistic_validation.jpg", dpi=210, facecolor="white", pil_kwargs={"quality": 92})
    plt.close(fig)


def write_findings(cases: pd.DataFrame, metrics: pd.DataFrame, permutation: pd.DataFrame,
                   coefficients: pd.DataFrame, states: pd.DataFrame) -> None:
    signature = metrics[(metrics.model == "Delta signature") &
                        (metrics.prediction == "Regularised logistic")]
    lofo = signature[signature.validation == "Leave one function out"].iloc[0]
    chrono = signature[signature.validation == "Expanding week"].iloc[0]
    strongest = coefficients.iloc[coefficients.standardised_coefficient.abs().argmax()]
    state_table = ["| Influence state | Cases | Next improvements | Next improvement rate | Median next change |",
                   "| --- | ---: | ---: | ---: | ---: |"]
    for row in states.itertuples():
        state_table.append(
            f"| {row.influence_state} | {int(row.cases)} | {int(row.next_improvements)} | "
            f"{row.next_improvement_rate:.3f} | {row.median_next_change:.3f} |"
        )
    lines = [
        "# Advanced PDHIS Delta analysis",
        "",
        "## Question",
        "",
        "Can Delta information available at the end of one week help classify whether the following weekly output improves?",
        "",
        "## Design",
        "",
        f"The analysis contains {len(cases)} forward cases from eight functions. The outcome is balanced: "
        f"{int(cases.next_improved.sum())} improvements and {int((1 - cases.next_improved).sum())} non-improvements. "
        "Delta 1 to Delta 5 are scaled only with history available by the prediction week. Regularised logistic regression is compared with a prevalence baseline. "
        "Leave-one-function-out testing assesses transfer to an unseen function, while expanding-week testing preserves chronology.",
        "",
        "## Main results",
        "",
        f"The full Delta signature reached leave-one-function-out balanced accuracy of {lofo.balanced_accuracy:.3f}, ROC AUC of {lofo.roc_auc:.3f} and Brier score of {lofo.brier_score:.3f}. "
        f"Expanding-week balanced accuracy was {chrono.balanced_accuracy:.3f}, with ROC AUC {chrono.roc_auc:.3f} and Brier score {chrono.brier_score:.3f}. "
        f"The within-function permutation p value was {permutation.permutation_p.iloc[0]:.4f}. "
        f"The largest absolute standardised coefficient was {strongest.feature} at {strongest.standardised_coefficient:.3f}, with a cluster-bootstrap interval from "
        f"{strongest.bootstrap_95_low:.3f} to {strongest.bootstrap_95_high:.3f}.",
        "",
        "## Interpretation",
        "",
        "Gradient-based optimisation is used only to fit the logistic model. It is not treated as separate scientific evidence. "
        "The model is exploratory because the dataset is small, repeated observations within a function are dependent and several Delta features are related. "
        "A useful out-of-sample result would justify prospective testing on later data. It would not recover a hidden equation or establish a causal influence state.",
        "",
        "## Influence-state summary",
        "",
        "\n".join(state_table),
        "",
        "## Reproducibility",
        "",
        "Run `python Post_BBO_BBR/PDHIS/generate_pdhis_advanced_analysis.py` from the repository root.",
    ]
    (OUT / "PDHIS_ADVANCED_FINDINGS.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    weekly = load_weekly()
    cases = build_cases(weekly)
    predictions = validation_predictions(cases)
    metrics = validation_metrics(predictions)
    permutation = permutation_test(cases)
    coefficients = coefficient_stability(cases)
    states = state_summary(cases)

    cases.to_csv(OUT / "PDHIS_ADVANCED_CASES.csv", index=False)
    predictions.to_csv(OUT / "PDHIS_LOGISTIC_VALIDATION.csv", index=False)
    metrics.to_csv(OUT / "PDHIS_LOGISTIC_METRICS.csv", index=False)
    permutation.to_csv(OUT / "PDHIS_LOGISTIC_PERMUTATION.csv", index=False)
    coefficients.to_csv(OUT / "PDHIS_LOGISTIC_COEFFICIENTS.csv", index=False)
    states.to_csv(OUT / "PDHIS_INFLUENCE_STATES.csv", index=False)
    make_figure(metrics, coefficients)
    write_findings(cases, metrics, permutation, coefficients, states)
    print(metrics.to_string(index=False))
    print("\n", permutation.to_string(index=False))


if __name__ == "__main__":
    main()
