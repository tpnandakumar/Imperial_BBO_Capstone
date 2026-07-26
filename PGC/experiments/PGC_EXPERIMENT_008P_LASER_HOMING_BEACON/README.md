# PGC Experiment 008P: Laser-Targeted Homing Beacon Bullet Train Conduit

## Status

Completed trial evidence. Not publication evidence.

## Protected anchor

The adaptive-entry Combi Conduit remained the protected anchor. The experimental layers added a laser targeting lens, homing beacon quality estimate, acceleration to case-specific Vmax, A0 maintenance thrust, dynamic precision deceleration, terminal micro-guidance and rollback.

## Design

- datasets: Breast Cancer Wisconsin, Wine and Digits
- ten fixed seeds per dataset
- 60% training, 20% validation and 20% protected test
- protected-test labels excluded from tuning
- five model cores: logistic regression, random forest, support vector classifier, Extra Trees and histogram gradient boosting

## Arms

1. Adaptive-entry Combi anchor
2. Laser targeting lens
3. Homing Vmax acceleration
4. A0 maintenance thrust
5. Dynamic precision deceleration
6. Terminal micro-guidance
7. Full laser homing-beacon conduit

## Aggregate protected-test results

| Arm | Mean accuracy | Macro-F1 | Balanced accuracy | Log loss | Rescues | Harms | Net rescue | Worst-case accuracy |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Adaptive-entry Combi anchor | 0.978645 | 0.977713 | 0.976630 | 0.135946 | 0 | 0 | 0 | 0.938596 |
| Laser targeting lens | 0.978246 | 0.977270 | 0.976193 | **0.134098** | 4 | 4 | 0 | 0.929825 |
| Homing Vmax acceleration | 0.978645 | 0.977713 | 0.976630 | 0.135705 | 0 | 0 | 0 | 0.938596 |
| A0 maintenance thrust | 0.978645 | 0.977713 | 0.976630 | 0.135705 | 0 | 0 | 0 | 0.938596 |
| Dynamic precision deceleration | 0.978645 | 0.977713 | 0.976630 | 0.134830 | 0 | 0 | 0 | 0.938596 |
| Terminal micro-guidance | 0.978645 | 0.977713 | 0.976630 | 0.134819 | 0 | 0 | 0 | 0.938596 |
| Full laser homing-beacon conduit | 0.978645 | 0.977713 | 0.976630 | 0.134408 | 0 | 0 | 0 | 0.938596 |

## Dataset-specific findings

- Breast Cancer Wisconsin: the raw laser targeting lens caused two net harms.
- Digits: the raw laser targeting lens produced two net rescues.
- Wine: all protected variants preserved the anchor result.

## Interpretation

The targeting lens found potentially useful alternative endpoints, but its class changes were not yet reliable across domains. It rescued four cases and harmed four, producing zero net rescue and lower worst-case accuracy.

The homing, acceleration, thrust, deceleration and terminal-guidance layers successfully suppressed unsafe class changes while improving probability quality. The full conduit preserved the anchor accuracy and improved log loss from 0.135946 to 0.134408.

The experiment did not exceed the previous focused-acceleration benchmark of 0.978738. The next refinement should make the beacon domain-conditional and class-conditional, so that the successful Digits guidance is retained while the harmful Breast Cancer guidance is blocked.

## Current conclusion

The laser-homing architecture is useful as a calibration and targeting shell, but not yet as an unrestricted decision-changing controller.
