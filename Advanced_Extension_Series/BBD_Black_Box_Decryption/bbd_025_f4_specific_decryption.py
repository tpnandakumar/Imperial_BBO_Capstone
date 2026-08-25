from __future__ import annotations

from pathlib import Path
import warnings

import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, RegressorMixin, clone
from sklearn.ensemble import ExtraTreesRegressor, RandomForestRegressor
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
F = 4
D = 4
MIN_TRAIN = 5
RANDOM_STATE = 42
CENTRES = (0.0, 0.25, 0.5, 0.75, 1.0)
SCALES = (0.5, 1.0, 2.0, 5.0, 10.0, 20.0)


def rosenbrock_feature(X: np.ndarray, centre: float, scale: float) -> np.ndarray:
    z = scale * (np.asarray(X, dtype=float) - centre)
    values = np.sum(
        100.0 * (z[:, 1:] - z[:, :-1] ** 2) ** 2
        + (1.0 - z[:, :-1]) ** 2,
        axis=1,
    )
    return values.reshape(-1, 1)


class NestedRosenbrockRegressor(BaseEstimator, RegressorMixin):
    """Select the Rosenbrock transform inside each training window only."""

    def __init__(self, centres=CENTRES, scales=SCALES):
        self.centres = centres
        self.scales = scales

    def fit(self, X, y):
        X = np.asarray(X, dtype=float)
        y = np.asarray(y, dtype=float)
        best = None
        for centre in self.centres:
            for scale in self.scales:
                preds = np.empty(len(y), dtype=float)
                for i in range(len(y)):
                    keep = np.arange(len(y)) != i
                    model = LinearRegression().fit(
                        rosenbrock_feature(X[keep], centre, scale), y[keep]
                    )
                    preds[i] = model.predict(
                        rosenbrock_feature(X[i:i + 1], centre, scale)
                    )[0]
                mae = float(mean_absolute_error(y, preds))
                candidate = (mae, centre, scale)
                if best is None or candidate < best:
                    best = candidate
        _, self.centre_, self.scale_ = best
        self.model_ = LinearRegression().fit(
            rosenbrock_feature(X, self.centre_, self.scale_), y
        )
        return self

    def predict(self, X):
        return self.model_.predict(
            rosenbrock_feature(np.asarray(X, dtype=float), self.centre_, self.scale_)
        )


def gp(kind: str):
    base = (
        Matern(np.ones(D), (1e-3, 1e3), nu=2.5)
        if kind == "matern"
        else RBF(np.ones(D), (1e-3, 1e3))
    )
    kernel = ConstantKernel(1.0, (1e-3, 1e3)) * base + WhiteKernel(
        1e-6, (1e-10, 1e1)
    )
    return Pipeline([
        ("scale", StandardScaler()),
        ("model", GaussianProcessRegressor(
            kernel=kernel,
            normalize_y=True,
            n_restarts_optimizer=2,
            random_state=RANDOM_STATE,
        )),
    ])


def ridge(degree: int, alpha: float):
    steps = []
    if degree > 1:
        steps.append(("poly", PolynomialFeatures(degree, include_bias=False)))
    steps.extend([("scale", StandardScaler()), ("model", Ridge(alpha=alpha))])
    return Pipeline(steps)


def candidates():
    return [
        ("nested_rosenbrock_affine", NestedRosenbrockRegressor()),
        ("linear_ridge_1e-4", ridge(1, 1e-4)),
        ("linear_ridge_1e-2", ridge(1, 1e-2)),
        ("quadratic_ridge_1e-4", ridge(2, 1e-4)),
        ("quadratic_ridge_1e-2", ridge(2, 1e-2)),
        ("quadratic_ridge_0.1", ridge(2, 0.1)),
        ("cubic_ridge_1e-2", ridge(3, 1e-2)),
        ("gp_matern_2.5", gp("matern")),
        ("gp_rbf", gp("rbf")),
        ("random_forest", RandomForestRegressor(
            n_estimators=500, min_samples_leaf=1, random_state=RANDOM_STATE
        )),
        ("extra_trees", ExtraTreesRegressor(
            n_estimators=500, min_samples_leaf=1, random_state=RANDOM_STATE
        )),
    ]


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
            prediction = float(np.asarray(model.predict(X[i:i + 1])).ravel()[0])
        row = {
            "week": int(g.loc[i, "week"]),
            "actual": float(y[i]),
            "prediction": prediction,
            "absolute_error": abs(float(y[i]) - prediction),
        }
        if isinstance(model, NestedRosenbrockRegressor):
            row["selected_centre"] = model.centre_
            row["selected_scale"] = model.scale_
        rows.append(row)
    return pd.DataFrame(rows)


