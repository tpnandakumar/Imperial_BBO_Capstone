# PGC Experiment 008

## Dynamic Vortex Cognitive Scramjet with Maximum Accuracy Directed Thrust Vectoring

### Objective

Test whether a dynamic Rankine-Navier vortex scramjet controller can direct additional computation along the strongest validation-supported accuracy vector, improving protected-test accuracy while preserving calibration, efficiency, selective coverage and laminar stability.

### Evidence status

All outputs are trial evidence. No publication claim is permitted from this experiment alone.

## Target

The long-term target is 100% accuracy on answerable cases and at least 99.99% selective accuracy on sufficiently large protected evaluations. Experiment 008 must report coverage, abstention and sample size alongside accuracy. A finite 100% result must never be described as universal perfection.

## Datasets

Use the existing Experiment 007 Block A datasets first:

- Breast Cancer Wisconsin
- Wine
- Digits

Then repeat on at least two harder datasets with more overlap, noise or dimensionality before promotion.

## Splits and seeds

- 60% training
- 20% validation
- 20% protected test
- minimum 10 fixed seeds per dataset
- protected-test labels unavailable to all tuning, gating and vectoring decisions

## Comparison arms

1. Fusion anchor
2. Rankine cruise only
3. Full-time Navier-inspired processing
4. Fixed Rankine-Navier hybrid
5. Dynamic scramjet without thrust vectoring
6. Dynamic scramjet with confidence-directed vectoring
7. Dynamic scramjet with maximum-accuracy-directed vectoring
8. Maximum-accuracy-directed vectoring with gated afterburner and rollback
9. Oracle route allocation, evaluation only

## Controller state

Each case maintains:

- route probabilities
- confidence margin
- calibration residual
- model disagreement
- domain familiarity
- distribution-shift score
- expected rescue probability
- expected harm probability
- compute cost estimate
- vortex radius
- angular displacement
- axial utility
- thrust magnitude
- thrust direction
- thrust duration
- afterburner state
- counter-thrust state

## Rankine cruise

Rankine mode is the default low-cost conduit. It handles high-confidence, familiar and low-conflict observations using the least expensive validated route.

## Navier-inspired mode

Navier-inspired processing is activated only when validation evidence predicts that richer interaction modelling may improve the decision. Its computational analogues are:

- pressure: competing objective pressure
- viscosity: damping and stability control
- forcing: new evidence and predicted gain
- diffusion: information sharing among nearby candidate routes
- convection: state-dependent route movement

## Maximum-accuracy thrust vector

Let the tunable controller state be Theta. Candidate corrections are estimated on training and validation data only.

The selected thrust vector is the bounded candidate direction with the greatest expected validation accuracy gain, subject to:

- no reduction in safety-critical recall beyond the preregistered tolerance
- no material worsening of calibration
- compute budget compliance
- retention and effective recall preservation
- laminarity floor

Corrections pointing away from the validated accuracy direction are rejected or converted into counter-thrust.

## Timed thrust phases

1. Acquisition
2. Alignment
3. Acceleration
4. Honing
5. Braking
6. Lock

The controller must record onset, duration, taper and disengagement for every activation.

## Afterburner gate

Afterburner activation requires:

- predicted error probability above threshold
- positive expected rescue-minus-harm utility
- expected accuracy gain greater than normalised extra compute cost
- validation support above the minimum evidence threshold

Afterburner must be temporary, bounded and reversible.

## Selective decision outputs

The engine may:

- commit
- clarify or acquire more evidence
- abstain and escalate

Report selective accuracy and coverage together.

## Primary metrics

- protected-test accuracy
- selective accuracy
- coverage
- macro-F1
- balanced accuracy
- log loss
- expected calibration error
- rescue rate
- harm rate
- net rescue utility
- worst-seed accuracy
- worst-dataset accuracy

## Efficiency metrics

- training time
- inference latency
- peak memory
- route evaluations per case
- Navier activation rate
- afterburner activation rate
- compute added per rescued decision
- accuracy gain per unit compute

## Vortex and laminar metrics

- radial convergence
- angular travel
- axis-angle change
- threshold reversal rate
- thrust reversal rate
- overshoot frequency
- counter-thrust frequency
- path variation
- laminarity index
- convergence steps

## Promotion criteria

The maximum-accuracy-directed controller may advance only if it:

1. improves mean protected-test accuracy over the fusion anchor
2. does not reduce worst-seed accuracy
3. has positive rescue-minus-harm utility
4. preserves safety-critical recall
5. satisfies the laminarity floor
6. demonstrates a favourable accuracy-efficiency trade-off
7. reproduces across multiple datasets

## First implementation milestone

Implement and compare the four core modes first:

- Rankine cruise
- full-time Navier processing
- fixed hybrid
- dynamic hybrid with maximum-accuracy-directed thrust vectoring

Then add afterburner and counter-thrust only after the base vectoring behaviour is validated.
