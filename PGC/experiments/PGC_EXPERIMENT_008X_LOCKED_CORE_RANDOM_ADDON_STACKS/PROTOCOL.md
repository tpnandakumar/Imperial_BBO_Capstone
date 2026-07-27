# PGC Experiment 008X: Locked-Core Random Add-on Stacks

## Status

Forward protocol locked. Execution remains pending because the first two in-session runs exceeded the execution window before completing all cached base-model predictions. No result claim is permitted until a complete run finishes.

## Permanent locked core

Every future configuration must contain all four of the following models:

- XGBoost
- LightGBM
- probabilistic SVC
- logistic regression

These models form the fixed sphere-of-influence core identified from Experiments 008V and 008W.

## Locked regularisation region

The stacking meta-layer must use ridge regularisation restricted to:

- alpha 0.3
- alpha 1.0

## Random add-on inventory

The following models may be added individually or in combinations around the locked core:

- CatBoost
- Extra Trees
- Histogram Gradient Boosting
- Random Forest

The locked core may never be removed during this experiment family.

## Search schedule

- 10 random configurations per batch
- 10 independent batches
- 100 total sampled configurations
- 10 fixed seeds
- stratified five-fold cross-fitting
- frozen 20% protected test
- protected-test labels unavailable to all model, inventory and threshold selection

## Selection rule

Rank configurations using development data only, in this order:

1. highest mean out-of-fold accuracy
2. highest worst-seed out-of-fold accuracy
3. lowest out-of-fold accuracy standard deviation

Open the protected test once, only for the selected configuration.

## Required outputs

- `random_addon_stack_results.csv`
- `winner_protected_test_results.csv`
- `inventory_influence_summary.csv`
- `results_summary.json`
- `README.md`

## Promotion criteria

A candidate may advance only if it:

1. exceeds the Experiment 008W mean protected-test accuracy of 0.986072
2. preserves or improves worst-case accuracy of 0.956140
3. shows non-negative influence from each retained add-on
4. remains stable across ten fixed seeds
5. preserves the frozen protected-test rule

## Execution integrity

Interrupted or partial runs must not be reported as completed experiments. Only fully generated outputs may be stored as trial results.
