# PGC Experiment 008AV: Heart-Connected Free-Form Specialist Microcirculation

## Status

Completed three-seed development trial. This is development evidence and is not yet confirmatory.

## Core architecture

Nodal specialist conduits are free to form, but every conduit is connected to the computational heart.

The heart does not decide which nodes may connect. It regulates whether a newly formed conduit receives enough perfusion to remain active, strengthen, weaken or close.

The nodal topology is therefore free-forming, while perfusion remains centrally autoregulated.

## Moving systolic-diastolic pressure gradient

The heart generates a travelling pressure wave through the specialist microcirculation.

### Systole

- raises upstream pressure
- propels specialist influence forwards
- increases flow to active specialist nodes
- supports rapid correction of salient difficult samples

### Diastole

- lowers downstream pressure
- permits conduit refill
- returns influence towards basal cortical flow
- prevents persistent over-pressurisation
- supports recovery and closure of unhelpful pathways

## Specialists

- boundary decision-tree specialist
- local-neighbourhood specialist
- Gaussian reliability specialist
- Extra Trees specialist

## Experimental arms

- 008AR reference
- static heart tether
- systolic propulsion only
- travelling systolic-diastolic gradient
- phase-locked specialist microcirculation
- full autonomic moving microcirculation

## Search design

- 20 configurations per arm
- 120 total configurations
- three seeds: 11, 37 and 71
- stratified five-fold cross-fitting
- specialist learners trained within development folds
- protected test opened only after all development winners were fixed

## Result

The fixed 008AR reference remained the accuracy leader.

- protected accuracy: **0.988596**
- macro-F1: 0.988333
- balanced accuracy: 0.987516
- worst-case accuracy: 0.964912
- log loss: 0.809307

The strongest moving-pressure arm was the travelling systolic-diastolic gradient.

- protected accuracy: **0.981140**
- log loss: **0.777642**
- protected specialist activation rate: 0.798571

## Interpretation

The moving pressure gradient substantially improved probability calibration but reduced classification accuracy.

This indicates that the heart-linked specialist circulation was too permissive. Specialist perfusion altered many samples for which the general cortical ensemble was already correct.

The experiment supports the moving systolic-diastolic pressure gradient as a real computational control mechanism, but not yet as a route to a higher accuracy ceiling.

The next refinement must use a selective valve that opens only when expected Net Specialist Gain is positive. The valve should use development-only evidence to predict whether specialist intervention is likely to correct an error without damaging an already correct decision.

## Evidence boundary

Temperature, pressure, heart rate, systole, diastole and perfusion are computational control proxies. They are not physical or physiological measurements.
