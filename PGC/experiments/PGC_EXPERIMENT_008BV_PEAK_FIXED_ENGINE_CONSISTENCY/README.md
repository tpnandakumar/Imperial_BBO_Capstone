# PGC Experiment 008BV: Peak-Fixed Engine Consistency

## Purpose

Isolate the highest-accuracy configuration observed in 008BU, freeze its parameters as a separate engine and test whether the peak reproduces consistently across all matched seeds and repeats.

## Source configuration

- source engine: DTRRR protected stochastic + A-DMIC
- source seed: 307
- source repeat: 1
- observed source peak accuracy: 0.997222

The following were frozen separately for each dataset:

- base-model composition
- base fusion weights
- recruited specialist
- disagreement threshold
- stochastic retention probabilities
- anchor model
- A-DMIC coefficients

## Frozen engine result

### Peak-Fixed DTRRR Protected Stochastic + A-DMIC

- evaluations: 100
- mean accuracy: 0.981635
- median accuracy: 0.982115
- mode accuracy: 0.979337
- standard deviation: 0.009922
- 95% confidence interval for mean accuracy: 0.979666 to 0.983603
- maximum accuracy: 0.996296
- minimum accuracy: 0.956043
- mean worst-dataset accuracy: 0.968392
- mean log loss: 0.072345
- mean active models: 2.666
- mean Net Regenerative Efficiency: 0.876173
- mean state reuse: 0.975097

The original 0.997222 peak was not reproduced in any of the 100 frozen-engine aggregate evaluations.

## Transfer excluding source seed 307

- evaluations: 90
- mean accuracy: 0.980489
- median accuracy: 0.979873
- standard deviation: 0.009773
- 95% confidence interval: 0.978442 to 0.982537
- maximum accuracy: 0.996296
- minimum accuracy: 0.956043

## Comparison with retuned reference

Compared with the retuned DTRRR protected stochastic + A-DMIC candidate:

- mean difference: -0.001704
- wins: 47
- ties: 1
- losses: 52
- Wilcoxon p value: 0.061602

## Interpretation

The isolated peak configuration was not consistently superior. Freezing the peak parameters reduced mean accuracy relative to the retuned candidate and did not reproduce the 0.997222 maximum.

The peak therefore appears to be a favourable seed-specific operating state rather than a universally transferable engine configuration.

A-DMIC still improved calibration, state reuse and regenerative efficiency without changing class decisions.

## Evidence boundary

This remains comparative development evidence. The reused protected holdout structure means it is not final confirmation.
