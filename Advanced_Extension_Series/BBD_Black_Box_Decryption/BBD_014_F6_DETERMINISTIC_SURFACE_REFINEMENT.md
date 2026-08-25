# BBD 014: F6 Deterministic Surface Refinement

## Purpose

BBD 010 to BBD 013 left F6 with a strong static coordinate-dependent component plus an unresolved residual. Before treating that residual as genuine noise or hidden state, BBD 014 tests a simpler possibility: the baseline Gaussian Process may be missing deterministic geometry.

## Question

> Can a richer coordinate-only model reduce prospective F6 prediction error without adding time, previous-output or other state variables?

If the answer is yes, part of the apparent residual process was probably unresolved surface structure. If the answer is no, the case for a genuinely non-coordinate component becomes stronger.

## Model competition

All models use only the five F6 coordinates. They are compared with the same expanding-window chronological validation used in BBD 010.

The competition includes Matérn Gaussian Processes with several smoothness assumptions, RBF and Rational Quadratic Gaussian Processes, regularised quadratic and cubic polynomial surfaces, RBF kernel ridge regression, Extra Trees, Random Forest and Gradient Boosting. The BBD 010 Matérn 2.5 Gaussian Process is retained explicitly as the baseline.

## Result

The original BBD 010 Matérn 2.5 Gaussian Process remained the strongest deterministic surface.

| Rank | Coordinate-only model | Normalised walk-forward MAE |
|---|---|---:|
| 1 | Matérn 2.5 GP baseline | 0.044066 |
| 2 | Cubic ridge surface | 0.049131 |
| 3 | RBF GP | 0.049646 |
| 4 | Quadratic ridge | 0.054719 |
| 5 | Gradient boosting | 0.058589 |

The remaining candidates were weaker still. Therefore the best richer alternative produced no gain over the established baseline:

`absolute normalised gain over baseline = 0.000000`

`relative gain over baseline = 0.000000`

The deterministic-geometry refinement flag is consequently **false**.

## Interpretation

This is a useful negative result. The unexplained F6 component does not disappear when the coordinate-only surface family is widened substantially. In the observed 13-round record, the Matérn 2.5 GP remains the strongest tested deterministic coordinate model.

This strengthens the working representation:

`observed F6 = strong static coordinate surface + unresolved non-coordinate variation`

It does not prove that the residual is intrinsically stochastic. The remaining variation could still reflect an unrecorded variable, evaluator variation, or deterministic geometry outside the tested model families. What BBD 014 establishes is that several plausible richer deterministic surfaces did not improve prospective prediction.

## Determinism boundary

The repeated-coordinate evidence remains decisive. F6 contains two repeated-coordinate groups with non-identical outputs. The maximum within-coordinate output range is approximately `0.100675`, and the empirical repeated-coordinate MAE floor is approximately `0.030852`.

Therefore exact coordinate-only determinism remains falsified for the recorded observations.

## Outputs

Running `bbd_014_f6_deterministic_surface_refinement.py` creates:

- `outputs/BBD_014_F6_DETERMINISTIC_SURFACE_COMPETITION.csv`
- `outputs/BBD_014_F6_WALK_FORWARD_PREDICTIONS.csv`
- `outputs/BBD_014_F6_DETERMINISTIC_SURFACE_SUMMARY.csv`

## Evidence boundary

BBD 014 is a post-capstone system-identification experiment. It does not claim recovery of the original Imperial function. Exact recovery remains false and an independent discriminatory evaluation remains necessary.
