# PGC Experiment 008AX: Stack Depth 3, 5, 8 and 10 with Ten Seeds and Ten Repeats

## Status

Completed comparative multi-seed, multi-repeat experiment. This is not a single untouched confirmatory test.

## Purpose

Compare whether the pulsatile pressure-gradient conduit benefits from increasing predictive stack depth from 3 to 5, 8 and 10 models.

## Design

- stack sizes: 3, 5, 8 and 10
- independent split seeds: 10
- random conduit repeats per seed: 10
- repeat-level evaluations per stack: 100
- development candidates per repeat: 30
- total screened development candidates: 12,000
- five-fold stratified cross-fitting
- three datasets: breast cancer, wine and digits

## Conduit arms

- static reference
- pulsatile pressure-gradient conduit
- full closed loop with outer laminar venous return

## Selection protocol

All candidates were screened using development-only probability fusion. The strongest candidate from each arm was then refined using a cross-fitted ridge meta-classifier. The winning arm was frozen before protected evaluation.

## Nested stack composition

### 3-stack

- HistGradientBoosting
- Extra Trees
- logistic regression

### 5-stack

Adds:

- Random Forest
- linear discriminant analysis

### 8-stack

Adds:

- KNN
- Gaussian Naive Bayes
- SGD logistic classifier

### 10-stack

Adds:

- decision tree
- quadratic discriminant analysis

## Results

| Stack | Mean protected accuracy | 95% CI | Minimum | Maximum | Runs at or above 0.99 | Mean log loss |
|---|---:|---:|---:|---:|---:|---:|
| 3 | 0.979848 | 0.978704 to 0.980993 | 0.970712 | 0.990448 | 1 | 0.813427 |
| 5 | 0.980950 | 0.979196 to 0.982704 | 0.962378 | 0.996296 | 20 | 0.808951 |
| 8 | 0.981828 | 0.980391 to 0.983266 | 0.965156 | 0.994298 | 10 | 0.805766 |
| 10 | **0.983954** | **0.982565 to 0.985342** | **0.974756** | **0.995224** | **20** | **0.801245** |

## Main finding

The 10-stack was strongest overall.

- highest mean protected accuracy: 0.983954
- best calibration: log loss 0.801245
- best observed repeat: 0.995224
- 20 of 100 repeat-level evaluations reached or exceeded 0.99

The result shows that deeper stacks improved average performance and calibration. However, the system did not remain above 0.99 consistently. The above-0.99 outcomes were repeat-specific rather than a stable new operating level.

## Interpretation

The 3-stack appears under-capacitated. The 5-stack adds useful diversity but has greater variability. The 8-stack improves mean performance and calibration. The 10-stack provides the strongest balance of accuracy, worst-repeat protection and probability calibration.

The pulsatile conduit therefore benefits from additional specialist diversity, but the next step should focus on identifying which conditions produce the 0.99-plus runs and converting those conditions into a stable development-only routing policy.

## Evidence boundary

Each seed-specific protected split was reused across ten predeclared repeat selections. Protected labels were not used to select candidates within a repeat, but this remains a comparative repeated-evaluation study rather than a single untouched confirmation.

The ten-model architecture also differs from the earlier locked seven-model architecture by using lightweight diverse learners suitable for the 10-seed, 10-repeat replication.
