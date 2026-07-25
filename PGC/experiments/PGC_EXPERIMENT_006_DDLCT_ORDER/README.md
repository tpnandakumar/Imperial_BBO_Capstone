# PGC Experiment 006: DDLCT Order Comparison

## Objective

Compare three matched Dynamic Dual Live Co-ordinated Tuning sequences:

1. Accuracy then laminarity
2. Laminarity then accuracy
3. Simultaneous DDLCT

All arms used identical data generation, seeds, train-validation-protected-test separation, tuning grades and protected-test governance.

## Design

- 20 fixed seeds
- 60% training, 20% validation and 20% protected test
- no protected-test label feedback
- identical tuning budget across all DDLCT variants
- validation gain safeguard retained
- trial evidence only

## Aggregate protected-test results

| Arm | Accuracy | Macro-F1 | Balanced accuracy | Worst-seed accuracy | Laminarity |
|---|---:|---:|---:|---:|---:|
| Fusion anchor | 0.9854 | 0.9867 | 0.9877 | 0.9583 | not applicable |
| Accuracy then laminarity | **0.9867** | **0.9879** | **0.9885** | **0.9667** | 0.9905 |
| Laminarity then accuracy | 0.9858 | 0.9871 | 0.9880 | 0.9583 | **0.9968** |
| Simultaneous DDLCT | 0.9858 | 0.9871 | 0.9880 | 0.9583 | **0.9968** |

Urgent-threat recall remained 1.0000 and false-escalation rate remained 0.0000 in all arms.

## Interpretation

Accuracy then laminarity produced the highest mean accuracy, macro-F1, balanced accuracy and worst-seed accuracy. Laminarity then accuracy and simultaneous DDLCT produced slightly smoother threshold trajectories but did not match the accuracy-first sequence.

The observed order effect was small:

`accuracy-first minus laminarity-first = 0.0008333`

This is initial trial evidence of a possible order effect, not proof of superiority. The next stage must repeat all three variants across multiple datasets and multiple cognitive domains.

## Next stage

PGC Experiment 007 will create a multi-domain, multi-dataset validation matrix covering numerical, language, vision, temporal, memory and integrated multimodal tasks. The same three DDLCT sequences will be retained so that domain-general order effects can be measured directly.

## Evidence status

Trial evidence only. Not publication evidence.
