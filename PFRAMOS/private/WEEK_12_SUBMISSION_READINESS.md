# Week 12 Submission Readiness Review

## Status

Private controlled research only. Not submitted.

## Review basis

- Canonical Weeks 1 to 11 history, 88 observations
- Walk-forward model comparison
- Multi-model consensus
- PHCS coherence scoring
- Local perturbation robustness
- Terminal Active Node resolution
- Six-decimal BBO formatting
- Distance from the Week 11 submitted point
- Boundary-contact review

## Candidate review

| Function | Candidate | Coherence | Robustness | Uncertainty | Distance from Week 11 | Review state |
|---|---|---:|---:|---:|---:|---|
| F1 | 0.606993-0.530883 | 0.917354 | 0.990752 | 0.041323 | 0.069470 | Ready for controlled review |
| F2 | 0.631264-0.887657 | 0.914883 | 0.991949 | 0.042558 | 0.089157 | Ready for controlled review |
| F3 | 0.280000-0.875000-0.315000 | 0.792634 | 0.997671 | 0.103683 | 1.049023 | Hold. Large exploratory jump |
| F4 | 0.320000-0.720000-0.680000-0.220000 | 0.699542 | 0.983602 | 0.150229 | 0.488365 | Hold. Substantial jump and highest uncertainty |
| F5 | 0.068179-1.000000-1.000000-0.999221 | 0.927121 | 0.995235 | 0.036440 | 0.041874 | Hold for boundary-safe refinement |
| F6 | 0.625342-0.220219-0.638913-0.677632-0.155425 | 0.882896 | 0.985647 | 0.058552 | 0.121170 | Ready for controlled review |
| F7 | 0.031685-0.424155-0.243112-0.192234-0.408965-0.705680 | 0.915325 | 0.995297 | 0.042337 | 0.080371 | Ready for controlled review |
| F8 | 0.104941-0.031854-0.036165-0.000000-0.370539-0.799427-0.365166-0.908124 | 0.912688 | 0.999850 | 0.043656 | 0.158987 | Hold for boundary-safe refinement |

## Decision

The model-consensus experiment passed the aggregate review gate, but the full eight-function set is not yet authorised for submission.

### Provisionally acceptable

- F1
- F2
- F6
- F7

### Requires a second-stage constrained experiment

- F3 because the Euclidean movement from Week 11 is unusually large
- F4 because the movement is substantial and uncertainty is the highest in the set
- F5 because two coordinates reach the upper boundary
- F8 because one coordinate reaches the lower boundary

## Next gate

Run constrained local candidate experiments for F3, F4, F5 and F8 using:

1. bounded movement from the Week 11 point
2. no exact 0.000000 or 1.000000 coordinates unless boundary superiority is independently demonstrated
3. preserved or improved coherence
4. robustness at least 0.95
5. uncertainty no greater than the current candidate
6. comparison against the unconstrained candidate and Week 11 incumbent

The final Week 12 submission should be assembled only after these four functions pass the constrained gate.
