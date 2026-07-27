# PGC Experiment 008AL: Dynamic Wavefront Rhythm Comparison

## Status

Completed three-seed development trial. This is development evidence and is not yet confirmatory.

## Purpose

Compare dynamically tuned amplitude and frequency under four wavefront behaviours:

- symmetrical rhythmic wavefront
- asymmetrical rhythmic wavefront
- symmetrical variable-rhythm wavefront
- asymmetrical variable-rhythm wavefront

Two additional dynamically tuned arms tested symmetrical and asymmetrical wavefronts with amplitude and frequency changing according to bootstrap confidence and goal alignment.

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

The strongest arm was **symmetrical rhythmic wavefront with dynamically tuned frequency and amplitude**.

- winner configuration: 16
- batch: 2
- trial: 6
- amplitude: 0.060822
- frequency: 2.489911
- recoil: 0.037724
- accumulated spin: 0.35 radians
- rifling twist: 0.562676 radians
- ridge alpha: 1.365777
- mean out-of-fold accuracy: 0.985211
- bootstrap standard deviation: 0.001976
- protected-test mean accuracy: **0.988596**
- protected-test worst accuracy: 0.964912
- macro-F1: 0.988333
- balanced accuracy: 0.987516
- log loss: 0.809546

## Interpretation

The best regime combined dynamic amplitude and frequency with a symmetrical rhythmic wavefront. It reproduced the current 008AD and 008AJ peak of 0.988596 while showing the lowest bootstrap uncertainty among the leading regimes.

Asymmetry was not beneficial in this trial. Variable or arrhythmic rhythm also failed to improve transfer. This suggests that the pear-shaped search field may be asymmetric globally, while the propagating recoil wave itself performs better when locally symmetrical and rhythmically phase-locked.

The strongest operating region is therefore:

- asymmetric pear-shaped search medium
- symmetrical rhythmic peristaltic wavefront
- dynamically tuned amplitude and frequency
- goal-alignment-modulated spin
- low-amplitude rifling

This result requires exact extraction and ten-seed confirmation before promotion.
