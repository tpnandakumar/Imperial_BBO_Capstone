# PGC Experiment 008D: Wrapped Accuracy-Determined Free-Form Conduit

## Status

Completed trial evidence. Not publication evidence.

## Design

This experiment wrapped the matched Experiment 008C fusion anchor rather than replacing it. Three arms were compared across Breast Cancer Wisconsin, Wine and Digits, using ten fixed seeds, a 60% training split, 20% validation split and 20% protected test split.

The protected-test labels were excluded from all tuning and gate selection.

## Arms

1. Fusion anchor
2. Single wrapped conduit with a validation-selected benefit gate
3. Double wrapped conduit with a benefit gate and an additional harm gate

## Aggregate protected-test results

| Arm | Mean accuracy | Macro-F1 | Balanced accuracy | Log loss | Intervention rate | Rescues | Harms | Net rescue | Worst-case accuracy |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Fusion anchor | 0.976287 | 0.975342 | 0.974281 | 0.131531 | 0.000000 | 0 | 0 | 0 | 0.929825 |
| Single wrapped conduit | **0.977398** | **0.976368** | **0.975232** | 0.131603 | 0.292714 | 5 | 2 | **+3** | 0.929825 |
| Double wrapped conduit | 0.976472 | 0.975514 | 0.974306 | **0.129695** | 0.112997 | 3 | 1 | +2 | 0.929825 |

## Interpretation

The single wrapped conduit achieved the highest matched accuracy and produced five rescues against two harms. The double wrapper intervened less often and achieved the best log loss, but its stricter harm gate blocked one net rescue and therefore reduced the final accuracy gain.

The result supports the wrapped-conduit principle. A protected anchor can be improved by selective adaptive intervention. It also shows that a second safety gate must be calibrated carefully because excessive conservatism can suppress valid rescues.

This experiment used the Experiment 008C model pool and split design. It does not yet recreate the separate earlier 0.986126 fusion-anchor benchmark exactly, so it cannot be used to claim that the previous project best has been surpassed.
