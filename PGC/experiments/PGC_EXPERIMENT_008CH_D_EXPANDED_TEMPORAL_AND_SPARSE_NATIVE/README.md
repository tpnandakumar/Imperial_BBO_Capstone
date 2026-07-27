# PGC Experiment 008CH-D: Expanded Temporal and Sparse-Native Validation

## Status

Completed comparative development experiment. This is not final independent confirmation.

## Design

- two targeted conditions
- ten fresh seeds
- 60 arm-runs
- 60% training, 20% validation and 20% protected test
- zero overlap between all partitions
- protected test labels were not used for selection, blending or gating
- A-DMIC Computational Milieu Intérieur preserved throughout

## Temporal-drift result

The temporal specialist produced a strong and consistent improvement.

- reference mean accuracy: 0.577222
- A-DMIC gated mean accuracy: 0.659722
- mean gain: 0.082500
- wins: 10 of 10 seeds
- paired Wilcoxon p: 0.001953
- reference minimum accuracy: 0.536111
- gated minimum accuracy: 0.605556
- reference macro-F1: 0.576890
- gated macro-F1: 0.656208
- reference log loss: 0.745657
- gated log loss: 0.664095
- specialist activation: 59.0%
- mean active models: 3.59

This is statistically supported development evidence that the temporal-drift specialist improves accuracy and floor behaviour under the tested drift process.

## Sparse-native result

The redesigned sparse-native specialist did not produce a meaningful improvement.

- reference mean accuracy: 0.608056
- gated mean accuracy: 0.610833
- mean gain: 0.002778
- wins: 3
- ties: 6
- losses: 1
- paired Wilcoxon p: 0.625
- specialist activation: 37.8%
- mean active models: 3.38

The result is too small and statistically unsupported for promotion.

## Decision

- Promote temporal-drift gating to the integrated PCEEC candidate architecture.
- Do not promote the current sparse-native specialist.
- Retain A-DMIC gating because it achieved the temporal gain with lower model use than permanent specialist activation.
- Begin reliability, stability and energy-regeneration validation using the promoted temporal route.

## Evidence boundary

Electrical energy and direct monetary cost were not measured. Active-model count remains a computational-efficiency proxy. No PCEEC level 4 or 5 claim is made from this experiment alone.
