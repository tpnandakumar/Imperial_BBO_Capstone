# PGC Experiment 008AG: Local Rifling with Slow Box Rotation

## Status

Completed three-seed development trial. This is development evidence, not confirmatory evidence.

## Purpose

Test whether rifling can be restricted to the strongest single-model direction while the full 008AD pear-shaped Box rotates slowly around its stable purpose axis.

## Locked architecture

- XGBoost
- LightGBM
- probabilistic SVC
- logistic regression
- CatBoost
- Extra Trees
- Random Forest
- ridge meta-classifier

## Arms

- 008AD-style control
- Random Forest local rifling
- Extra Trees local rifling
- CatBoost local rifling
- Random Forest local rifling with slow Box rotation
- Random Forest local rifling with slow Box rotation and recoil

## Search design

- 100 configurations per arm
- 600 total configurations
- three seeds: 11, 37 and 71
- stratified five-fold cross-fitting
- frozen 20% protected test
- all arm winners fixed before protected-test evaluation

## Best result

The strongest arm was:

**Random Forest local rifling with slow Box rotation**

- winner configuration: 45
- ridge alpha: 1.233362
- local twist: 0.158694 radians
- slow Box rotation: 0.133333 radians
- recoil: 0
- mean out-of-fold accuracy: 0.985276
- worst out-of-fold accuracy: 0.973626
- protected-test mean accuracy: **0.985510**
- protected-test worst accuracy: 0.964912
- macro-F1: 0.985445
- balanced accuracy: 0.984430
- log loss: 0.808575

## Interpretation

The winning arm confirms that low local twist and slow whole-Box rotation are preferable to the excessive rifling seen in 008AF. However, the configuration did not reproduce the 008AD peak of 0.988596.

The strongest evidence from this experiment is that Random Forest is the best single-model rifling direction among the tested candidates. Slow rotation was tolerated and selected at a modest angle, but the gain-producing 008AD geometry was not recovered.

This suggests that the benefit in 008AD depended on the exact coupled geometry of pear asymmetry, low rifling and peristaltic recoil, rather than on local rifling or slow rotation alone.

The 008AD result remains the active leader.
