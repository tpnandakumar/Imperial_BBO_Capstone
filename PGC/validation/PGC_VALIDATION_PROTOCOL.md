# PGC Validation Protocol

## Purpose

PGC must be validated as a configurable cognitive system, not merely as a collection of models.

## Capability claim ladder

1. implemented
2. executable
3. internally validated
4. replicated
5. externally benchmarked
6. publication ready

No capability may skip a level without documented evidence.

## Required controls

- fixed task definition
- fixed train, validation and protected-test separation
- recorded random seeds
- matched parameter and compute budgets where comparisons are made
- single-module baselines
- static-routing baseline
- random-routing baseline
- PGC routing ablation
- PHCS coherence ablation
- PIMF persistence ablation
- memory ablation
- efficiency measurement

## Primary evaluation families

### State and sequence cognition

- alternating-state tracking
- parity
- modular arithmetic
- induction and delayed retrieval
- multi-register updates
- long-context retrieval

### Memory

- retention recall
- forgetting precision
- conflicting-update stability
- outlier recovery
- memory-write coherence
- deletion and rollback reliability

### Multimodal cognition

- text-image consistency
- audio-visual grounding
- video action and object continuity
- cross-modal retrieval

### Applied cognition

- time-series forecasting
- anomaly detection
- optimisation under limited evaluations
- dialogue consistency
- code reasoning

## PGC-level metrics

- task success
- macro capability score
- coherence
- robustness
- uncertainty calibration
- routing regret against the best eligible expert
- compute cost
- energy where measurable
- memory cost
- recovery after module failure
- cross-domain transfer

## Failure protocol

A failed experiment remains part of the evidence record. It must identify:

- failure type
- affected module
- dataset or benchmark version
- configuration
- logs and seeds
- whether the failure is reproducible
- proposed correction

## Publication rule

A PGC result becomes publication evidence only when:

- the full configuration is version pinned
- the data and licence record is complete
- protected evaluation is preserved
- all reported metrics are reproducible
- at least one independent rerun agrees within the predefined tolerance
- negative and null findings are retained
