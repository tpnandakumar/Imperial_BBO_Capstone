# PGC Experiment 008CH-C: Targeted Remediation

## Status

Completed comparative development experiment. This is not final independent confirmation.

## Design

- three targeted challenge conditions
- five fresh seeds: 1201, 1213, 1229, 1249 and 1277
- 45 arm-runs
- 60% training, 20% validation and 20% protected test
- zero split overlap
- protected test labels were not used for model selection, residual correction, blending or gating
- A-DMIC Computational Milieu Intérieur remained the basal regulatory layer

## Arms

1. Reference residual engine
2. Full condition-specific specialist
3. A-DMIC gated specialist

## Results

### High-dimensional sparse

- reference mean accuracy: 0.605333
- targeted specialist mean accuracy: 0.610667
- A-DMIC gated specialist mean accuracy: 0.610667
- mean gain: 0.005333
- gated specialist activation: 96.6%
- paired Wilcoxon p: 0.7500

The specialist produced only a small, non-significant gain and required near-continuous activation. This does not qualify as an efficient remediation.

### Noisy missing binary

- reference mean accuracy: 0.790667
- targeted specialist mean accuracy: 0.790667
- A-DMIC gated specialist mean accuracy: 0.790667
- mean gain: 0.000000
- A-DMIC activation: 0%
- paired Wilcoxon p: 1.0000

The validation controller correctly rejected specialist recruitment because it offered no improvement.

### Temporal drift binary

- reference mean accuracy: 0.578000
- targeted specialist mean accuracy: 0.598667
- A-DMIC gated specialist mean accuracy: 0.598667
- mean gain: 0.020667
- wins: 5 of 5 seeds
- paired Wilcoxon p: 0.0625
- A-DMIC activation: 40%
- reference minimum accuracy: 0.533333
- remediated minimum accuracy: 0.570000
- reference SD: 0.029117
- remediated SD: 0.019090

Temporal remediation improved mean accuracy, minimum accuracy and stability across every seed. The p-value did not cross 0.05 because only five matched seeds were used. This result requires a larger confirmatory run.

## Decision

- Promote the temporal-drift specialist to expanded validation.
- Do not promote the current high-dimensional sparse specialist because the gain is small and recruitment is nearly continuous.
- Retain the A-DMIC no-intervention decision for noisy missing data.
- Develop a new sparse-specialist architecture using feature selection, sparse-native linear models and calibrated routing.

## PCEEC evidence boundary

- Accuracy, reliability and stability evidence remain developmental.
- Active-model count is a compute proxy, not direct electrical energy.
- Electrical energy and direct monetary cost were not measured.
- No PCEEC level 4 or 5 claim is made from this experiment alone.
