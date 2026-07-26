# Precision Burst Positioning, Intensity and Accuracy Response Surface

## Status

Control extension for predictive forward-compensation bursts and Experiment 008BF.

## Core proposition

A burst should be delivered only at the tunnel location, time, phase and intensity where development evidence predicts the greatest positive accuracy gain.

There is no universally correct burst. The correct burst is conditional on the sample state, tunnel state, specialist route and expected harm.

## Precision burst coordinates

Every burst command should specify:

- tunnel segment
- specialist destination
- predicted wave-front arrival time
- pulse onset time
- phase offset
- pulse-pressure intensity
- frequency
- pulse count
- viscosity state
- aperture state
- burst duration
- strategic diastolic recovery duration

## Accuracy Response Surface

The controller should learn an Accuracy Response Surface over burst-control variables.

```text
Accuracy Response Surface
=
expected predictive gain as a function of
location, time, phase, intensity, frequency,
viscosity, aperture, specialist route and recovery
```

The surface should be estimated only from development folds.

## Precision objective

```text
Optimal Burst Command
=
arg max
(
expected error correction
-
expected new error
-
latency cost
-
activation cost
-
phase-instability cost
-
recovery overhead
)
```

## Positioning rule

The burst should be placed at the earliest tunnel segment where:

- the local predictive deficit is detectable
- the selected specialist can still alter the decision
- phase alignment remains recoverable
- pressure attenuation remains bounded
- expected Net Burst Gain is positive

A burst delivered too early may amplify noise. A burst delivered too late may fail to alter the anterior decision.

## Intensity rule

Burst intensity should be the minimum intensity predicted to cross the local correction threshold.

```text
minimum effective intensity
>
local correction threshold

but

minimum effective intensity
<
overshoot and harm threshold
```

The controller should avoid maximum intensity unless development evidence specifically supports it.

## Phase-locked delivery

Burst onset should be phase-locked to the predicted wave front.

- phase lead prepares the downstream aperture before arrival
- zero-phase alignment reinforces the active wave front
- controlled phase lag may support posterior recoil or venous recovery
- destructive phase opposition should terminate the burst

## Pulse-by-pulse micro-adjustment

After each pulse, surface sensors should update:

- observed confidence gain
- observed entropy reduction
- specialist correction probability
- phase error
- pressure attenuation
- reflection amplitude
- local viscosity mismatch
- remaining correction requirement

The next pulse should then be repositioned, strengthened, weakened, phase-shifted or cancelled.

## Accuracy-lock condition

A burst should terminate when:

- the corrected class remains stable across a validated confidence margin
- entropy no longer falls meaningfully
- the next pulse has non-positive expected Net Burst Gain
- specialist harm probability rises above threshold
- strategic diastole is required for recovery

## Validation requirements

- all burst coordinates selected from development folds only
- no holdout-label feedback during response-surface fitting
- identical candidate budgets across comparator systems
- early stopping rules fixed before holdout evaluation
- report both correction and harm counts

## Primary measurements

- accuracy
- macro-F1
- balanced accuracy
- log loss
- correction rate
- harm rate
- Net Burst Gain
- burst activation rate
- mean pulse count
- mean intensity
- phase error
- viscosity adjustment
- models activated per sample
- inference latency
- regenerative reuse rate

## Experiment 008BF

Compare:

1. stable 5-stack interior
2. single fixed pulse
3. fixed uniform burst
4. phase-compensated burst
5. viscosity-compensated burst
6. precision-positioned intensity-matched burst
7. full precision burst with pulse-by-pulse sensors, strategic diastole and regenerative reuse

## Priority statement

Precision is more important than force. The correct burst is the lowest-cost burst that reaches the local correction threshold at the correct tunnel segment and phase without causing overshoot, harm or incomplete recovery.
