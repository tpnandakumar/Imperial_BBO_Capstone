# PGC Experiment 007, Multi-Domain Block A

## Scope

This first execution block tested the same DDLCT sequence variants across three structurally different CPU-manageable datasets:

1. Breast Cancer Wisconsin, binary clinical tabular classification
2. Wine, multiclass chemical tabular classification
3. Digits, image-derived handwritten digit feature classification

Each dataset used ten fixed seeds and a stratified 60% training, 20% validation and 20% protected-test split. No protected-test labels were used for tuning.

## Models forming the fusion anchor

- standardised logistic regression
- random forest
- standardised probabilistic support vector classifier

## Aggregate protected-test results

| Variant | Accuracy | Macro-F1 | Balanced accuracy | Log loss | Laminarity |
|---|---:|---:|---:|---:|---:|
| Fusion anchor | **0.9809** | **0.9802** | **0.9791** | 0.1290 | 1.0000 |
| Accuracy then laminarity | 0.9808 | 0.9800 | 0.9788 | 0.1157 | 0.8360 |
| Laminarity then accuracy | 0.9790 | 0.9782 | 0.9775 | **0.1014** | 0.6098 |
| Simultaneous DDLCT | 0.9790 | 0.9782 | 0.9775 | **0.1014** | 0.6098 |

## Dataset-specific accuracy

| Dataset | Anchor | Accuracy then laminarity | Laminarity then accuracy | Simultaneous |
|---|---:|---:|---:|---:|
| Breast cancer | **0.9684** | 0.9675 | 0.9632 | 0.9632 |
| Wine | **0.9917** | 0.9889 | 0.9889 | 0.9889 |
| Digits | 0.9825 | **0.9858** | 0.9850 | 0.9850 |

## Interpretation

The current DDLCT implementation does not yet provide domain-general accuracy superiority. Accuracy-first tuning improved the image-derived digits task, but slightly reduced performance on the breast-cancer and wine datasets. The reverse and simultaneous sequences improved probabilistic calibration, as reflected by lower log loss, but reduced mean accuracy.

This is an important negative and differentiating result. A single unconditional tuning sequence is not suitable across all domains. The next controller should use validation-derived domain and context gating:

- retain the fusion anchor when expected accuracy gain is weak
- activate accuracy-first honing only when validation rescue exceeds validation harm by a pre-registered margin
- prefer laminar or simultaneous tuning when calibration improves without material accuracy loss
- roll back automatically to the strongest validated state

## Next execution block

Block B will test a Domain-Conditional DDLCT selector. It will choose among anchor, accuracy-first, laminar-first and simultaneous control using validation data only, then freeze the selected route before protected-test evaluation.

## Evidence status

Trial evidence only. Not publication evidence.
