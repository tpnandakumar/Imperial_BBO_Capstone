# PGC Experiment 008AH: Bootstrap-Stabilised RIPPLE Pear

## Status

Completed three-seed development trial. This is development evidence, not confirmatory evidence.

## Purpose

Test whether bootstrap consensus can stabilise MaxInflu propagation, rifling and recoil while preserving the 008AD asymmetric pear geometry.

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

- 008AD control
- bootstrap validation only
- bootstrap MaxInflu
- bootstrap uncertainty-controlled recoil
- bootstrap Random Forest rifling
- full bootstrap RIPPLE

## Search design

- 100 configurations per arm
- 600 total configurations
- 200 bootstrap resamples per candidate
- three seeds: 11, 37 and 71
- stratified five-fold cross-fitting
- frozen 20% protected test
- all arm winners fixed before protected-test evaluation

## Best protected-test result

The strongest protected-test arm was the **008AD control**.

- winner configuration: 57
- ridge alpha: 1.224984
- stretch: 0.025457
- recoil: 0.0536
- local twist: 1.1107 radians
- mean out-of-fold accuracy: 0.985288
- bootstrap standard deviation: 0.002282
- bootstrap 95% interval: 0.981039 to 0.989350
- protected-test mean accuracy: **0.985510**
- protected-test worst accuracy: 0.964912
- macro-F1: 0.985479
- balanced accuracy: 0.984871
- log loss: 0.810054

## Development finding

Bootstrap Random Forest rifling produced the highest development mean accuracy among the tested arms:

- mean out-of-fold accuracy: 0.985455
- bootstrap standard deviation: 0.002171

However, that development advantage did not transfer to the protected test.

## Interpretation

Bootstrapping improved uncertainty estimation and reduced reliance on a single noisy batch winner, but it did not recover or exceed the 008AD peak of 0.988596.

The result suggests that bootstrap consensus is more useful as a validation and confidence layer than as a direct search deformation mechanism under the tested schedule.

The 008AD rifled pear with peristaltic recoil remains the active leader.
