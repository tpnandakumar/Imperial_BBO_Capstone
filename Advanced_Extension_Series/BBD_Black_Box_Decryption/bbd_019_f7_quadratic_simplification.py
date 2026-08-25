from __future__ import annotations

from pathlib import Path
import warnings
import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

from bbd_001_system_identification import load_history

HERE = Path(__file__).resolve().parent
OUT = HERE / "outputs"
OUT.mkdir(exist_ok=True)
F = 7
D = 6
MIN_TRAIN = 5
ALPHA = 1e-4
TOP_K_GRID = [3, 5, 7, 9, 12, 15, 20, 27]


def fit_ranked_quadratic(X: np.ndarray, y: np.ndarray, top_k: int):
    poly = PolynomialFeatures(degree=2, include_bias=False)
    Z = poly.fit_transform(X)
    names = np.asarray(poly.get_feature_names_out([f"x{i}" for i in range(1, D + 1)]))
    scaler = StandardScaler()
    Zs = scaler.fit_transform(Z)
    ridge = Ridge(alpha=ALPHA).fit(Zs, y)
    raw_coef = ridge.coef_ / scaler.scale_
    raw_intercept = float(ridge.intercept_ - np.dot(ridge.coef_, scaler.mean_ / scaler.scale_))
    order = np.argsort(-np.abs(raw_coef))
    keep = order[: min(top_k, len(order))]
    return poly, names, keep, raw_coef, raw_intercept


def refit_selected(X: np.ndarray, y: np.ndarray, poly, keep: np.ndarray):
    Z = poly.transform(X)[:, keep]
    scaler = StandardScaler()
    Zs = scaler.fit_transform(Z)
    ridge = Ridge(alpha=ALPHA).fit(Zs, y)
    return scaler, ridge


def walk_forward_complexity(g: pd.DataFrame, top_k: int) -> pd.DataFrame:
    xcols = [f"x{i}" for i in range(1, D + 1)]
    X = g[xcols].to_numpy(float)
    y = g["output"].to_numpy(float)
    rows = []
    for i in range(MIN_TRAIN, len(g)):
        poly, names, keep, _, _ = fit_ranked_quadratic(X[:i], y[:i], top_k)
        scaler, ridge = refit_selected(X[:i], y[:i], poly, keep)
        Ztest = poly.transform(X[i:i+1])[:, keep]
        pred = float(ridge.predict(scaler.transform(Ztest))[0])
        rows.append({
            "top_k": top_k,
            "week": int(g.loc[i, "week"]),
            "actual": float(y[i]),
            "prediction": pred,
            "absolute_error": abs(float(y[i]) - pred),
            "selected_terms": "|".join(names[keep].tolist()),
        })
    return pd.DataFrame(rows)


def coefficient_stability(g: pd.DataFrame) -> pd.DataFrame:
    xcols = [f"x{i}" for i in range(1, D + 1)]
    X = g[xcols].to_numpy(float)
    y = g["output"].to_numpy(float)
    rows = []
    for i in range(MIN_TRAIN, len(g) + 1):
        poly, names, _, raw, _ = fit_ranked_quadratic(X[:i], y[:i], len(poly_names()) if False else 999)
        for name, coef in zip(names, raw):
            rows.append({"train_through_week": int(g.loc[i-1, "week"]), "term": name, "coefficient": float(coef)})
    c = pd.DataFrame(rows)
    out = []
    for term, grp in c.groupby("term"):
        vals = grp["coefficient"].to_numpy(float)
        nz = np.abs(vals) > 1e-10
        signs = np.sign(vals[nz])
        sign_stability = float(max(np.mean(signs > 0), np.mean(signs < 0))) if len(signs) else 0.0
        out.append({
            "term": term,
            "mean_coefficient": float(vals.mean()),
            "median_coefficient": float(np.median(vals)),
            "mean_abs_coefficient": float(np.mean(np.abs(vals))),
            "coefficient_sd": float(vals.std(ddof=0)),
            "sign_stability": sign_stability,
            "n_training_windows": len(vals),
        })
    return pd.DataFrame(out).sort_values(["sign_stability", "mean_abs_coefficient"], ascending=[False, False]).reset_index(drop=True)


