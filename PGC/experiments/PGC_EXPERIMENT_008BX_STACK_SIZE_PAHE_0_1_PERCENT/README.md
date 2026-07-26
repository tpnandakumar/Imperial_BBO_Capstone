# PGC Experiment 008BX: Stack Size under A-DMIC-PAHE ±0.1%

## Status

Completed fresh matched comparative development experiment. This is not final confirmatory evidence.

## Design

- datasets: breast cancer, wine and digits
- model counts: 3, 5, 8, 10 and 11
- 10 independent cycle seeds
- 10 random subset repeats per cycle
- 100 aggregate evaluations per model count
- fresh training of all 11 candidate models
- A-DMIC-PAHE atmospheric band: ±0.1 percentage points, equal to ±0.001 on the 0 to 1 scale

The 11-model family contained logistic regression, GaussianNB, KNN, decision tree, ExtraTrees, Random Forest, HistGradientBoosting, SGD logistic, LDA, AdaBoost and an RBF SVC specialist.

## Primary ranking rule

1. median accuracy
2. minimum accuracy
3. mean accuracy
4. lower standard deviation

## Results

| Models | Median | Median 95% bootstrap CI | Mode or modal band | SD | Mean 95% CI | Minimum | Maximum | NRE |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 3 | 0.975024 | 0.970712 to 0.977193 | multimodal | 0.016156 | 0.965585 to 0.971997 | 0.908821 | 0.993372 | 0.868650 |
| 5 | 0.978046 | 0.974561 to 0.979971 | multimodal | 0.009096 | 0.975144 to 0.978754 | 0.953265 | 0.994298 | 0.801549 |
| 8 | 0.981969 | 0.980897 to 0.982895 | 0.9829 | 0.006205 | 0.980509 to 0.982971 | 0.969298 | 0.992446 | 0.701687 |
| 10 | 0.982895 | 0.978972 to 0.984284 | 0.9886 | 0.006352 | 0.981073 to 0.983594 | 0.968080 | 0.994298 | 0.635313 |
| 11 | 0.981433 | 0.979971 to 0.984284 | cycle-specific multimodal | 0.006604 | 0.981170 to 0.983791 | 0.973977 | 0.991520 | 0.601996 |

## Best typical-performance engine

The 10-model arm ranked first by median accuracy:

- median accuracy: 0.982895
- modal accuracy band: 0.9886
- modal frequency: 9 of 100
- sample SD: 0.006352
- mean accuracy: 0.982333
- 95% CI for mean: 0.981073 to 0.983594
- minimum accuracy: 0.968080
- maximum accuracy: 0.994298

## Stability interpretation

The 11-model engine had the strongest minimum accuracy, 0.973977, and the narrowest range, 0.017544. It therefore provided the strongest floor protection, despite a lower median than the 10-model arm.

The 8-model arm had the lowest SD, 0.006205, and a median close to the 10-model arm while using fewer models.

The 3-model arm had the highest regenerative efficiency but markedly worse variability and minimum accuracy.

## Statistical comparison

The overall Friedman test was significant:

- statistic: 84.039583
- p value: 2.42e-17

The 10-model engine significantly exceeded the 3-model and 5-model arms after Holm correction. Differences versus 8 and 11 models were not statistically confirmed.

## Bootstrap boundary

Random Forest internal bootstrap is part of the predictive engine.

Bootstrap confidence intervals for the median are post-experiment evaluation only and do not alter the engine or its predictions.
