# PGC Experiment 008BC: Strategic Diastole

## Status

Completed cross-domain strategic-diastole validation. This is not a final confirmatory result.

## Purpose

Test diastole as an active computational control phase rather than passive recovery.

Strategic diastole estimates whether additional specialist flow is likely to help or harm each sample, then regulates specialist withdrawal, venous return, congestion relief and recovery duration before the next systolic demand.

## Design

- 12 heterogeneous datasets
- 3 new seeds: 701, 719 and 743
- 36 dataset-seed units
- three-fold cross-fitting
- development-only utility modelling
- identical protected holdouts for all systems

## Systems compared

- static 5-stack
- continuous microcirculation
- fixed diastolic recovery
- utility-triggered diastole
- full strategic diastole

## Strategic controls

- estimated specialist helpfulness
- estimated specialist harm
- specialist-flow threshold
- recovery gain
- congestion gain
- venous return
- diastolic duration

## Main result

The static 5-stack remained strongest overall.

- mean accuracy: 0.872995
- worst-unit accuracy: 0.380556
- macro-F1: 0.796493
- balanced accuracy: 0.796924
- log loss: 0.349582

Full strategic diastole did not outperform the static 5-stack or continuous microcirculation overall.

## Relative findings

Compared with fixed diastolic recovery, full strategic diastole improved mean accuracy by 0.000338.

Compared with utility-triggered diastole, full strategic diastole improved mean accuracy by 0.000251.

Compared with continuous microcirculation, the mean difference was effectively zero.

Compared with the static 5-stack, full strategic diastole was lower by 0.000231.

None of these differences remained statistically significant after Holm correction.

## Statistical evidence

The Friedman comparison across all five systems was not significant:

- statistic: 3.839196
- p value: 0.428206

## Interpretation

Strategic diastole improved the ordering of recovery mechanisms but did not improve the overall predictive ceiling.

The result indicates that active recovery is most useful as a control and stabilisation layer. It can reduce unnecessary specialist persistence and improve on simpler recovery rules, but it should not replace the efficient stable interior when no strong evidence supports extra flow.

The next implementation should combine strategic diastole with selective specialist microcirculation only in samples where development evidence predicts a positive Net Specialist Gain.

## Evidence boundary

All utility models and control parameters were fitted from development-only out-of-fold predictions. Holdout labels were not used to define diastolic strategy.

Heart, pressure, venous return and diastolic duration are computational control-state definitions. Electrical energy was not measured.
