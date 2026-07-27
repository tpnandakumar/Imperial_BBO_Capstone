# PGC Experiment 008L: Launch-Supported Free-Flight Combi Conduit

## Status

Completed trial evidence. Not publication evidence.

## Research question

Does an initiating physics-inspired scaffold improve generalisation, then inhibit accuracy if retained after the data support free-form flight?

The experiment separated two factors:

1. scaffold authority, fixed versus progressively released
2. entry-flow profile, fixed versus case-adaptive

## Design

- datasets: Breast Cancer Wisconsin, Wine and Digits
- ten fixed seeds per dataset
- 60% training, 20% validation and 20% protected test
- protected-test labels excluded from tuning
- five model cores: logistic regression, random forest, support vector classifier, Extra Trees and histogram gradient boosting
- Braided ZMI used as the protected reference

## Aggregate protected-test results

| Arm | Mean accuracy | Macro-F1 | Balanced accuracy | Log loss | Rescues | Harms | Net rescue | Worst-case accuracy |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Braided ZMI | 0.977690 | 0.976703 | 0.975629 | 0.133256 | 0 | 0 | 0 | 0.929825 |
| Fixed launch scaffold | 0.978445 | 0.977499 | 0.976497 | 0.137232 | 11 | 5 | +6 | 0.938596 |
| **Adaptive entry profile** | **0.978645** | **0.977713** | **0.976630** | 0.135946 | 8 | 2 | **+6** | **0.938596** |
| Progressive release, fixed profile | 0.978445 | 0.977499 | 0.976497 | 0.137232 | 11 | 5 | +6 | 0.938596 |
| Progressive release, adaptive profile | **0.978645** | **0.977713** | **0.976630** | 0.135946 | 8 | 2 | **+6** | **0.938596** |
| Reversible release | **0.978645** | **0.977713** | **0.976630** | 0.135946 | 8 | 2 | **+6** | **0.938596** |
| Free flight without scaffold | 0.976287 | 0.975342 | 0.974281 | 0.131531 | 1 | 5 | -4 | 0.929825 |
| Rollback-protected launch/free flight | 0.977690 | 0.976706 | 0.975629 | **0.131205** | 1 | 1 | 0 | 0.929825 |

## Scaffold-release finding

The mean validation-selected release strength was 0.0 for both fixed and adaptive entry profiles.

This means the validation process consistently retained the launch scaffold. Progressive release, reversible release and their corresponding non-release forms therefore produced the same protected-test decisions.

## Dataset-specific findings

- Breast Cancer Wisconsin improved from 0.961404 with Braided ZMI to 0.963158 with the adaptive entry profile.
- Digits improved from 0.982778 to 0.983889 with the adaptive entry profile. The fixed launch scaffold reached 0.984167.
- Wine remained unchanged at 0.988889 under the structured launch models.
- Free flight without the scaffold reduced performance on all three datasets.

## Interpretation

The initiating structure did not inhibit accuracy in this matched trial. The strongest result came from retaining the scaffold while adapting the radial entry-flow profile case by case.

The no-scaffold free-flight control produced one rescue and five harms, giving a net rescue of minus four. This indicates that removing the structure introduced harmful route changes more often than useful corrections.

The adaptive entry profile improved mean accuracy by 0.0955 percentage points over Braided ZMI and improved worst-case accuracy from 0.929825 to 0.938596. The gain came from adapting how evidence entered the scaffold, not from releasing the scaffold.

## Current conclusion

> Initial structure supports accuracy. The entry-flow profile should adapt freely, but scaffold release should occur only when stronger validation evidence appears.

The current provisional anchor is the adaptive-entry Combi Conduit, with Braided ZMI retained as the internal rollback state.
