# BBD 021: F8-Specific Decryption

## Purpose

F8 previously produced the cleanest compact equation in BBD 004, a degree-1 model with normalised leave-one-out error of approximately `0.017307`. It also showed strong gradient agreement in BBD 003. However, BBD 007 found that the SOC surrogate predicted F8 much better in chronological forward testing.

BBD 021 addresses that contradiction directly by rebuilding F8 as a function-specific problem and testing whether the apparent linear structure survives stricter chronological prediction.

## Method

The thirteen F8 observations are ordered by week. Each candidate model is trained only on the observations available before the test week and then predicts the next unseen observation.

The model set includes ordinary linear regression, several linear ridge models, quadratic ridge and lasso models, elastic-net models and a Matérn 2.5 Gaussian Process.

## Result

The best function-specific model was **ordinary linear regression**, with eight chronological walk-forward tests and normalised MAE:

`0.016539`

The next two models were essentially identical:

- linear ridge `alpha = 1e-6`: `0.016539`;
- linear ridge `alpha = 1e-4`: `0.016570`.

The best quadratic model was slightly weaker at `0.017342`, and the Matérn Gaussian Process was weaker again at `0.029135`.

This is a major change from the original BBD 007 F8 result. Under the F8-specific protocol, the compact linear surface predicts chronologically unseen observations much more accurately than the earlier general BBD implementation.

The BBD 021 result is also lower than the historical BBD 007 SOC normalised MAE of `0.043917`. This comparison is informative but is **not labelled as a fresh BBD-versus-SOC win**, because SOC has not yet been rerun under the exact BBD 021 train/test protocol.

## Recovered linear equation

The full-history low-regularisation linear equation is:

`F8(x) ≈ 10.97788502 + 0.116539399*x1 + 0.1910685871*x2 + 0.05156106233*x3 + 0.8145764473*x4 + 0.3239666929*x5 - 1.411856604*x6 - 0.7715635142*x7 - 0.04556514659*x8`

This is effectively the same equation identified in BBD 004.

## Coefficient stability

All eight final coefficient signs were stable in at least 75% of expanding training windows. Five coordinates had 100% sign stability and the remaining three were still directionally consistent enough to pass the pre-specified 75% threshold.

The strongest effects were:

1. `x6 = -1.411857`
2. `x4 = +0.814576`
3. `x7 = -0.771564`
4. `x5 = +0.323967`
5. `x2 = +0.191069`

This aligns well with the earlier BBD 003 gradient evidence, where F8 had a global-versus-recent gradient cosine of approximately `0.936764`.

## Repeatability

F8 contains one repeated coordinate group, repeated four times:

`0.060000-0.070000-0.030000-0.040000-0.410000-0.820000-0.500000-0.910000`

All four outputs were identical, with output range `0.0`.

Unlike F6, there is therefore no observed repeatability contradiction to a coordinate-only deterministic F8 mechanism over the sampled points.

## Interpretation

BBD 021 materially strengthens the case that F8 is governed, at least over the sampled region, by a stable static linear or very low-order surface.

The evidence now combines:

- BBD 004 compact linear LOOCV error of approximately `0.017307`;
- BBD 021 chronological walk-forward error of approximately `0.016539`;
- BBD 003 gradient coherence of approximately `0.936764`;
- 100% of coefficients meeting the 75% sign-stability threshold;
- four identical outputs at the repeated F8 coordinate.

This resolves much of the earlier apparent contradiction from BBD 007. The weakness appears to have been in the earlier general-purpose BBD implementation rather than in the F8 linear hypothesis itself.

## Evidence boundary

Exact function recovery remains false. BBD 008 showed that candidate F8 models can still diverge strongly away from the historical trajectory. The next test must therefore be discriminatory falsification using independent coordinates, ideally with SOC rerun under the same prospective protocol before any claim of true recovery is made.
