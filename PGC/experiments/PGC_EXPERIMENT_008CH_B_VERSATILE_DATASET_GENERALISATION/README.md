# PGC Experiment 008CH-B: Versatile Dataset Generalisation Panel

## Status

Completed comparative development experiment. This is not final independent confirmation.

## Design

- 7 new dataset conditions
- 3 independent seeds
- 21 completed runs
- 60% training, 20% validation and 20% protected test
- zero overlap between training, validation and test partitions
- protected test labels were not used for model or residual-correction selection
- A-DMIC Computational Milieu Intérieur preserved as the basal regulatory layer

## Dataset conditions

1. Iris small multiclass
2. Imbalanced binary classification
3. High-dimensional sparse classification
4. Noisy classification with missing values
5. Five-class multiclass classification
6. Nonlinear moons classification
7. Ordered temporal-drift classification

## Results

| Dataset | Median accuracy | Mean accuracy | Minimum accuracy | SD |
|---|---:|---:|---:|---:|
| Imbalanced binary | 0.975000 | 0.965278 | 0.937500 | 0.024414 |
| Iris small multiclass | 0.966667 | 0.966667 | 0.933333 | 0.033333 |
| Nonlinear moons | 0.916667 | 0.923611 | 0.916667 | 0.012028 |
| Five-class multiclass | 0.876923 | 0.871795 | 0.857692 | 0.012364 |
| Noisy missing binary | 0.795833 | 0.780556 | 0.737500 | 0.037807 |
| Temporal drift binary | 0.758333 | 0.758333 | 0.725000 | 0.033333 |
| High-dimensional sparse | 0.604545 | 0.577273 | 0.490909 | 0.076466 |

## Interpretation

The engine generalised strongly on imbalanced, small multiclass and nonlinear tasks. Performance remained moderate on noisy missing-data and temporal-drift tasks. The high-dimensional sparse condition exposed a major weakness and becomes a priority for specialist routing, sparse feature handling and stability optimisation.

## PCEEC evidence boundary

- Accuracy, reliability and stability evidence are comparative development results.
- Mean active models remained fixed at 3.0 for this panel.
- Latency and memory were measured as computational-efficiency indicators.
- Electrical energy was not directly measured.
- Direct monetary cost was not measured.
- No PCEEC level 4 or 5 claim is made from this experiment alone.

## Decision

Proceed to targeted remediation for high-dimensional sparse, noisy-missing and temporal-drift conditions before integrated PCEEC scoring.
