from __future__ import annotations

import csv
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.compose import TransformedTargetRegressor
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import ConstantKernel, RBF, WhiteKernel
from sklearn.linear_model import Ridge
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
OUT = HERE / "outputs"
OUT.mkdir(exist_ok=True)

DIMS = {1: 2, 2: 2, 3: 3, 4: 4, 5: 4, 6: 5, 7: 6, 8: 8}


def load_history() -> pd.DataFrame:
    early = pd.read_csv(ROOT / "PFRAMOS" / "data" / "recovered_exact_history.csv")
    early = early[early["Week"].astype(int) <= 11].copy()
    rows = []
    for _, r in early.iterrows():
        f = int(r["Function"])
        row = {"week": int(r["Week"]), "function": f, "output": float(r["Output"])}
        for i in range(1, DIMS[f] + 1):
            row[f"x{i}"] = float(r[f"Input_{i}"])
        rows.append(row)

    for week in (12, 13):
        inp = pd.read_csv(ROOT / f"Week_{week:02d}" / f"week_{week:02d}_inputs.csv")
        out = pd.read_csv(ROOT / f"Week_{week:02d}" / f"week_{week:02d}_results.csv")
        for f in range(1, 9):
            irow = inp.iloc[f - 1]
            orow = out.iloc[f - 1]
            row = {"week": week, "function": f, "output": float(orow["output"])}
            for i in range(1, DIMS[f] + 1):
                row[f"x{i}"] = float(irow[f"x{i}"])
            rows.append(row)
    return pd.DataFrame(rows).sort_values(["function", "week"]).reset_index(drop=True)


def enrich(g: pd.DataFrame, dim: int) -> pd.DataFrame:
    g = g.sort_values("week").copy()
    xcols = [f"x{i}" for i in range(1, dim + 1)]
    g["t_norm"] = (g["week"] - 1) / 12.0
    for c in xcols:
        g[f"d_{c}"] = g[c].diff().fillna(0.0)
    dcols = [f"d_{c}" for c in xcols]
    g["step_norm"] = np.sqrt((g[dcols] ** 2).sum(axis=1))
    g["prev_y"] = g["output"].shift(1)
    return g


def model_specs(dim: int):
    x = [f"x{i}" for i in range(1, dim + 1)]
    dx = [f"d_x{i}" for i in range(1, dim + 1)]
    gp_kernel = ConstantKernel(1.0) * RBF(length_scale=1.0) + WhiteKernel(noise_level=1e-5)
    return {
        "H0_static_ridge": (x, Pipeline([("scale", StandardScaler()), ("ridge", Ridge(alpha=1.0))])),
        "H0_static_quadratic": (x, Pipeline([("poly", PolynomialFeatures(degree=2, include_bias=False)), ("scale", StandardScaler()), ("ridge", Ridge(alpha=2.0))])),
        "H0_static_gp": (x, Pipeline([("scale", StandardScaler()), ("gp", GaussianProcessRegressor(kernel=gp_kernel, optimizer=None, normalize_y=True, random_state=42))])),
        "H2_time_ridge": (x + ["t_norm"], Pipeline([("scale", StandardScaler()), ("ridge", Ridge(alpha=1.0))])),
        "H2_time_gp": (x + ["t_norm"], Pipeline([("scale", StandardScaler()), ("gp", GaussianProcessRegressor(kernel=gp_kernel, optimizer=None, normalize_y=True, random_state=42))])),
        "H5_movement_ridge": (x + ["t_norm"] + dx + ["step_norm"], Pipeline([("scale", StandardScaler()), ("ridge", Ridge(alpha=2.0))])),
        "H4_state_ridge": (x + ["t_norm"] + dx + ["step_norm", "prev_y"], Pipeline([("scale", StandardScaler()), ("ridge", Ridge(alpha=2.0))])),
    }


