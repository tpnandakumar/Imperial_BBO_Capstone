# PGC Experiment 008: DVCSE MADVT

## Status

Historical in-session evidence restored from screenshots supplied by the user. The original executable code, complete per-run dataframe and probability arrays were not recovered from the repository or File Library.

This record must therefore be treated as **screenshot-supported historical trial evidence**, not as an independently reproduced run.

## Main verified result

The best overall arm reported in the original run was:

**Fusion Anchor without dynamic vectoring**

- mean protected-test accuracy: **0.986126**
- dynamic vectoring: neutral for the Fusion Anchor

## Other reported findings

- Dynamic vectoring produced a small positive net gain only for Rankine cruise.
- Dynamic vectoring was neutral for Fusion Anchor, Navier processing and dynamic scramjet.
- Dynamic vectoring slightly harmed fixed hybrid.
- No model reached 0.9999 mean protected-test accuracy across all datasets.

## Selective performance

Selective accuracy was reported separately from full-coverage accuracy:

- dynamic scramjet: approximately **0.999588** selective accuracy at approximately **0.6091** coverage
- Fusion Anchor: approximately **0.999543** selective accuracy at approximately **0.2336** coverage

These values must not be described as full-coverage mean protected-test accuracy.

## Evidence integrity

The screenshots confirm the aggregate findings above, but do not provide enough information to reconstruct the exact per-run CSV faithfully. No synthetic or inferred per-run values have been created.

## Successor experiment

The exact successor protocol is stored at:

`PGC/experiments/PGC_EXPERIMENT_008R_LASER_ACCELERATED_DVCSE_FUSION_ANCHOR/PROTOCOL.md`

Execution of that successor requires recovery of the original DVCSE Fusion Anchor implementation or its validation and protected-test probability outputs.
