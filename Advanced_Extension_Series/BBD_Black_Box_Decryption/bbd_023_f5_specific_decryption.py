from __future__ import annotations

from pathlib import Path
import warnings

import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin, clone
from sklearn.ensemble import ExtraTreesRegressor, GradientBoostingRegressor, RandomForestRegressor
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import ConstantKernel, Matern, RBF, WhiteKernel
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.metrics import mean_absolute_error
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

from bbd_001_system_identification import load_history

HERE = Path(__file__).resolve().parent
OUT = HERE / "outputs"
OUT.mkdir(exist_ok=True)
F = 5
D = 4
MIN_TRAIN = 5
RANDOM_STATE = 42


class BoundaryFeatures(BaseEstimator, TransformerMixin):
    """Raw coordinates plus monotone distance-to-upper-boundary features."""

    def __init__(self, epsilon: float = 1e-6):
        self.epsilon = epsilon

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = np.asarray(X, dtype=float)
        gap = np.clip(1.0 - X, self.epsilon, None)
        log_closeness = -np.log(gap)
        reciprocal_closeness = 1.0 / gap
        return np.column_stack([X, log_closeness, reciprocal_closeness])


def gp(kernel_name: str):
    if kernel_name == "matern":
        base = Matern(length_scale=np.ones(D), length_scale_bounds=(1e-3, 1e3), nu=2.5)
    else:
        base = RBF(length_scale=np.ones(D), length_scale_bounds=(1e-3, 1e3))
    kernel = ConstantKernel(1.0, (1e-3, 1e3)) * base + WhiteKernel(
        noise_level=1e-6, noise_level_bounds=(1e-10, 1e1)
    )
    return Pipeline([
        ("scale", StandardScaler()),
        ("gp", GaussianProcessRegressor(
            kernel=kernel,
            normalize_y=True,
            n_restarts_optimizer=2,
            random_state=RANDOM_STATE,
        )),
    ])


def linear_ols():
    return Pipeline([("scale", StandardScaler()), ("model", LinearRegression())])


def linear_ridge(alpha: float):
    return Pipeline([("scale", StandardScaler()), ("model", Ridge(alpha=alpha))])


def poly_ridge(degree: int, alpha: float):
    return Pipeline([
        ("poly", PolynomialFeatures(degree=degree, include_bias=False)),
        ("scale", StandardScaler()),
        ("model", Ridge(alpha=alpha)),
    ])


