# PGC Experiment 008M: Rail-Guided Braided Core

## Status

Protocol locked for execution.

## Governing principle

The protected Braided ZMI core remains the main line. Fish-Net ZMI and specialist conduits act as adaptive junctions, sidings and express tracks. Guidance is structured, but route selection is case-dependent.

## Architecture

```text
Adaptive entry station
        ↓
Fish-Net ZMI sorting junction
        ↓
Case-dependent rail switching
        ↓
Braided ZMI main line
        ↓
Protected output or rollback
```

## Railway mapping

- Main line: Braided ZMI protected core
- Junctions and points: Fish-Net ZMI local influence switches
- Express track: high-confidence specialist route
- Passing loop: parallel comparison of two competent routes
- Siding: unresolved or low-confidence hypothesis retention
- Signal block: prevents conflicting routes entering the core simultaneously
- Buffer stop: rollback and overshoot protection
- Temporary track: short-lived case-specific route that dissolves after inference

## Routing rule

For each case, route selection maximises:

`ExpectedAccuracyGain - 2 x ExpectedHarm - SwitchingCost - InstabilityPenalty`

The main line remains the default when no alternative track demonstrates positive net utility.

## Experiment arms

1. Braided ZMI core
2. Adaptive entry-profile Combi anchor
3. Fixed rail-guided core
4. Validation-selected junction routing
5. Case-adaptive rail switching
6. Dynamic temporary-track generation
7. Passing-loop parallel comparison
8. Rail-guided core with signal-block conflict prevention
9. Complete rail-guided braided core with rollback
10. Free-flight no-rail control

## Validation design

- identical datasets, seeds and splits to Experiment 008L
- all switch thresholds selected on validation data only
- protected-test labels excluded from tuning
- paired case-level comparison against Braided ZMI and adaptive-entry Combi
- report accuracy, macro-F1, balanced accuracy, log loss, rescues, harms, net rescue, switching rate and worst-seed accuracy

## Promotion criteria

The rail-guided architecture is promoted only if it:

- exceeds the adaptive-entry Combi accuracy benchmark of 0.978645
- preserves or improves worst-case accuracy of 0.938596
- produces positive net rescue
- does not materially increase harms
- preserves or improves calibration
- shows reproducible gain across datasets and seeds

## Locked interpretation

The rail guides information flow but does not predetermine the destination. Junctions adapt to local evidence, while Braided ZMI remains the protected axial main line.
