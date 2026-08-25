from __future__ import annotations

from pathlib import Path
import warnings

import numpy as np
import pandas as pd
from sklearn.base import clone
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import ConstantKernel, Matern, WhiteKernel
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.metrics import mean_absolute_error
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

from bbd_001_system_identification import load_history

HERE = Path(__file__).resolve().parent
OUT = HERE / "outputs"
OUT.mkdir(exist_ok=True)
F = 8
D = 8
MIN_TRAIN = 5


def gp(dim: int):
    kernel = ConstantKernel(1.0, (1e-3, 1e3)) * Matern(
        length_scale=np.ones(dim), length_scale_bounds=(1e-3, 1e3), nu=2.5
    ) + WhiteKernel(noise_level=1e-4, noise_level_bounds=(1e-8, 1e1))
    return GaussianProcessRegressor(
        kernel=kernel,
        normalize_y=True,
        random_state=42,
        n_restarts_optimizer=2,
    )


def linear_ols():
    return Pipeline([
        ("scale", StandardScaler()),
        ("linear", LinearRegression()),
    ])


def linear_ridge(alpha: float):
    return Pipeline([
        ("scale", StandardScaler()),
        ("ridge", Ridge(alpha=alpha)),
    ])


def poly_ridge(degree: int, alpha: float):
    return Pipeline([
        ("poly", PolynomialFeatures(degree=degree, include_bias=False)),
        ("scale", StandardScaler()),
        ("ridge", Ridge(alpha=alpha)),
    ])


def poly_lasso(degree: int, alpha: float):
    return Pipeline([
        ("poly", PolynomialFeatures(degree=degree, include_bias=False)),
        ("scale", StandardScaler()),
        ("lasso", Lasso(alpha=alpha, max_iter=100000, random_state=42)),
    ])


def linear_elastic(alpha: float, l1_ratio: float):
    return Pipeline([
        ("scale", StandardScaler()),
        ("elastic", ElasticNet(alpha=alpha, l1_ratio=l1_ratio, max_iter=100000, random_state=42)),
    ])


def walk_forward(g: pd.DataFrame, estimator) -> pd.DataFrame:
    xcols = [f"x{i}" for i in range(1, D + 1)]
    X = g[xcols].to_numpy(float)
    y = g["output"].to_numpy(float)
    rows = []
    for i in range(MIN_TRAIN, len(g)):
        model = clone(estimator)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            model.fit(X[:i], y[:i])
            pred = float(np.asarray(model.predict(X[i:i + 1])).ravel()[0])
        rows.append({
            "week": int(g.loc[i, "week"]),
            "actual": float(y[i]),
            "prediction": pred,
            "absolute_error": abs(float(y[i]) - pred),
        })
    return pd.DataFrame(rows)


def repeat_summary(g: pd.DataFrame) -> pd.DataFrame:
    xcols = [f"x{i}" for i in range(1, D + 1)]
    rows = []
    for coords, grp in g.groupby(xcols, sort=False, dropna=False):
        if len(grp) < 2:
            continue
        vals = grp["output"].to_numpy(float)
        rows.append({
            "coordinate": "-".join(f"{float(v):.6f}" for v in coords),
            "n_repeats": len(grp),
            "output_range": float(vals.max() - vals.min()),
            "identical_outputs": bool(np.allclose(vals, vals[0], atol=1e-12, rtol=0.0)),
        })
    return pd.DataFrame(rows)


def raw_linear_coefficients(model: Pipeline) -> tuple[np.ndarray, float]:
    scaler = model.named_steps["scale"]
    if "ridge" in model.named_steps:
        reg = model.named_steps["ridge"]
    elif "linear" in model.named_steps:
        reg = model.named_steps["linear"]
    else:
        raise ValueError("linear coefficient extraction requires ridge or linear estimator")
    raw = np.asarray(reg.coef_, dtype=float) / scaler.scale_
    intercept = float(reg.intercept_ - np.sum(np.asarray(reg.coef_) * scaler.mean_ / scaler.scale_))
    return raw, intercept


