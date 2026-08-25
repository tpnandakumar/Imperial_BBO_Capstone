# BBD 011: F6 Residual Decomposition

## Purpose

BBD 010 favoured a static coordinate-dependent surface for F6, but exact repeated coordinates still produced non-identical outputs. BBD 011 therefore holds the static-surface interpretation as the baseline and studies the remaining prediction residual separately.

The aim is not to force a hidden-state explanation. It is to test whether the unexplained component shows reproducible structure related to uncertainty, novelty, movement, local response roughness or short-memory behaviour.

## Baseline

For each chronologically unseen F6 observation after the first five points, a coordinate-only Gaussian Process is fitted to the earlier observations only. The experiment records the prediction, predictive standard deviation and residual.

## Residual features

The following quantities are examined:

- GP predictive standard deviation;
- distance to the nearest previously sampled coordinate;
- movement from the previous F6 coordinate;
- local output dispersion among the nearest historical points;
- output difference from the nearest historical coordinate;
- previous walk-forward residual;
- week index.

Spearman associations are reported for both signed and absolute residuals. With only eight walk-forward residuals these correlations are treated as exploratory diagnostics rather than confirmatory statistical evidence.

## Predictive residual correction

BBD 011 also tests whether observable residual features can improve forward prediction. Residual-correction models are trained only on residuals already observed at that stage and then applied to later predictions.

The tested corrections include uncertainty-only, novelty-only, movement-only, previous-residual-only, local-roughness-only and a combined observable model. A residual mechanism is considered a candidate only if it improves expanding forward prediction over the uncorrected static Gaussian Process on the same test points.

## Repeated-coordinate context

Exact repeated F6 coordinates are retained as a separate diagnostic. Their week gaps, signed output changes and absolute output changes are recorded. This preserves the evidence that coordinate-only determinism cannot reproduce every observed value exactly, while avoiding the assumption that time itself caused the difference.

## Outputs

Running `bbd_011_f6_residual_decomposition.py` creates:

- `outputs/BBD_011_F6_STATIC_GP_RESIDUALS.csv`
- `outputs/BBD_011_F6_RESIDUAL_DIAGNOSTICS.csv`
- `outputs/BBD_011_F6_REPEAT_CONTEXT.csv`
- `outputs/BBD_011_F6_RESIDUAL_CORRECTION_COMPETITION.csv`
- `outputs/BBD_011_F6_RESIDUAL_CORRECTION_PREDICTIONS.csv`
- `outputs/BBD_011_F6_RESIDUAL_DECOMPOSITION_SUMMARY.csv`

## Evidence boundary

This remains a post-capstone system-identification experiment. A small-sample residual association is not evidence of the exact hidden mechanism. Exact recovery remains false unless a genuinely independent black-box evaluation discriminates the surviving explanations.
