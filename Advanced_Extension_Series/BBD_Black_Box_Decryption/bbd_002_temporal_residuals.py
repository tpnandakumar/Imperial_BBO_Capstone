from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import spearmanr
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import ConstantKernel, RBF, WhiteKernel
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from bbd_001_system_identification import DIMS, enrich, load_history

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
OUT = HERE / "outputs"
OUT.mkdir(exist_ok=True)


def static_gp() -> Pipeline:
    kernel = ConstantKernel(1.0) * RBF(length_scale=1.0) + WhiteKernel(noise_level=1e-5)
    return Pipeline([
        ("scale", StandardScaler()),
        ("gp", GaussianProcessRegressor(
            kernel=kernel,
            optimizer=None,
            normalize_y=True,
            random_state=42,
        )),
    ])


def walk_forward_static_residuals(g: pd.DataFrame, dim: int) -> pd.DataFrame:
    xcols = [f"x{i}" for i in range(1, dim + 1)]
    records = []
    for week in sorted(int(w) for w in g["week"].unique() if int(w) >= 5):
        train = g[g["week"] < week].dropna(subset=xcols + ["output"])
        test = g[g["week"] == week].dropna(subset=xcols + ["output"])
        if len(train) < 4 or test.empty:
            continue
        model = static_gp()
        model.fit(train[xcols], train["output"])
        pred = float(model.predict(test[xcols])[0])
        truth = float(test["output"].iloc[0])
        records.append({
            "week": week,
            "prediction": pred,
            "truth": truth,
            "residual": truth - pred,
            "abs_error": abs(truth - pred),
        })
    return pd.DataFrame(records)


def safe_spearman(a: pd.Series, b: pd.Series) -> tuple[float, float]:
    if len(a) < 4 or a.nunique() < 2 or b.nunique() < 2:
        return np.nan, np.nan
    result = spearmanr(a, b)
    return float(result.statistic), float(result.pvalue)


def lag1_corr(s: pd.Series) -> float:
    if len(s) < 4:
        return np.nan
    x = s.iloc[:-1].to_numpy(dtype=float)
    y = s.iloc[1:].to_numpy(dtype=float)
    if np.std(x) == 0 or np.std(y) == 0:
        return np.nan
    return float(np.corrcoef(x, y)[0, 1])


def residual_trend_forecast(resids: pd.DataFrame) -> pd.DataFrame:
    """Forecast each residual using only earlier residuals and time.

    Two corrections are compared with no correction:
    1. linear residual drift over week;
    2. AR(1)-style correction using the immediately preceding residual.
    """
    rows = []
    for idx in range(3, len(resids)):
        train = resids.iloc[:idx].copy()
        test = resids.iloc[idx]
        week = float(test["week"])
        truth = float(test["residual"])

        coef = np.polyfit(train["week"].to_numpy(float), train["residual"].to_numpy(float), deg=1)
        drift_pred = float(np.polyval(coef, week))
        ar1_pred = float(train["residual"].iloc[-1])

        rows.extend([
            {"week": int(week), "correction": "none", "predicted_residual": 0.0, "truth_residual": truth, "abs_error": abs(truth)},
            {"week": int(week), "correction": "linear_time_drift", "predicted_residual": drift_pred, "truth_residual": truth, "abs_error": abs(truth - drift_pred)},
            {"week": int(week), "correction": "previous_residual", "predicted_residual": ar1_pred, "truth_residual": truth, "abs_error": abs(truth - ar1_pred)},
        ])
    return pd.DataFrame(rows)


def repeat_detail(g: pd.DataFrame, dim: int) -> pd.DataFrame:
    xcols = [f"x{i}" for i in range(1, dim + 1)]
    tmp = g.copy()
    tmp["coord_key"] = tmp[xcols].round(12).astype(str).agg("|".join, axis=1)
    records = []
    for key, z in tmp.groupby("coord_key"):
        if len(z) < 2:
            continue
        vals = z["output"].to_numpy(float)
        records.append({
            "coordinate": key,
            "n": len(z),
            "weeks": ";".join(str(int(w)) for w in z["week"]),
            "outputs": ";".join(f"{v:.17g}" for v in vals),
            "range": float(vals.max() - vals.min()),
            "std_population": float(np.std(vals, ddof=0)),
            "identical_outputs": bool(np.all(vals == vals[0])),
        })
    return pd.DataFrame(records)


def main() -> None:
    hist = load_history()
    summary_rows = []
    residual_rows = []
    correction_rows = []
    repeat_rows = []

    for f in range(1, 9):
        g = enrich(hist[hist["function"] == f], DIMS[f])
        resids = walk_forward_static_residuals(g, DIMS[f])
        if resids.empty:
            continue
        resids.insert(0, "function", f)
        residual_rows.append(resids)

        rho_time, p_time = safe_spearman(resids["week"], resids["residual"])
        rho_abs_time, p_abs_time = safe_spearman(resids["week"], resids["abs_error"])
        lag_corr = lag1_corr(resids["residual"])

        corrections = residual_trend_forecast(resids)
        if not corrections.empty:
            corrections.insert(0, "function", f)
            correction_rows.append(corrections)
            mae_by_method = corrections.groupby("correction")["abs_error"].mean().to_dict()
        else:
            mae_by_method = {}

        rep = repeat_detail(g, DIMS[f])
        if not rep.empty:
            rep.insert(0, "function", f)
            repeat_rows.append(rep)

        baseline_mae = mae_by_method.get("none", np.nan)
        drift_mae = mae_by_method.get("linear_time_drift", np.nan)
        prev_mae = mae_by_method.get("previous_residual", np.nan)
        best_corr = "none"
        vals = {"none": baseline_mae, "linear_time_drift": drift_mae, "previous_residual": prev_mae}
        finite_vals = {k: v for k, v in vals.items() if np.isfinite(v)}
        if finite_vals:
            best_corr = min(finite_vals, key=finite_vals.get)

        summary_rows.append({
            "function": f,
            "n_walk_forward_residuals": len(resids),
            "residual_spearman_with_week": rho_time,
            "residual_time_p_value": p_time,
            "abs_error_spearman_with_week": rho_abs_time,
            "abs_error_time_p_value": p_abs_time,
            "residual_lag1_correlation": lag_corr,
            "baseline_residual_mae": baseline_mae,
            "linear_drift_residual_mae": drift_mae,
            "previous_residual_mae": prev_mae,
            "best_residual_correction": best_corr,
            "temporal_correction_improves": bool(best_corr != "none" and finite_vals.get(best_corr, np.inf) < finite_vals.get("none", np.inf)),
            "repeat_groups": 0 if rep.empty else len(rep),
            "nonidentical_repeat_groups": 0 if rep.empty else int((~rep["identical_outputs"]).sum()),
            "max_repeat_range": 0.0 if rep.empty else float(rep["range"].max()),
        })

    summary = pd.DataFrame(summary_rows)
    summary.to_csv(OUT / "BBD_002_TEMPORAL_RESIDUAL_SUMMARY.csv", index=False)
    if residual_rows:
        pd.concat(residual_rows, ignore_index=True).to_csv(OUT / "BBD_002_STATIC_GP_RESIDUALS.csv", index=False)
    if correction_rows:
        pd.concat(correction_rows, ignore_index=True).to_csv(OUT / "BBD_002_RESIDUAL_CORRECTION_COMPETITION.csv", index=False)
    if repeat_rows:
        pd.concat(repeat_rows, ignore_index=True).to_csv(OUT / "BBD_002_REPEATABILITY_DETAIL.csv", index=False)

    print(summary.to_string(index=False))
    print(f"\nOutputs written to {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
