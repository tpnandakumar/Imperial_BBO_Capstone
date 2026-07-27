# PGC Experiment 008Q: Laser-Focused Accelerated Fusion Anchor

## Status

Completed trial evidence. Not publication evidence.

## Verified anchor

The exact matched Fusion Anchor used in Experiments 008C to 008F was reproduced as an unweighted mean of the five base-model probability outputs.

Mean protected-test accuracy: **0.976287**

This matches the stored Fusion Anchor evidence. The previously quoted value of 0.986126 was not found in the repository or local experiment files and is therefore not treated as verified.

## Design

- datasets: Breast Cancer Wisconsin, Wine and Digits
- ten fixed seeds per dataset
- 60% training, 20% validation and 20% protected test
- protected-test labels excluded from tuning
- five model cores: logistic regression, random forest, support vector classifier, Extra Trees and histogram gradient boosting

## Experimental stack

1. Fusion Anchor
2. Laser target only
3. Laser-focused acceleration
4. Laser acceleration with A0 maintenance thrust
5. Dynamic soft deceleration
6. Full laser-accelerated Fusion Anchor with protected rollback

## Aggregate protected-test results

| Arm | Mean accuracy | Macro-F1 | Balanced accuracy | Log loss | Rescues | Harms | Net rescue | Worst-case accuracy |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Fusion Anchor | 0.976287 | 0.975342 | 0.974281 | 0.131531 | 0 | 0 | 0 | 0.929825 |
| **Laser target only** | **0.978246** | **0.977270** | **0.976190** | **0.131982** | **13** | **3** | **+10** | 0.929825 |
| Laser-focused acceleration | 0.976287 | 0.975342 | 0.974281 | 0.131613 | 0 | 0 | 0 | 0.929825 |
| Laser acceleration with A0 thrust | 0.976287 | 0.975342 | 0.974281 | 0.131640 | 0 | 0 | 0 | 0.929825 |
| Dynamic soft deceleration | 0.976287 | 0.975342 | 0.974281 | 0.131640 | 0 | 0 | 0 | 0.929825 |
| Full laser-accelerated Fusion Anchor | 0.976287 | 0.975342 | 0.974281 | 0.131640 | 0 | 0 | 0 | 0.929825 |

## Dataset-specific findings

- Breast Cancer Wisconsin: laser target improved mean accuracy from 0.960526 to 0.961404, net rescue +1.
- Digits: laser target improved mean accuracy from 0.982222 to 0.984444, net rescue +8.
- Wine: laser target improved mean accuracy from 0.986111 to 0.988889, net rescue +1.

## Interpretation

The laser target itself substantially improved the verified Fusion Anchor, producing thirteen rescues and three harms. However, the acceleration controller was too conservative to move enough probability mass across decision boundaries. As a result, the accelerated and rollback-protected variants retained the original Fusion Anchor decisions.

The raw laser target reached 0.978246, which is better than the verified Fusion Anchor but remains below the current matched best of 0.978738 from focused and continuous acceleration applied to the adaptive-entry Combi anchor.

## Current conclusion

The Fusion Anchor benefits from laser retargeting, but not from the present acceleration schedule. The next refinement should preserve the laser target's positive net rescue while adding class-conditional harm gating rather than suppressing all decision changes.
