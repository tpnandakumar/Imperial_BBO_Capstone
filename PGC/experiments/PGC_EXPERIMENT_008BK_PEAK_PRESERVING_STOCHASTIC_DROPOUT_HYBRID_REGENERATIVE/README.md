# PGC Experiment 008BK: Peak-Preserving Stochastic Dropout Hybrid with Regenerative Efficiency

## Status

Completed comparative 10-seed × 10-repeat regenerative hybrid experiment. This is not a final confirmatory result.

## Purpose

Compare the preserved non-dropout engine and the stable-core stochastic-dropout engine under equal regenerative-efficiency rules, then test a peak-preserving dual-arm selector and a Ripple-Delta regenerative hybrid.

## Design

- datasets: breast cancer, wine and digits
- 10 seeds
- 10 repeats per seed
- 100 aggregate evaluations per system
- 300 dataset-level evaluations per system
- regeneration applied to both primary engines
- 10 candidate configurations per arm
- development-only fold-aware selection

## Systems compared

- preserved 10-model regenerative engine
- stable 5-model core plus specialist-dropout regenerative engine
- peak-preserving dual-arm regenerative selector
- Ripple-Delta regenerative hybrid

## Main result

The stable 5-model core plus specialist-dropout regenerative engine was strongest.

- mean accuracy: 0.981962
- standard deviation: 0.007066
- maximum accuracy: 0.993519
- minimum accuracy: 0.968080
- macro-F1: 0.981668
- balanced accuracy: 0.981323
- log loss: 0.135963
- mean worst-dataset accuracy: 0.969934
- mean active models: 5.900
- mean dropout fraction: 0.463636
- mean cache reuse rate: 0.994039
- mean avoided-model fraction: 0.463636
- mean net regenerative efficiency: 0.704593

## Statistical evidence

The overall Friedman comparison was significant:

- statistic: 45.289604
- p value: 8.03 × 10⁻¹⁰

### Stable dropout-regenerative engine versus preserved regenerative engine

- mean difference: +0.004527
- wins: 66
- ties: 3
- losses: 31
- Holm-adjusted p value: 9.02 × 10⁻⁷

### Peak-preserving dual arm versus preserved regenerative engine

- mean difference: +0.004527
- wins: 66
- ties: 3
- losses: 31
- Holm-adjusted p value: 9.02 × 10⁻⁷

### Peak-preserving dual arm versus stable dropout-regenerative engine

- mean difference: 0.000000
- ties: 100

### Ripple-Delta hybrid versus peak-preserving dual arm

- mean difference: -0.000106
- Holm-adjusted p value: 0.626464

## Arm selection behaviour

The dual-arm selector chose:

- dropout arm: 96%
- preservation arm: 4%

## Interpretation

Applying regenerative efficiency to both engines did not restore the preserved ten-model engine to first place.

The stable five-model interior with stochastic specialist recruitment remained superior because it combined:

```text
high cache coherence
+
substantial avoided computation
+
limited model interference
+
selective peripheral recruitment
```

The peak-preserving selector selected the preservation arm only 4% of the time. This indicates that the earlier high peak was not the dominant operating region across these 100 repeated aggregate evaluations.

The Ripple-Delta blend did not improve further. Its sample-level interpolation slightly diluted the stronger dropout arm.

## Evidence boundary

Regenerative efficiency is a computational reuse proxy derived from cache coherence, avoided model activation, storage overhead and recovery overhead. It is not a measurement of electrical power or energy consumption.
