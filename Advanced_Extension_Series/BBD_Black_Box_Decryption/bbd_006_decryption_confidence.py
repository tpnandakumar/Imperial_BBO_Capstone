from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
OUT = HERE / "outputs"
OUT.mkdir(exist_ok=True)


def clamp01(x: float) -> float:
    return float(np.clip(x, 0.0, 1.0))


def inv_error_score(err: float, scale: float = 0.25) -> float:
    """Map a non-negative normalised error to [0, 1], with lower error scoring higher."""
    if not np.isfinite(err):
        return 0.0
    return clamp01(1.0 / (1.0 + err / scale))


def main() -> None:
    p1 = OUT / "BBD_001_HYPOTHESIS_SUMMARY.csv"
    p2 = OUT / "BBD_002_TEMPORAL_RESIDUAL_SUMMARY.csv"
    p3 = OUT / "BBD_003_GRADIENT_SUMMARY.csv"
    p4 = OUT / "BBD_004_RECOVERED_EQUATIONS.csv"
    p5 = OUT / "BBD_005_BENCHMARK_WINNERS.csv"

    missing = [str(p.name) for p in [p1, p2, p3, p4, p5] if not p.exists()]
    if missing:
        raise FileNotFoundError(
            "BBD 006 requires outputs from BBD 001 to 005. Missing: " + ", ".join(missing)
        )

    h1 = pd.read_csv(p1)
    h2 = pd.read_csv(p2)
    h3 = pd.read_csv(p3)
    h4 = pd.read_csv(p4)
    h5 = pd.read_csv(p5)

    rows = []
    for f in range(1, 9):
        r1 = h1[h1["function"] == f].iloc[0]
        r2 = h2[h2["function"] == f].iloc[0]
        r3 = h3[h3["function"] == f].iloc[0]
        r4 = h4[h4["function"] == f].iloc[0]
        r5 = h5[h5["function"] == f].iloc[0]

        # Evidence dimensions are deliberately separated so no single model fit can dominate.
        # 1) Predictive equation evidence
        symbolic_error = float(r4["normalised_loocv_mae"])
        equation_predictive = inv_error_score(symbolic_error, scale=0.20)

        # 2) Equation compactness. Fewer retained terms earn more structural confidence.
        terms = float(r4["reported_nontrivial_terms"])
        compactness = clamp01(np.exp(-max(terms - 4.0, 0.0) / 10.0))

        # 3) Gradient coherence combines held-out transition skill and global-local agreement.
        grad_r2 = clamp01(float(r3["global_gradient_r2_like"]))
        cosine = float(r3["global_local_gradient_cosine"])
        cosine_score = clamp01((cosine + 1.0) / 2.0)
        gradient_coherence = 0.60 * grad_r2 + 0.40 * cosine_score

        # 4) Determinism/repeatability evidence penalises non-identical repeats.
        repeats = float(r2["repeat_groups"])
        nonident = float(r2["nonidentical_repeat_groups"])
        max_range = float(r2["max_repeat_range"])
        if repeats <= 0:
            repeatability = 0.60  # neutral rather than perfect when no repeat experiment exists
        else:
            disagreement_fraction = nonident / repeats
            repeatability = clamp01((1.0 - disagreement_fraction) * np.exp(-5.0 * max_range))

        # 5) Mechanism simplicity. Static winners score highest; temporal/state winners are
        # treated as less fully decrypted unless subsequent residual testing supports them.
        winner_model = str(r1["winning_model"])
        if winner_model.startswith("H0_static"):
            mechanism_simplicity = 1.0
        elif winner_model.startswith("H2_time"):
            mechanism_simplicity = 0.65
        elif winner_model.startswith("H4_state") or winner_model.startswith("H5"):
            mechanism_simplicity = 0.55
        else:
            mechanism_simplicity = 0.60

        if bool(r2["temporal_correction_improves"]):
            mechanism_simplicity *= 0.85

        # 6) Benchmark agreement is supporting evidence only. A benchmark that beats BBD 004
        # adds modest confidence in recognisable geometry, while symbolic superiority does not
        # count against decryption because the hidden function need not be a standard benchmark.
        benchmark_error = float(r5["normalised_loocv_mae"])
        benchmark_support = inv_error_score(benchmark_error, scale=0.20)
        if bool(r5["benchmark_beats_bbd004"]):
            benchmark_geometry = benchmark_support
        else:
            benchmark_geometry = 0.50 * benchmark_support

        # Weighted ensemble. Predictive structure and gradient coherence carry most weight.
        score = (
            0.30 * equation_predictive
            + 0.15 * compactness
            + 0.25 * gradient_coherence
            + 0.15 * repeatability
            + 0.10 * mechanism_simplicity
            + 0.05 * benchmark_geometry
        )
        score = 100.0 * clamp01(score)

        if score >= 80:
            confidence_band = "high"
        elif score >= 65:
            confidence_band = "moderate_high"
        elif score >= 50:
            confidence_band = "moderate"
        elif score >= 35:
            confidence_band = "low_moderate"
        else:
            confidence_band = "low"

        # Select the most defensible current structural description.
        if bool(r5["benchmark_beats_bbd004"]) and benchmark_error < symbolic_error:
            current_best_description = f"{r5['winning_family']}_like_geometry"
            current_best_error = benchmark_error
        else:
            current_best_description = f"degree_{int(r4['selected_degree'])}_symbolic_equation"
            current_best_error = symbolic_error

        rows.append({
            "function": f,
            "decryption_confidence_score": score,
            "confidence_band": confidence_band,
            "current_best_description": current_best_description,
            "current_best_normalised_loocv_mae": current_best_error,
            "equation_predictive_score": equation_predictive,
            "equation_compactness_score": compactness,
            "gradient_coherence_score": gradient_coherence,
            "repeatability_score": repeatability,
            "mechanism_simplicity_score": mechanism_simplicity,
            "benchmark_geometry_score": benchmark_geometry,
            "winning_bbd001_model": winner_model,
            "symbolic_degree": int(r4["selected_degree"]),
            "symbolic_terms": int(r4["reported_nontrivial_terms"]),
            "symbolic_normalised_loocv_mae": symbolic_error,
            "benchmark_family": str(r5["winning_family"]),
            "benchmark_normalised_loocv_mae": benchmark_error,
            "benchmark_beats_symbolic": bool(r5["benchmark_beats_bbd004"]),
            "nonidentical_repeat_groups": int(r2["nonidentical_repeat_groups"]),
            "gradient_global_local_cosine": float(r3["global_local_gradient_cosine"]),
        })

    df = pd.DataFrame(rows).sort_values("decryption_confidence_score", ascending=False).reset_index(drop=True)
    df.insert(0, "confidence_rank", np.arange(1, len(df) + 1))
    df.to_csv(OUT / "BBD_006_DECRYPTION_CONFIDENCE.csv", index=False)

    summary_cols = [
        "confidence_rank", "function", "decryption_confidence_score", "confidence_band",
        "current_best_description", "current_best_normalised_loocv_mae",
        "symbolic_terms", "nonidentical_repeat_groups", "gradient_global_local_cosine"
    ]
    print("BBD 006 decryption confidence ranking")
    print(df[summary_cols].to_string(index=False))
    print(f"\nOutput written to {OUT / 'BBD_006_DECRYPTION_CONFIDENCE.csv'}")


if __name__ == "__main__":
    main()
