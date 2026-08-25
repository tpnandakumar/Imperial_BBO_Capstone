# BBD 023: F5-Specific Decryption

## Purpose

F5 is one of the most important contradictions in the BBD programme. BBD 004 produced an exceptionally accurate full-history quadratic reconstruction, with normalised leave-one-out MAE of approximately `0.005749`, and BBD 003 found near-perfect agreement between global and recent gradient directions. However, BBD 007 found that the SOC surrogate family predicted F5 better under its prospective challenge.

BBD 023 therefore rebuilds F5 as a dedicated four-dimensional identification problem and tests whether the strong quadratic interpretation survives stricter chronological prediction.

## Function-specific model set

The thirteen F5 observations are ordered by week. Each candidate is trained only on observations available before the test week and then predicts the next unseen observation. Testing begins after five training observations, producing eight chronological forward tests.

The candidate set includes:

- ordinary linear regression;
- regularised linear regression;
- quadratic ridge models across several regularisation strengths;
- cubic ridge models;
- Matérn and RBF Gaussian Processes;
- gradient boosting, random forest and extra trees;
- a boundary-aware feature model using raw coordinates together with distance-to-upper-boundary transforms.

The boundary-aware candidate is included because the historical F5 trajectory moved strongly towards `x2`, `x3` and `x4` values close to 1. It is treated as a competing hypothesis, not as an assumed mechanism.

## Structural checks

BBD 023 also records expanding-window linear coefficient stability and repeated-coordinate behaviour. Stable directions across growing histories strengthen directional interpretation even when the full generating equation remains uncertain.

## Prior evidence retained for comparison

The experiment records the earlier results without treating them as new tests:

- BBD 004 quadratic normalised LOOCV MAE: approximately `0.005749`;
- BBD 003 global versus recent gradient cosine: approximately `0.992036`;
- BBD 007 BBD prospective normalised MAE: approximately `0.028072`;
- BBD 007 SOC prospective normalised MAE: approximately `0.009054`.

## Evidence boundary

A strong function-specific chronological result can establish that a low-order deterministic surface predicts the sampled trajectory well. It cannot by itself prove the exact Imperial generating equation. F5 still requires independent discriminatory evaluation away from the historical optimisation path before exact recovery can be claimed.
