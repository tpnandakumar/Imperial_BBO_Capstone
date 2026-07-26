# PGC Experiment 008R: Laser-Focused Accelerated DVCSE Fusion Anchor

## Status

Protocol locked. Execution pending recovery of the original DVCSE_MADVT Fusion Anchor implementation or its saved per-run probability outputs.

## Verified parent evidence

The parent DVCSE_MADVT experiment recorded a Fusion Anchor mean protected-test accuracy of 0.986126 without dynamic vectoring. This result is preserved as historical in-session evidence from screenshots, but the original executable code, per-run dataframe and exact probability outputs are not currently present in the repository.

## Governing rule

Do not reconstruct or substitute the 0.986126 anchor with the later five-model mean Fusion Anchor. The rerun must use the exact original DVCSE_MADVT anchor or its stored out-of-fold and protected-test probabilities.

## Architecture

```text
DVCSE Fusion Anchor
        ↓
Class-conditional laser targeting lens
        ↓
Homing-beacon target confidence
        ↓
Focused acceleration to case-specific Vmax
        ↓
A0 maintenance thrust
        ↓
Dynamic distance-aware soft deceleration
        ↓
Terminal micro-guidance
        ↓
Protected rollback to DVCSE Fusion Anchor
```

## Experimental arms

1. DVCSE Fusion Anchor
2. Laser target only
3. Laser target with class-conditional harm gate
4. Focused acceleration to Vmax
5. Vmax plus A0 maintenance thrust
6. Dynamic soft deceleration
7. Terminal micro-guidance
8. Full laser-focused accelerated DVCSE Fusion Anchor

## Validation constraints

- use the original DVCSE_MADVT datasets, splits, seeds and model pool
- use validation-only threshold and control selection
- keep protected-test labels frozen
- report paired case-level rescues and harms
- preserve the original full-coverage metric definition
- report selective accuracy separately from full-coverage accuracy

## Primary promotion criteria

The full architecture is promoted only if it:

- exceeds mean protected-test accuracy of 0.986126
- preserves or improves the parent worst-case accuracy
- produces positive net rescue
- avoids material increase in harms
- preserves or improves log loss
- does not obtain gain by reducing coverage

## Required recovery artefacts

At least one of the following is required before execution:

- original DVCSE_MADVT Python experiment code
- original per-run prediction dataframe
- original validation and protected-test probability arrays
- exact serialised model and split configuration sufficient to reproduce the 0.986126 anchor

## Evidence integrity statement

The protocol is executable only after recovery of the original parent anchor. Running the later 0.976287 Fusion Anchor under this name would be an invalid substitution and is prohibited.
