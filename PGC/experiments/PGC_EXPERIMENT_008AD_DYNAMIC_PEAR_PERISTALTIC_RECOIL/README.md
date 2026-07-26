# PGC Experiment 008AD: Dynamic Pear Pandora with Peristaltic Recoil

## Status

Completed three-seed shape trial. This is development evidence and requires ten-seed confirmation.

## Purpose

Test a purpose-directed asymmetric pear-shaped search field with elastic stretch, travelling peristaltic recoil and optional rifled helical movement.

## Locked architecture

- XGBoost
- LightGBM
- probabilistic SVC
- logistic regression
- CatBoost
- Extra Trees
- Random Forest

## Shapes compared

- ellipsoid control
- static pear
- purpose-directed pear stretch
- pear with peristaltic recoil
- rifled pear
- rifled pear with peristaltic recoil

Each shape received 100 configurations, giving 600 total configurations. The protected test remained sealed until all development winners were fixed.

## Best result

The strongest shape was the **rifled pear with peristaltic recoil**.

- winner configuration: 8
- ridge alpha: 1.272416
- stretch: 0.019798
- recoil: 0.053561
- twist: 1.110664 radians
- mean out-of-fold accuracy: 0.985122
- worst out-of-fold accuracy: 0.973626
- protected-test accuracy: **0.988596**
- protected-test worst-case accuracy: 0.964912
- macro-F1: 0.988333
- balanced accuracy: 0.987516
- log loss: 0.809415

## Interpretation

This is the first trial in this sequence to exceed the previous three-seed Pandora peak of 0.987622.

The improvement was produced by combining three geometric effects:

1. asymmetric pear-shaped exploration around the productive heterogeneous region
2. low-amplitude rifled movement for local angular coverage
3. a travelling recoil wave that compressed the search field behind the advancing front

The winning configuration used only modest stretch and recoil. This suggests that the benefit came from controlled directional modulation rather than aggressive deformation.

The result is promising but not yet confirmatory. The architecture must now be extracted and reproduced over ten fixed seeds before promotion.
