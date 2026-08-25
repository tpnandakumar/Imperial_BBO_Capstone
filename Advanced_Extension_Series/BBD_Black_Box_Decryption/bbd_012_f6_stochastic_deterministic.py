from __future__ import annotations

from pathlib import Path
import warnings

import numpy as np
import pandas as pd
from scipy.optimize import minimize
from scipy.stats import spearmanr
from sklearn.base import clone
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import ConstantKernel, Matern, WhiteKernel

from bbd_001_system_identification import load_history

HERE = Path(__file__).resolve().parent
OUT = HERE / "outputs"
OUT.mkdir(exist_ok=True)
F = 6
D = 5
MIN_TRAIN = 5
EPS = 1e-10


def gp(dim: int):
    kernel = ConstantKernel(1.0, (1e-3, 1e3)) * Matern(
        length_scale=np.ones(dim), length_scale_bounds=(1e-3, 1e3), nu=2.5
    ) + WhiteKernel(noise_level=1e-4, noise_level_bounds=(1e-8, 1e1))
    return GaussianProcessRegressor(kernel=kernel, normalize_y=True, random_state=42, n_restarts_optimizer=2)


def walk_forward_residuals(g: pd.DataFrame) -> pd.DataFrame:
    xcols = [f"x{i}" for i in range(1, D + 1)]
    X = g[xcols].to_numpy(float)
    y = g["output"].to_numpy(float)
    rows = []
    for i in range(MIN_TRAIN, len(g)):
        model = clone(gp(D))
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            model.fit(X[:i], y[:i])
            pred, std = model.predict(X[i:i+1], return_std=True)
        residual = float(y[i] - pred[0])
        rows.append({
            "week": int(g.loc[i, "week"]),
            "actual": float(y[i]),
            "prediction": float(pred[0]),
            "gp_std": float(std[0]),
            "residual": residual,
            "abs_residual": abs(residual),
        })
    return pd.DataFrame(rows)


def gaussian_ll(resid: np.ndarray, mean: np.ndarray, var: np.ndarray) -> float:
    var = np.maximum(var, EPS)
    return float(-0.5 * np.sum(np.log(2 * np.pi * var) + (resid - mean) ** 2 / var))


def aicc(ll: float, k: int, n: int) -> float:
    aic = 2 * k - 2 * ll
    if n <= k + 1:
        return float("inf")
    return float(aic + (2 * k * (k + 1)) / (n - k - 1))


def fit_iid(r: np.ndarray) -> dict:
    mu = float(np.mean(r))
    var = float(np.mean((r - mu) ** 2)) + EPS
    ll = gaussian_ll(r, np.full_like(r, mu), np.full_like(r, var))
    return {"model":"iid_gaussian", "k":2, "log_likelihood":ll, "aicc":aicc(ll,2,len(r)), "parameter_1":mu, "parameter_2":var}


def fit_ar1(r: np.ndarray) -> dict:
    if len(r) < 3:
        return {"model":"ar1_gaussian", "k":3, "log_likelihood":np.nan, "aicc":np.inf, "parameter_1":np.nan, "parameter_2":np.nan}
    x, y = r[:-1], r[1:]
    A = np.column_stack([np.ones(len(x)), x])
    beta, *_ = np.linalg.lstsq(A, y, rcond=None)
    c, phi = map(float, beta)
    err = y - (c + phi * x)
    var = float(np.mean(err ** 2)) + EPS
    ll = gaussian_ll(y, c + phi * x, np.full_like(y, var))
    return {"model":"ar1_gaussian", "k":3, "log_likelihood":ll, "aicc":aicc(ll,3,len(y)), "parameter_1":phi, "parameter_2":var}


def fit_hetero(r: np.ndarray, s: np.ndarray) -> dict:
    # Gaussian residual with constant mean and log-variance linear in standardised GP uncertainty.
    z = (s - np.mean(s)) / (np.std(s) + EPS)
    mu0 = float(np.mean(r))
    logv0 = float(np.log(np.var(r) + EPS))
    def nll(theta):
        mu, a, b = theta
        var = np.exp(np.clip(a + b * z, -30, 30))
        return -gaussian_ll(r, np.full_like(r, mu), var)
    res = minimize(nll, x0=np.array([mu0, logv0, 0.0]), method="L-BFGS-B")
    mu, a, b = map(float, res.x)
    ll = -float(res.fun)
    return {"model":"heteroscedastic_gpstd", "k":3, "log_likelihood":ll, "aicc":aicc(ll,3,len(r)), "parameter_1":b, "parameter_2":mu}


