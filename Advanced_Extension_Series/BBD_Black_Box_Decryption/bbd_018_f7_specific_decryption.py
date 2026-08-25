from __future__ import annotations

from pathlib import Path
import warnings
import numpy as np
import pandas as pd
from sklearn.base import clone
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import ConstantKernel, Matern, WhiteKernel
from sklearn.linear_model import Ridge, Lasso
from sklearn.metrics import mean_absolute_error
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

from bbd_001_system_identification import load_history

HERE = Path(__file__).resolve().parent
OUT = HERE / "outputs"
OUT.mkdir(exist_ok=True)
F = 7
D = 6
MIN_TRAIN = 5


def gp(dim: int):
    kernel = ConstantKernel(1.0, (1e-3, 1e3)) * Matern(
        length_scale=np.ones(dim), length_scale_bounds=(1e-3, 1e3), nu=2.5
    ) + WhiteKernel(noise_level=1e-4, noise_level_bounds=(1e-8, 1e1))
    return GaussianProcessRegressor(kernel=kernel, normalize_y=True, random_state=42, n_restarts_optimizer=2)


def linear_ridge(alpha: float):
    return Pipeline([("scale", StandardScaler()), ("ridge", Ridge(alpha=alpha))])


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


def walk_forward(g: pd.DataFrame, estimator) -> pd.DataFrame:
    xcols = [f"x{i}" for i in range(1, D + 1)]
    X = g[xcols].to_numpy(float)
    y = g["output"].to_numpy(float)
    rows = []
    for i in range(MIN_TRAIN, len(g)):
        m = clone(estimator)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            m.fit(X[:i], y[:i])
            pred = float(np.asarray(m.predict(X[i:i+1])).ravel()[0])
        rows.append({"week": int(g.loc[i,"week"]), "actual": float(y[i]), "prediction": pred,
                     "absolute_error": abs(float(y[i]) - pred)})
    return pd.DataFrame(rows)


def repeat_summary(g: pd.DataFrame) -> pd.DataFrame:
    xcols = [f"x{i}" for i in range(1, D + 1)]
    rows=[]
    for coords, grp in g.groupby(xcols, sort=False, dropna=False):
        if len(grp) < 2:
            continue
        vals=grp["output"].to_numpy(float)
        rows.append({
            "coordinate":"-".join(f"{float(v):.6f}" for v in coords),
            "n_repeats":len(grp),
            "output_range":float(vals.max()-vals.min()),
            "identical_outputs":bool(np.allclose(vals, vals[0], atol=1e-12, rtol=0.0)),
        })
    return pd.DataFrame(rows)


def coefficient_table(g: pd.DataFrame) -> pd.DataFrame:
    xcols=[f"x{i}" for i in range(1,D+1)]
    X=g[xcols].to_numpy(float)
    y=g["output"].to_numpy(float)
    model=linear_ridge(1e-4)
    model.fit(X,y)
    coef=model.named_steps["ridge"].coef_
    scale=model.named_steps["scale"].scale_
    raw=coef/scale
    rows=[]
    for i,c in enumerate(raw, start=1):
        rows.append({"coordinate":i,"linear_effect":float(c),"absolute_rank":0,"direction":"increase" if c>0 else "decrease"})
    order=np.argsort(-np.abs(raw))
    for rank,idx in enumerate(order,start=1):
        rows[idx]["absolute_rank"]=rank
    return pd.DataFrame(rows)


def main():
    hist=load_history()
    g=hist[hist["function"]==F].sort_values("week").reset_index(drop=True)
    y=g["output"].to_numpy(float)
    yrange=float(np.ptp(y)) or 1.0

    candidates=[
        ("gp_matern_2.5", gp(D)),
        ("linear_ridge_1e-4", linear_ridge(1e-4)),
        ("linear_ridge_1e-2", linear_ridge(1e-2)),
        ("quadratic_ridge_1e-4", poly_ridge(2,1e-4)),
        ("quadratic_ridge_1e-2", poly_ridge(2,1e-2)),
        ("quadratic_ridge_0.1", poly_ridge(2,0.1)),
        ("quadratic_lasso_1e-3", poly_lasso(2,1e-3)),
        ("quadratic_lasso_1e-2", poly_lasso(2,1e-2)),
    ]

    comp=[]; preds=[]
    for name,est in candidates:
        p=walk_forward(g,est)
        p.insert(0,"model",name)
        preds.append(p)
        mae=float(mean_absolute_error(p["actual"],p["prediction"]))
        comp.append({"model":name,"walk_forward_tests":len(p),"walk_forward_mae":mae,
                     "normalised_walk_forward_mae":mae/yrange,
                     "max_absolute_error":float(p["absolute_error"].max())})
    comp=pd.DataFrame(comp).sort_values("normalised_walk_forward_mae").reset_index(drop=True)
    comp.insert(0,"rank",np.arange(1,len(comp)+1))
    comp.to_csv(OUT/"BBD_018_F7_MODEL_COMPETITION.csv",index=False)
    pd.concat(preds,ignore_index=True).to_csv(OUT/"BBD_018_F7_WALK_FORWARD_PREDICTIONS.csv",index=False)

    reps=repeat_summary(g)
    reps.to_csv(OUT/"BBD_018_F7_REPEAT_SUMMARY.csv",index=False)
    coefs=coefficient_table(g)
    coefs.to_csv(OUT/"BBD_018_F7_LINEAR_EFFECTS.csv",index=False)

    best=comp.iloc[0]
    repeat_groups=len(reps)
    nonident=int((~reps["identical_outputs"]).sum()) if repeat_groups else 0
    max_repeat=float(reps["output_range"].max()) if repeat_groups else 0.0

    # BBD 003 previously found high global/recent gradient cosine for F7. We retain that as prior structural evidence.
    gradient_cosine=0.975357
    prospective_soc_normalised_mae=0.195676
    bbd007_normalised_mae=0.291394

    summary=pd.DataFrame([{
        "function":F,
        "n_observations":len(g),
        "best_model":best["model"],
        "best_normalised_walk_forward_mae":float(best["normalised_walk_forward_mae"]),
        "bbd003_global_recent_gradient_cosine":gradient_cosine,
        "bbd007_bbd_normalised_mae":bbd007_normalised_mae,
        "bbd007_soc_normalised_mae":prospective_soc_normalised_mae,
        "repeat_groups":repeat_groups,
        "nonidentical_repeat_groups":nonident,
        "max_repeat_range":max_repeat,
        "mechanism_interpretation":"static_structured_surface_candidate" if nonident==0 else "structured_surface_plus_repeat_variation",
        "exact_function_recovered":False,
        "independent_query_required":True,
    }])
    summary.to_csv(OUT/"BBD_018_F7_DECRYPTION_SUMMARY.csv",index=False)

    print("BBD 018 F7-specific decryption")
    print(comp.to_string(index=False))
    print("\nLinear coordinate effects")
    print(coefs.to_string(index=False))
    print("\nSummary")
    print(summary.to_string(index=False))
    print(f"\nOutputs written to {OUT}")

if __name__ == "__main__":
    main()
