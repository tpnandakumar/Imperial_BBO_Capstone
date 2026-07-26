# PGC Experiment 008BT: Engine Choice and Sequencing Protocol

## Status

Completed comparative development experiment. This is not final confirmatory evidence.

## Purpose

Test whether a dynamic free-choice controller can select one engine or a sequence of engines per sample and improve accuracy, regenerative efficiency, operational economy and versatility.

## Systems compared

- AX-R-BK reference
- AX-R-DTRRR
- DTRRR followed by protected stochastic suppression
- stochastic suppression followed by DTRRR
- fixed triple reference
- ECSP dynamic free-choice engine

## Design

- datasets: breast cancer, wine and digits
- seeds: 181, 197, 211, 227, 241, 257, 271, 283, 307 and 331
- 10 repeats per seed
- exact preserved AY fresh-seed out-of-fold and protected-test probabilities
- cross-fitted shallow decision-tree route selector
- per-sample route choice among BK, DTRRR, DTRRR then protected stochastic, stochastic then DTRRR and LSR
- development route target minimised log loss plus active-model complexity penalty

## Best mean-accuracy system

The fixed triple reference ranked first by mean accuracy.

- mean accuracy: 0.984299
- standard deviation: 0.007486
- maximum accuracy: 0.996296
- minimum accuracy: 0.966715
- macro-F1: 0.983964
- balanced accuracy: 0.983123
- log loss: 0.089498
- mean worst-dataset accuracy: 0.973930
- mean active models: 3.476
- Net Regenerative Efficiency: 0.837365

## ECSP dynamic result

- mean accuracy: 0.983764
- maximum accuracy: 0.996296
- minimum accuracy: 0.955458
- macro-F1: 0.983419
- balanced accuracy: 0.982743
- log loss: 0.081835
- mean worst-dataset accuracy: 0.974363
- mean active models: 3.040
- mean dropout fraction: 0.695978
- mean cache reuse rate: 0.995944
- mean state reuse rate: 0.940000
- mean Net Regenerative Efficiency: 0.855583

## Dynamic route use

- DTRRR then protected stochastic: 24.97%
- LSR: 24.25%
- BK: 21.43%
- stochastic then DTRRR: 18.64%
- DTRRR: 10.70%

## Statistical evidence

The overall Friedman comparison was significant:

- statistic: 11.285438
- p value: 0.046005

The fixed triple significantly outperformed DTRRR followed by protected stochastic suppression after Holm correction:

- mean difference: +0.001850
- Holm-adjusted p value: 0.028144

Its advantage over ECSP was not statistically confirmed:

- mean difference: +0.000535
- Holm-adjusted p value: 0.683597

## Interpretation

Dynamic engine choice did make a difference, but not in the form of higher mean accuracy.

ECSP improved:

```text
calibration
+
worst-dataset accuracy
+
active-model economy
+
regenerative efficiency
```

However, it reduced the minimum observed aggregate accuracy and did not surpass the fixed triple on mean accuracy.

Therefore ECSP should be retained as an efficiency-oriented and calibration-oriented controller, not promoted as the new default accuracy engine.

The current evidence suggests that dynamic route choice is useful, but the route gate needs stronger floor protection and a more conservative fallback rule before it can be considered superior.

## Evidence boundary

Regenerative efficiency is a computational reuse proxy. Electrical energy was not measured.
