# PGC Experiment 008AJ: Dynamic Spin-Modulated RIPPLE Pear

## Status

Completed three-seed development trial. This is development evidence and requires ten-seed confirmation.

## Purpose

Test whether whole-Box spin should be dynamically modulated rather than fixed, using bootstrap confidence, goal alignment, recoil phase and distance from the current goal.

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

- 008AD reference
- confidence-modulated spin
- goal-alignment-modulated spin
- recoil-phase-modulated spin
- distance-modulated spin
- full dynamic spin modulation

## Search design

- 100 configurations per arm
- 600 total configurations
- 200 bootstrap resamples per candidate
- three seeds: 11, 37 and 71
- stratified five-fold cross-fitting
- frozen 20% protected test
- all arm winners fixed before protected-test evaluation

## Best result

The strongest arm was **goal-alignment-modulated spin**.

- winner configuration: 46
- batch: 5
- trial: 6
- ridge alpha: 1.218509
- spin rate: 0.119759 radians per step
- accumulated spin: 0.35 radians
- recoil: 0.047473
- dynamic twist: 0.781884 radians
- mean out-of-fold accuracy: 0.985288
- bootstrap standard deviation: 0.002194
- protected-test mean accuracy: **0.988596**
- protected-test worst accuracy: 0.964912
- macro-F1: 0.988333
- balanced accuracy: 0.987516
- log loss: 0.809576

## Interpretation

Dynamic spin modulation recovered the 008AD peak of 0.988596. The winning rule was not confidence-only, distance-only or recoil-phase-only. It was spin controlled by alignment between the current goal axis and the validated base axis.

The result suggests that spin is beneficial when it preserves forward agreement with the goal direction. Spin should increase while the goal remains aligned, but should not continue freely when the axis diverges.

The winning configuration used moderate recoil and sub-radian rifling. This supports the view that the highest-performing region is laminar and low amplitude.

No new accuracy record was set, but 008AJ provides a second independent mechanism that reproduces the 008AD peak. The next step is ten-seed extraction and confirmation of the goal-alignment spin rule.
