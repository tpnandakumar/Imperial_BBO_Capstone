from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

from bbd_001_system_identification import DIMS, load_history

HERE = Path(__file__).resolve().parent
OUT = HERE / "outputs"
OUT.mkdir(exist_ok=True)

ALPHAS = [1e-8, 1e-6, 1e-4, 1e-2, 1e-1, 1.0, 10.0, 100.0]


def design_matrix(x: np.ndarray, degree: int) -> tuple[np.ndarray, list[str], PolynomialFeatures]:
    poly = PolynomialFeatures(degree=degree, include_bias=False)
    z = poly.fit_transform(x)
    names = poly.get_feature_names_out([f"x{i+1}" for i in range(x.shape[1])]).tolist()
    return z, names, poly


def loocv_score(x: np.ndarray, y: np.ndarray, degree: int, alpha: float) -> float:
    preds = []
    truths = []
    for i in range(len(y)):
        train = np.ones(len(y), dtype=bool)
        train[i] = False
        z_train, _, poly = design_matrix(x[train], degree)
        z_test = poly.transform(x[~train])
        scaler = StandardScaler()
        zs_train = scaler.fit_transform(z_train)
        zs_test = scaler.transform(z_test)
        model = Ridge(alpha=alpha)
        model.fit(zs_train, y[train])
        preds.append(float(model.predict(zs_test)[0]))
        truths.append(float(y[i]))
    return float(mean_absolute_error(truths, preds))


def fit_equation(x: np.ndarray, y: np.ndarray, degree: int, alpha: float):
    z, names, poly = design_matrix(x, degree)
    scaler = StandardScaler()
    zs = scaler.fit_transform(z)
    model = Ridge(alpha=alpha)
    model.fit(zs, y)

    # Convert coefficients from scaled polynomial features back to the original basis.
    coef = model.coef_ / scaler.scale_
    intercept = float(model.intercept_ - np.sum(model.coef_ * scaler.mean_ / scaler.scale_))
    pred = intercept + z @ coef
    return intercept, coef, names, pred


def compact_terms(intercept: float, coef: np.ndarray, names: list[str], y_scale: float):
    # Keep terms that are non-negligible relative to the response scale. This is a reporting
    # threshold only. The predictive score is always calculated from the full fitted equation.
    threshold = max(abs(y_scale) * 1e-6, 1e-10)
    items = [(n, float(c)) for n, c in zip(names, coef) if abs(c) >= threshold]
    items.sort(key=lambda p: abs(p[1]), reverse=True)
    return intercept, items


def equation_string(intercept: float, terms: list[tuple[str, float]], max_terms: int = 12) -> str:
    pieces = [f"{intercept:.10g}"]
    for name, c in terms[:max_terms]:
        sign = "+" if c >= 0 else "-"
        pieces.append(f" {sign} {abs(c):.10g}*{name}")
    if len(terms) > max_terms:
        pieces.append(f" + ... [{len(terms) - max_terms} smaller retained terms]")
    return "".join(pieces)


def main() -> None:
    hist = load_history()
    competition = []
    equations = []
    terms_out = []

    for f in range(1, 9):
        dim = DIMS[f]
        g = hist[hist["function"] == f].sort_values("week").copy()
        xcols = [f"x{i}" for i in range(1, dim + 1)]
        x = g[xcols].to_numpy(float)
        y = g["output"].to_numpy(float)
        y_sd = float(np.std(y, ddof=1)) or 1.0

        degrees = [1, 2]
        # Degree 3 is allowed only when the polynomial library is not grossly larger than the
        # thirteen-point dataset. This prevents high-dimensional cubic fits being mislabelled as
        # recovered equations.
        if dim <= 3:
            degrees.append(3)

        candidates = []
        for degree in degrees:
            n_features = PolynomialFeatures(degree=degree, include_bias=False).fit(x).n_output_features_
            for alpha in ALPHAS:
                mae = loocv_score(x, y, degree, alpha)
                nmae = mae / y_sd
                # A mild minimum-description-length style penalty prevents selecting a huge
                # polynomial library for a tiny reduction in validation error.
                complexity_penalty = 0.01 * (n_features / max(len(y), 1))
                score = nmae + complexity_penalty
                row = {
                    "function": f,
                    "degree": degree,
                    "alpha": alpha,
                    "n_features": int(n_features),
                    "loocv_mae": mae,
                    "normalised_loocv_mae": nmae,
                    "complexity_penalty": complexity_penalty,
                    "selection_score": score,
                }
                competition.append(row)
                candidates.append(row)

        winner = min(candidates, key=lambda r: r["selection_score"])
        intercept, coef, names, pred = fit_equation(x, y, winner["degree"], winner["alpha"])
        train_mae = float(mean_absolute_error(y, pred))
        r2_like = 1.0 - float(np.sum((y - pred) ** 2) / max(np.sum((y - np.mean(y)) ** 2), 1e-15))
        _, retained = compact_terms(intercept, coef, names, y_sd)

        equations.append({
            "function": f,
            "selected_degree": winner["degree"],
            "selected_alpha": winner["alpha"],
            "n_library_features": winner["n_features"],
            "loocv_mae": winner["loocv_mae"],
            "normalised_loocv_mae": winner["normalised_loocv_mae"],
            "selection_score": winner["selection_score"],
            "training_mae": train_mae,
            "training_r2_like": r2_like,
            "intercept": intercept,
            "reported_nontrivial_terms": len(retained),
            "compact_equation": equation_string(intercept, retained),
        })

        for rank, (name, c) in enumerate(retained, start=1):
            terms_out.append({
                "function": f,
                "rank_by_abs_coefficient": rank,
                "term": name,
                "coefficient": c,
                "abs_coefficient": abs(c),
            })

    comp = pd.DataFrame(competition)
    eq = pd.DataFrame(equations)
    terms = pd.DataFrame(terms_out)
    comp.to_csv(OUT / "BBD_004_EQUATION_COMPETITION.csv", index=False)
    eq.to_csv(OUT / "BBD_004_RECOVERED_EQUATIONS.csv", index=False)
    terms.to_csv(OUT / "BBD_004_EQUATION_TERMS.csv", index=False)

    print("BBD 004 recovered-equation summary")
    print(eq[["function", "selected_degree", "selected_alpha", "normalised_loocv_mae", "training_r2_like", "reported_nontrivial_terms", "compact_equation"]].to_string(index=False))
    print(f"\nOutputs written to {OUT}")


if __name__ == "__main__":
    main()
