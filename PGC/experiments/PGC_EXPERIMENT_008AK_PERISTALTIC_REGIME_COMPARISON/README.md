# PGC Experiment 008AK: Peristaltic Regime Comparison

## Status

Completed three-seed development trial. This is development evidence, not confirmatory evidence.

## Purpose

Compare three peristaltic control regimes while preserving the 008AD asymmetric pear geometry, bootstrap validation, goal-alignment spin and low-amplitude rifling.

## Regimes tested

1. low amplitude, high speed and high frequency
2. high amplitude, low speed and low frequency
3. dynamically varying amplitude, speed and frequency

Two intermediate controls were also included:

- dynamic amplitude with fixed speed and frequency
- fixed amplitude with dynamic speed and frequency

## Locked architecture

- XGBoost
- LightGBM
- probabilistic SVC
- logistic regression
- CatBoost
- Extra Trees
- Random Forest
- ridge meta-classifier

## Search design

- 100 configurations per arm
- 600 total configurations
- 200 bootstrap resamples per candidate
- three seeds: 11, 37 and 71
- stratified five-fold cross-fitting
- frozen 20% protected test
- all arm winners fixed before protected-test evaluation

## Best result

The strongest arm was **dynamic amplitude with fixed speed and frequency**.

- winner configuration: 14
- batch: 2
- trial: 4
- peristaltic amplitude: 0.056215
- peristaltic speed: 1.0
- peristaltic frequency: 3.0
- recoil: 0.031397
- accumulated spin: 0.35 radians
- rifling twist: 0.674337 radians
- ridge alpha: 1.370280
- mean out-of-fold accuracy: 0.985288
- protected-test mean accuracy: **0.985510**
- protected-test worst accuracy: 0.964912
- macro-F1: 0.985445
- balanced accuracy: 0.984430
- log loss: 0.808972

## Interpretation

None of the tested peristaltic regimes exceeded the 008AD or 008AJ peak of 0.988596.

The result indicates that dynamic amplitude is more useful than fully dynamic amplitude, speed and frequency under the tested schedule. Allowing all three quantities to vary simultaneously did not improve transfer and likely introduced excess phase variability.

The highest-performing region still favours moderate speed, moderate frequency and controlled recoil rather than extreme or fully free peristaltic behaviour.

The 008AD and 008AJ result remains the active leader.
