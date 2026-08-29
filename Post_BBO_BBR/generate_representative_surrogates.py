"""Fit and export complete-evidence representative surrogates for F5 and F7."""

from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "BBO_Dashboard" / "data" / "complete_internal_evidence.csv"
OUT = Path(__file__).resolve().parent / "representative_surrogates"


def ordered_function(function: int, dimensions: int) -> tuple[pd.DataFrame, np.ndarray, np.ndarray, int]:
    frame = pd.read_csv(DATA)
    frame = frame[frame.function == function].copy()
    frame["source_order"] = frame.source.map({"starter": 0, **{f"week_{week:02d}": week for week in range(1, 14)}})
    frame = frame.sort_values(["source_order", "sequence"]).reset_index(drop=True)
    columns = [f"x{index}" for index in range(1, dimensions + 1)]
    starter_count = int((frame.source == "starter").sum())
    return frame, frame[columns].to_numpy(float), frame.output.to_numpy(float), starter_count


def scale_fit(x: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    mean = x.mean(axis=0)
    scale = x.std(axis=0)
    scale[scale == 0] = 1.0
    return (x - mean) / scale, mean, scale


def matern52(x1: np.ndarray, x2: np.ndarray, length_scale: float) -> np.ndarray:
    differences = (x1[:, None, :] - x2[None, :, :]) / length_scale
    distance = np.sqrt(np.sum(differences ** 2, axis=2))
    root5 = np.sqrt(5.0) * distance
    return (1.0 + root5 + 5.0 * distance ** 2 / 3.0) * np.exp(-root5)


def fit_gp(x: np.ndarray, y: np.ndarray, length_scale: float, noise: float) -> dict[str, np.ndarray | float]:
    z, x_mean, x_scale = scale_fit(x)
    y_mean = float(y.mean())
    y_scale = float(y.std()) or 1.0
    target = (y - y_mean) / y_scale
    kernel = matern52(z, z, length_scale) + noise * np.eye(len(z))
    jitter = 1e-10
    for _ in range(7):
        try:
            alpha = np.linalg.solve(kernel + jitter * np.eye(len(z)), target)
            break
        except np.linalg.LinAlgError:
            jitter *= 10
    else:
        raise np.linalg.LinAlgError("F5 kernel could not be stabilised.")
    return {"x": x, "z": z, "x_mean": x_mean, "x_scale": x_scale,
            "y_mean": y_mean, "y_scale": y_scale, "alpha": alpha,
            "length_scale": length_scale, "noise": noise, "jitter": jitter}


def predict_gp(model: dict[str, np.ndarray | float], x: np.ndarray) -> np.ndarray:
    z = (x - model["x_mean"]) / model["x_scale"]
    kernel = matern52(z, model["z"], float(model["length_scale"]))
    return float(model["y_mean"]) + float(model["y_scale"]) * (kernel @ model["alpha"])


def quadratic_features(z: np.ndarray) -> tuple[np.ndarray, list[str]]:
    dimensions = z.shape[1]
    blocks = [z]
    names = [f"z{index}" for index in range(1, dimensions + 1)]
    blocks.append(z ** 2)
    names.extend(f"z{index}^2" for index in range(1, dimensions + 1))
    interactions = []
    for left, right in combinations(range(dimensions), 2):
        interactions.append(z[:, left] * z[:, right])
        names.append(f"z{left + 1}*z{right + 1}")
    blocks.append(np.column_stack(interactions))
    return np.column_stack(blocks), names


def fit_quadratic(x: np.ndarray, y: np.ndarray, alpha: float) -> dict[str, np.ndarray | float | list[str]]:
    z, x_mean, x_scale = scale_fit(x)
    features, names = quadratic_features(z)
    design = np.column_stack([np.ones(len(features)), features])
    penalty = np.eye(design.shape[1])
    penalty[0, 0] = 0.0
    coefficients = np.linalg.solve(design.T @ design + alpha * penalty, design.T @ y)
    return {"x_mean": x_mean, "x_scale": x_scale, "intercept": float(coefficients[0]),
            "coefficients": coefficients[1:], "feature_names": names, "alpha": alpha}


def predict_quadratic(model: dict[str, np.ndarray | float | list[str]], x: np.ndarray) -> np.ndarray:
    z = (x - model["x_mean"]) / model["x_scale"]
    features, _ = quadratic_features(z)
    return float(model["intercept"]) + features @ model["coefficients"]


def validate_f5(x: np.ndarray, y: np.ndarray, starter_count: int) -> tuple[pd.DataFrame, pd.DataFrame]:
    rows = []
    settings = []
    output_range = float(np.ptp(y)) or 1.0
    for length_scale in [0.25, 0.4, 0.6, 0.8, 1.0, 1.4, 2.0, 3.0, 4.0, 6.0, 10.0, 15.0, 20.0, 30.0]:
        for noise in [1e-8, 1e-6, 1e-4, 1e-3, 1e-2, 1e-1]:
            predictions = []
            for boundary in range(starter_count, len(y)):
                model = fit_gp(x[:boundary], y[:boundary], length_scale, noise)
                predictions.append(float(predict_gp(model, x[boundary:boundary + 1])[0]))
            actual = y[starter_count:]
            mae = float(np.mean(np.abs(np.asarray(predictions) - actual)))
            settings.append({"length_scale": length_scale, "noise": noise,
                             "walk_forward_mae": mae, "normalised_mae": mae / output_range})
    settings_frame = pd.DataFrame(settings).sort_values(["normalised_mae", "length_scale", "noise"]).reset_index(drop=True)
    winner = settings_frame.iloc[0]
    for boundary in range(starter_count, len(y)):
        model = fit_gp(x[:boundary], y[:boundary], float(winner.length_scale), float(winner.noise))
        prediction = float(predict_gp(model, x[boundary:boundary + 1])[0])
        rows.append({"model": "F5 Matérn 2.5 GP", "target_index": boundary + 1,
                     "actual": y[boundary], "prediction": prediction,
                     "absolute_error": abs(prediction - y[boundary])})
    return settings_frame, pd.DataFrame(rows)


def validate_f7(x: np.ndarray, y: np.ndarray, starter_count: int) -> tuple[pd.DataFrame, pd.DataFrame]:
    settings = []
    output_range = float(np.ptp(y)) or 1.0
    for alpha in [1e-6, 1e-4, 1e-3, 1e-2, 1e-1, 1.0, 10.0, 100.0]:
        predictions = []
        for boundary in range(starter_count, len(y)):
            model = fit_quadratic(x[:boundary], y[:boundary], alpha)
            predictions.append(float(predict_quadratic(model, x[boundary:boundary + 1])[0]))
        actual = y[starter_count:]
        mae = float(np.mean(np.abs(np.asarray(predictions) - actual)))
        settings.append({"alpha": alpha, "walk_forward_mae": mae, "normalised_mae": mae / output_range})
    settings_frame = pd.DataFrame(settings).sort_values(["normalised_mae", "alpha"]).reset_index(drop=True)
    winner = settings_frame.iloc[0]
    rows = []
    for boundary in range(starter_count, len(y)):
        model = fit_quadratic(x[:boundary], y[:boundary], float(winner.alpha))
        prediction = float(predict_quadratic(model, x[boundary:boundary + 1])[0])
        rows.append({"model": "F7 full quadratic", "target_index": boundary + 1,
                     "actual": y[boundary], "prediction": prediction,
                     "absolute_error": abs(prediction - y[boundary])})
    return settings_frame, pd.DataFrame(rows)


def export_f5(frame: pd.DataFrame, x: np.ndarray, y: np.ndarray, settings: pd.DataFrame) -> dict[str, float]:
    winner = settings.iloc[0]
    model = fit_gp(x, y, float(winner.length_scale), float(winner.noise))
    weights = frame[["source", "sequence", "x1", "x2", "x3", "x4", "output"]].copy()
    for index in range(4):
        weights[f"z{index + 1}"] = model["z"][:, index]
    weights["kernel_weight_alpha"] = model["alpha"]
    weights.to_csv(OUT / "F5_MATERN52_WEIGHTS.csv", index=False)
    scaling = pd.DataFrame({"coordinate": [f"x{i}" for i in range(1, 5)],
                            "mean": model["x_mean"], "scale": model["x_scale"]})
    scaling.to_csv(OUT / "F5_INPUT_SCALING.csv", index=False)
    fitted = predict_gp(model, x)
    return {"length_scale": float(winner.length_scale), "noise": float(winner.noise),
            "jitter": float(model["jitter"]), "output_mean": float(model["y_mean"]),
            "output_scale": float(model["y_scale"]), "training_rows": len(y),
            "walk_forward_mae": float(winner.walk_forward_mae),
            "normalised_walk_forward_mae": float(winner.normalised_mae),
            "training_max_abs_error": float(np.max(np.abs(fitted - y)))}


def export_f7(x: np.ndarray, y: np.ndarray, settings: pd.DataFrame) -> dict[str, float]:
    winner = settings.iloc[0]
    model = fit_quadratic(x, y, float(winner.alpha))
    pd.DataFrame({"coordinate": [f"x{i}" for i in range(1, 7)],
                  "mean": model["x_mean"], "scale": model["x_scale"]}).to_csv(OUT / "F7_INPUT_SCALING.csv", index=False)
    coefficient_frame = pd.DataFrame({"term": ["intercept", *model["feature_names"]],
                                      "coefficient": [model["intercept"], *model["coefficients"]]})
    coefficient_frame.to_csv(OUT / "F7_QUADRATIC_COEFFICIENTS.csv", index=False)
    fitted = predict_quadratic(model, x)
    return {"alpha": float(winner.alpha), "training_rows": len(y),
            "terms_excluding_intercept": len(model["coefficients"]),
            "walk_forward_mae": float(winner.walk_forward_mae),
            "normalised_walk_forward_mae": float(winner.normalised_mae),
            "training_rmse": float(np.sqrt(np.mean((fitted - y) ** 2))),
            "training_max_abs_error": float(np.max(np.abs(fitted - y)))}


def write_guide(f5: dict[str, float], f7: dict[str, float]) -> None:
    text = f"""# Representative F5 and F7 surrogate equations

These models approximate the complete sampled input-output record. They are not the original hidden BBO equations and should not be extrapolated beyond the observed domain without new validation.

## F5 Matérn 2.5 surrogate

The representative equation is:

`F5_hat(x) = output_mean + output_scale * sum(alpha_i * K52(z, z_i))`

where `z_j = (x_j - mean_j) / scale_j` and:

`K52 = (1 + sqrt(5)r + 5r^2/3) * exp(-sqrt(5)r)`

The selected standardised length scale is `{f5['length_scale']}` and the diagonal noise setting is `{f5['noise']}`. Weekly walk-forward MAE was `{f5['walk_forward_mae']:.6f}`, equal to `{f5['normalised_walk_forward_mae']:.6f}` of the complete F5 output range.

`F5_INPUT_SCALING.csv` contains the coordinate transformation. `F5_MATERN52_WEIGHTS.csv` contains every training coordinate and kernel weight required to calculate the surrogate.

## F7 quadratic surrogate

The representative equation is:

`F7_hat(x) = beta_0 + sum(beta_j * phi_j(z))`

where `z_j = (x_j - mean_j) / scale_j`. The 27 features comprise six linear terms, six squared terms and fifteen pairwise interactions. Ridge alpha `{f7['alpha']}` was selected by weekly walk-forward validation. MAE was `{f7['walk_forward_mae']:.6f}`, equal to `{f7['normalised_walk_forward_mae']:.6f}` of the complete F7 output range.

`F7_INPUT_SCALING.csv` contains the coordinate transformation. `F7_QUADRATIC_COEFFICIENTS.csv` contains the intercept and all 27 numerical coefficients.

## Validation boundary

Hyperparameters were selected by predicting each of the thirteen weekly observations from the starter data and earlier weeks only. The final parameters were then refitted to the complete evidence for representative use. This final refit describes the sampled record and is not an independent prospective validation.
"""
    (OUT / "README.md").write_text(text, encoding="utf-8")


def make_figure(predictions: pd.DataFrame, f7_coefficients: pd.DataFrame) -> None:
    fig, axes = plt.subplots(1, 3, figsize=(15.5, 6.3), gridspec_kw={"width_ratios": [1, 1, 1.25]})
    for axis, model, colour in [
        (axes[0], "F5 Matérn 2.5 GP", "#4f9d96"),
        (axes[1], "F7 full quadratic", "#7c67ad"),
    ]:
        frame = predictions[predictions.model == model].reset_index(drop=True)
        weeks = np.arange(1, len(frame) + 1)
        axis.plot(weeks, frame.actual, marker="o", label="Observed", color="#263b59", linewidth=2)
        axis.plot(weeks, frame.prediction, marker="o", label="Walk-forward prediction", color=colour, linewidth=2)
        axis.set_title(model, weight="bold")
        axis.set_xlabel("Weekly target")
        axis.grid(alpha=.2)
        axis.legend(fontsize=8)
    coefficients = f7_coefficients[f7_coefficients.term != "intercept"].copy()
    coefficients["absolute"] = coefficients.coefficient.abs()
    coefficients = coefficients.nlargest(10, "absolute").sort_values("coefficient")
    axes[2].barh(coefficients.term, coefficients.coefficient,
                 color=np.where(coefficients.coefficient >= 0, "#ca6f7b", "#72a7c4"))
    axes[2].axvline(0, color="#475569", linewidth=1)
    axes[2].set_title("F7 largest standardised terms", weight="bold")
    axes[2].set_xlabel("Quadratic coefficient")
    fig.suptitle("Representative F5 and F7 surrogate equations", fontsize=18, weight="bold", color="#14213d")
    fig.text(.5, .015, "Predictions use starter observations and earlier weeks only. Final equations are complete-evidence representative refits.", ha="center", fontsize=10)
    fig.tight_layout(rect=[0, .045, 1, .93])
    fig.savefig(OUT / "F5_F7_REPRESENTATIVE_SURROGATES.jpg", dpi=180, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    OUT.mkdir(exist_ok=True)
    f5_frame, f5_x, f5_y, f5_starter = ordered_function(5, 4)
    _, f7_x, f7_y, f7_starter = ordered_function(7, 6)
    f5_settings, f5_predictions = validate_f5(f5_x, f5_y, f5_starter)
    f7_settings, f7_predictions = validate_f7(f7_x, f7_y, f7_starter)
    f5_settings.to_csv(OUT / "F5_HYPERPARAMETER_VALIDATION.csv", index=False)
    f7_settings.to_csv(OUT / "F7_HYPERPARAMETER_VALIDATION.csv", index=False)
    pd.concat([f5_predictions, f7_predictions], ignore_index=True).to_csv(OUT / "WEEKLY_WALK_FORWARD_PREDICTIONS.csv", index=False)
    f5_metadata = export_f5(f5_frame, f5_x, f5_y, f5_settings)
    f7_metadata = export_f7(f7_x, f7_y, f7_settings)
    metadata = {"F5_Matern_2_5": f5_metadata, "F7_full_quadratic": f7_metadata}
    (OUT / "MODEL_METADATA.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")
    write_guide(f5_metadata, f7_metadata)
    make_figure(
        pd.concat([f5_predictions, f7_predictions], ignore_index=True),
        pd.read_csv(OUT / "F7_QUADRATIC_COEFFICIENTS.csv"),
    )
    print(json.dumps(metadata, indent=2))


if __name__ == "__main__":
    main()
