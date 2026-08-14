# Week 11 Evidence and Provenance

## Purpose

This file links the main Week 11 conclusions to the evidence from which they were derived. It separates direct observations, derived analysis and strategic interpretation.

## Evidence chain

```text
Verified Week 10 record
        |
        v
Week 11 submitted query
        |
        v
Week 11 returned output
        |
        v
Comparison with Week 10 and historical best
        |
        v
PCA structural review
        |
        v
Function specific strategy comparison
        |
        v
Submitted Week 12 query
```

## Provenance matrix

| Claim | Direct evidence | Derived evidence | Strategic interpretation |
| --- | --- | --- | --- |
| Function 1 reproduced a prior best | Week 11 input `0.600000,0.600000`; output `0.025559285339829783` | Exact match with Week 3 best | Repeatability outweighed the need for a new direction |
| Function 2 reached a new best | Week 11 input `0.695000,0.950000`; output `0.5848554940277205` | Improvement over Week 10 and prior best | One further small local refinement was justified |
| Function 3 recovered towards a stronger region | Week 11 output `-0.06542982421105416` | Improvement over Week 10 and proximity to Week 4 best | Historical best remained more informative than PCA extrapolation |
| Function 4 showed a large recovery | Week 11 output `-4.868852987697114` | Improvement of `8.614789667334044` from Week 10 | Return to the exact stronger historical point |
| Function 5 reached a new best | Week 11 output `4411.0387356061765` | Improvement beyond the Week 9 and Week 10 plateau | PCA structure and objective trend supported a further boundary refinement |
| Function 6 recovered | Week 11 output `-0.7268715077444687` | Improvement over Week 10 and movement towards the Week 3 basin | Historical best provided the clearer Week 12 target |
| Function 7 remained productive | Week 11 output `1.3579108517237013` | Strong positive value close to prior best | Known productive point remained stronger evidence than a PCA based extrapolation |
| Function 8 reproduced a prior best | Week 11 input repeated the Week 1 best point; output `9.58024` | Exact repeated best | Retain the confirmed point |

## PCA evidence

PCA was applied only after the Week 11 outputs were known. For Functions 3 to 8, the first one or two principal components captured most of the variance in the submitted query histories.

The analysis was used as a structural comparison tool. It did not replace the objective values. This distinction is important because concentrated query variance can arise from the way the search was conducted rather than from the hidden function itself.

## Week 12 link

The final Week 12 strategy is recorded in [PCA_STRATEGY_COMPARISON.md](PCA_STRATEGY_COMPARISON.md) and [WEEK_12_DECISION_RECORD.md](WEEK_12_DECISION_RECORD.md). The exact submitted Week 12 vectors are stored separately in `../Week_12/week_12_inputs.csv`.

## Interpretation boundary

This provenance record describes the evidence available at the transition from Week 11 to Week 12. Later Week 12 outputs can evaluate the strategy but cannot change the evidence that was available when the decision was made.