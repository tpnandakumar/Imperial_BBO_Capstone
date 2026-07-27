# PFRAMOS Experiment Suite 001 Results

## Run status

GitHub Actions run: `30038046326`

- Completed architecture experiments: 7
- Passed architecture experiments: 7
- Failed completed experiments: 0
- Blocked historical experiment: 1

## Experiment results

| ID | Experiment | Measured result | Outcome |
|---|---|---:|---|
| E01 | Positive coherence detection | +0.7117241379305436 | Passed |
| E02 | Conflict detection | -0.7117241379305436 | Passed |
| E03 | Coherence-stimulated activity | 1.0, bounded | Passed |
| E04 | Terminal Active Node selection | Boundary node | Passed |
| E05 | Maximum Coherence Conduit | 4-node path, sphere radius 0.2250 | Passed |
| E06 | Multi-core shared cache | 2 repeated calculations avoided | Passed |
| E07 | Quality-first energy scheduling | `efficient_equal` selected | Passed |
| E08 | Historical BBO readiness | 0 canonical rows | Blocked |

## What was demonstrated

1. Signed coherence responds symmetrically to support and conflict.
2. Coherence-stimulated activity remains bounded and cannot exceed 1.0.
3. Terminal authority requires threshold, support and tie checks.
4. A connected Maximum Coherence Conduit can form across data, trajectory, boundary and candidate nodes.
5. High pathway coherence contracts the pathway envelope.
6. Multi-core conduits reuse shared calculations through a thread-safe cache.
7. Computational and energy savings are applied only inside the protected quality basin.
8. Historical optimisation remains blocked until the canonical data gate is satisfied.

## Historical harmony findings

The Harmony Test identified 14 critical issues:

- Weeks 1, 2, 3 and 7 lack discoverable input and result CSV files.
- Week 4 uses the input schema `week,function,input_values`.
- Weeks 5 and 6 use separate `Input_1` to `Input_8` columns.
- Week 6 result CSV has no recognised header.
- Week 10 and Week 11 folders are absent from the current repository branch.

## Interpretation

The PFRAMOS architecture passed its first controlled synthetic and structural tests. No claim is yet made about improved BBO optimisation performance because the historical 88-observation dataset has not passed the Harmony Repair Gate.

## Next experiment gate

Experiment Suite 002 may begin after:

1. recovering or reconstructing Weeks 1, 2, 3 and 7 source data
2. adding Week 10 and Week 11 folders
3. extending schema normalisation for Weeks 4, 5 and 6
4. validating exactly 88 historical observations
5. rerunning walk-forward model and pathway experiments
