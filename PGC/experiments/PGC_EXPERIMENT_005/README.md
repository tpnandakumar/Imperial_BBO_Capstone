# PGC Experiment 005

## Dynamic Live Accuracy Honing

This trial tests DLAH-SDVGTC, Dynamic Live Accuracy Honing with Sequential Dynamic Variable-Grade Threshold Convergence.

## Design

- deterministic multimodal scenario generator inherited from Experiment 004
- five fixed seeds: 11, 23, 37, 53 and 71
- 60% train, 20% validation and 20% protected test
- no protected-test label feedback
- fusion decision retained as the anchor
- thresholds honed through grade widths of 0.08, 0.04, 0.02, 0.01 and 0.005
- a tuned threshold set is accepted only when it improves validation correctness by at least two cases

## Protected-test results

| Arm | Accuracy | Urgent recall | False escalation | Emotional proportionality |
|---|---:|---:|---:|---:|
| Fusion anchor | 0.9900 | 1.0000 | 0.0000 | 0.9973 |
| DLAH-SDVGTC | **0.9933** | **1.0000** | **0.0000** | **0.9984** |

Absolute accuracy gain: **0.0033**, equivalent to 0.33 percentage points.

The honing rule improved two seeds, preserved three seeds and degraded none after the validation-gain safeguard was applied.

## Interpretation

The experiment provides initial trial evidence that sequential dynamic threshold honing can improve accuracy while preserving urgent-threat recall and false-escalation performance. The benefit is small because the fusion anchor is already close to saturation on this synthetic task.

The result does not establish publication-level superiority. Replication is required on a harder independent dataset with greater ambiguity, noise and distribution shift. Statistical uncertainty should also be reported before any promotion decision.

## Conduit relation

Experiment 004 established that laminar regulation reduces oscillatory threshold movement. Experiment 005 adds an accuracy-directed heading while keeping changes validation-gated. The next combined trial should measure accuracy gain and laminarity in the same controller rather than treating them as separate endpoints.

## Evidence status

Trial evidence only. Not publication evidence.
