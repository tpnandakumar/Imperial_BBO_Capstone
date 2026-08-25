# BBD 014: F6 Deterministic Surface Refinement

## Purpose

BBD 010 to BBD 013 left F6 with a strong static coordinate-dependent component plus an unresolved residual. Before treating that residual as genuine noise or hidden state, BBD 014 tests a simpler possibility: the baseline Gaussian Process may be missing deterministic geometry.

## Question

> Can a richer coordinate-only model reduce prospective F6 prediction error without adding time, previous-output or other state variables?

If the answer is yes, part of the apparent residual process was probably unresolved surface structure. If the answer is no, the case for a genuinely non-coordinate component becomes stronger.

## Model competition

All models use only the five F6 coordinates. They are compared with the same expanding-window chronological validation used in BBD 010.

The competition includes:

- Matérn Gaussian Processes with several smoothness assumptions;
- RBF and Rational Quadratic Gaussian Processes;
- regularised quadratic and cubic polynomial surfaces;
- RBF kernel ridge regression;
- Extra Trees;
- Random Forest;
- Gradient Boosting.

The BBD 010 Matérn 2.5 Gaussian Process is retained explicitly as the baseline.

## Determinism boundary

A better deterministic surface can reduce prediction error, but it cannot by itself overturn the repeated-coordinate finding. F6 contains identical coordinates with different recorded outputs. Therefore exact coordinate-only determinism remains falsified for the observed record unless those differences arise from measurement or evaluator variation.

## Outputs

Running `bbd_014_f6_deterministic_surface_refinement.py` creates:

- `outputs/BBD_014_F6_DETERMINISTIC_SURFACE_COMPETITION.csv`
- `outputs/BBD_014_F6_WALK_FORWARD_PREDICTIONS.csv`
- `outputs/BBD_014_F6_DETERMINISTIC_SURFACE_SUMMARY.csv`

## Interpretation rule

A richer deterministic model is treated as meaningful only if it improves chronological normalised MAE over the BBD 010 baseline by more than a trivial amount. Retrospective training fit is not used as proof.

## Evidence boundary

BBD 014 is a post-capstone system-identification experiment. It does not claim recovery of the original Imperial function. Exact recovery remains false and an independent discriminatory evaluation remains necessary.
