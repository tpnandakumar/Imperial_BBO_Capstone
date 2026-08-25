# BBD 019: F7 Quadratic Simplification and Term Recovery

## Purpose

BBD 018 established that a low-regularisation quadratic ridge model predicts F7 strongly in chronological walk-forward testing, with normalised MAE around `0.03487`. BBD 019 asks whether that performance genuinely requires the full quadratic feature set or whether a smaller set of stable terms can preserve, or improve, predictive accuracy.

The aim is not simply to make the equation shorter. A reduced expression is useful only if it survives chronological prediction.

## Method

For each walk-forward training window, BBD 019:

1. expands the six F7 coordinates to all degree-2 polynomial terms;
2. fits a low-regularisation ridge model;
3. ranks the quadratic terms by absolute coefficient magnitude inside that training window;
4. retains only the top `k` terms;
5. refits the model using those selected terms;
6. predicts the next unseen week.

The tested complexity levels are `3, 5, 7, 9, 12, 15, 20, 27` terms.

This nested selection prevents later observations from deciding which terms are available for an earlier prediction.

## Stability analysis

The experiment also tracks each quadratic coefficient as the training history grows. For every term it records mean and median coefficient, coefficient dispersion, average absolute magnitude and sign stability across training windows.

A term is structurally more persuasive when it is both predictive and directionally stable, rather than merely large in the final full-history fit.

## Final candidate equation

After the best complexity level is selected prospectively, BBD 019 refits that number of terms using the full thirteen-round F7 history and reports the resulting compact equation.

That expression is a **candidate local generating equation over the sampled region**, not a claim that the original hidden Imperial function has been recovered exactly.

## Evidence boundary

Exact function recovery remains false until the compact equation survives independent discriminatory queries away from the historical trajectory. BBD 008 already showed that competing F7 models can diverge substantially in unsampled regions, so simplification must be followed by falsification rather than treated as proof.
