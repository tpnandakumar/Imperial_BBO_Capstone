# BBD 024: F5 Direct SOC Rechallenge and Discriminatory Falsification

## Purpose

BBD 023 found that a dedicated Matérn 2.5 Gaussian Process predicted the historical F5 trajectory more accurately than the earlier general BBD and SOC comparisons. BBD 024 tests that result under a direct same-protocol contest and then converts the remaining model disagreement into prospective falsification coordinates.

## Direct rechallenge

The BBD 023 winning Matérn 2.5 model was compared against the full SOC model library using the same chronological walk-forward protocol. Each model trained only on observations available before the test week. Testing began after five historical observations and produced eight forward predictions.

The validated result was:

| Rank | Model | Normalised walk-forward MAE |
| --- | --- | ---: |
| 1 | BBD023 GP Matérn 2.5 | 0.001616 |
| 2 | SOC Gaussian Process Matérn | 0.001616 |
| 3 | SOC Gaussian Process RBF | 0.001666 |
| 4 | SOC Extra Trees | 0.031355 |
| 5 | SOC Random Forest | 0.055520 |
| 6 | SOC Distance Weighted KNN | 0.069500 |

The BBD 023 Matérn model and SOC Matérn model produced the same error because, in this implementation, they are effectively the same Matérn Gaussian Process. The direct result is therefore recorded as:

`tie_equivalent_matern_implementation`

This is not independent confirmation from two unrelated mechanisms. It resolves the earlier BBD versus SOC label conflict by showing that the strongest dedicated F5 model and the strongest SOC model are the same effective model family under the matched protocol.

The RBF Gaussian Process was only slightly weaker at `0.001666`. The meaningful mechanism comparison is therefore between a smooth Gaussian-process response surface and the interpretable quadratic reconstruction, rather than between the BBD and SOC labels themselves.

## Falsification roster

The duplicate SOC Matérn implementation was removed from the falsification roster so that identical models did not artificially increase agreement. The five retained models were:

- BBD 023 Matérn 2.5 Gaussian Process;
- BBD 023 quadratic ridge model;
- SOC Gaussian Process RBF;
- SOC Extra Trees;
- SOC Random Forest.

## Highest-value discriminatory coordinate

The strongest proposed F5 falsification point was:

`1.000000-0.000000-0.000000-0.000000`

At this coordinate the validated printed predictions included:

| Model | Predicted F5 |
| --- | ---: |
| BBD 023 Matérn 2.5 GP | 3013.054147 |
| BBD 023 quadratic ridge | 28467.707925 |
| SOC Gaussian Process RBF | 3699.993190 |
| SOC Extra Trees | 1415.876394 |

The fifth retained model, SOC Random Forest, is included in the underlying falsification calculation and output file but was not included in the compact printed query table produced by the workflow log.

The validated discrimination score was `7.601011`, the normalised prediction spread was `8.942515`, and novelty relative to the historical F5 coordinates was `1.732339`.

The quadratic reconstruction therefore makes a radically different global extrapolation from the smooth GP and tree-based models. A genuine black-box response at this coordinate would provide far more information about the generating mechanism than another small refinement near the historical optimum.

## Sequential falsification queue

Ten spatially separated candidate points were retained. The validated coordinates are:

1. `1.000000-0.000000-0.000000-0.000000`
2. `0.999303-0.279466-0.027128-0.043419`
3. `0.692926-0.068398-0.025112-0.000089`
4. `1.000000-1.000000-0.000000-0.000000`
5. `0.920541-0.734015-0.036031-0.010284`
6. `0.889024-0.024863-0.260639-0.044857`
7. `0.859402-0.026780-0.066852-0.224917`
8. `0.802693-0.464679-0.017355-0.062125`
9. `0.973451-0.325259-0.005047-0.293595`
10. `0.759187-0.243902-0.212109-0.004874`

These should be used sequentially if independent evaluator access becomes available. After each genuine observation, the surviving models should be refitted before the next coordinate is chosen.

## Interpretation

BBD 024 strengthens the conclusion that F5 is a highly smooth, strongly directional deterministic surface over the sampled trajectory. It also shows that excellent local prediction does not identify the global equation. The quadratic model remains valuable as an interpretable local approximation, but its extreme extrapolation at the leading falsification point means that global quadratic structure is not established.

The result therefore narrows the unresolved question to:

`locally excellent smooth GP representation` versus `globally valid low-order algebraic structure`.

## Evidence boundary

The discriminatory coordinates are proposed experiments only. No generated prediction is recorded as an Imperial black-box observation. The exact original F5 generating equation remains unproved until an independent evaluator returns values at genuinely unseen discriminatory coordinates.

`exact_function_recovered = False`
