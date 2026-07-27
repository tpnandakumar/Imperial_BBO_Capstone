# GitHub Repair Session 001

## Outcome

The Imperial BBO historical dataset has been harmonised and repaired successfully.

## Authoritative recovery sources

- Strategic Optimisation Engine v1 exact Weeks 1 to 10 input and output history
- Exact Week 11 submitted inputs
- Exact Week 11 returned outputs

## Repairs completed

1. Added `PFRAMOS/data/recovered_exact_history.csv` with all 88 observations.
2. Extended schema normalisation for packed coordinate columns.
3. Extended schema normalisation for split `Input_1` to `Input_8` columns.
4. Added leading-blank-line handling for CSV headers.
5. Standardised coordinate comparison at six-decimal submission precision.
6. Compared recovered history against available weekly CSV copies.
7. Rebuilt `canonical_bbo_observations.csv` from the validated recovered history.
8. Added source manifest, congruence report, harmony readiness marker and learning log.
9. Restricted downstream analysis to the canonical dataset.
10. Reran the complete validation and experiment workflow.

## Final validation

GitHub Actions run `30038933136` completed successfully.

The following stages passed:

- unit tests
- architecture experiment suite
- harmony test
- repair and canonicalisation
- post-repair experiment suite
- historical data audit
- walk-forward fit comparison
- public audit artefact upload

## Data status

- Weeks: 11
- Functions per week: 8
- Canonical observations: 88
- Missing observations: 0
- Unresolved numeric conflicts: 0
- Forwarding state: ready

## Learning

The apparent Week 6 and Week 8 conflicts were formatting differences rather than numerical disagreements. Values such as `0.50` and `0.500000` are identical at the BBO submission precision. Congruence testing must compare numerical values at canonical precision rather than raw strings.

## Next authorised stage

The repaired dataset is ready for full retrospective walk-forward analysis, active-node pathway construction and controlled Week 12 candidate experiments. No candidate should be submitted until the resulting recommendations pass coherence, robustness and audit gates.
