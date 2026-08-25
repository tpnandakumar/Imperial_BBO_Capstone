from __future__ import annotations

from pathlib import Path
import sys
import warnings
import numpy as np
import pandas as pd
from scipy.stats import qmc
from sklearn.base import clone
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import ConstantKernel, Matern, WhiteKernel
from sklearn.linear_model import Ridge, LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

from bbd_001_system_identification import load_history
from bbd_007_bbd_vs_soc_challenge import benchmark_feature

HERE = Path(__file__).resolve().parent
OUT = HERE / "outputs"
OUT.mkdir(exist_ok=True)
ROOT = HERE.parents[1]
SOC_DIR = ROOT / "Advanced_Extension_Series" / "SOC_Surrogate_Optimisation_Competition"
sys.path.insert(0, str(SOC_DIR))
from surrogate_evaluator import model_library as soc_model_library  # noqa: E402

F = 7
D = 6
RANDOM_STATE = 42
N_SOBOL = 2 ** 15
TOP_N = 10
MIN_SEP = 0.12 * np.sqrt(D)


def poly2(alpha=1e-4):
    return Pipeline([
        ("poly", PolynomialFeatures(degree=2, include_bias=False)),
        ("scale", StandardScaler()),
        ("ridge", Ridge(alpha=alpha)),
    ])


def linear(alpha=1e-4):
    return Pipeline([("scale", StandardScaler()), ("ridge", Ridge(alpha=alpha))])


def gp():
    k = ConstantKernel(1.0, (1e-3, 1e3)) * Matern(
        length_scale=np.ones(D), length_scale_bounds=(1e-3, 1e3), nu=2.5
    ) + WhiteKernel(noise_level=1e-4, noise_level_bounds=(1e-8, 1e1))
    return GaussianProcessRegressor(kernel=k, normalize_y=True, random_state=42, n_restarts_optimizer=2)


def fit_soc_best(X, y):
    best = None
    for c in soc_model_library(len(y), D):
        try:
            m = clone(c.estimator)
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                m.fit(X, y)
            pred = np.asarray(m.predict(X), float)
            mae = float(np.mean(np.abs(pred-y)))
            if best is None or mae < best[0]:
                best = (mae, c.name, m)
        except Exception:
            pass
    if best is None:
        raise RuntimeError("No SOC model fitted")
    return best


def candidate_points():
    sampler = qmc.Sobol(d=D, scramble=True, seed=RANDOM_STATE)
    P = sampler.random_base2(m=int(np.log2(N_SOBOL)))
    corners = np.array([[float((mask >> j) & 1) for j in range(D)] for mask in range(2**D)])
    return np.unique(np.vstack([P, corners]), axis=0)


def novelty(P, X):
    d = np.sqrt(((P[:,None,:]-X[None,:,:])**2).sum(axis=2)).min(axis=1)
    return np.clip(d/np.sqrt(D),0,1)


def main():
    hist = load_history()
    g = hist[hist["function"]==F].sort_values("week").reset_index(drop=True)
    xcols=[f"x{i}" for i in range(1,D+1)]
    X=g[xcols].to_numpy(float)
    y=g["output"].to_numpy(float)
    yrange=float(np.ptp(y)) or 1.0
    ymed=float(np.median(y))

    models=[]
    for name, est in [("BBD019_quadratic27", poly2(1e-4)), ("linear_ridge", linear(1e-4)), ("matern_gp", gp())]:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            est.fit(X,y)
        models.append((name, est))

    soc_mae, soc_name, soc_model = fit_soc_best(X,y)
    models.append((f"SOC_{soc_name}", soc_model))

    # BBD005 best benchmark for F7 was Rosenbrock-like with centre 0.25 and scale 0.5.
    v=benchmark_feature(X, "rosenbrock", 0.25, 0.5)
    bench=LinearRegression().fit(v,y)
    models.append(("rosenbrock_c0.25_s0.5", (bench, "rosenbrock", 0.25, 0.5)))

    P=candidate_points()
    pred_cols=[]
    names=[]
    for name,m in models:
        names.append(name)
        if isinstance(m, tuple):
            reg,fam,c,s=m
            pred=np.asarray(reg.predict(benchmark_feature(P,fam,c,s)),float)
        else:
            pred=np.asarray(m.predict(P),float)
        pred_cols.append(pred)
    M=np.column_stack(pred_cols)

    credible=np.all(np.isfinite(M),axis=1)
    credible &= np.all(np.abs(M-ymed) <= 6.0*yrange, axis=1)
    P=P[credible]; M=M[credible]

    std=np.std(M,axis=1)/yrange
    spread=(np.max(M,axis=1)-np.min(M,axis=1))/yrange
    nov=novelty(P,X)
    # Emphasise disagreement while retaining novelty so queries are informative away from the sampled path.
    score=(0.55*std+0.45*spread)*(0.55+0.45*nov)

    order=np.argsort(score)[::-1]
    chosen=[]
    for idx in order:
        if all(np.linalg.norm(P[idx]-P[j])>=MIN_SEP for j in chosen):
            chosen.append(int(idx))
        if len(chosen)>=TOP_N:
            break

    rows=[]
    for rank,idx in enumerate(chosen,1):
        row={"function":F,"query_rank":rank,"discrimination_score":float(score[idx]),
             "normalised_prediction_std":float(std[idx]),"normalised_prediction_spread":float(spread[idx]),
             "novelty":float(nov[idx]),"predicted_min":float(M[idx].min()),"predicted_max":float(M[idx].max())}
        for j in range(D): row[f"x{j+1}"]=float(P[idx,j])
        for k,n in enumerate(names): row[f"prediction_{n}"]=float(M[idx,k])
        rows.append(row)
    q=pd.DataFrame(rows)
    q.to_csv(OUT/"BBD_020_F7_DISCRIMINATORY_QUERIES.csv",index=False)

    roster=pd.DataFrame({"model":names})
    roster.to_csv(OUT/"BBD_020_F7_MODEL_ROSTER.csv",index=False)

    top=q.iloc[0]
    summary=pd.DataFrame([{
        "function":F,
        "top_query":"-".join(f"{top[f'x{i}']:.6f}" for i in range(1,D+1)),
        "top_discrimination_score":float(top["discrimination_score"]),
        "top_normalised_prediction_spread":float(top["normalised_prediction_spread"]),
        "top_novelty":float(top["novelty"]),
        "models_compared":len(names),
        "independent_black_box_evaluation_required":True,
        "exact_function_recovered":False,
        "interpretation":"falsification_queries_defined_not_executed"
    }])
    summary.to_csv(OUT/"BBD_020_F7_FALSIFICATION_SUMMARY.csv",index=False)

    print("BBD 020 F7 discriminatory falsification design")
    print("\nModel roster")
    print(roster.to_string(index=False))
    print("\nTop discriminatory queries")
    print(q.to_string(index=False))
    print("\nSummary")
    print(summary.to_string(index=False))
    print(f"\nOutputs written to {OUT}")

if __name__ == "__main__":
    main()
