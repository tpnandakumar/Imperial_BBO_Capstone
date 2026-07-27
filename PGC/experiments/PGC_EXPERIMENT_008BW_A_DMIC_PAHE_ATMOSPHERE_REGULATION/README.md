# PGC Experiment 008BW: A-DMIC PAHE Atmosphere Regulation

## Purpose

Create and test two peak-atmosphere regulators for the DTRRR protected stochastic + A-DMIC engine.

- PAHE-Lock: holds the peak atmosphere at the target values.
- PAHE-0.05: permits each atmospheric variable to vary only within ±0.05 percentage points, equal to ±0.0005 on the 0 to 1 scale.

## Target atmosphere

- sympathetic drive: 0.1947
- parasympathetic recovery: 0.8957
- viscosity: 0.7843
- temperature: 0.6446
- resistance: 0.7693
- recoil: 0.8531
- venous return: 0.9749
- target active models: 2.6919

## Design

- datasets: breast cancer, wine and digits
- seeds: 181, 197, 211, 227, 241, 257, 271, 283, 307 and 331
- 10 repeats per seed
- systems: A-DMIC reference, PAHE-Lock, PAHE-0.05
- exact preserved AY out-of-fold and protected-test probabilities

## Results

All three systems produced identical class decisions.

### Accuracy

- mean accuracy: 0.982819
- standard deviation: 0.008810
- maximum accuracy: 0.997222
- minimum accuracy: 0.958382
- mean worst-dataset accuracy: 0.972364

PAHE did not alter accuracy because this implementation regulated probability concentration and homeostatic state without changing route membership or class rank.

### PAHE-Lock

- mean log loss: 0.074853
- mean active models: 2.717
- state reuse: 0.974900
- Net Regenerative Efficiency: 0.874473
- all target variables held exactly at the target atmosphere

Compared with the A-DMIC reference:

- log-loss change: -0.002197
- p value: 3.63e-13
- Net Regenerative Efficiency change: +0.000041
- p value: 0.00400

### PAHE-0.05

- mean log loss: 0.074854
- mean active models: 2.717
- state reuse: 0.975250
- Net Regenerative Efficiency: 0.874543
- maximum atmospheric component deviation: 0.000350
- all components remained within the requested ±0.0005 band

Compared with the A-DMIC reference:

- log-loss change: -0.002195
- p value: 3.45e-13
- Net Regenerative Efficiency change: +0.000111
- p value: 1.64e-13

## Interpretation

The requested atmosphere was successfully recreated and regulated.

PAHE-0.05 was the stronger regulator because it preserved a small degree of autonomic movement while maintaining every atmospheric variable within the requested tolerance. It achieved slightly higher regenerative efficiency than the exact lock.

The next implementation must allow the atmospheric controller to influence route activation, specialist duration and stopping decisions under floor protection. That is required before the recreated atmosphere can alter accuracy rather than calibration alone.

## Evidence boundary

This is comparative development evidence. Cardiovascular and atmospheric terms are computational control analogues. Regenerative efficiency is a computational reuse proxy. Electrical energy was not measured.
