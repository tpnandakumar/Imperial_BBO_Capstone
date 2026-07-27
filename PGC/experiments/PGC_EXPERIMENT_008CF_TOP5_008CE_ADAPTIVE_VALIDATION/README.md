# PGC Experiment 008CF: Top Five Engines with 008CE Adaptive Controller

## Status

Completed fresh matched comparative development experiment. This is not final independent confirmation.

## Design

Five selected candidate configurations were tested in their existing form and with the full 008CE adaptive controller:

- ECSP 3-model baseline
- ECSP 11-model ILS-H
- AX-R-BK 11-model ILS-H
- DTRRR protected stochastic 3-model baseline
- AX-R-BK 3-model FBW-PVF

The evaluation used breast cancer, wine and digits, 10 matched seeds and 10 repeats per seed. Each candidate and mode received 100 aggregate evaluations. Holdout labels were excluded from controller decisions.

The 008CE controller incorporated:

- development-only intervention-benefit prediction
- stack-aware targeting
- progressive model recruitment
- measured-oscillation stability spin
- direct latency and resident-memory measurement

Electrical energy and monetary cost were not measured and are not estimated.

## Adaptive ranking

| Rank | Candidate | Median | Mean | Minimum | SD | Active models | NRE | Mean latency |
|---:|---|---:|---:|---:|---:|---:|---:|---:|
| 1 equal | ECSP 11 + ILS-H | 0.983821 | 0.984698 | 0.977973 | 0.005080 | 10.948 | 0.573644 | 59.27 ms |
| 1 equal | ECSP 3 baseline | 0.983285 | 0.984250 | 0.972710 | 0.005713 | 3.325 | 0.853491 | 44.90 ms |
| 3 | DTRRR PS 3 baseline | 0.981823 | 0.981157 | 0.970712 | 0.007245 | 3.317 | 0.853799 | 41.21 ms |
| 4 | AX-R-BK 3 + FBW-PVF | 0.982895 | 0.984051 | 0.966228 | 0.004793 | 5.218 | 0.782472 | 40.18 ms |
| 5 | AX-R-BK 11 + ILS-H | 0.983821 | 0.983778 | 0.968713 | 0.006545 | 10.994 | 0.571788 | 52.90 ms |

## Main finding

Two systems tied on the composite multi-objective score:

- ECSP 11 + ILS-H delivered the strongest accuracy floor and highest mean accuracy.
- ECSP 3 baseline delivered nearly the same mean accuracy with about one third of the active models and much higher Net Regenerative Efficiency.

For deployment, ECSP 3 with 008CE adaptive escalation is the strongest balance of accuracy, efficiency, versatility and cost proxy. ECSP 11 + ILS-H remains the accuracy and floor ceiling.

## Controller behaviour

The sparse ECSP candidate recruited a specialist on approximately 4.9% of samples and the full stack on approximately 4.1%. Its mean active-model count remained 3.325.

The dense ECSP candidate required full recruitment on only approximately 3.1% of samples, but its base route already used nearly all models.

Stability spin activation remained below measured oscillation in every candidate, satisfying the 008CE control constraint.

## Evidence boundary

The measured latency values include controller fitting and application within the notebook runtime and are not deployment benchmarks. Resident-memory changes were small and process-dependent. Electrical energy and monetary inference cost remain unmeasured.