def repeat_summary(g: pd.DataFrame) -> pd.DataFrame:
    xcols = [f"x{i}" for i in range(1, D + 1)]
    rows = []
    for coords, group in g.groupby(xcols, sort=False, dropna=False):
        if len(group) < 2:
            continue
        values = group["output"].to_numpy(float)
        rows.append({
            "coordinate": "-".join(f"{float(v):.6f}" for v in coords),
            "weeks": ";".join(str(int(v)) for v in group["week"]),
            "n_repeats": len(group),
            "output_range": float(values.max() - values.min()),
            "identical_outputs": bool(np.allclose(values, values[0], atol=1e-12, rtol=0.0)),
        })
    return pd.DataFrame(rows)


def coefficient_stability(g: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    xcols = [f"x{i}" for i in range(1, D + 1)]
    X = g[xcols].to_numpy(float)
    y = g["output"].to_numpy(float)
    rows = []
    for n in range(MIN_TRAIN, len(g) + 1):
        model = ridge(1, 1e-4).fit(X[:n], y[:n])
        scaler = model.named_steps["scale"]
        reg = model.named_steps["model"]
        raw = np.asarray(reg.coef_) / scaler.scale_
        row = {"through_week": int(g.loc[n - 1, "week"]), "n_train": n}
        row.update({f"x{i}": float(value) for i, value in enumerate(raw, 1)})
        rows.append(row)
    windows = pd.DataFrame(rows)
    summary = []
    for i in range(1, D + 1):
        values = windows[f"x{i}"].to_numpy(float)
        final = float(values[-1])
        summary.append({
            "coordinate": f"x{i}",
            "full_history_effect": final,
            "absolute_rank": 0,
            "sign_stability": float(np.mean(np.sign(values) == np.sign(final))),
            "window_std": float(np.std(values)),
            "direction": "increase" if final > 0 else "decrease",
        })
    order = np.argsort([-abs(row["full_history_effect"]) for row in summary])
    for rank, index in enumerate(order, 1):
        summary[index]["absolute_rank"] = rank
    return windows, pd.DataFrame(summary).sort_values("absolute_rank")


def main():
    history = load_history()
    g = history[history["function"] == F].sort_values("week").reset_index(drop=True)
    output_range = float(np.ptp(g["output"].to_numpy(float))) or 1.0

    comparisons, predictions = [], []
    for name, estimator in candidates():
        result = walk_forward(g, estimator)
        result.insert(0, "model", name)
        predictions.append(result)
        comparisons.append({
            "model": name,
            "walk_forward_tests": len(result),
            "walk_forward_mae": float(result["absolute_error"].mean()),
            "normalised_walk_forward_mae": float(result["absolute_error"].mean() / output_range),
            "median_absolute_error": float(result["absolute_error"].median()),
            "max_absolute_error": float(result["absolute_error"].max()),
        })

    competition = pd.DataFrame(comparisons).sort_values(
        "normalised_walk_forward_mae"
    ).reset_index(drop=True)
    competition.insert(0, "rank", np.arange(1, len(competition) + 1))
    competition.to_csv(OUT / "BBD_025_F4_MODEL_COMPETITION.csv", index=False)
    pd.concat(predictions, ignore_index=True).to_csv(
        OUT / "BBD_025_F4_WALK_FORWARD_PREDICTIONS.csv", index=False
    )

    repeats = repeat_summary(g)
    repeats.to_csv(OUT / "BBD_025_F4_REPEAT_SUMMARY.csv", index=False)
    windows, effects = coefficient_stability(g)
    windows.to_csv(OUT / "BBD_025_F4_LINEAR_EFFECT_WINDOWS.csv", index=False)
    effects.to_csv(OUT / "BBD_025_F4_LINEAR_EFFECT_STABILITY.csv", index=False)

    best = competition.iloc[0]
    rosenbrock_rank = int(
        competition.loc[competition["model"] == "nested_rosenbrock_affine", "rank"].iloc[0]
    )
    summary = pd.DataFrame([{
        "function": F,
        "n_observations": len(g),
        "best_model": best["model"],
        "best_normalised_walk_forward_mae": float(best["normalised_walk_forward_mae"]),
        "nested_rosenbrock_rank": rosenbrock_rank,
        "repeat_groups": len(repeats),
        "nonidentical_repeat_groups": int((~repeats["identical_outputs"]).sum()) if len(repeats) else 0,
        "mechanism_interpretation": "static_coordinate_surface_with_rosenbrock_lead_under_test",
        "exact_function_recovered": False,
        "independent_query_required": True,
    }])
    summary.to_csv(OUT / "BBD_025_F4_DECRYPTION_SUMMARY.csv", index=False)

    print("BBD 025 F4-specific decryption")
    print(competition.to_string(index=False))
    print("\nRepeatability")
    print(repeats.to_string(index=False) if len(repeats) else "No repeated coordinates")
    print("\nLinear-effect stability")
    print(effects.to_string(index=False))
    print("\nSummary")
    print(summary.to_string(index=False))


if __name__ == "__main__":
    main()
