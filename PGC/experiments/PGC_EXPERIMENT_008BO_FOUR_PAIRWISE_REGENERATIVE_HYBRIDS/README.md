# PGC Experiment 008BO: Four Pairwise Regenerative Hybrids

## Status

Completed comparative 10-seed × 10-repeat experiment. This is comparative evidence, not final confirmation.

## Purpose

Compare four pairwise hybrid architectures under identical seeds, splits, candidate budgets and regenerative-efficiency accounting:

1. AX-R + BJ
2. AX-R + BK
3. AY-R + BJ
4. AY-R + BK

## Design

- datasets: breast cancer, wine and digits
- seeds: 181, 197, 211, 227, 241, 257, 271, 283, 307 and 331
- 10 repeats per seed
- 10 candidates per parent route
- development-only parent preservation or bounded pairwise blending
- common source: exact preserved AY fresh-seed records

BJ was represented as stable-core stochastic specialist dropout without regenerative reward in development selection.

BK used the same stable-core dropout family with regenerative reward and stronger state reuse.

The preserved ten-model probability family was used. RBF SVC was not included because it was absent from the preserved AY probability records.

## Best system

AX-R + BK ranked first.

- mean accuracy: 0.984650
- standard deviation: 0.007382
- maximum accuracy: 0.996296
- minimum accuracy: 0.968080
- macro-F1: 0.984403
- balanced accuracy: 0.983886
- log loss: 0.088474
- mean worst-dataset accuracy: 0.974816
- mean active models: 3.383
- mean dropout fraction: 0.661667
- mean cache reuse rate: 0.996079
- mean avoided-model fraction: 0.661667
- mean state reuse rate: 0.820075
- mean Net Regenerative Efficiency: 0.819201

## Statistical evidence

The overall Friedman test was not significant:

- statistic: 3.105263
- p value: 0.375679

### AX-R + BK versus AX-R + BJ

- mean difference: +0.000568
- wins: 19
- ties: 74
- losses: 7
- Holm-adjusted p value: 0.011063

### AX-R + BK versus AY-R + BJ

- mean difference: +0.000712
- Holm-adjusted p value: 1.000000

### AX-R + BK versus AY-R + BK

- mean difference: +0.000216
- Holm-adjusted p value: 1.000000

## Interpretation

Adding BK regenerative selection to AX-R produced the strongest mean accuracy, worst-dataset accuracy and regenerative efficiency among the four pairwise hybrids.

The clear gain over AX-R + BJ indicates that regenerative reward improved the AX pathway. However, the four systems were close overall, and the Friedman test did not establish a global difference.

The next experiment should compare Accuracy, Versatility, Regenerative Use and Complexity across AX-R, AY-R, the three-route 008BN hybrid and the strongest pairwise 008BO hybrid.

## Evidence boundary

Regenerative efficiency is a computational reuse proxy. Electrical energy consumption was not measured.
