# PGC Experiment 008AB: Pandora Axial Centrifuge

## Status

Completed three-seed development trial. This is development evidence, not confirmatory publication evidence.

## Architecture

The seven-model Pandora stack remained the protected fallback:

- XGBoost
- LightGBM
- probabilistic SVC
- logistic regression
- CatBoost
- Extra Trees
- Random Forest

## Axial centrifuge phases

1. formation of a validation-weighted probability axis
2. persistent A0 spin-up
3. temporary acceleration towards Vmax
4. radial separation of unstable routes
5. rescue-annulus gating
6. projection of the correction back onto the axis
7. terminal Vmax drop with A0 retained

## Search design

- 100 random configurations
- 10 batches
- 10 trials per batch
- three seeds: 11, 37 and 71
- stratified five-fold cross-fitting
- frozen protected test opened only for the selected winner

## Winning validation configuration

- search order: 8
- batch: 1
- trial: 8
- A0: 0.05
- Vmax: 0.70
- radial quantile: 0.85
- rescue-annulus width: 0.15
- axis power: 2.0
- projection strength: 0.10
- acceleration curve: linear
- mean out-of-fold accuracy: 0.985455
- worst development accuracy: 0.973626
- development rescues: 4
- development harms: 2
- development net rescue: +2
- activation rate: 0.141064

## Protected-test result

- axial centrifuge accuracy: **0.984227**
- Pandora fallback accuracy: **0.987622**
- macro-F1: 0.984125
- balanced accuracy: 0.983782
- log loss: 0.796753
- worst-case accuracy: 0.964912
- rescues: 0
- harms: 2
- net rescue: -2
- activation rate: 0.149415
- mean peak thrust on active cases: 0.254358
- terminal A0: 0.05

## Interpretation

Axial sorting substantially reduced intervention compared with the earlier dynamic ATA experiments. Protected-test activation fell to approximately 15%, compared with about 45% in Experiment 008AA and about 83% in Experiment 008Z.

However, the selected axial route still produced no protected-test rescues and introduced two harms. The centrifuge therefore improved sparsity and route discipline, but not classification accuracy.

The failure suggests that radial instability is useful for identifying unusual cases, but it is insufficient for deciding whether a correction is beneficial. Future ATA interventions should require both radial eligibility and direct cross-fitted evidence that the specific alternative prediction corrects the Pandora fallback.

No 008AB configuration is promoted. The unmodified Pandora stack remains the active three-seed leader.
