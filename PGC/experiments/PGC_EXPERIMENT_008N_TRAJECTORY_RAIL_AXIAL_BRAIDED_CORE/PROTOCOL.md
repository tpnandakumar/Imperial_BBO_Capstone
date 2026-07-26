# PGC Experiment 008N: Trajectory-Focused Dynamic Railroad Central Axial Braided Core

## Status

Protocol locked for execution.

## Governing principle

The system optimises the complete route trajectory towards the most accurate stable endpoint, rather than selecting only the next local junction.

The protected Braided ZMI core forms the central axial main line. Dynamic railroad guidance plans, evaluates and updates the route taken by each case.

## Architecture

```text
Adaptive entry station
        ↓
Trajectory estimation
        ↓
Dynamic railroad network
        ↓
Case-dependent junction control
        ↓
Central axial Braided ZMI core
        ↓
Protected destination or rollback
```

## Core components

### Central axial Braided core

- protected Braided ZMI decision state
- stable axial direction
- default main line
- final rollback state

### Dynamic railroad layer

- main line for stable high-confidence flow
- express tracks for validated specialist dominance
- passing loops for parallel comparison
- sidings for unresolved hypotheses
- temporary tracks for case-specific rescue routes
- switch points controlled by local competence
- signal blocks preventing route conflict
- buffer stops preventing overshoot and harmful commitment

### Trajectory controller

The controller evaluates a route sequence:

`T(x) = [entry, switch_1, switch_2, ..., axial_core, destination]`

and maximises:

`TrajectoryUtility = ExpectedFinalAccuracy - 2 x ExpectedHarm - SwitchingCost - Instability - RouteLengthPenalty`

## Dynamic trajectory behaviour

The selected trajectory may:

- remain on the axial main line
- enter an express specialist route
- use a passing loop for comparison
- divert into a siding while uncertainty persists
- return to the main line
- generate a temporary track
- close an unproductive route
- revise its destination when new evidence appears

## Experiment arms

1. Braided ZMI axial core
2. Adaptive-entry Combi anchor
3. Rail-guided Braided core with local switches only
4. Trajectory-planned railroad core
5. Trajectory-planned core with passing loops
6. Trajectory-planned core with sidings and delayed commitment
7. Dynamic temporary-track generation
8. Signal-block conflict prevention
9. Full trajectory-focused dynamic railroad axial Braided core
10. Free-form no-rail control

## Validation design

- identical datasets, seeds and splits to Experiment 008L
- all trajectory parameters learned on validation data only
- protected-test labels excluded from tuning
- paired case-level comparison against Braided ZMI and adaptive-entry Combi
- report accuracy, macro-F1, balanced accuracy, log loss, rescues, harms, net rescue, switch count, path length, intervention rate and worst-seed accuracy

## Promotion criteria

The architecture is promoted only if it:

- exceeds mean protected-test accuracy of 0.978645
- preserves or improves worst-case accuracy of 0.938596
- produces positive net rescue
- avoids material increase in harms
- preserves or improves calibration
- reduces unnecessary route switching
- demonstrates reproducible gain across datasets and seeds

## Locked interpretation

The railroad provides adaptive guidance, but the central Braided ZMI core remains the protected axis. Accuracy determines the full trajectory, while the rail network constrains unsafe drift and preserves rollback.
