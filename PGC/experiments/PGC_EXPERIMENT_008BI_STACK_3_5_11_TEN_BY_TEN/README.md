# PGC Experiment 008BI: 3, 5 and 11 Stack, 10 × 10

## Status

Completed comparative 10-seed × 10-repeat stack-depth experiment. This is not a final confirmatory result.

## Purpose

Test whether stack size itself explains the recent accuracy behaviour, and determine whether the specialist-expanded 11-model family improves over smaller selected stacks.

## Design

- datasets: breast cancer, wine and digits
- 10 fresh seeds
- 10 repeats per seed
- 10 random subset-and-weight candidates per repeat
- stack sizes: 3, 5 and 11
- 100 aggregate evaluations per stack
- 300 dataset-level evaluations per stack
- development-only out-of-fold configuration selection
- RBF-kernel SVC added as the 11th specialist

## Main result

The 5-stack ranked first.

- mean accuracy: 0.978417
- standard deviation: 0.008493
- maximum aggregate accuracy: 0.994444
- minimum aggregate accuracy: 0.955604
- macro-F1: 0.977843
- balanced accuracy: 0.977286
- log loss: 0.139553
- mean worst-dataset accuracy: 0.963102

## Pairwise findings

### 5-stack versus 3-stack

- mean difference: +0.001475
- wins: 58
- ties: 3
- losses: 39
- raw p value: 0.038536
- Holm-adjusted p value: 0.115609

### 11-stack versus 5-stack

- mean difference: -0.000327
- wins: 47
- ties: 7
- losses: 46
- Holm-adjusted p value: 0.961797

### 11-stack versus 3-stack

- mean difference: +0.001148
- wins: 55
- ties: 3
- losses: 42
- Holm-adjusted p value: 0.168264

The Friedman comparison was not significant:

- statistic: 3.989664
- p value: 0.136037

## Recurrent model inclusions

The RBF SVC specialist was the most frequently selected model in both smaller stacks.

### 3-stack

- RBF SVC specialist: 52.67%
- logistic regression: 41.00%
- KNN: 34.00%
- LDA: 32.33%
- Extra Trees: 31.33%
- HistGradientBoosting: 30.33%

### 5-stack

- RBF SVC specialist: 66.33%
- SGD logistic: 56.67%
- KNN: 56.33%
- logistic regression: 56.00%
- Extra Trees: 52.33%
- Random Forest: 51.33%

## Interpretation

The experiment indicates a medium-depth optimum.

The 3-stack is occasionally too sparse and omits useful complementary structure. The 11-stack includes all models, but its additional members do not add enough independent information to offset dilution and weight competition. The 5-stack provides the strongest balance of diversity, specialist contribution and limited interference.

The strongest recurring 5-stack components are:

```text
RBF SVC specialist
+
linear correction pathway
+
local-neighbourhood pathway
+
tree-ensemble pathway
+
one additional complementary model
```

This suggests that the next specialist architecture should keep a stable 5-model interior and recruit the remaining models only when Delta Bridge evidence predicts positive specialist gain.

## Evidence boundary

Runtime is measured wall-clock time. Candidate count is a compute proxy. Electrical energy was not measured.
