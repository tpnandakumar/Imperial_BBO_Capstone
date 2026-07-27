# PGC Experiment 008V: Random Stack Search with Brownian Spread Analysis

## Status

Completed trial evidence. Not publication evidence. This is a three-seed development experiment with a single frozen protected-test opening for the validation-selected winner.

## Design

- 300 unique random stack configurations
- 10 independent repetitions
- 30 random configurations per repetition
- five-fold stratified cross-fitting
- three development seeds: 11, 37 and 71
- cached XGBoost and LightGBM out-of-fold predictions
- optional inclusion of probabilistic SVC and logistic regression
- closed-form ridge meta-classifier
- one continuous probability-vector representation
- protected-test labels excluded from all configuration selection

The 300 configurations varied:

- XGBoost candidate
- LightGBM candidate
- ridge regularisation strength
- stack composition

## Winning validation configuration

- search order: 74
- repetition: 3
- trial: 14
- XGBoost configuration: 0
- LightGBM configuration: 0
- ridge alpha: 1.0
- stack mode: full heterogeneous
- mean out-of-fold accuracy: 0.984955
- out-of-fold accuracy standard deviation: 0.008066

## Protected-test result

- mean accuracy: **0.987622**
- macro-F1: **0.987291**
- balanced accuracy: **0.986745**
- log loss: 0.808176
- worst-case accuracy: **0.964912**

## Comparison

- historical screenshot-supported DVCSE maximum: 0.986126
- best reproducible Experiment 008T result: 0.981248
- Experiment 008U heterogeneous stack development result: 0.984893
- Experiment 008V random-stack winner: **0.987622**

The 008V winner exceeds the historical full-coverage accuracy numerically, but it is not yet promoted because it has only been confirmed over three seeds and its probability calibration is poor, as shown by the high log loss.

## Brownian-motion-inspired spread analysis

The configuration search was treated as a stochastic sequence for descriptive analysis only. This is a computational analogy, not a claim that model accuracy literally follows physical Brownian motion.

- mean validation score: 0.976141
- validation score standard deviation: 0.008537
- mean sequential drift: approximately -0.000006
- diffusion coefficient: approximately 0.000075
- best validation score: 0.984955
- median validation score: 0.980030

The near-zero drift indicates that random search did not improve simply because later trials were sampled later. Improvement came from isolated favourable configurations rather than a directional trend through the search sequence.

## Interpretation

The strongest result came from the full heterogeneous stack rather than from a pure XGBoost-LightGBM pairing. This confirms that error diversity remains more valuable than using several closely related boosting models.

The accuracy result is highly promising. However, the ridge meta-layer generated poorly calibrated probabilities. The next confirmatory experiment should preserve the winning base configuration while replacing or calibrating the meta-layer, then repeat across ten seeds before promotion.