def walk_forward_scores(g: pd.DataFrame, dim: int) -> list[dict]:
    specs = model_specs(dim)
    results = []
    # Start at week 5 so each training fold has at least four observations.
    test_weeks = [w for w in g["week"].tolist() if w >= 5]
    scale = float(np.std(g["output"], ddof=1)) or 1.0
    for name, (features, model) in specs.items():
        errs = []
        preds = []
        truths = []
        weeks = []
        for w in test_weeks:
            train = g[g["week"] < w].dropna(subset=features + ["output"])
            test = g[g["week"] == w].dropna(subset=features + ["output"])
            if len(train) < 3 or test.empty:
                continue
            try:
                model.fit(train[features], train["output"])
                pred = float(model.predict(test[features])[0])
            except Exception:
                continue
            truth = float(test["output"].iloc[0])
            errs.append(abs(pred - truth))
            preds.append(pred)
            truths.append(truth)
            weeks.append(w)
        if errs:
            results.append({
                "model": name,
                "n_forecasts": len(errs),
                "mae": float(np.mean(errs)),
                "normalised_mae": float(np.mean(errs) / scale),
                "last_week_pred": preds[-1],
                "last_week_truth": truths[-1],
                "last_test_week": weeks[-1],
            })
    return results


def repeated_coordinate_diagnostics(g: pd.DataFrame, dim: int) -> dict:
    xcols = [f"x{i}" for i in range(1, dim + 1)]
    tmp = g.copy()
    tmp["coord_key"] = tmp[xcols].round(12).astype(str).agg("|".join, axis=1)
    repeated = tmp.groupby("coord_key").filter(lambda z: len(z) > 1)
    if repeated.empty:
        return {"repeated_groups": 0, "repeated_observations": 0, "max_repeat_range": 0.0, "nonidentical_repeat_groups": 0}
    ranges = repeated.groupby("coord_key")["output"].agg(lambda s: float(s.max() - s.min()))
    return {
        "repeated_groups": int(ranges.shape[0]),
        "repeated_observations": int(repeated.shape[0]),
        "max_repeat_range": float(ranges.max()),
        "nonidentical_repeat_groups": int((ranges > 0).sum()),
    }


def main() -> None:
    hist = load_history()
    competition = []
    diagnostics = []
    summary = []

    for f in range(1, 9):
        g = enrich(hist[hist["function"] == f], DIMS[f])
        scores = walk_forward_scores(g, DIMS[f])
        for s in scores:
            competition.append({"function": f, **s})
        diag = repeated_coordinate_diagnostics(g, DIMS[f])
        diagnostics.append({"function": f, **diag})

        ranked = sorted(scores, key=lambda r: r["normalised_mae"])
        winner = ranked[0] if ranked else None
        best_static = min((r for r in ranked if r["model"].startswith("H0_")), key=lambda r: r["normalised_mae"], default=None)
        best_temporal = min((r for r in ranked if not r["model"].startswith("H0_")), key=lambda r: r["normalised_mae"], default=None)
        temporal_gain = None
        if best_static and best_temporal:
            temporal_gain = best_static["normalised_mae"] - best_temporal["normalised_mae"]
        summary.append({
            "function": f,
            "winning_model": winner["model"] if winner else "none",
            "winning_normalised_mae": winner["normalised_mae"] if winner else np.nan,
            "best_static_model": best_static["model"] if best_static else "none",
            "best_temporal_model": best_temporal["model"] if best_temporal else "none",
            "temporal_gain_over_static": temporal_gain,
            "temporal_signal_flag": bool(temporal_gain is not None and temporal_gain > 0),
            "nonidentical_repeat_groups": diag["nonidentical_repeat_groups"],
        })

    pd.DataFrame(competition).to_csv(OUT / "BBD_001_MODEL_COMPETITION.csv", index=False)
    pd.DataFrame(diagnostics).to_csv(OUT / "BBD_001_TEMPORAL_DIAGNOSTICS.csv", index=False)
    pd.DataFrame(summary).to_csv(OUT / "BBD_001_HYPOTHESIS_SUMMARY.csv", index=False)

    print(pd.DataFrame(summary).to_string(index=False))
    print(f"\nOutputs written to {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
