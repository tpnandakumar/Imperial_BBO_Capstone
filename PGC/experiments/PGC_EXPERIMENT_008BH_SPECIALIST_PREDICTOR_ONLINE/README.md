# PGC Experiment 008BH: Specialist Predictor Online

## Status

Completed cross-domain specialist-predictor validation. This is not a final confirmatory result.

## Purpose

Bring the specialist predictor online and test whether development-defined error phenotypes can recruit distinct specialist routes that improve predictive accuracy.

## Design

- 12 heterogeneous datasets
- 3 new seeds: 1103, 1129 and 1151
- 36 dataset-seed units
- three-fold cross-fitting
- development-only specialist targeting

## Specialist routes

- posterior local specialist
- mid-tunnel nonlinear specialist
- anterior linear specialist

## Systems compared

- stable 5-stack
- fixed uniform burst
- rule-based specialist routing
- learned specialist predictor
- full Ripple plus Delta specialist controller

## Main result

The fixed uniform burst remained strongest overall.

- mean accuracy: 0.872865
- worst-unit accuracy: 0.397222
- macro-F1: 0.796506
- balanced accuracy: 0.796935
- log loss: 0.346288
- corrected errors: 39
- new errors: 20
- Net Specialist Gain: 19
- activation rate: 0.375355
- models activated per sample: 6.876773
- mean intensity: 0.060057

## Specialist predictor findings

The learned specialist predictor improved mean accuracy over the stable 5-stack by 0.000591.

The full Ripple plus Delta specialist controller improved mean accuracy over the learned specialist predictor by 0.000579.

The learned specialist predictor remained below the fixed uniform burst by 0.001119.

None of these pairwise differences remained statistically significant after Holm correction.

## Statistical evidence

- Friedman statistic: 4.300300
- Friedman p value: 0.366887

## Interpretation

The specialist predictor is now functioning and can identify development-defined cases in which a specialist route may correct the stable interior.

The learned selector and the Ripple plus Delta feedback layer both produced small positive mean gains relative to simpler baselines, but the fixed moderate burst still provided the best overall balance of correction and harm.

The next stage should increase specialist distinctiveness. The present routes are grouped from the existing ten-model family. Higher accuracy is more likely when each specialist uses a genuinely different feature transformation, objective or local decision structure.

## Evidence boundary

Ripple, Delta and specialist terminology describe computational control states. Training and inference times are measured wall-clock values. Electrical energy was not measured.
