# PGC Experiment 008G: Braided ZMI Protected Core

## Status

Protocol locked for execution.

## Governing principle

Braided ZMI is the protected cognitive core. No augmentation may replace its prediction unless validation evidence demonstrates a positive expected rescue-minus-harm value.

## Protected core

The protected core consists of:

- multiple semi-independent model cores
- braided laminar coordination
- case-level Zones of Maximum Influence
- locally weighted core dominance
- no compulsory ripple propagation
- no compulsory conduit closure

The protected output is:

`p_core(x) = BraidedZMI(x)`

## Optional augmentation layers

The following layers operate outside the protected core:

1. domain-gated ripple capture
2. secondary and tertiary conduit closure and reopening
3. free-form adaptive routing
4. LLM specialist afterburner
5. emergent behaviour modulation
6. uncertainty and out-of-distribution detection

Each layer must produce an alternative prediction `p_aug(x)` and a predicted net utility.

## Intervention rule

An augmentation is accepted only when:

`PredictedRescue - 2 x PredictedHarm - ComputePenalty - InstabilityPenalty > threshold`

Otherwise:

`p_final(x) = p_core(x)`

## Rollback rule

Rollback to Braided ZMI occurs when any of the following is detected:

- augmentation confidence falls below the protected core
- ripple instability rises
- closure consensus becomes fragile
- out-of-distribution risk rises
- predicted harm exceeds predicted rescue
- calibration deteriorates

## Experiment arms

1. Fusion anchor
2. Braided ZMI protected core
3. Braided ZMI plus domain-gated ripple capture
4. Braided ZMI plus dynamic closure and reopening
5. Braided ZMI plus free-form routing
6. Braided ZMI plus LLM specialist
7. Braided ZMI plus emergent behaviour modulation
8. Complete wrapped augmentation system

## Validation design

- identical datasets, seeds and splits to the matched Experiment 008F protocol
- all augmentation thresholds selected on validation data only
- protected-test labels excluded from tuning
- paired comparison against Braided ZMI on every case
- report rescues, harms, net rescue, intervention rate, accuracy, macro-F1, balanced accuracy, log loss and worst-seed accuracy

## Promotion criteria

A candidate augmentation is promoted only when it:

- exceeds Braided ZMI mean protected-test accuracy
- produces positive net rescue
- causes no material loss in worst-case accuracy
- preserves or improves calibration
- repeats the gain across datasets and seeds
- demonstrates no protected-test leakage

## Locked architecture

```text
Braided ZMI protected core
        ↓
Accuracy and uncertainty sensing
        ↓
Optional augmentation generation
        ↓
Rescue-minus-harm prediction
        ↓
Independent safety check
        ↓
Accept augmentation or roll back to Braided ZMI
```

## Scientific interpretation

Braided ZMI is now the reference architecture. Ripple capture and other dynamic mechanisms are treated as conditional augmentations rather than core requirements.
