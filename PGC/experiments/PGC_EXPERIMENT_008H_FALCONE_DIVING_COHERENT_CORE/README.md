# PGC Experiment 008H: Falcone Diving Coherent Core Conduit

## Status

Completed trial evidence. Not publication evidence.

## Protected core

Braided ZMI remained the protected core throughout. Coherent axial recruitment and the diving pulse were permitted to augment it only when validation-selected conditions were met. Pull-out rollback returned the decision to Braided ZMI whenever the proposed boost increased uncertainty.

## Design

- datasets: Breast Cancer Wisconsin, Wine and Digits
- ten fixed seeds per dataset
- 60% training, 20% validation and 20% protected test
- protected-test labels excluded from tuning
- five model cores: logistic regression, random forest, support vector classifier, Extra Trees and histogram gradient boosting

## Arms

1. Braided ZMI protected core
2. Coherent axial boost without pull-out protection
3. Falcone diving pulse with validation-selected activation and entropy-based pull-out

## Aggregate protected-test results

| Arm | Mean accuracy | Macro-F1 | Balanced accuracy | Log loss | Rescues | Harms | Net rescue | Worst-case accuracy |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Braided ZMI core | **0.976472** | **0.975515** | **0.974306** | 0.133232 | 0 | 0 | 0 | 0.929825 |
| Coherent axial boost | 0.975546 | 0.974659 | 0.973512 | 0.133995 | 0 | 1 | -1 | 0.929825 |
| Falcone diving pulse | **0.976472** | **0.975515** | **0.974306** | **0.133231** | 0 | 0 | 0 | 0.929825 |

## Interpretation

The unprotected coherent axial boost caused one harm on the Wine dataset and reduced aggregate accuracy. The Falcone diving pulse detected insufficient validated gain, pulled out, and preserved the Braided ZMI decision. It therefore matched the protected core while marginally improving log loss.

This trial supports the pull-out and rollback mechanism, but it does not yet show an accuracy improvement. The average coherence estimate was low, approximately 0.264, which indicates that the recruited layers were not sufficiently aligned to justify a concentrated dive in most cases.

The next refinement should improve the coherence representation and trigger the diving pulse only within validated hard-case regions where at least one specialist has demonstrated unique rescue capability.
