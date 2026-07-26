# PGC Experiment 008BS: AX-R Triple Engine with LSR, DTRRR and Protected Stochastic Suppression

## Status

Completed comparative development experiment. This is not final confirmatory evidence.

## Systems compared

- AX-R-BK stochastic recruitment
- AX-R-DTRRR
- AX-R-LSR
- AX-R-DTRRR + LSR
- AX-R-DTRRR + protected stochastic suppression
- full AX-R triple engine

## Design

- datasets: breast cancer, wine and digits
- seeds: 181, 197, 211, 227, 241, 257, 271, 283, 307 and 331
- 10 repeats per seed
- exact preserved AY fresh-seed out-of-fold and protected-test probabilities
- DTRRR-selected specialist protected from stochastic suppression

## Best system

AX-R-DTRRR + protected stochastic suppression ranked first.

- mean accuracy: 0.983826
- standard deviation: 0.007540
- maximum accuracy: 0.997222
- minimum accuracy: 0.967008
- macro-F1: 0.983473
- balanced accuracy: 0.982856
- log loss: 0.090408
- mean worst-dataset accuracy: 0.973509
- mean active models: 2.747
- mean dropout fraction: 0.725300
- mean cache reuse rate: 0.996136
- mean avoided-model fraction: 0.725300
- mean state reuse rate: 0.910000
- mean Net Regenerative Efficiency: 0.860095

## Statistical evidence

The overall Friedman comparison was significant:

- statistic: 21.041345
- p value: 0.000796

The protected stochastic route significantly outperformed AX-R-LSR after Holm correction:

- mean difference: +0.001200
- Holm-adjusted p value: 0.040737

Its advantage over AX-R-DTRRR + LSR was borderline after Holm correction:

- mean difference: +0.001280
- Holm-adjusted p value: 0.050976

Differences versus AX-R-BK stochastic, AX-R-DTRRR and the full triple engine were not statistically confirmed.

## Interpretation

The full triple engine did not outperform the simpler protected two-stage route.

The strongest architecture in this experiment was:

```text
AX-R sparse core
+
DTRRR disagreement trigger
+
protected specialist recruitment
+
stochastic suppression of redundant non-protected models
+
regenerative reuse
```

LSR did not add value in this implementation. The learned specialist-selection layer reduced performance relative to the deterministic disagreement route.

The protected stochastic route achieved the highest regenerative efficiency and lowest active-model count among the leading systems, but its mean accuracy was below the earlier 008BQ DTRRR result. Therefore it should be retained as an efficiency-focused candidate rather than replacing the current accuracy-leading candidate.

## Evidence boundary

Regenerative efficiency is a computational reuse proxy. Electrical energy was not measured.
