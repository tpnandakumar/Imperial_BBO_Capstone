# PGC Experiment 008AE: RIPPLE-Propagated MaxInflu with Dynamic Rifling

## Status

Completed three-seed development trial. This is development evidence and is not yet confirmatory.

## Purpose

Test whether the MaxInflu direction can be recalculated after each batch, propagated into the next search region and combined with dynamically oriented rifling.

## Locked architecture

- XGBoost
- LightGBM
- probabilistic SVC
- logistic regression
- CatBoost
- Extra Trees
- Random Forest

## Arms compared

- fixed purpose-axis control
- batch-updated MaxInflu
- momentum-propagated MaxInflu
- MaxInflu with recoil
- dynamic rifled MaxInflu
- dynamic rifled MaxInflu with recoil

Each arm received 100 configurations, giving 600 total configurations. All arm winners were fixed before protected-test evaluation.

## Best result

The strongest arm was **dynamic rifled MaxInflu**.

- winner configuration: 14
- batch: 2
- trial: 4
- stretch: 0.08
- recoil: 0.00
- twist: 10.681415 radians
- ridge alpha: 1.262156
- mean out-of-fold accuracy: 0.985211
- worst out-of-fold accuracy: 0.973626
- protected-test accuracy: **0.988288**
- protected-test worst-case accuracy: 0.964912
- macro-F1: 0.988024
- balanced accuracy: 0.987208
- log loss: 0.809489

## Interpretation

Dynamic purpose-directed rifling improved on the original Pandora peak of 0.987622, confirming that the search direction can be updated from the strongest batch-wise influence rather than remaining fixed.

However, it did not exceed Experiment 008AD, where the rifled pear with peristaltic recoil reached 0.988596. In this trial, the best MaxInflu arm used no recoil at the winning point.

This suggests that MaxInflu propagation and rifling are beneficial, but the peristaltic pear geometry remains the stronger overall mechanism. The next confirmatory design should combine the exact 008AD pear geometry with batch-wise MaxInflu updating rather than replacing the pear field with a fully free dynamic axis.
