# BBD 025: F4-Specific Decryption

## Purpose

BBD 025 begins dedicated decryption of Function 4 after function-specific work on F6, F7, F8 and F5. F4 was selected next because BBD 005 found the largest apparent improvement from benchmark-family matching: a transformed Rosenbrock feature reduced retrospective error relative to the earlier quadratic reconstruction.

That earlier result did not establish a Rosenbrock mechanism. BBD 025 therefore asks a stricter question: does the Rosenbrock lead survive when its centre and scale are selected using only the observations available inside each historical training window?

## Method

Eleven competing models were tested using expanding-window chronological prediction. Each model began with Weeks 1 to 5 and predicted the next unseen historical round. The training window then expanded by one round, producing eight prospective historical tests through Week 13.

The comparison included:

- a nested Rosenbrock-affine model;
- linear ridge models;
- quadratic and cubic ridge models;
- Matérn 2.5 and RBF Gaussian Processes;
- Random Forest and Extra Trees models.

For the Rosenbrock model, centre and coordinate scale were reselected by leave-one-out validation within each training window. This prevents the full thirteen-round record from choosing the transformation before earlier weeks are predicted.

Errors were normalised by the observed F4 output range. Repeated-coordinate behaviour and the stability of linear coordinate effects were examined separately.

## Model competition

| Rank | Model | Normalised walk-forward MAE | Median absolute error | Maximum absolute error |
| ---: | --- | ---: | ---: | ---: |
| 1 | Matérn 2.5 Gaussian Process | `0.021834` | `0.654575` | `1.383405` |
| 2 | Cubic ridge, alpha 0.01 | `0.027802` | `0.148211` | `4.242679` |
| 3 | Quadratic ridge, alpha 0.0001 | `0.029126` | `0.224619` | `3.936526` |
| 4 | Quadratic ridge, alpha 0.01 | `0.029203` | `0.218119` | `3.927965` |
| 5 | Nested Rosenbrock affine | `0.032816` | `0.851949` | `2.051960` |
| 6 | Quadratic ridge, alpha 0.1 | `0.036504` | `0.616610` | `3.854859` |
| 7 | Extra Trees | `0.037705` | `0.249459` | `3.762963` |
| 8 | RBF Gaussian Process | `0.040816` | `0.592346` | `4.790632` |
| 9 | Random Forest | `0.082557` | `0.947326` | `5.978507` |
| 10 | Linear ridge, alpha 0.01 | `0.421023` | `8.874630` | `34.474927` |
| 11 | Linear ridge, alpha 0.0001 | `0.459274` | `8.559916` | `36.169065` |

The Matérn 2.5 Gaussian Process was the strongest model. Its mean absolute error was approximately `0.586094` F4 output units, equivalent to `0.021834` of the observed output range.

## What happened to the Rosenbrock lead?

The nested Rosenbrock model remained competitive but fell to fifth place. Its selected centre was consistently `0.0`; the selected coordinate scale changed from `10.0` to `20.0` in the early expansion windows before returning to `10.0` from the Week 9 prediction onwards.

This changes the interpretation of BBD 005. The Rosenbrock feature captures genuine structure in the observed F4 trajectory, but it is not the strongest forward predictor when transformation selection is kept inside the historical training boundary. The earlier benchmark result is therefore evidence of Rosenbrock-like geometry, not evidence that F4 is a transformed Rosenbrock equation.

## Repeatability

The coordinate

`0.600000-0.430000-0.420000-0.250000`

was evaluated in Weeks 1, 12 and 13. It returned exactly the same value on all three occasions:

`-4.359874926582439`

The observed repeat range is `0.0`. Unlike F6, the F4 history contains no contradiction to a static coordinate-only mechanism.

## Coordinate effects

The full-history linear ridge diagnostic ranked the coordinate effects as x2, x1, x3 and x4 by absolute magnitude. These coefficients must be interpreted cautiously. The sign of x2 was stable across all expanding windows, but x3 and x4 changed sign frequently. The submitted F4 coordinates are also strongly correlated along parts of the trajectory, so the individual linear coefficients do not identify independent causal effects.

The poor performance of both linear ridge models confirms that F4 should not be treated as a simple additive linear surface.

## Interpretation

BBD 025 supports a static, repeatable and strongly nonlinear F4 response surface over the sampled region. A Matérn Gaussian Process currently provides the strongest chronological prediction, while low-order polynomial and Rosenbrock-like representations remain useful structural approximations.

The result narrows the unresolved mechanism question to:

`locally smooth nonlinear surface` versus `globally valid algebraic or Rosenbrock-like structure`.

The exact F4 equation has not been recovered. A decisive next stage would construct spatially novel coordinates where the Matérn, polynomial and nested Rosenbrock models disagree most, then use independent black-box evaluation if available.

## Evidence boundary

All results are post-capstone reconstructions from the preserved Week 01 to Week 13 record. No prediction is labelled as an Imperial evaluator output. No global optimum or exact generating equation is claimed.

`exact_function_recovered = False`