def poly_names():
    p = PolynomialFeatures(degree=2, include_bias=False)
    p.fit(np.zeros((1, D)))
    return p.get_feature_names_out([f"x{i}" for i in range(1, D + 1)])


def final_equation(g: pd.DataFrame, top_k: int):
    xcols = [f"x{i}" for i in range(1, D + 1)]
    X = g[xcols].to_numpy(float)
    y = g["output"].to_numpy(float)
    poly, names, keep, _, _ = fit_ranked_quadratic(X, y, top_k)
    scaler, ridge = refit_selected(X, y, poly, keep)
    raw = ridge.coef_ / scaler.scale_
    intercept = float(ridge.intercept_ - np.dot(ridge.coef_, scaler.mean_ / scaler.scale_))
    terms = pd.DataFrame({"term": names[keep], "coefficient": raw})
    terms["absolute_coefficient"] = np.abs(terms["coefficient"])
    terms = terms.sort_values("absolute_coefficient", ascending=False).reset_index(drop=True)
    eq = f"{intercept:.10g}"
    for _, r in terms.iterrows():
        c = float(r["coefficient"])
        eq += f" {'+' if c >= 0 else '-'} {abs(c):.10g}*{r['term'].replace(' ', '*')}"
    return intercept, terms, eq


def main():
    hist = load_history()
    g = hist[hist["function"] == F].sort_values("week").reset_index(drop=True)
    y = g["output"].to_numpy(float)
    yrange = float(np.ptp(y)) or 1.0

    pred_frames = []
    comp = []
    for k in TOP_K_GRID:
        p = walk_forward_complexity(g, k)
        pred_frames.append(p)
        mae = float(mean_absolute_error(p["actual"], p["prediction"]))
        comp.append({
            "top_k_terms": k,
            "walk_forward_tests": len(p),
            "walk_forward_mae": mae,
            "normalised_walk_forward_mae": mae / yrange,
            "max_absolute_error": float(p["absolute_error"].max()),
        })

    comp = pd.DataFrame(comp).sort_values(["normalised_walk_forward_mae", "top_k_terms"]).reset_index(drop=True)
    comp.insert(0, "rank", np.arange(1, len(comp) + 1))
    comp.to_csv(OUT / "BBD_019_F7_COMPLEXITY_COMPETITION.csv", index=False)
    pd.concat(pred_frames, ignore_index=True).to_csv(OUT / "BBD_019_F7_WALK_FORWARD_PREDICTIONS.csv", index=False)

    stability = coefficient_stability(g)
    stability.to_csv(OUT / "BBD_019_F7_TERM_STABILITY.csv", index=False)

    best_k = int(comp.iloc[0]["top_k_terms"])
    intercept, terms, equation = final_equation(g, best_k)
    terms.to_csv(OUT / "BBD_019_F7_FINAL_TERMS.csv", index=False)

    best_mae = float(comp.iloc[0]["normalised_walk_forward_mae"])
    full27 = float(comp.loc[comp["top_k_terms"] == 27, "normalised_walk_forward_mae"].iloc[0])
    bbd018 = 0.034870
    simplification_gain = full27 - best_mae

    summary = pd.DataFrame([{
        "function": F,
        "n_observations": len(g),
        "selected_term_count": best_k,
        "selected_normalised_walk_forward_mae": best_mae,
        "full_27_term_normalised_walk_forward_mae": full27,
        "normalised_gain_vs_full_quadratic": simplification_gain,
        "bbd018_best_normalised_walk_forward_mae": bbd018,
        "final_intercept": intercept,
        "compact_equation": equation,
        "exact_function_recovered": False,
        "independent_discriminatory_query_required": True,
        "interpretation": "simplified_quadratic_candidate" if best_k < 27 else "full_quadratic_still_required",
    }])
    summary.to_csv(OUT / "BBD_019_F7_SIMPLIFICATION_SUMMARY.csv", index=False)

    print("BBD 019 F7 quadratic simplification")
    print("\nComplexity competition")
    print(comp.to_string(index=False))
    print("\nSelected equation terms")
    print(terms.to_string(index=False))
    print("\nCompact equation")
    print(equation)
    print("\nSummary")
    print(summary.to_string(index=False))
    print(f"\nOutputs written to {OUT}")


if __name__ == "__main__":
    main()