def boundary_ridge(alpha: float):
    return Pipeline([
        ("boundary", BoundaryFeatures()),
        ("scale", StandardScaler()),
        ("model", Ridge(alpha=alpha)),
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
    reg = model.named_steps["model"]
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
        nz = vals[np.abs(vals) > 1e-12]
        sign_stability = float(np.mean(np.sign(nz) == np.sign(full))) if len(nz) else np.nan
        summary.append({
            "coordinate": j,
            "full_history_coefficient": full,
            "mean_window_coefficient": float(np.mean(vals)),
            "median_window_coefficient": float(np.median(vals)),
            "coefficient_std": float(np.std(vals, ddof=0)),
            "sign_stability_vs_full": sign_stability,
            "direction": "increase" if full > 0 else "decrease",
        })
    s = pd.DataFrame(summary)
    s["absolute_rank"] = s["full_history_coefficient"].abs().rank(method="first", ascending=False).astype(int)
    return windows, s.sort_values("absolute_rank").reset_index(drop=True)


def main():
    hist = load_history()
    g = hist[hist["function"] == F].sort_values("week").reset_index(drop=True)
    y = g["output"].to_numpy(float)
    yrange = float(np.ptp(y)) or 1.0

    candidates = [
        ("linear_ols", linear_ols()),
        ("linear_ridge_1e-4", linear_ridge(1e-4)),
        ("linear_ridge_1e-2", linear_ridge(1e-2)),
        ("quadratic_ridge_1e-8", poly_ridge(2, 1e-8)),
        ("quadratic_ridge_1e-4", poly_ridge(2, 1e-4)),
        ("quadratic_ridge_1e-2", poly_ridge(2, 1e-2)),
        ("quadratic_ridge_0.1", poly_ridge(2, 0.1)),
        ("cubic_ridge_1e-4", poly_ridge(3, 1e-4)),
        ("cubic_ridge_1e-2", poly_ridge(3, 1e-2)),
        ("boundary_ridge_1e-4", boundary_ridge(1e-4)),
        ("boundary_ridge_1e-2", boundary_ridge(1e-2)),
        ("gp_matern_2.5", gp("matern")),
        ("gp_rbf", gp("rbf")),
        ("gradient_boosting", GradientBoostingRegressor(random_state=RANDOM_STATE, n_estimators=300, max_depth=2, learning_rate=0.03)),
        ("random_forest", RandomForestRegressor(n_estimators=500, random_state=RANDOM_STATE, min_samples_leaf=1)),
        ("extra_trees", ExtraTreesRegressor(n_estimators=500, random_state=RANDOM_STATE, min_samples_leaf=1)),
    ]

    comp = []
    pred_frames = []
    for name, est in candidates:
        p = walk_forward(g, est)
        p.insert(0, "model", name)
        pred_frames.append(p)
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
    comp.to_csv(OUT / "BBD_023_F5_MODEL_COMPETITION.csv", index=False)
    pd.concat(pred_frames, ignore_index=True).to_csv(OUT / "BBD_023_F5_WALK_FORWARD_PREDICTIONS.csv", index=False)

    reps = repeat_summary(g)
    reps.to_csv(OUT / "BBD_023_F5_REPEAT_SUMMARY.csv", index=False)

    coef_windows, coef_summary = coefficient_stability(g)
    coef_windows.to_csv(OUT / "BBD_023_F5_LINEAR_COEFFICIENT_WINDOWS.csv", index=False)
    coef_summary.to_csv(OUT / "BBD_023_F5_LINEAR_COEFFICIENT_STABILITY.csv", index=False)

    best = comp.iloc[0]
    repeat_groups = len(reps)
    nonident = int((~reps["identical_outputs"]).sum()) if repeat_groups else 0
    max_repeat = float(reps["output_range"].max()) if repeat_groups else 0.0

    summary = pd.DataFrame([{
        "function": F,
        "n_observations": len(g),
        "best_model": best["model"],
        "best_normalised_walk_forward_mae": float(best["normalised_walk_forward_mae"]),
        "bbd004_quadratic_normalised_loocv_mae": 0.005749,
        "bbd007_bbd_normalised_mae": 0.028072,
        "bbd007_soc_normalised_mae": 0.009054,
        "bbd003_global_recent_gradient_cosine": 0.992036,
        "repeat_groups": repeat_groups,
        "nonidentical_repeat_groups": nonident,
        "max_repeat_range": max_repeat,
        "dominant_linear_coordinate": int(coef_summary.iloc[0]["coordinate"]),
        "all_linear_coefficient_signs_stable_75pct": bool(np.all(coef_summary["sign_stability_vs_full"] >= 0.75)),
        "mechanism_interpretation": "strong_boundary_directed_static_surface_candidate" if nonident == 0 else "structured_surface_plus_repeat_variation",
        "exact_function_recovered": False,
        "independent_discriminatory_query_required": True,
    }])
    summary.to_csv(OUT / "BBD_023_F5_DECRYPTION_SUMMARY.csv", index=False)

    print("BBD 023 F5-specific decryption")
    print("\nModel competition")
    print(comp.to_string(index=False))
    print("\nLinear coefficient stability")
    print(coef_summary.to_string(index=False))
    if repeat_groups:
        print("\nRepeat summary")
        print(reps.to_string(index=False))
    print("\nSummary")
    print(summary.to_string(index=False))
    print(f"\nOutputs written to {OUT}")


if __name__ == "__main__":
    main()