def coefficient_stability(g: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    xcols = [f"x{i}" for i in range(1, D + 1)]
    X = g[xcols].to_numpy(float)
    y = g["output"].to_numpy(float)
    rows = []
    for n_train in range(MIN_TRAIN, len(g) + 1):
        model = linear_ridge(1e-4)
        model.fit(X[:n_train], y[:n_train])
        raw, intercept = raw_linear_coefficients(model)
        row = {"n_train": n_train, "through_week": int(g.loc[n_train - 1, "week"]), "intercept": intercept}
        for j, coef in enumerate(raw, start=1):
            row[f"x{j}"] = float(coef)
        rows.append(row)
    windows = pd.DataFrame(rows)

    summary = []
    for j in range(1, D + 1):
        vals = windows[f"x{j}"].to_numpy(float)
        full = float(vals[-1])
        nonzero = vals[np.abs(vals) > 1e-12]
        if len(nonzero):
            sign_stability = float(np.mean(np.sign(nonzero) == np.sign(full)))
        else:
            sign_stability = np.nan
        denom = abs(float(np.mean(vals)))
        cv = float(np.std(vals, ddof=0) / denom) if denom > 1e-12 else np.nan
        summary.append({
            "coordinate": j,
            "full_history_coefficient": full,
            "mean_window_coefficient": float(np.mean(vals)),
            "median_window_coefficient": float(np.median(vals)),
            "coefficient_std": float(np.std(vals, ddof=0)),
            "coefficient_cv_abs_mean": cv,
            "sign_stability_vs_full": sign_stability,
            "direction": "increase" if full > 0 else "decrease",
        })
    summary_df = pd.DataFrame(summary)
    summary_df["absolute_rank"] = summary_df["full_history_coefficient"].abs().rank(method="first", ascending=False).astype(int)
    return windows, summary_df.sort_values("absolute_rank").reset_index(drop=True)


def main():
    hist = load_history()
    g = hist[hist["function"] == F].sort_values("week").reset_index(drop=True)
    y = g["output"].to_numpy(float)
    yrange = float(np.ptp(y)) or 1.0

    candidates = [
        ("linear_ols", linear_ols()),
        ("linear_ridge_1e-6", linear_ridge(1e-6)),
        ("linear_ridge_1e-4", linear_ridge(1e-4)),
        ("linear_ridge_1e-2", linear_ridge(1e-2)),
        ("linear_ridge_0.1", linear_ridge(0.1)),
        ("quadratic_ridge_1e-4", poly_ridge(2, 1e-4)),
        ("quadratic_ridge_1e-2", poly_ridge(2, 1e-2)),
        ("quadratic_ridge_0.1", poly_ridge(2, 0.1)),
        ("quadratic_lasso_1e-3", poly_lasso(2, 1e-3)),
        ("quadratic_lasso_1e-2", poly_lasso(2, 1e-2)),
        ("linear_elastic_1e-3", linear_elastic(1e-3, 0.5)),
        ("linear_elastic_1e-2", linear_elastic(1e-2, 0.5)),
        ("gp_matern_2.5", gp(D)),
    ]

    comp = []
    preds = []
    for name, estimator in candidates:
        p = walk_forward(g, estimator)
        p.insert(0, "model", name)
        preds.append(p)
        mae = float(mean_absolute_error(p["actual"], p["prediction"]))
        comp.append({
            "model": name,
            "walk_forward_tests": len(p),
            "walk_forward_mae": mae,
            "normalised_walk_forward_mae": mae / yrange,
            "median_absolute_error": float(p["absolute_error"].median()),
            "max_absolute_error": float(p["absolute_error"].max()),
        })

    comp = pd.DataFrame(comp).sort_values("normalised_walk_forward_mae").reset_index(drop=True)
    comp.insert(0, "rank", np.arange(1, len(comp) + 1))
    comp.to_csv(OUT / "BBD_021_F8_MODEL_COMPETITION.csv", index=False)
    pd.concat(preds, ignore_index=True).to_csv(OUT / "BBD_021_F8_WALK_FORWARD_PREDICTIONS.csv", index=False)

    reps = repeat_summary(g)
    reps.to_csv(OUT / "BBD_021_F8_REPEAT_SUMMARY.csv", index=False)

    coef_windows, coef_summary = coefficient_stability(g)
    coef_windows.to_csv(OUT / "BBD_021_F8_LINEAR_COEFFICIENT_WINDOWS.csv", index=False)
    coef_summary.to_csv(OUT / "BBD_021_F8_LINEAR_COEFFICIENT_STABILITY.csv", index=False)

    full_linear = linear_ridge(1e-4)
    xcols = [f"x{i}" for i in range(1, D + 1)]
    full_linear.fit(g[xcols].to_numpy(float), y)
    raw, intercept = raw_linear_coefficients(full_linear)
    terms = [f"{intercept:.10g}"]
    for j, coef in enumerate(raw, start=1):
        sign = "+" if coef >= 0 else "-"
        terms.append(f" {sign} {abs(float(coef)):.10g}*x{j}")
    equation = "".join(terms)

    best = comp.iloc[0]
    repeat_groups = len(reps)
    nonident = int((~reps["identical_outputs"]).sum()) if repeat_groups else 0
    max_repeat = float(reps["output_range"].max()) if repeat_groups else 0.0

    # Prior evidence retained for direct comparison, not treated as a rerun.
    bbd004_linear_loocv = 0.017307
    bbd007_bbd_normalised_mae = 0.167497
    bbd007_soc_normalised_mae = 0.043917
    bbd003_gradient_cosine = 0.936764

    stable_sign_fraction = float(np.mean(coef_summary["sign_stability_vs_full"] >= 0.75))

    summary = pd.DataFrame([{
        "function": F,
        "n_observations": len(g),
        "best_model": best["model"],
        "best_normalised_walk_forward_mae": float(best["normalised_walk_forward_mae"]),
        "bbd004_linear_normalised_loocv_mae": bbd004_linear_loocv,
        "bbd007_bbd_normalised_mae": bbd007_bbd_normalised_mae,
        "bbd007_soc_normalised_mae": bbd007_soc_normalised_mae,
        "bbd003_global_recent_gradient_cosine": bbd003_gradient_cosine,
        "linear_coefficients_with_at_least_75pct_sign_stability_fraction": stable_sign_fraction,
        "repeat_groups": repeat_groups,
        "nonidentical_repeat_groups": nonident,
        "max_repeat_range": max_repeat,
        "full_history_linear_equation": equation,
        "mechanism_interpretation": "static_linear_or_low_order_surface_candidate" if nonident == 0 else "structured_surface_plus_repeat_variation",
        "exact_function_recovered": False,
        "independent_discriminatory_query_required": True,
    }])
    summary.to_csv(OUT / "BBD_021_F8_DECRYPTION_SUMMARY.csv", index=False)

    print("BBD 021 F8-specific decryption")
    print("\nModel competition")
    print(comp.to_string(index=False))
    print("\nLinear coefficient stability")
    print(coef_summary.to_string(index=False))
    if repeat_groups:
        print("\nRepeat summary")
        print(reps.to_string(index=False))
    print("\nFull-history linear equation")
    print(equation)
    print("\nSummary")
    print(summary.to_string(index=False))
    print(f"\nOutputs written to {OUT}")


if __name__ == "__main__":
    main()
