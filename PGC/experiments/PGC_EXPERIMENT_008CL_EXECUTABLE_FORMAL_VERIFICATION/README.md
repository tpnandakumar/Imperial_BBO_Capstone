# PGC Experiment 008CL: Executable Verification and Formal Constraint Validation

## Status

Completed controlled executable-verification benchmark. Formal SMT confirmation remains pending because `z3-solver` was unavailable in the execution environment.

## Design

- 5 deterministic tasks
- 8 fresh seeds
- 40 task-runs
- bounded correction loop with a maximum of 3 cycles
- runtime tests, adversarial fuzzing and invariant checking
- counterexample-guided correction
- A-DMIC Computational Milieu Intérieur preserved throughout

## Initial result

- overall runtime-verification success: 80%
- self-correction rate: 100%
- deterministic violation release rate: 0%
- homeostasis restoration rate: 100%
- formal proof rate: 0% because Z3 was unavailable

Four tasks reached complete runtime verification after correction:

1. absolute value
2. safe divide
3. bounded clamp
4. monotonic increment

## Important defect detected

The original probability-normalisation specification could produce negative values when the total remained positive. The release gate blocked the result rather than accepting an invalid probability state.

The specification was repaired using non-negative simplex projection:

- negative inputs are projected to zero
- the positive components are normalised to sum to one
- when both projected values are zero, the fallback is `(0.5, 0.5)`

The repaired probability-normalisation task achieved:

- runtime verification success: 100% across 8 fresh reruns
- deterministic violation release rate: 0%
- formal proof status: pending Z3 dependency

## Evidence boundary

This experiment demonstrates executable testing, adversarial fuzzing, invariant enforcement and bounded counterexample-guided correction. It does not yet demonstrate SMT proof because neither `z3-solver` nor Hypothesis was installed in the runtime.

## Decision

Promote the corrected invariant-first verification loop. The next stage is an instrumented rerun with Z3 and Hypothesis installed, followed by integrated PCEEC scoring.
