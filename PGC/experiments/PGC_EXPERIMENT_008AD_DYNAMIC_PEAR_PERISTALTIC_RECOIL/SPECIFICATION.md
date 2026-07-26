# Experiment 008AD Specification

## Title

Dynamic Purpose-Directed Pear Pandora with Peristaltic Recoil

## Objective

Evaluate whether an asymmetric pear-shaped search field can improve model discovery by stretching towards a validated purpose axis, applying low-rate rifled local exploration and propagating a delayed peristaltic recoil wave behind the advancing search front.

## Locked predictive architecture

The predictive stack is fixed throughout the experiment:

- XGBoost
- LightGBM
- probabilistic SVC
- logistic regression
- CatBoost
- Extra Trees
- Random Forest
- ridge meta-classifier

No model may be removed after search begins.

## Data protocol

- datasets: breast cancer, wine and digits
- development seeds: 11, 37 and 71
- protected-test split: frozen 20%
- cross-fitting: stratified five-fold
- protected-test labels: not used during search or selection
- class-probability ordering: fixed per dataset

## Search arms

1. Ellipsoid control
2. Static pear
3. Purpose-directed pear stretch
4. Pear with peristaltic recoil
5. Rifled pear
6. Rifled pear with peristaltic recoil

## Search budget

- 100 configurations per arm
- 6 arms
- 600 total configurations
- equal compute budget per arm
- all six development winners fixed before protected-test evaluation

## Purpose axis

The initial purpose axis is the validated heterogeneous-diversity direction, with stronger positive extension towards CatBoost, Extra Trees and Random Forest while retaining the locked core.

The purpose axis controls axial stretch but does not directly determine the winner.

## Pear geometry

The pear field must have:

- a broad asymmetric lower chamber for exploration
- an offset bulge towards the productive heterogeneous region
- progressive narrowing towards the extraction neck
- stronger compression in historically weak directions
- bounded scales for every model block

## Purpose-directed stretch

Stretch is permitted only along the declared purpose axis.

The maximum stretch increases gradually with search progress. Stretch must remain bounded and cannot permanently displace the Box centre.

## Rifling

Rifling is implemented as a bounded helical displacement around the purpose axis.

Required parameters:

- twist angle
- twist rate
- helical radius
- rotation direction
- axial advance
- terminal damping

Rifling must improve local angular coverage without replacing the axial objective.

## Peristaltic recoil

Recoil is implemented as a travelling contraction wave behind the advancing search front.

Required properties:

- delayed relative to stretch
- phase-dependent
- bounded amplitude
- progressive compression of the chamber radius
- partial return of ridge alpha towards 1.0
- no direct use of protected-test feedback

## Candidate parameterisation

Each candidate contains:

- seven model probability-block scales
- ridge alpha
- stretch magnitude
- recoil magnitude
- twist angle
- search-arm identity
- configuration index

## Inner optimisation

For each candidate:

1. scale each model probability block
2. concatenate the seven blocks
3. fit the ridge meta-classifier on cross-fitted development predictions
4. generate out-of-fold probabilities
5. calculate mean accuracy, worst accuracy and standard deviation across dataset-seed combinations

## Selection rule

Within each arm, select by:

1. highest mean out-of-fold accuracy
2. highest worst-case out-of-fold accuracy
3. lowest out-of-fold standard deviation

The protected test is opened only after every arm winner is fixed.

## Primary metrics

- mean out-of-fold accuracy
- worst out-of-fold accuracy
- out-of-fold standard deviation
- protected-test mean accuracy
- protected-test worst-case accuracy
- macro-F1
- balanced accuracy
- log loss

## Winning configuration recorded in 008AD

- arm: rifled pear with peristaltic recoil
- configuration: 8
- ridge alpha: 1.272415531945832
- stretch: 0.0197979797979798
- recoil: 0.05356136401409906
- twist: 1.1106640694509369 radians
- protected-test mean accuracy: 0.9885964912280701

## Promotion rule

The result remains provisional until the exact extracted configuration is reproduced over ten fixed seeds with:

- no protected-test feedback
- preserved or improved worst-case accuracy
- no material degradation in calibration
- deterministic recording of all model scales and seeds

## Reproducibility outputs

Required files:

- README.md
- SPECIFICATION.md
- results_summary.json
- all_shape_configurations.csv
- shape_comparison_summary.csv
- shape_winner_protected_test_results.csv

## Interpretation boundary

This experiment tests search geometry. It does not prove that peristaltic recoil is itself a predictive mechanism. Any gain must be attributed to improved configuration discovery unless standalone extraction demonstrates otherwise.
