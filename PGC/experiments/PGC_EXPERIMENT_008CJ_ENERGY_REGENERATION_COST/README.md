# PGC Experiment 008CJ: Energy Efficiency, Regeneration and Cost Efficiency

## Status

Completed comparative development experiment. This is not final independent confirmation.

## Design

- three system arms
- five fresh seeds
- three workload conditions
- 45 arm-runs
- 15 repeated inference batches per arm
- 60% temporal training, 20% temporal validation and 20% protected temporal test
- zero overlap between all partitions
- protected test labels were not used for fitting, blend selection or gate selection
- A-DMIC Computational Milieu Intérieur preserved throughout

## Arms

1. three-model reference core
2. permanent four-model specialist
3. A-DMIC gated specialist

## Main findings

### Accuracy

The A-DMIC gated route improved mean accuracy over the reference core in all three workloads:

- clean: +0.045000
- missingness: +0.043333
- intensified temporal drift: +0.023333

The permanent specialist remained more accurate than the gated route:

- clean: gated lower by 0.030833
- missingness: gated lower by 0.026667
- intensified temporal drift: gated lower by 0.015833

### Computational efficiency

The gated route used substantially fewer active models than the permanent specialist:

- gated: approximately 3.32 active models
- permanent specialist: 4.00 active models

The gated route also reduced the normalised compute cost index relative to permanent activation for clean and intensified-drift workloads. Missingness produced near-equivalent cost, with the gated route slightly higher in this small run.

### Regeneration

- measured memory-recovery ratio: 1.00 in all arms and workloads
- worker-thread leak rate: 0%
- software-level recovery completed after every repeated inference route

These are software resource-recovery measurements, not hardware energy regeneration.

## Evidence boundary

- Electrical energy was not measured directly.
- Monetary cost in pounds was not measured.
- The reported cost measure is a transparent normalised compute cost index based on CPU time and observed RSS-time.
- Only five fresh seeds were used, so paired p-values are underpowered and no confirmatory significance claim is made.

## Decision

The A-DMIC gated route provides a useful middle operating point: better accuracy than the three-model reference, materially fewer active models than permanent specialist activation, complete software-level resource recovery and no worker leakage. It does not yet equal the permanent specialist accuracy ceiling. The next optimisation should improve gate sensitivity while preserving the lower compute profile.
