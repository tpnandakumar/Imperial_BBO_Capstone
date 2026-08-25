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

## Result

The strict predictive winner remained the full 27-term quadratic:

| Terms retained | Normalised walk-forward MAE |
|---:|---:|
| 27 | **0.034870** |
| 20 | 0.035026 |
| 15 | 0.039251 |
| 12 | 0.043354 |
| 9 | 0.047645 |
| 7 | 0.053126 |
| 5 | 0.054900 |
| 3 | 0.105531 |

Therefore BBD 019 did **not** establish a smaller equation that predicts better than the complete quadratic feature set.

The 20-term model is nevertheless practically close. Its normalised MAE is only `0.000156` higher, about `0.45%` relative deterioration compared with the 27-term model. This means some compression is possible with very little loss, but the strict evidence rule retains 27 terms because it has the lowest prospective error.

## Recovered full-history quadratic

The full-history refit gives the current local F7 candidate:

`3.222883305 - 6.206057477*x1*x4 - 4.923745036*x5^2 - 3.797132871*x1*x5 + 3.446675454*x4 - 2.849456561*x4*x5 + 2.280576415*x1^2 + 1.927903931*x1 - 1.879457184*x2*x5 + 1.815170033*x1*x2 - 1.580173815*x2*x4 + 1.571575904*x5 + 1.519593818*x3^2 + 1.415401762*x1*x6 - 1.263975393*x3*x5 + 1.106076304*x1*x3 - 1.030552944*x6 - 0.9928952301*x2 - 0.9338415791*x2*x3 + 0.8658612655*x3 + 0.8320693141*x4*x6 - 0.6367826485*x2*x6 - 0.5786588889*x2^2 + 0.5294575222*x3*x4 + 0.4970744051*x4^2 - 0.4067067698*x6^2 - 0.2575313218*x5*x6 + 0.02628985877*x3*x6`

The strongest fitted terms include the interactions `x1*x4`, `x1*x5` and `x4*x5`, together with the `x5^2` curvature term. This is consistent with BBD 018 showing that F7 is not merely a simple additive linear surface.

## Interpretation

BBD 019 gives a useful negative result. F7's excellent predictive performance is not preserved by aggressive term pruning. The data currently favour a **distributed quadratic interaction surface** rather than a sparse equation with only a few dominant terms.

The near-equivalence of the 20-term model suggests that the weakest seven terms may contribute little, but removing more terms progressively degrades chronological prediction. This is exactly the distinction BBD is intended to preserve: retrospective elegance is not allowed to override prospective performance.

## Evidence boundary

The 27-term equation is a **candidate local generating equation over the sampled region**, not proof of the original hidden Imperial function. Exact function recovery remains false until the equation survives independent discriminatory evaluations away from the historical trajectory. BBD 008 already showed substantial model disagreement in unsampled F7 regions, so the next F7 step should test the full quadratic candidate against alternative models at deliberately high-disagreement coordinates.
