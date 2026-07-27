# PGC Experiment 008CL-B: Dependency-Enabled Formal Proof

## Status

Configured for execution in GitHub Actions.

## Purpose

This experiment completes the formal-verification stage that could not run in the local environment because `z3-solver` and `hypothesis` were unavailable.

## Verification layers

1. Z3 counterexample generation for deliberately flawed proposals
2. Z3 proof by contradiction for corrected proposals
3. Hypothesis property-based testing with 1,000 generated examples per task
4. Explicit handling of `sat`, `unsat` and `unknown`
5. Zero release of unresolved deterministic violations
6. Preservation of A-DMIC Computational Milieu Intérieur

## Tasks

- absolute value
- safe division
- bounded clamp
- monotonic increment
- corrected non-negative probability-simplex projection

## Required success criteria

- formal proof success rate: 100%
- property-based test success rate: 100%
- flawed counterexample generation rate: 100%
- false proof claim rate: 0%
- deterministic violation release rate: 0%

## Reproducibility

Dependencies are declared in `requirements.txt`. The workflow uses Python 3.12 on Ubuntu and uploads `formal_results.csv` and `results_summary.json` as retained workflow artefacts.

## Evidence boundary

An `unsat` result proves only the property encoded in the stated symbolic model. It does not independently prove operating-system security, hardware safety, termination, memory safety or correctness of an external specification.
