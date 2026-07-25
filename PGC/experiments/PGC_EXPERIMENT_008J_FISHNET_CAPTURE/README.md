# PGC Experiment 008J: Fish-Net Ripple and Bubble Capture Conduit

## Status

Completed trial evidence. Not publication evidence.

## Protected core

Braided ZMI remained permanently available as the protected core. The fish-net layer acted as a selective capture lattice around it. Only persistent, coherent and locally influential strands were transmitted inward.

## Design

- datasets: Breast Cancer Wisconsin, Wine and Digits
- ten fixed seeds per dataset
- 60% training, 20% validation and 20% protected test
- protected-test labels excluded from tuning
- five model cores: logistic regression, random forest, support vector classifier, Extra Trees and histogram gradient boosting

## Arms

1. Braided ZMI protected core
2. Fish-Net ZMI capture
3. Fish-Net ripple capture
4. Fish-Net bubble capture
5. Full Fish-Net capture

## Aggregate protected-test results

| Arm | Mean accuracy | Macro-F1 | Balanced accuracy | Log loss | Rescues | Harms | Net rescue | Worst-case accuracy |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Braided ZMI core | 0.977690 | 0.976703 | 0.975629 | 0.133256 | 0 | 0 | 0 | 0.929825 |
| **Fish-Net ZMI capture** | **0.977982** | **0.977034** | **0.976026** | 0.132432 | 1 | 0 | **+1** | **0.938596** |
| Fish-Net ripple capture | 0.977690 | 0.976703 | 0.975629 | 0.131250 | 0 | 0 | 0 | 0.929825 |
| Fish-Net full capture | 0.977690 | 0.976703 | 0.975629 | **0.130394** | 0 | 0 | 0 | 0.929825 |
| Fish-Net bubble capture | 0.977597 | 0.976609 | 0.975534 | 0.131467 | 1 | 2 | -1 | 0.929825 |

## Interpretation

Fish-Net ZMI capture was the strongest arm. It improved mean accuracy, macro-F1, balanced accuracy and worst-case accuracy, while producing one rescue and no harms.

Ripple and full capture improved probability quality but did not change decisions. Bubble capture was too permissive and caused two harms against one rescue.

The result supports a selective mesh in which ZMI knots control transmission. Ripple and bubble behaviour should remain external evidence signals rather than direct decision-changing pathways until domain-specific rescue gates are stronger.

## Main conclusion

The best current architecture is:

```text
Braided ZMI protected core
        ↓
Adaptive Fish-Net ZMI capture layer
        ↓
Persistent local knot reinforcement
        ↓
Selective inward transmission
        ↓
Rollback to Braided ZMI when capture utility is insufficient
```
