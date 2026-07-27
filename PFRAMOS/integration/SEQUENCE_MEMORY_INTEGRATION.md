# Sequence Memory Integration Across PFRAMOS, PIMF and the BBO Engine

## Purpose

State Space Models, Mamba and Titans introduce useful ideas for long-context sequence processing, selective retention, adaptive forgetting and test-time memory. These ideas are integrated as candidates, not copied wholesale.

## Separation of responsibility

### PIMF

PIMF diagnoses how influence develops through observations and higher-order change.

It receives:

- current value
- ΔD
- Δ²D
- Δ³D
- persistence
- surprise
- coherence
- uncertainty
- contamination risk

It classifies the signal as Emerging, MaxInflu, Plateau, Reversal, Boundary, Oscillation, Recovery or Equilibrium where supported by the evidence.

### PFRAMOS

PFRAMOS decides what to do with the diagnosed signal.

Available actions include:

- selective retention
- surprise-weighted shadow update
- adaptive forgetting
- observation without update
- quarantine

PFRAMOS also chooses the active conduit and records the retention and forgetting weights.

### BBO engine

The BBO engine receives only approved state updates. It stores function-specific historical features and never exposes private future candidates or protected outputs.

The initial integration is shadow-only. No memory update is written into live candidate generation until prospective validation passes.

## Architecture mapping

| External idea | PFRAMOS use | PIMF use | BBO use |
|---|---|---|---|
| SSM compressed state | bounded sequential state | persistent influence signature | compact function history |
| Mamba selection | input-dependent retention | identify influential observations | retain or forget features by function |
| Hardware-aware scan | multicore conduit execution | parallel delta calculation | efficient weekly history processing |
| State Space Duality | compare recurrent and attention-like routes | compare influence views | hybrid optimiser-state representation |
| Titans surprise | novelty-weighted shadow memory | Emerging-state evidence | flag unusual observations for review |
| Titans forgetting | context-dependent decay | Plateau, Reversal and persistence analysis | reduce stale historical influence |
| Persistent memory | stable rules and constraints | long-lived influence baseline | function dimensions, bounds and format rules |

## BBO memory layers

```text
Persistent memory
  Function dimensions
  Bounds
  Formatting rules
  Competition constraints

Long-term validated memory
  Exact historical inputs and outputs
  Reproducible delta trajectories
  Validated influence states
  Confirmed response patterns

Short-term working memory
  Recent weekly observations
  Candidate comparisons
  Current uncertainty and coherence

Quarantine memory
  Contaminated evidence
  Unverified emergence
  Unsafe or unstable updates
```

## Adaptive forgetting policy

Forgetting does not delete historical evidence. It reduces the decision weight of evidence that is stale, contradictory, unstable or no longer relevant.

The immutable audit history remains available for retrospective analysis.

## Safety controls

- no automatic architecture integration
- no direct test-time learning on live BBO submissions
- no memory write from unverified external text
- no update when contamination risk is high
- no use of future outputs during historical reconstruction
- every state update links to an audit record
- rollback remains available
- PIMF diagnoses, PFRAMOS regulates, and the BBO engine executes only approved decisions

## Publication tracks

The integration supports separate evidence for:

- Paper 1, core optimisation architecture
- Paper 2, P-C4 efficient computation
- Paper 3, concurrent multi-source schooling
- Paper 5, emergent behaviour and laminar conduits
- Paper 6, mouldability and Pisharamisation

## Current activation state

The bridge contracts are implemented. Sequence-memory updates remain in shadow mode until controlled retrospective, ablation and prospective tests demonstrate reproducible benefit.
