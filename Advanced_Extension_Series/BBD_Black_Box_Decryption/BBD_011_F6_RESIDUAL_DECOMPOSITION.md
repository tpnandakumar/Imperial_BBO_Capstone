# BBD 011: F6 Residual Decomposition

## Purpose

BBD 010 favoured a static coordinate-dependent surface for F6, but exact repeated coordinates still produced non-identical outputs. BBD 011 therefore holds the static-surface interpretation as the baseline and studies the remaining prediction residual separately.

The aim is not to force a hidden-state explanation. It is to test whether the unexplained component shows reproducible structure related to uncertainty, novelty, movement, local response roughness or short-memory behaviour.

## Baseline

For each chronologically unseen F6 observation after the first five points, a coordinate-only Gaussian Process is fitted to the earlier observations only. The experiment records the prediction, predictive standard deviation and residual.

The baseline static Gaussian Process retained a walk-forward MAE of `0.064473`, equivalent to a normalised MAE of `0.044066` over the observed F6 output range.

## Residual features

The following quantities were examined:

- GP predictive standard deviation;
- distance to the nearest previously sampled coordinate;
- movement from the previous F6 coordinate;
- local output dispersion among the nearest historical points;
- output difference from the nearest historical coordinate;
- previous walk-forward residual;
- week index.

No exploratory Spearman association reached conventional significance. The largest signed-residual association was with week, `rho = 0.381`, while the largest absolute-residual association was with local output dispersion, `rho = -0.476`. With only eight walk-forward residuals these remain descriptive signals only.

## Predictive residual correction

Residual-correction models were trained only on residuals already observed at each stage and applied to later predictions.

The strongest result came from the **previous-residual-only** correction. Across the five eligible forward tests, the uncorrected static GP had MAE `0.056843` on those same observations. The previous-residual correction reduced this to `0.048096`, an improvement of `0.008747`, with normalised corrected MAE `0.032873`.

A novelty-only correction produced only a negligible improvement, from `0.056843` to `0.056795`. Movement, GP uncertainty, local roughness and the combined observable correction all worsened prediction.

The result therefore supports a **short-memory residual candidate**, but not a broad state model. This is consistent with BBD 010: the dominant mechanism remains a static coordinate-dependent surface, while a small part of the remaining error may carry information from the immediately preceding residual.

## Repeated-coordinate context

Exact repeated F6 coordinates remain a separate diagnostic. Three repeat-to-repeat comparisons are available across the two repeated-coordinate groups, and the maximum absolute change remains `0.100675`.

This confirms that a deterministic coordinate-only equation cannot reproduce every recorded F6 value exactly. BBD 011 does not establish whether that difference comes from evaluator noise, hidden state, numerical context or another unobserved factor.

## Current F6 representation

The most defensible working representation after BBD 010 and BBD 011 is:

```text
observed F6 response
=
static coordinate-dependent surface
+
small unresolved residual component
```

with preliminary evidence that the residual component may have short-memory structure. The available evidence does **not** justify replacing the static surface with a general time-dependent or state-dependent function.

## Outputs

Running `bbd_011_f6_residual_decomposition.py` creates:

- `outputs/BBD_011_F6_STATIC_GP_RESIDUALS.csv`
- `outputs/BBD_011_F6_RESIDUAL_DIAGNOSTICS.csv`
- `outputs/BBD_011_F6_REPEAT_CONTEXT.csv`
- `outputs/BBD_011_F6_RESIDUAL_CORRECTION_COMPETITION.csv`
- `outputs/BBD_011_F6_RESIDUAL_CORRECTION_PREDICTIONS.csv`
- `outputs/BBD_011_F6_RESIDUAL_DECOMPOSITION_SUMMARY.csv`

## Evidence boundary

This remains a post-capstone system-identification experiment. The previous-residual result is based on five corrected forward tests and is therefore a candidate mechanism, not proof of the hidden evaluator process. Exact recovery remains false unless genuinely independent black-box evidence discriminates the surviving explanations.
