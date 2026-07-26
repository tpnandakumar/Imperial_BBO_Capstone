# PGC Experiment 008BQ: AX-R-LSR Learned Specialist Recruitment

## Status

Completed comparative development experiment. This is not final confirmatory evidence.

## Purpose

Test whether a low-stochastic specialist-recruitment architecture can improve on AX-R-BK random recruitment while preserving sparse operation and regenerative reuse.

## Systems compared

- AX-R-BK random recruitment
- AX-R deterministic disagreement-triggered recruitment
- AX-R deterministic error-phenotype recruitment
- AX-R-LSR learned specialist recruitment

## Design

- datasets: breast cancer, wine and digits
- seeds: 181, 197, 211, 227, 241, 257, 271, 283, 307 and 331
- 10 repeats per seed
- exact preserved AY fresh-seed out-of-fold and protected-test probabilities
- sparse three-model AX base
- zero or one recruited specialist
- fixed 30% specialist fusion weight
- cross-fitted shallow decision-tree gate for AX-R-LSR

## Best system

AX-R deterministic disagreement-triggered recruitment ranked first.

- mean accuracy: 0.985519
- standard deviation: 0.006560
- maximum accuracy: 0.997222
- minimum accuracy: 0.965302
- macro-F1: 0.985155
- balanced accuracy: 0.984546
- log loss: 0.084992
- mean worst-dataset accuracy: 0.975686
- mean active models: 3.112
- mean dropout fraction: 0.688754
- mean cache reuse rate: 0.995858
- mean avoided-model fraction: 0.688754
- mean state reuse rate: 0.860000
- mean Net Regenerative Efficiency: 0.836870

## Statistical evidence

The Friedman comparison was significant:

- statistic: 18.844371
- p value: 0.000294

### Disagreement recruitment versus random recruitment

- mean difference: +0.001152
- wins: 52
- ties: 15
- losses: 33
- Holm-adjusted p value: 0.008370

### Disagreement recruitment versus error-phenotype recruitment

- mean difference: +0.002145
- wins: 44
- ties: 25
- losses: 31
- Holm-adjusted p value: 0.002563

### Disagreement recruitment versus AX-R-LSR

- mean difference: +0.003265
- wins: 63
- ties: 12
- losses: 25
- Holm-adjusted p value: 0.000058

## Interpretation

The first learned specialist gate did not outperform the simpler deterministic disagreement rule.

The strongest low-stochastic architecture was:

```text
AX-R sparse core
+
disagreement-triggered specialist recruitment
+
regenerative state reuse
```

This architecture improved mean accuracy over random AX-R-BK recruitment while using only about 3.11 active models.

AX-R-LSR remains a valid candidate family, but the current tree gate should not replace AX-R-BK. The disagreement-triggered route should be treated as the stronger second-candidate direction.

## Evidence boundary

Regenerative efficiency is a computational reuse proxy. Electrical energy was not measured.