def deterministic_repeat_test(g: pd.DataFrame) -> pd.DataFrame:
    xcols = [f"x{i}" for i in range(1, D + 1)]
    rows = []
    for coords, grp in g.groupby(xcols, sort=False):
        if len(grp) < 2:
            continue
        vals = grp["output"].to_numpy(float)
        rows.append({
            "coordinate":"-".join(f"{float(v):.6f}" for v in coords),
            "n":len(vals),
            "output_range":float(np.ptp(vals)),
            "identical":bool(np.allclose(vals, vals[0], atol=1e-12, rtol=0.0)),
        })
    return pd.DataFrame(rows)


def main() -> None:
    hist = load_history()
    g = hist[hist["function"] == F].sort_values("week").reset_index(drop=True)
    wf = walk_forward_residuals(g)
    wf.to_csv(OUT / "BBD_012_F6_RESIDUAL_SEQUENCE.csv", index=False)

    r = wf["residual"].to_numpy(float)
    s = wf["gp_std"].to_numpy(float)
    models = pd.DataFrame([fit_iid(r), fit_ar1(r), fit_hetero(r,s)]).sort_values("aicc").reset_index(drop=True)
    models.insert(0, "rank", np.arange(1, len(models)+1))
    models.to_csv(OUT / "BBD_012_F6_STOCHASTIC_MODEL_COMPARISON.csv", index=False)

    rho_abs_std, p_abs_std = spearmanr(wf["abs_residual"], wf["gp_std"])
    lag1 = float(np.corrcoef(r[:-1], r[1:])[0,1]) if len(r) > 2 else np.nan
    repeats = deterministic_repeat_test(g)
    repeats.to_csv(OUT / "BBD_012_F6_REPEAT_DETERMINISM.csv", index=False)
    nonident = int((~repeats["identical"]).sum()) if not repeats.empty else 0

    best = models.iloc[0]
    second = models.iloc[1]
    delta = float(second["aicc"] - best["aicc"]) if np.isfinite(best["aicc"]) and np.isfinite(second["aicc"]) else np.nan

    # Conservative evidence rule because the residual sequence is extremely small.
    if nonident == 0:
        deterministic_status = "coordinate_determinism_not_falsified"
    else:
        deterministic_status = "coordinate_only_exact_determinism_falsified_by_repeats"

    if np.isfinite(delta) and delta >= 4:
        residual_class = str(best["model"])
        strength = "tentative"
    else:
        residual_class = "unresolved_between_tested_stochastic_models"
        strength = "insufficient_small_sample_separation"

    summary = pd.DataFrame([{
        "function":F,
        "n_observations":len(g),
        "n_walk_forward_residuals":len(wf),
        "best_stochastic_model":str(best["model"]),
        "best_aicc":float(best["aicc"]),
        "delta_aicc_to_second":delta,
        "residual_classification":residual_class,
        "classification_strength":strength,
        "lag1_residual_correlation":lag1,
        "abs_residual_vs_gpstd_spearman":float(rho_abs_std),
        "abs_residual_vs_gpstd_p":float(p_abs_std),
        "repeat_groups":len(repeats),
        "nonidentical_repeat_groups":nonident,
        "deterministic_status":deterministic_status,
        "exact_function_recovered":False,
        "independent_query_required":True,
    }])
    summary.to_csv(OUT / "BBD_012_F6_STOCHASTIC_DETERMINISTIC_SUMMARY.csv", index=False)

    print("BBD 012 F6 stochastic-versus-deterministic decomposition")
    print(models.to_string(index=False))
    print("\nSummary")
    print(summary.to_string(index=False))
    print(f"\nOutputs written to {OUT}")


if __name__ == "__main__":
    main()
