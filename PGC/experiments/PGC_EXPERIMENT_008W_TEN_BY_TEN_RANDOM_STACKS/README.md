# PGC Experiment 008W: Ten-by-Ten Random Stack Search

## Status

Completed trial evidence. Not publication evidence.

## Design

- 10 random stacks per batch
- 10 batches
- 100 unique random stack configurations
- 10 fixed seeds
- 1,000 configuration-seed evaluations
- stratified five-fold cross-fitting
- cached XGBoost, LightGBM, probabilistic SVC and logistic-regression probability outputs
- closed-form ridge meta-classifier
- protected-test labels excluded from configuration selection

## Winning validation configuration

- search order: 53
- batch: 6
- trial: 3
- XGBoost configuration: 0
- LightGBM configuration: 1
- ridge alpha: 1.0
- stack mode: full heterogeneous
- mean out-of-fold accuracy: 0.982337
- out-of-fold accuracy standard deviation: 0.007394
- worst development-seed accuracy: 0.957746

## Protected-test result

- mean accuracy: **0.986072**
- macro-F1: **0.985397**
- balanced accuracy: **0.984536**
- log loss: 0.805447
- worst-case accuracy: **0.956140**

## Comparison

- Historical DVCSE result: 0.986126
- Experiment 008V three-seed provisional result: 0.987622
- Experiment 008W ten-seed result: 0.986072

The ten-seed result is 0.000054 below the historical DVCSE result, equivalent to approximately 0.0054 percentage points. It is also lower than the three-seed 008V development result, showing that the earlier gain was partly seed-sensitive.

## Brownian spread analysis

- mean validation score: 0.974966
- validation score standard deviation: 0.008091
- sequential drift: approximately -0.000029
- diffusion coefficient: approximately 0.000067
- best validation score: 0.982337
- median validation score: 0.979341

The near-zero drift again indicates that improvement did not arise from later trial order. Strong configurations appeared as isolated favourable states within the random search field.

## Interpretation

The full heterogeneous stack remained the best architecture. Expanding from three to ten seeds reduced the apparent mean gain and produced a more credible estimate of out-of-sample stability.

The model is effectively tied with the historical DVCSE result on accuracy, but calibration remains poor. The next experiment should preserve the winning class decisions while calibrating probabilities separately, without allowing calibration tuning to alter the selected class labels.
