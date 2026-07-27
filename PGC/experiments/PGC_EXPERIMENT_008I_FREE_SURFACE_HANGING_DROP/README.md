# PGC Experiment 008I: Free-Surface Hanging-Drop Conduit

## Status

Completed trial evidence. Not publication evidence.

## Protected core

Braided ZMI remained the protected core. The hanging-drop layers were treated as pressure-curvature augmentations that could alter probabilities or form a narrow specialist neck, with rollback to the core when validated benefit was insufficient.

## Design

- datasets: Breast Cancer Wisconsin, Wine and Digits
- ten fixed seeds per dataset
- 60% training, 20% validation and 20% protected test
- protected-test labels excluded from tuning
- five model cores: logistic regression, random forest, support vector classifier, Extra Trees and histogram gradient boosting

## Arms

1. Braided ZMI protected core
2. Free-form routing with adaptive laminarity
3. Hanging-drop free-surface pressure-curvature control
4. Hanging-drop model with dynamic necking
5. Complete free-surface conduit with rollback

## Aggregate protected-test results

| Arm | Mean accuracy | Macro-F1 | Balanced accuracy | Log loss | Rescues | Harms | Net rescue | Worst-case accuracy |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Braided ZMI core | **0.977690** | **0.976703** | **0.975629** | 0.133256 | 0 | 0 | 0 | 0.929825 |
| Hanging-drop surface | **0.977690** | **0.976703** | **0.975629** | 0.133128 | 0 | 0 | 0 | 0.929825 |
| Hanging-drop dynamic necking | **0.977690** | **0.976702** | **0.975629** | 0.132947 | 0 | 0 | 0 | 0.929825 |
| Complete free-surface conduit | 0.976857 | 0.975928 | 0.974796 | **0.131585** | 1 | 1 | 0 | 0.929825 |
| Free-form adaptive laminarity | 0.976764 | 0.975836 | 0.974703 | 0.133215 | 0 | 1 | -1 | 0.929825 |

## Interpretation

The hanging-drop surface and dynamic-necking variants preserved the protected core accuracy while improving log loss. This means the free-surface formulation refined probability quality without changing most class decisions.

The complete free-surface conduit generated one rescue on Digits but one harm on Wine. The unrestricted switching rule therefore remained too permissive. The free-form adaptive-laminarity arm also caused one harm on Wine.

The best current design is Braided ZMI with a hanging-drop calibration shell and dynamic necking available as a probability refinement layer. Decision replacement should remain disabled until a domain-specific rescue gate can distinguish the successful Digits intervention from the harmful Wine intervention.

## Main conclusion

Allowing shape and laminarity to emerge improved calibration, but did not yet improve protected-test accuracy. The pressure-curvature model appears useful as a soft probability-shaping shell rather than as an independent decision-changing conduit.
