# BBD 022: F8 Direct SOC Rechallenge and Discriminatory Falsification

## Purpose

BBD 021 found that F8 is predicted extremely well by a simple linear model under chronological walk-forward testing. The normalised MAE was approximately `0.016539`, substantially better than the earlier general-purpose BBD 007 result. BBD 022 reruns the SOC model families under the same chronological protocol and then defines high-value falsification coordinates.

## Direct same-protocol rechallenge

The thirteen F8 observations were ordered by week. Each model was trained only on observations available before the test week, beginning after five training observations. Eight later observations were therefore predicted using identical chronological splits.

The result was:

| Rank | Model | Normalised walk-forward MAE |
|---:|---|---:|
| 1 | SOC Gaussian Process RBF | 0.012542 |
| 2 | SOC Gaussian Process Matérn | 0.012716 |
| 3 | BBD 021 linear OLS | 0.016539 |
| 4 | SOC Extra Trees | 0.031358 |
| 5 | SOC Distance Weighted KNN | 0.047975 |
| 6 | SOC Random Forest | 0.059839 |

The direct winner is therefore the **SOC Gaussian Process RBF**, not the linear equation. Relative to the best SOC result, the BBD linear MAE is approximately 31.9% higher.

This is a more precise result than BBD 007. The linear hypothesis is substantially stronger than the earlier general BBD implementation suggested, but a flexible smooth Gaussian-process surface still predicts the historical chronology slightly better when both are tested under the same protocol.

## What survives from the linear hypothesis

The BBD 021 linear model remains unusually strong for an eight-dimensional function. Its normalised walk-forward MAE of `0.016539` is close to the GP values and materially better than the tree and nearest-neighbour SOC models.

Combined with the stable coefficient signs, strong gradient agreement and four identical repeated outputs at one coordinate, the evidence still supports a strong low-order deterministic component over the sampled region.

The present comparison does not justify replacing that interpretation with a purely local surrogate view. Instead it narrows the competition to a compact linear surface versus a slightly more accurate smooth nonlinear GP surface.

## Discriminatory falsification search

The BBD linear model and the three strongest SOC families were fitted to all thirteen historical F8 observations. A scrambled Sobol design over the eight-dimensional unit cube was supplemented with binary corners, and candidate coordinates were ranked by prediction disagreement and novelty.

The highest-value prospective coordinate is:

`1.000000-1.000000-1.000000-1.000000-1.000000-0.000000-0.000000-0.000000`

At this point the model predictions are approximately:

| Model | Predicted F8 |
|---|---:|
| BBD 021 linear OLS | 12.475058 |
| SOC Gaussian Process RBF | 9.558443 |
| SOC Gaussian Process Matérn | 9.908922 |
| SOC Extra Trees | 9.555345 |

The prediction spread is about `21.27` historical F8 response ranges and the novelty score is approximately `2.389`. This is therefore an extremely strong falsification point, although it is also far outside the region sampled during the competition.

A genuine evaluator result near `12.48` would strongly support global continuation of the linear equation. A result around `9.56` to `9.91` would support the nonlinear/local-surrogate interpretation and would show that the compact equation is primarily a local reconstruction.

## Interpretation

BBD 022 resolves the earlier contradiction more carefully than either BBD 007 or BBD 021 alone.

The evidence now supports:

`F8 is highly structured and close to linear over the sampled trajectory, but exact global linearity has not been established.`

The direct same-protocol contest favours the RBF Gaussian Process, but only by a relatively small absolute error margin. The strongest remaining scientific question is therefore not which model fits the thirteen observations, but which extrapolates correctly to a deliberately discriminatory new coordinate.

## Evidence boundary

BBD 022 does not fabricate outputs for the proposed discriminatory coordinates. The generated values are model predictions only. Exact F8 recovery remains false until independent evaluator observations are available at sufficiently discriminatory points.
