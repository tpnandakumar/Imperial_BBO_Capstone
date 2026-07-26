# PGC Experiment 008BU: Autonomic DMIC Candidate-Engine Integration

## Status

Completed comparative development experiment. This is not final confirmatory evidence.

## Purpose

Apply the same Autonomic Dynamic Milieu Interior Configuration to four current candidate engines and compare each engine with and without A-DMIC.

## Engines

- AX-R-BK
- AX-R-DTRRR
- DTRRR with protected stochastic suppression
- ECSP dynamic free-choice engine

## Design

- datasets: breast cancer, wine and digits
- seeds: 181, 197, 211, 227, 241, 257, 271, 283, 307 and 331
- 10 repeats per seed
- exact preserved AY fresh-seed out-of-fold and protected-test probabilities
- closed-system autonomic control only

## A-DMIC functions

- sympathetic computational drive
- parasympathetic recovery
- dynamic viscosity
- dynamic temperature
- dynamic resistance
- recoil
- venous-return-like state reuse
- homeostatic restoration

## Main finding

A-DMIC preserved every class decision in this implementation.

Therefore it did not change:

- accuracy
- macro-F1
- balanced accuracy
- active-model count

It did alter probability calibration and increased state reuse and Net Regenerative Efficiency.

## Best A-DMIC engine

AX-R-BK + A-DMIC ranked first among the A-DMIC variants.

- mean accuracy: 0.984088
- standard deviation: 0.007209
- maximum accuracy: 0.996296
- minimum accuracy: 0.966082
- macro-F1: 0.983754
- balanced accuracy: 0.983102
- log loss: 0.074975
- mean worst-dataset accuracy: 0.973971
- mean active models: 3.337
- mean dropout fraction: 0.666333
- mean cache reuse rate: 0.996123
- mean state reuse rate: 0.964572
- mean Net Regenerative Efficiency: 0.850047

## Mean autonomic state for AX-R-BK + A-DMIC

- sympathetic drive: 0.182959
- parasympathetic recovery: 0.898635
- viscosity: 0.789361
- temperature: 0.641650
- resistance: 0.775149
- recoil: 0.854386
- venous return: 0.964572

## Interpretation

The first A-DMIC implementation behaves as a homeostatic probability and reuse regulator rather than an accuracy-changing controller.

That is a useful result. It shows that the autonomic layer can be integrated without disturbing established class decisions while improving calibration and regenerative reserve.

The next development step should allow A-DMIC to alter route activation and stopping decisions under strict floor protection. Only then can it potentially improve accuracy or reduce active-model count further.

## Evidence boundary

Cardiovascular terms are computational analogues. Regenerative efficiency is a computational reuse proxy. Electrical energy was not measured.
