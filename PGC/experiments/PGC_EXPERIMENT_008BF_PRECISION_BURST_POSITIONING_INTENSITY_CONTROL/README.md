# PGC Experiment 008BF: Precision Burst Positioning and Intensity Control

## Status

Completed cross-domain precision-burst validation. This is not a final confirmatory result.

## Purpose

Test whether selecting the exact tunnel segment, specialist route, phase, intensity, pulse count, frequency, viscosity and recovery state from development evidence improves predictive accuracy and Net Burst Gain.

## Design

- 12 heterogeneous datasets
- 3 new seeds: 907, 929 and 953
- 36 dataset-seed units
- three-fold cross-fitting
- 108 response-surface candidates per unit
- development-only utility modelling and burst selection

## Systems compared

- stable 5-stack
- single fixed pulse
- fixed uniform burst
- phase-viscosity-compensated burst
- precision-positioned intensity-matched burst
- full sensor-guided regenerative burst

## Main result

The fixed uniform burst was strongest overall.

- mean accuracy: 0.871208
- worst-unit accuracy: 0.422222
- macro-F1: 0.795870
- balanced accuracy: 0.795382
- log loss: 0.350593
- corrected errors: 52
- newly introduced errors: 24
- Net Burst Gain: 28
- activation rate: 0.388968
- models activated per sample: 6.944842
- mean pulse count: 0.777937
- mean intensity: 0.062235
- mean phase error: 0.026462
- mean viscosity: 0.647222
- mean recovery: 0.225073

## Statistical evidence

The overall Friedman comparison was significant:

- statistic: 24.502688
- p value: 0.000174

However, the precision-positioned burst did not outperform the fixed uniform burst.

- precision versus stable 5-stack: mean difference -0.001071, Holm p = 0.135778
- precision versus fixed uniform burst: mean difference -0.003412, Holm p = 0.051910
- full regenerative burst versus precision burst: mean difference 0.000000, Holm p = 1.000000

## Interpretation

The experiment shows that burst placement and intensity matter, but the first learned precision controller was not calibrated well enough to identify the optimal local command consistently.

A moderate fixed uniform burst produced the best balance of correction and harm. The precision controller was too selective or assigned the wrong route, phase or intensity on several units.

This does not invalidate precision control. It demonstrates that a hand-designed response surface is insufficient. The next controller should learn burst response from accumulated dataset-seed outcomes, with explicit calibration of predicted gain against observed correction and harm.

## Evidence boundary

Burst position, pressure, phase and viscosity are computational control-state proxies. Training and inference times are measured wall-clock values. Electrical energy was not measured.
