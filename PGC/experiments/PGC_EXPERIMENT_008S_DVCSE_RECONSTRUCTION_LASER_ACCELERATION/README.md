# PGC Experiment 008S: DVCSE Reconstruction with Laser Acceleration

## Status

Completed reconstruction trial. This is not a reproduction of the original DVCSE_MADVT experiment.

## Purpose

The original DVCSE_MADVT executable implementation was not recovered. This experiment therefore rebuilt five conceptually matched arms under the current frozen protocol:

- Fusion Anchor
- Navier processing
- Rankine cruise
- Dynamic scramjet
- Fixed hybrid

Each arm was tested with and without dynamic vectoring. A laser-targeted accelerated Fusion Anchor was also tested.

## Experimental design

- datasets: Breast Cancer Wisconsin, Wine and Digits
- ten fixed seeds per dataset
- 60% training, 20% validation and 20% protected test
- five base models: logistic regression, random forest, support vector classifier, Extra Trees and histogram gradient boosting
- all thresholds selected on validation data only
- protected-test labels excluded from tuning

## Aggregate protected-test results

| Model | Routing | Mean accuracy | Macro-F1 | Balanced accuracy | Log loss | Rescues | Harms | Net rescue | Worst-case accuracy |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **Fixed hybrid** | **With vectoring** | **0.978538** | **0.977616** | **0.976595** | 0.137131 | 1 | 0 | **+1** | **0.938596** |
| Laser-accelerated Fusion Anchor | Laser targeted | 0.978246 | 0.977285 | 0.976039 | **0.132203** | 4 | 3 | +1 | 0.938596 |
| Fixed hybrid | Without vectoring | 0.978246 | 0.977306 | 0.976364 | 0.136537 | 0 | 0 | 0 | 0.938596 |
| Navier processing | Without vectoring | 0.977861 | 0.976869 | 0.975863 | 0.131874 | 0 | 0 | 0 | 0.929825 |
| Fusion Anchor | Without vectoring | 0.977753 | 0.976735 | 0.975664 | 0.132152 | 0 | 0 | 0 | 0.929825 |
| Navier processing | With vectoring | 0.977276 | 0.976227 | 0.975067 | 0.132971 | 1 | 3 | -2 | 0.929825 |
| Fusion Anchor | With vectoring | 0.976891 | 0.975813 | 0.974592 | 0.133169 | 0 | 5 | -5 | 0.929825 |
| Rankine cruise | With vectoring | 0.975546 | 0.974728 | 0.973681 | 0.150896 | 2 | 2 | 0 | 0.916667 |
| Rankine cruise | Without vectoring | 0.975346 | 0.974500 | 0.973382 | 0.151106 | 0 | 0 | 0 | 0.916667 |
| Dynamic scramjet | With vectoring | 0.971555 | 0.970452 | 0.969265 | 0.160160 | 0 | 0 | 0 | 0.916667 |
| Dynamic scramjet | Without vectoring | 0.971555 | 0.970452 | 0.969265 | 0.169120 | 0 | 0 | 0 | 0.916667 |

## Interpretation

The reconstructed experiment did not reproduce the historical 0.986126 Fusion Anchor result. This confirms that the original DVCSE_MADVT implementation used materially different model definitions, routing logic, data preparation or evaluation conditions.

Within the reconstruction, dynamic vectoring improved the fixed hybrid by one rescue with no harms. It harmed the reconstructed Fusion Anchor and Navier processing. The laser-accelerated Fusion Anchor produced four rescues and three harms, giving a small positive net rescue but remaining below the best reconstructed fixed hybrid.

## Current conclusion

The reconstruction provides useful directional evidence but must not replace the historical DVCSE_MADVT record. The historical 0.986126 result remains the project maximum, pending exact reproduction from the original implementation.
