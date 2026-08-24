from __future__ import annotations

from pathlib import Path
import sys
import warnings

import numpy as np
import pandas as pd
from sklearn.base import clone
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.metrics import mean_absolute_error
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

from bbd_001_system_identification import DIMS, load_history

HERE = Path(__file__).resolve().parent
OUT = HERE / "outputs"
OUT.mkdir(exist_ok=True)
ROOT = HERE.parents[2]
SOC_DIR = ROOT / "Advanced_Extension_Series" / "SOC_Surrogate_Optimisation_Competition"
sys.path.insert(0, str(SOC_DIR))
from surrogate_evaluator import model_library as soc_model_library  # noqa: E402

CENTRES = [0.0, 0.25, 0.5, 0.75, 1.0]
SCALES = [0.5, 1.0, 2.0, 5.0, 10.0, 20.0]
ALPHAS = [1e-4, 1e-2, 0.1, 1.0, 10.0]
MIN_TRAIN = 5


def sphere(z):
    return np.sum(z ** 2, axis=1)


def ellipsoid(z):
    w = np.logspace(0, 3, z.shape[1])
    return np.sum(w * z ** 2, axis=1)


def rastrigin(z):
    return 10.0 * z.shape[1] + np.sum(z ** 2 - 10.0 * np.cos(2.0 * np.pi * z), axis=1)


def ackley(z):
    d = z.shape[1]
    a = -20.0 * np.exp(-0.2 * np.sqrt(np.sum(z ** 2, axis=1) / d))
    b = -np.exp(np.sum(np.cos(2.0 * np.pi * z), axis=1) / d)
    return a + b + 20.0 + np.e


def griewank(z):
    idx = np.sqrt(np.arange(1, z.shape[1] + 1))
    return np.sum(z ** 2, axis=1) / 4000.0 - np.prod(np.cos(z / idx), axis=1) + 1.0


def schwefel(z):
    return 418.9829 * z.shape[1] - np.sum(z * np.sin(np.sqrt(np.abs(z))), axis=1)


def rosenbrock(z):
    if z.shape[1] < 2:
        return z[:, 0] ** 2
    return np.sum(100.0 * (z[:, 1:] - z[:, :-1] ** 2) ** 2 + (1.0 - z[:, :-1]) ** 2, axis=1)


BENCHMARKS = {
    "sphere": sphere,
    "ellipsoid": ellipsoid,
    "rastrigin": rastrigin,
    "ackley": ackley,
    "griewank": griewank,
    "schwefel": schwefel,
    "rosenbrock": rosenbrock,
}


def loo_predictions(estimator, X, y):
    pred = np.empty(len(y), dtype=float)
    for i in range(len(y)):
        mask = np.ones(len(y), dtype=bool)
        mask[i] = False
        m = clone(estimator)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            m.fit(X[mask], y[mask])
        pred[i] = float(m.predict(X[i:i+1])[0])
    return pred


def select_soc(X, y):
    candidates = []
    for c in soc_model_library(len(y), X.shape[1]):
        try:
            p = loo_predictions(c.estimator, X, y)
            candidates.append((float(mean_absolute_error(y, p)), c.name, c.estimator))
        except Exception:
            pass
    return min(candidates, key=lambda r: r[0])


def symbolic_candidates(dim):
    out = []
    for degree in [1, 2]:
        for alpha in ALPHAS:
            est = Pipeline([
                ("poly", PolynomialFeatures(degree=degree, include_bias=False)),
                ("scale", StandardScaler()),
                ("ridge", Ridge(alpha=alpha)),
            ])
            out.append((f"symbolic_d{degree}_a{alpha:g}", est))
    return out


def benchmark_feature(X, family, centre, scale):
    z = scale * (X - centre)
    return BENCHMARKS[family](z).reshape(-1, 1)


def select_benchmark(X, y):
    best = None
    for family in BENCHMARKS:
        for centre in CENTRES:
            for scale in SCALES:
                v = benchmark_feature(X, family, centre, scale)
                pred = loo_predictions(LinearRegression(), v, y)
                mae = float(mean_absolute_error(y, pred))
                row = (mae, f"benchmark_{family}_c{centre:g}_s{scale:g}", family, centre, scale)
                if best is None or row[0] < best[0]:
                    best = row
    return best


