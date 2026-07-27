# PGC Experiment 008BJ: Random Stack and Stochastic Dropout, 10 × 10

## Status

Completed comparative random-dropout experiment. This is not a final confirmatory result.

## Purpose

Test both random stack composition dropout and stochastic activation dropout across the full 11-model family.

## Design

- datasets: breast cancer, wine and digits
- 10 fresh seeds
- 10 repeats per seed
- 10 development-only candidate configurations per repeat
- 100 aggregate evaluations per system
- 300 dataset-level evaluations per system
- 11-model family including an RBF SVC specialist

## Systems compared

- random 3-stack dropout
- random 5-stack dropout
- full 11-model stochastic dropout
- stable 5-model core plus stochastic specialist dropout

## Main result

The stable 5-model core plus stochastic specialist dropout was strongest.

- mean accuracy: 0.984975
- standard deviation: 0.005078
- maximum accuracy: 0.994298
- minimum accuracy: 0.971004
- macro-F1: 0.984476
- balanced accuracy: 0.984212
- log loss: 0.134564
- mean worst-dataset accuracy: 0.973766
- mean active models: 6.313
- mean dropout fraction: 0.426061

## Statistical evidence

The overall Friedman comparison was significant:

- statistic: 13.367049
- p value: 0.003906

### Stable core plus specialist dropout versus random 5-stack

- mean difference: +0.002069
- wins: 60
- ties: 3
- losses: 37
- Holm-adjusted p value: 0.007732

### Stable core plus specialist dropout versus full 11-model stochastic dropout

- mean difference: +0.001815
- wins: 53
- ties: 10
- losses: 37
- Holm-adjusted p value: 0.007732

### Random 5-stack versus random 3-stack

- mean difference: +0.000721
- Holm-adjusted p value: 0.404481

### Full 11-model stochastic dropout versus random 5-stack

- mean difference: +0.000254
- Holm-adjusted p value: 0.505186

## Interpretation

The result identifies a clear architectural pattern:

```text
stable 5-model interior
+
stochastic recruitment of selected specialists
+
random dropout of unnecessary specialist pathways
```

This outperformed both a fully random 5-stack and stochastic dropout across the whole 11-model family.

The finding indicates that randomness is most useful around a stable core, not across the entire architecture. The stable core preserves reliable complementary structure, while dropout reduces interference and specialist recruitment adds diversity only when development evidence supports it.

This is the strongest current evidence that the cardiovascular and Ripple architecture should use a persistent interior with dynamic peripheral recruitment rather than continuously randomising the whole stack.

## Evidence boundary

Candidate count is a compute proxy. Runtime is measured wall-clock time. Electrical energy was not measured.
