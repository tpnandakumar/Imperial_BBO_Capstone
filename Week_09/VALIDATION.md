# Week 09 Validation Record

## Identification

- Course module: 21
- Capstone week: 09
- Optimisation round: 9
- Validator: Dr N T Pisharam with reproducible script support

## Validation objectives

The Week 09 validation process checks that the recorded data are internally consistent, the submitted coordinates satisfy the challenge constraints and the interpretation is supported by the observed outputs.

## Structural validation

- Eight input records are present.
- Eight output records are present.
- Function identifiers correspond from F1 to F8.
- Input dimensionality matches the function specification.
- All coordinates lie within `[0,1]`.
- Submission coordinates are recorded to six decimal places.
- Each input has one corresponding returned output.

## Data consistency

The objective values in `week_09_results.csv` agree with those used in `week_09_analysis_summary.csv` and the Week 09 README analysis. Rankings are based on the recorded scalar outputs. Because the functions use different scales, cross-function rank is used for portfolio description rather than direct claims of comparable difficulty.

## Strategy validation

| Function | Observed evidence | Strategy | Validation judgement |
|---|---|---|---|
| F1 | Effectively zero and unchanged | Explore | Supported |
| F2 | Positive but lower than Week 08 | Refine | Supported with caution |
| F3 | Negative and slightly lower | Reassess | Supported |
| F4 | Less negative than Week 08 | Refine | Supported |
| F5 | Highest output and improved | Exploit | Strongly supported |
| F6 | Negative and slightly lower | Reassess | Supported |
| F7 | Positive and broadly stable | Refine | Supported |
| F8 | High and highly stable | Refine | Supported |

## Robustness checks

- Recent movement was compared with the broader trajectory rather than interpreted in isolation.
- Stable positive functions were not treated as guaranteed optima.
- F5 exploitation retained awareness of diminishing returns and boundary concentration.
- F1 exploration was justified by repeated low information from the current region.
- Negative values were interpreted relative to prior observations, not automatically treated as failures.

## Limitations of validation

Validation cannot confirm global optimality because the objective functions, gradients and true optima are hidden. The small adaptive dataset also limits statistical inference. The checks therefore establish reproducibility, consistency and defensible decision logic rather than mathematical proof of optimality.

## Reproduction

Run:

- `week_09_analysis.py`
- `generate_week_09_figures.py`

Then compare generated summaries and figures with the committed Week 09 outputs. Any discrepancy should be investigated before later weekly documentation is finalised.

## Validation outcome

Week 09 passed the structural and internal consistency checks. The differentiated strategy of exploit, refine, reassess and explore was consistent with the available evidence and appropriate for progression to Week 10.