def select_bbd(X, y):
    best = None
    for name, est in symbolic_candidates(X.shape[1]):
        try:
            p = loo_predictions(est, X, y)
            row = (float(mean_absolute_error(y, p)), name, "symbolic", est)
            if best is None or row[0] < best[0]:
                best = row
        except Exception:
            pass
    b = select_benchmark(X, y)
    benchmark_row = (b[0], b[1], "benchmark", b[2:])
    if best is None or benchmark_row[0] < best[0]:
        best = benchmark_row
    return best


def fit_predict_bbd(choice, Xtr, ytr, Xte):
    _, _, kind, obj = choice
    if kind == "symbolic":
        m = clone(obj)
        m.fit(Xtr, ytr)
        return float(m.predict(Xte)[0])
    family, centre, scale = obj
    vtr = benchmark_feature(Xtr, family, centre, scale)
    vte = benchmark_feature(Xte, family, centre, scale)
    m = LinearRegression().fit(vtr, ytr)
    return float(m.predict(vte)[0])


def main():
    hist = load_history()
    rows = []
    summary = []

    for f in range(1, 9):
        d = DIMS[f]
        g = hist[hist["function"] == f].sort_values("week").reset_index(drop=True)
        xcols = [f"x{i}" for i in range(1, d + 1)]
        X = g[xcols].to_numpy(float)
        y = g["output"].to_numpy(float)
        weeks = g["week"].to_numpy(int)
        yscale = float(np.std(y, ddof=1)) or 1.0

        for test_idx in range(MIN_TRAIN, len(y)):
            Xtr, ytr = X[:test_idx], y[:test_idx]
            Xte = X[test_idx:test_idx + 1]
            truth = float(y[test_idx])

            bbd_choice = select_bbd(Xtr, ytr)
            bbd_pred = fit_predict_bbd(bbd_choice, Xtr, ytr, Xte)

            soc_mae, soc_name, soc_est = select_soc(Xtr, ytr)
            sm = clone(soc_est)
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                sm.fit(Xtr, ytr)
            soc_pred = float(sm.predict(Xte)[0])

            rows.append({
                "function": f,
                "test_week": int(weeks[test_idx]),
                "n_training_observations": int(test_idx),
                "truth": truth,
                "bbd_selected_model": bbd_choice[1],
                "bbd_training_loo_mae": bbd_choice[0],
                "bbd_prediction": bbd_pred,
                "bbd_absolute_error": abs(truth - bbd_pred),
                "soc_selected_model": soc_name,
                "soc_training_loo_mae": soc_mae,
                "soc_prediction": soc_pred,
                "soc_absolute_error": abs(truth - soc_pred),
            })

        part = pd.DataFrame([r for r in rows if r["function"] == f])
        bmae = float(part["bbd_absolute_error"].mean())
        smae = float(part["soc_absolute_error"].mean())
        bnorm, snorm = bmae / yscale, smae / yscale
        if abs(bnorm - snorm) < 1e-12:
            winner = "tie"
        else:
            winner = "BBD" if bnorm < snorm else "SOC"
        summary.append({
            "function": f,
            "n_prospective_tests": len(part),
            "bbd_mae": bmae,
            "soc_mae": smae,
            "bbd_normalised_mae": bnorm,
            "soc_normalised_mae": snorm,
            "relative_gain_of_bbd": (snorm - bnorm) / max(snorm, 1e-15),
            "winner": winner,
            "bbd_test_wins": int((part["bbd_absolute_error"] < part["soc_absolute_error"]).sum()),
            "soc_test_wins": int((part["soc_absolute_error"] < part["bbd_absolute_error"]).sum()),
        })

    detail = pd.DataFrame(rows)
    summ = pd.DataFrame(summary).sort_values("function")
    detail.to_csv(OUT / "BBD_007_PROSPECTIVE_PREDICTIONS.csv", index=False)
    summ.to_csv(OUT / "BBD_007_BBD_VS_SOC_SUMMARY.csv", index=False)

    overall = pd.DataFrame([{
        "functions_won_by_bbd": int((summ["winner"] == "BBD").sum()),
        "functions_won_by_soc": int((summ["winner"] == "SOC").sum()),
        "mean_bbd_normalised_mae": float(summ["bbd_normalised_mae"].mean()),
        "mean_soc_normalised_mae": float(summ["soc_normalised_mae"].mean()),
    }])
    overall.to_csv(OUT / "BBD_007_OVERALL_RESULT.csv", index=False)

    print("BBD 007 prospective BBD versus SOC challenge")
    print(summ.to_string(index=False))
    print("\nOverall")
    print(overall.to_string(index=False))
    print(f"\nOutputs written to {OUT}")


if __name__ == "__main__":
    main()
