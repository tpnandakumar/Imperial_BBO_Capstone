# PGC Experiment 008BR: AX-R-DTRRR Hybridised with BJ and BK

## Status

Completed comparative development experiment. This is not final confirmatory evidence.

## Purpose

Test whether hybridising AX-R Disagreement-Triggered Regenerative Recruitment, abbreviated AX-R-DTRRR, with BJ or BK improves performance.

## Systems compared

- AX-R-DTRRR
- AX-R-DTRRR + BJ
- AX-R-DTRRR + BK
- AX-R-BK reference

## Design

- datasets: breast cancer, wine and digits
- seeds: 181, 197, 211, 227, 241, 257, 271, 283, 307 and 331
- 10 repeats per seed
- exact preserved AY fresh-seed out-of-fold and protected-test probabilities
- development-only parent preservation or bounded blending

## Best system

AX-R-DTRRR + BJ ranked first.

- mean accuracy: 0.984357
- standard deviation: 0.007537
- maximum accuracy: 0.996296
- minimum accuracy: 0.967154
- macro-F1: 0.984045
- balanced accuracy: 0.983392
- log loss: 0.085019
- mean worst-dataset accuracy: 0.975231
- mean active models: 3.270
- mean dropout fraction: 0.673009
- mean cache reuse rate: 0.996018
- mean avoided-model fraction: 0.673009
- mean state reuse rate: 0.851367
- mean Net Regenerative Efficiency: 0.829571

## Statistical evidence

The overall Friedman comparison was not significant:

- statistic: 4.605634
- p value: 0.203059

### AX-R-DTRRR + BJ versus AX-R-DTRRR

- mean difference: +0.000288
- wins: 30
- ties: 49
- losses: 21
- Holm-adjusted p value: 0.579228

### AX-R-DTRRR + BJ versus AX-R-DTRRR + BK

- mean difference: +0.000047
- wins: 19
- ties: 68
- losses: 13
- Holm-adjusted p value: 0.579228

### AX-R-DTRRR + BJ versus AX-R-BK reference

- mean difference: +0.000529
- wins: 41
- ties: 32
- losses: 27
- Holm-adjusted p value: 0.428645

## Interpretation

AX-R-DTRRR + BJ produced the highest mean accuracy, but the gain was small and not statistically confirmed.

BK did not clearly improve the disagreement-triggered route in this experiment. The DTRRR mechanism already supplied strong selective activation and regenerative reuse, so the additional BK reward added little.

The practical conclusion is:

```text
AX-R-DTRRR + BJ
=
provisional leading hybrid in this experiment
```

However, AX-R-DTRRR remains the cleaner low-stochastic candidate because the hybrid advantage was not significant.

## Evidence boundary

Regenerative efficiency is a computational reuse proxy. Electrical energy was not measured.
