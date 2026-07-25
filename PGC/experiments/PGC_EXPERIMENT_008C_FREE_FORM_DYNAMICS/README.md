# PGC Experiment 008C: Accuracy-Determined Free-Form Dynamics

## Status

Completed trial evidence. Not publication evidence.

## Governing principle

Accuracy decides geometry. Geometry is not fixed in advance.

The controller learns case-specific model competence, produces continuous free-form route weights, permits no intervention, and rolls back to the fusion anchor when validation evidence is insufficient.

## Design

- datasets: Breast Cancer Wisconsin, Wine and Digits
- ten fixed seeds per dataset
- 60% training, 20% validation and 20% protected test
- protected-test labels excluded from tuning and gating
- five base models: logistic regression, random forest, support vector classifier, Extra Trees and histogram gradient boosting
- intervention parameters selected on validation data and frozen before protected testing

## Aggregate protected-test results

| Arm | Accuracy | Macro-F1 | Balanced accuracy | Log loss | Worst-case accuracy |
|---|---:|---:|---:|---:|---:|
| Fusion anchor | 0.976287 | 0.975342 | 0.974281 | 0.131531 | 0.929825 |
| Free-form dynamic geometry | **0.977398** | **0.976381** | **0.975232** | **0.129498** | 0.929825 |

## Intervention behaviour

- mean intervention rate: 0.0568
- total rescues: 4
- total harms: 1
- net rescue: +3
- mean effective routes: 4.63
- mean laminarity index: 0.7963

## Dataset-specific results

| Dataset | Fusion anchor | Free-form dynamic geometry |
|---|---:|---:|
| Breast cancer | 0.960526 | 0.960526 |
| Wine | 0.986111 | **0.988889** |
| Digits | 0.982222 | **0.982778** |

## Interpretation

The free-form controller improved mean accuracy, macro-F1, balanced accuracy and log loss while intervening in only about 5.7% of protected-test cases. It produced four rescues and one harm, giving positive net rescue utility.

The gain is modest and the earlier Experiment 008 fusion-anchor benchmark of 0.986126 remains higher because the model pool and experimental setup were not identical. Therefore, this result demonstrates that accuracy-determined free-form adaptation can improve its matched anchor, but it does not establish overall superiority.

The next refinement should improve the competence estimator, preserve stronger laminarity, and test cross-fitted gating on harder datasets.
