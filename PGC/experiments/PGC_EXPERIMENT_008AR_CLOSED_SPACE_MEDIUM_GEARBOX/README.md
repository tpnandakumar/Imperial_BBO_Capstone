# PGC Experiment 008AR: Closed-Space Medium Density and Viscosity Gearbox

## Status

Completed three-seed development trial. This is development evidence and is not yet confirmatory.

## Purpose

Compare operation in vacuum with operation inside media of increasing density and viscosity, including a dynamically geared medium and a closed bounded chamber.

## Computational interpretation

- density: inertia proxy
- viscosity: damping proxy
- gear ratio: transmission of search drive into deformation
- boundary confinement: resistance near the edge of the closed search space
- reflective wall: redirects excess displacement back into the admissible chamber
- flow efficiency: derived proxy, not a physical energy measurement

## Arms

- vacuum
- low-density, low-viscosity medium
- medium-density, medium-viscosity medium
- high-density, high-viscosity medium
- dynamically geared density-viscosity medium
- closed-space adaptive medium

## Search design

- 100 configurations per arm
- 600 total configurations
- 200 bootstrap resamples per candidate
- three seeds: 11, 37 and 71
- stratified five-fold cross-fitting
- frozen 20% protected test
- all arm winners fixed before protected-test evaluation

## Best result

The strongest arm was **medium-density, medium-viscosity medium**.

- winner configuration: 9
- batch: 1
- trial: 9
- density: 0.65
- viscosity: 0.90
- gear ratio: 0.72
- boundary confinement: 0.20
- recoil: 0.032143
- accumulated spin: 0.35 radians
- rifling twist: 0.447422 radians
- mean out-of-fold accuracy: 0.985211
- protected-test mean accuracy: **0.988596**
- protected-test worst accuracy: 0.964912
- macro-F1: 0.988333
- balanced accuracy: 0.987516
- log loss: 0.809307

## Interpretation

Vacuum was not optimal. The strongest result came from an intermediate medium that supplied enough inertia and damping to suppress erratic motion without preventing progress.

The winning gearbox ratio of 0.72 indicates that the search drive should be transmitted at a reduced but still substantial level. The medium therefore acts like a computational gearbox, converting unstable high-speed motion into slower, controlled, goal-directed movement.

The most important result is efficiency. The peak was reached by configuration 9, much earlier than in the preceding peak-matching experiments. This makes the medium-density, medium-viscosity regime the earliest peak-matching operating state observed so far.

The result requires exact extraction and ten-seed confirmation before promotion.
