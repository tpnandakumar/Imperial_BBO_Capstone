# PGC Experiment 008X: Fixed-Core Random Augmented Stacks

## Status

Completed three-seed development trial. This is not yet the ten-seed confirmatory result.

## Permanent fixed core

All future stack experiments retain the validated sphere-of-influence core:

- XGBoost
- LightGBM
- probabilistic SVC
- logistic regression
- stratified five-fold out-of-fold probabilities
- ridge meta-layer restricted to alpha 0.3 or 1.0
- frozen protected test

The fixed core is not randomly removed or replaced. Randomisation applies only to additional models stacked around it.

## Random augmentation design

- 10 random augmented configurations per batch
- 10 batches
- 100 random configurations
- three development seeds: 11, 37 and 71
- add-on inventory: Extra Trees, histogram gradient boosting, KNN and Gaussian Naive Bayes
- one to four add-ons per random configuration

## Development winner

The validation-selected winner was found at batch 4, trial 8:

- fixed core: XGBoost + LightGBM + SVC + logistic regression
- added model: Extra Trees
- ridge alpha: 1.0
- mean out-of-fold accuracy: 0.984735
- worst development accuracy: 0.971429

## Three-seed protected-test result

- mean accuracy: **0.990400**
- macro-F1: **0.989836**
- balanced accuracy: **0.989081**
- log loss: 0.808779
- worst-case accuracy: **0.964912**

This is the first project result above 99% mean full-coverage accuracy, but it remains provisional because it uses three development seeds. The exact winner must now be rerun across the full ten-seed confirmation set before promotion.

## Governing rule for future experiments

The fixed heterogeneous core remains permanent. Future experiments will:

1. retain the full core unchanged
2. create an inventory of additional candidate models or conduits
3. draw 10 random augmented configurations
4. repeat that process 10 times
5. select only by cross-fitted development evidence
6. open the protected test once for the selected winner
7. perform ten-seed confirmation before promotion
