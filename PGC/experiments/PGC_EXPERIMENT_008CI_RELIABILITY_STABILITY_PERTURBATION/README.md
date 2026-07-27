# PGC Experiment 008CI: Reliability, Stability and Perturbation Validation

## Status

Completed comparative development experiment. This is not final independent confirmation.

## Design

- promoted A-DMIC gated temporal specialist versus three-model reference
- 10 fresh seeds
- 6 test conditions
- 120 arm-runs
- 60% temporal training, 20% temporal validation and 20% protected temporal test
- zero overlap between all partitions
- protected test labels were not used for fitting, blend selection or gate selection
- A-DMIC Computational Milieu Intérieur preserved throughout

## Test conditions

1. clean
2. Gaussian noise
3. missing-value injection
4. outlier injection
5. feature-scale shift
6. intensified temporal drift

## Main result

The A-DMIC gated temporal route improved accuracy in all 60 matched seed-condition comparisons.

| Condition | Mean reference accuracy | Mean gated accuracy | Mean gain | Wins | Paired p |
|---|---:|---:|---:|---:|---:|
| Clean | 0.583571 | 0.649286 | 0.065714 | 10/10 | 0.001953 |
| Gaussian noise | 0.588095 | 0.649286 | 0.061190 | 10/10 | 0.001953 |
| Missingness | 0.572857 | 0.638810 | 0.065952 | 10/10 | 0.001953 |
| Outliers | 0.581667 | 0.649048 | 0.067381 | 10/10 | 0.001953 |
| Feature-scale shift | 0.601429 | 0.646667 | 0.045238 | 10/10 | 0.001953 |
| Intensified temporal drift | 0.623810 | 0.670714 | 0.046905 | 10/10 | 0.001953 |

## Stability findings

- The gated route retained a higher minimum accuracy in every condition.
- Accuracy variability was lower than the reference in five of six conditions.
- No invalid probability state was released.
- Rollback success was 100% in the implemented control checks.
- Homeostatic restoration was recorded as 100% after temporary state release and garbage collection.

## Important evidence limit

The rollback and homeostatic checks in this experiment are software-control checks, not hardware-level proof of full resource reclamation. Direct electrical energy and direct monetary cost were not measured. Active models, latency and memory remain computational-efficiency indicators only.

## Decision

Promote the A-DMIC gated temporal specialist to the energy-regeneration and cost-efficiency experiment. Reliability and perturbation robustness are strongly supported within this synthetic temporal-drift benchmark family. Independent external datasets remain necessary before a final PCEEC level is assigned.
