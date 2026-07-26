# PGC Experiment 008AF: AD and AE Hybrid

## Status

Completed three-seed hybrid trial. This is development evidence, not confirmatory evidence.

## Combined mechanism

Experiment 008AF combined:

- the asymmetric pear field from 008AD
- purpose-directed stretch
- peristaltic travelling recoil
- batch-wise MaxInflu propagation from 008AE
- momentum propagation
- dynamic purpose-directed rifling
- optional multi-front propagation

## Locked architecture

XGBoost, LightGBM, probabilistic SVC, logistic regression, CatBoost, Extra Trees and Random Forest were retained in every arm, with a ridge meta-classifier.

## Search design

- six hybrid arms
- 100 configurations per arm
- 600 configurations total
- three seeds: 11, 37 and 71
- stratified five-fold cross-fitting
- frozen 20% protected test
- all arm winners fixed before protected-test evaluation

## Best hybrid arm

The best arm was:

**Pear with dynamic rifled MaxInflu and peristaltic recoil**

- winner configuration: 75
- batch: 8
- trial: 5
- ridge alpha: 0.964059
- stretch: 0.209293
- recoil: 0.084237
- twist: 72.712523 radians
- mean out-of-fold accuracy: 0.985288
- worst out-of-fold accuracy: 0.973626
- protected-test mean accuracy: **0.985510**
- protected-test worst accuracy: 0.964912
- macro-F1: 0.985445
- balanced accuracy: 0.984430
- log loss: 0.808941

## Comparison with parent experiments

- 008AD rifled pear with peristaltic recoil: 0.988596
- 008AE dynamic rifled MaxInflu: 0.988288
- 008AF combined hybrid: 0.985510

## Interpretation

The combined system underperformed both parent mechanisms. The likely issue is over-modulation: the pear field, propagated MaxInflu, dynamic rifling and recoil all altered the candidate trajectory at once. The result suggests that 008AD and 008AE are not simply additive under this schedule.

The 008AD winner remains the active leader. A future hybrid should freeze the 008AD geometry and permit only low-amplitude MaxInflu adjustment of the rifling orientation, rather than allowing the full purpose axis to move.
