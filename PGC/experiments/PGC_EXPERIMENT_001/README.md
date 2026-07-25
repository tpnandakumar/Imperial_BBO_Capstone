# PGC Experiment 001

## Title

Evidence-Aware Cognitive Routing Under Mixed Synthetic Tasks

## Objective

Determine whether the PGC router selects a suitable cognitive configuration more reliably than static, random and confidence-only routing.

## Task families

- alternating-state tracking
- parity
- modular arithmetic
- delayed induction
- constrained black-box optimisation

## Candidate experts

- sequence-state expert
- arithmetic expert
- retrieval expert
- optimisation expert
- abstention route

## Experimental arms

1. static single expert
2. random expert
3. confidence-only router
4. oracle router
5. PGC evidence-aware router
6. PGC without PHCS coherence
7. PGC without PIMF persistence
8. PGC without efficiency term

## Primary endpoints

- task success
- routing accuracy
- routing regret against the oracle
- abstention precision
- coherence
- uncertainty calibration
- latency
- memory use

## Required controls

- fixed dataset-generation scripts
- five or more random seeds
- unseen sequence lengths
- balanced task families
- fixed candidate capabilities
- no protected-test exposure during router tuning

## Promotion criterion

PGC routing becomes eligible for wider integration only when it improves task success or materially reduces routing regret over the strongest non-oracle baseline without worsening safety, coherence or calibration beyond predefined tolerances.

## Current status

Protocol created. No experimental run has yet been executed.
