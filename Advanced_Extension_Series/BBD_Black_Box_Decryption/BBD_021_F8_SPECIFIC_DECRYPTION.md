# BBD 021: F8-Specific Decryption

## Purpose

F8 previously produced the cleanest compact equation in BBD 004, a degree-1 model with normalised leave-one-out error of approximately `0.017307`. It also showed strong gradient agreement in BBD 003. However, BBD 007 found that the SOC surrogate predicted F8 much better in chronological forward testing.

BBD 021 addresses that contradiction directly by rebuilding F8 as a function-specific problem and testing whether the apparent linear structure survives stricter chronological prediction.

## Method

The thirteen F8 observations are ordered by week. Each candidate model is trained only on the observations available before the test week and then predicts the next unseen observation.

The model set includes:

- ordinary linear regression;
- linear ridge models across several regularisation strengths;
- quadratic ridge models;
- quadratic lasso models;
- linear elastic-net models;
- a Matérn 2.5 Gaussian Process.

The comparison therefore asks whether F8 is best regarded as a compact linear surface, a lightly regularised low-order nonlinear surface, or a more flexible local function.

## Coefficient stability

A compact linear equation is persuasive only if its coefficients remain directionally stable as the history grows. BBD 021 therefore refits the low-regularisation linear ridge model after each additional observation and records the raw coordinate coefficients.

For each coordinate the experiment reports:

- full-history coefficient;
- mean and median coefficient across expanding windows;
- coefficient dispersion;
- sign stability relative to the final coefficient;
- absolute effect rank.

This distinguishes a genuinely stable linear mechanism from a final equation that appears clean only because all thirteen observations were fitted at once.

## Repeatability

F8 repeated coordinates are checked separately. Identical repeated outputs would support coordinate-only determinism over the sampled points, while non-identical repeats would require the same caution applied to F6.

## Prior evidence retained for comparison

BBD 021 records, but does not reinterpret as new tests, the earlier results:

- BBD 004 linear normalised LOOCV MAE: approximately `0.017307`;
- BBD 003 global versus recent gradient cosine: approximately `0.936764`;
- BBD 007 BBD forward normalised MAE: approximately `0.167497`;
- BBD 007 SOC forward normalised MAE: approximately `0.043917`.

The new function-specific chronological result is compared with those values, but it is not labelled as a fresh SOC contest unless SOC is rerun under the same BBD 021 protocol.

## Evidence boundary

A low walk-forward error would strengthen the case that F8 has a stable low-order generating surface in the sampled region. It would still not establish the exact Imperial function because BBD 008 showed large disagreement among surviving models away from the historical path.

Exact function recovery therefore remains false until independent discriminatory queries are evaluated.
