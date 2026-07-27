# PGC Experiment 008CL-B: Dependency-Enabled Formal Proof

## Status

Completed successfully and archived on `main`.

Trigger commit under observation: `efbdaac9ff97913bd3019e776c6e766d78a412d8`.

Committed evidence files:

- `formal_results.csv`
- `results_summary.json`

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

## Formal results

| Measure | Result |
|---|---:|
| Formal tasks | 5 |
| Formal proof success rate | 100% |
| Flawed-proposal counterexample rate | 100% |
| Hypothesis property-testing success rate | 100% |
| False proof claim rate | 0% |
| Deterministic violation release rate | 0% |
| Probability-simplex invariant | Proven |
| Solver `unknown` treated as proof | No |
| A-DMIC milieu intérieur | Preserved |

All five corrected symbolic propositions returned `unsat`. Every deliberately flawed proposition returned `sat` with a concrete counterexample. The probability-simplex invariant also returned `unsat`, supporting the encoded non-negativity, upper-bound and unit-sum conditions.

## Required success criteria

- formal proof success rate: 100%
- property-based test success rate: 100%
- flawed counterexample generation rate: 100%
- false proof claim rate: 0%
- deterministic violation release rate: 0%

All required criteria were met.

## Reproducibility

Dependencies are declared in `requirements.txt`. The workflow uses Python 3.12 on Ubuntu. The execution outputs are retained in the experiment directory as `formal_results.csv` and `results_summary.json`.

Runtime measurements in `formal_results.csv` and `results_summary.json` are execution-specific observations. They are not formal guarantees and should not be used as stable performance benchmarks.

## Evidence boundary

An `unsat` result proves only the property encoded in the stated symbolic model. It does not independently prove operating-system security, hardware safety, termination, memory safety, correctness of an external specification, or correctness of requirements that were not encoded.

Property-based testing provides empirical support over generated examples. It is not a substitute for proof outside the explicitly formalised propositions.

## Next steps

1. Freeze Experiment 008CL-B as the formal-proof baseline.
2. Add a machine-readable evidence manifest containing file hashes, workflow identity, trigger commit and environment metadata.
3. Apply the same proof-plus-counterexample pattern to the next safety-critical PGC experiment.
4. Separate formal correctness metrics from runtime efficiency metrics in later certification scoring.
5. Preserve the current evidence boundary in all downstream summaries and certification material.
