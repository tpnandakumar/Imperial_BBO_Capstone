# Advanced Extension Series

## Purpose

This series begins after the official thirteen-round capstone. It is deliberately separate from Week 01 to Week 13 and does not create an unofficial Week 14.

The aim is to continue the optimisation reasoning until each function has one defensible winning coordinate, with a documented reason to continue, eliminate a candidate, validate a winner or stop.

## Optimisation lifecycle

**Explore -> Exploit -> Extend -> Eliminate -> Validate -> Winner -> Stop**

A function can move backwards in this sequence when the evidence requires it. A failed exploitation step can reopen exploration. An apparent winner can return to validation if repeatability is uncertain.

## Current position after Week 13

| Function | Status entering extension | Current verified coordinate | Current verified value |
| --- | --- | --- | ---: |
| F1 | Provisionally confirmed winner | `0.600000-0.600000` | `0.025559285339829783` |
| F2 | Active | `0.690000-0.950000` | `0.7335252043269003` |
| F3 | Active | `0.855000-0.145000-0.855000` | `-0.05685061601567621` |
| F4 | Provisionally confirmed winner | `0.600000-0.430000-0.420000-0.250000` | `-4.359874926582439` |
| F5 | Active | `0.090000-0.999999-0.999999-0.999999` | `4440.957216598753` |
| F6 | Active, repeatability unresolved | `0.700000-0.200000-0.700000-0.700000-0.200000` | `-0.6071562248604215` best observed at this coordinate |
| F7 | Provisionally confirmed winner | `0.040000-0.480000-0.260000-0.220000-0.420000-0.740000` | `1.3809299933612855` |
| F8 | Provisionally confirmed winner | `0.060000-0.070000-0.030000-0.040000-0.410000-0.820000-0.500000-0.910000` | `9.58024` |

## Active functions

F2, F3, F5 and F6 remain active because the thirteen-round evidence does not yet justify a final stopping claim. F1, F4, F7 and F8 remain frozen unless new evidence gives a specific reason to reopen them.

## Extension numbering

All work after Week 13 uses the following sequence:

- Optimisation Extension 1
- Optimisation Extension 2
- Optimisation Extension 3
- subsequent extensions only when justified by new evidence

## Evidence rule

A proposed coordinate is not a verified winner until an objective value has actually been returned by the authorised evaluation process. Modelled, interpolated or extrapolated candidates are labelled as candidates. No output is invented.

This distinction is essential. The repository can complete the analytical design and candidate selection offline, but it cannot truthfully declare a new post-capstone objective winner without new evaluations from the black box.

## Completion rule

The Advanced Extension Series closes only when every function has one winning coordinate supported by the available evidence and a documented stopping reason. Where further black-box evaluation is unavailable, the series records the strongest verified winner and separately records unresolved candidate tests rather than presenting estimates as observations.
