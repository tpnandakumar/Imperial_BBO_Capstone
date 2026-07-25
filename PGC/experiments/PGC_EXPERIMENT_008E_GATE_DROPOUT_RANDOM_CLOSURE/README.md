# PGC Experiment 008E: Gate Dropout with Secondary and Tertiary Random Closure

## Status

Completed trial evidence. Not publication evidence.

## Design

The fusion anchor remained permanently open. A benefit gate was trained with feature dropout augmentation. Secondary and tertiary conduits were randomly closed and reopened across 25 masked passes. Consensus was then used to determine whether auxiliary routing should replace the anchor.

The experiment used Breast Cancer Wisconsin, Wine and Digits, ten fixed seeds, a 60% training split, 20% validation split and 20% protected test split. Protected-test labels were excluded from tuning.

## Aggregate protected-test results

| Arm | Mean accuracy | Macro-F1 | Balanced accuracy | Log loss | Rescues | Harms | Net rescue | Worst-case accuracy |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Fusion anchor | **0.976087** | **0.975107** | **0.973977** | 0.131571 | 0 | 0 | 0 | 0.929825 |
| Gate dropout only | 0.975687 | 0.974679 | 0.973702 | **0.130246** | 3 | 3 | 0 | 0.929825 |
| Random closure consensus | **0.976087** | **0.975107** | **0.973977** | 0.132905 | 0 | 0 | 0 | 0.929825 |
| Combined gate dropout plus closure | **0.976087** | **0.975107** | **0.973977** | 0.132905 | 0 | 0 | 0 | 0.929825 |

## Interpretation

Gate dropout improved log loss but did not improve accuracy. It produced three rescues and three harms, giving zero net rescue and a small reduction in mean accuracy.

The random closure consensus was too conservative. It preserved the anchor decisions almost completely and therefore protected accuracy, but it generated no additional rescues.

The result suggests that random closure should not be used as a hard consensus barrier. The next refinement should use dynamic reopening pressure, route-specific closure probabilities and a soft consensus score that augments rather than blocks the benefit gate.
