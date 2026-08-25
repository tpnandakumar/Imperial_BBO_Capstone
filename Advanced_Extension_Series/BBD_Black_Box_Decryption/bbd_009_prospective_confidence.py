from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
OUT = HERE / "outputs"


def band(score: float) -> str:
    if score >= 75:
        return "strong"
    if score >= 60:
        return "moderate_strong"
    if score >= 45:
        return "moderate"
    if score >= 30:
        return "limited"
    return "weak"


def main() -> None:
    retrospective = pd.read_csv(OUT / "BBD_006_DECRYPTION_CONFIDENCE.csv")
    prospective = pd.read_csv(OUT / "BBD_007_BBD_VS_SOC_SUMMARY.csv")
    queries = pd.read_csv(OUT / "BBD_008_DISCRIMINATORY_QUERIES.csv")

    top_query = (
        queries.loc[queries["query_rank"] == 1,
                    ["function", "discrimination_score", "normalised_prediction_spread", "novelty"]]
        .rename(columns={
            "discrimination_score": "top_discrimination_score",
            "normalised_prediction_spread": "top_prediction_spread",
            "novelty": "top_query_novelty",
        })
    )

    df = retrospective.merge(prospective, on="function", how="inner").merge(top_query, on="function", how="inner")

    # BBD 006 is retained as retrospective structural evidence only.
    df["retrospective_component"] = np.clip(df["decryption_confidence_score"] / 100.0, 0.0, 1.0)

    # Prospective competitiveness equals 1 when BBD matches or beats SOC and declines
    # proportionally when BBD's forward error is larger. This prevents retrospective fit
    # from dominating the evidence score.
    ratio = df["soc_normalised_mae"] / df["bbd_normalised_mae"].replace(0, np.nan)
    df["prospective_competitiveness"] = np.clip(ratio.fillna(1.0), 0.0, 1.0)
    df["forward_test_win_rate"] = df["bbd_test_wins"] / df["n_prospective_tests"].replace(0, np.nan)
    df["forward_test_win_rate"] = df["forward_test_win_rate"].fillna(0.0).clip(0.0, 1.0)

    # Large BBD 008 disagreement means substantial mechanism uncertainty remains.
    # The reciprocal transform is monotone and bounded without pretending the spread is a probability.
    df["mechanism_resolution"] = 1.0 / (1.0 + df["top_prediction_spread"].clip(lower=0.0))

    # Evidence weights are deliberately prospective-heavy. The result is an auditable
    # evidence-strength index, not a posterior probability of exact equation recovery.
    raw = 100.0 * (
        0.25 * df["retrospective_component"]
        + 0.40 * df["prospective_competitiveness"]
        + 0.20 * df["forward_test_win_rate"]
        + 0.15 * df["mechanism_resolution"]
    )

    # Forward evidence has veto power. If SOC wins the prospective function-level challenge,
    # BBD cannot be labelled strong regardless of retrospective fit. Even a BBD prospective
    # win is capped below "confirmed" because no genuinely new external black-box evaluation exists.
    caps = np.where(df["winner"].eq("BBD"), 85.0, 65.0)
    df["prospective_recalibrated_score"] = np.minimum(raw, caps)
    df["prospective_recalibrated_band"] = df["prospective_recalibrated_score"].map(band)

    df["evidence_change_from_bbd006"] = df["prospective_recalibrated_score"] - df["decryption_confidence_score"]
    df["exact_function_recovered"] = False
    df["independent_discriminatory_query_required"] = True

    df = df.sort_values(
        ["prospective_recalibrated_score", "prospective_competitiveness"],
        ascending=[False, False],
    ).reset_index(drop=True)
    df.insert(0, "recalibrated_rank", np.arange(1, len(df) + 1))

    keep = [
        "recalibrated_rank",
        "function",
        "prospective_recalibrated_score",
        "prospective_recalibrated_band",
        "decryption_confidence_score",
        "evidence_change_from_bbd006",
        "winner",
        "bbd_normalised_mae",
        "soc_normalised_mae",
        "prospective_competitiveness",
        "forward_test_win_rate",
        "top_prediction_spread",
        "mechanism_resolution",
        "top_discrimination_score",
        "top_query_novelty",
        "current_best_description",
        "exact_function_recovered",
        "independent_discriminatory_query_required",
    ]
    result = df[keep]
    result.to_csv(OUT / "BBD_009_PROSPECTIVE_CONFIDENCE.csv", index=False)

    print("BBD 009 prospective-evidence confidence recalibration")
    print(result[[
        "recalibrated_rank", "function", "prospective_recalibrated_score",
        "prospective_recalibrated_band", "winner", "forward_test_win_rate",
        "top_prediction_spread"
    ]].to_string(index=False))
    print(f"\nOutput written to {OUT / 'BBD_009_PROSPECTIVE_CONFIDENCE.csv'}")


if __name__ == "__main__":
    main()
