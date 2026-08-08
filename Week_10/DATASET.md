# Week 10 Dataset Record

## Purpose

This file provides a concise technical description of the verified dataset used for the Week 10 Bayesian Black Box Optimisation analysis. It complements the full [Datasheet](DATASHEET.md), which provides the broader documentation required for interpretation, provenance and responsible use.

## Dataset state

At the end of Week 10, the cumulative optimisation record contained ten submitted query vectors and ten returned objective values for each of the eight hidden functions. This corresponds to 80 submitted query vectors and 80 returned objective values across the portfolio.

The functions retain their fixed dimensionalities throughout the capstone:

| Function | Dimensions | Observations through Week 10 |
| --- | ---: | ---: |
| Function 1 | 2 | 10 |
| Function 2 | 2 | 10 |
| Function 3 | 3 | 10 |
| Function 4 | 4 | 10 |
| Function 5 | 4 | 10 |
| Function 6 | 5 | 10 |
| Function 7 | 6 | 10 |
| Function 8 | 8 | 10 |

## Authoritative Week 10 files

The submitted vectors are stored in [week_10_inputs.csv](week_10_inputs.csv). The returned objective values are stored in [week_10_results.csv](week_10_results.csv). These two files are the authoritative Week 10 numerical record.

Derived analytical files are:

- [week_10_analysis_summary.csv](week_10_analysis_summary.csv)
- [week_10_figure_data_summary.csv](week_10_figure_data_summary.csv)
- [week_10_analysis.py](week_10_analysis.py)
- [generate_week_10_figures.py](generate_week_10_figures.py)

Derived files do not replace or modify the source observations.

## Week 10 observations

| Function | Returned objective value |
| --- | ---: |
| Function 1 | 2.8950706668499033e-23 |
| Function 2 | 0.5311818841205426 |
| Function 3 | -0.08697581687486715 |
| Function 4 | -13.483642655031158 |
| Function 5 | 4394.868042481448 |
| Function 6 | -1.2283806967341901 |
| Function 7 | 1.285160161342515 |
| Function 8 | 9.4646525 |

## Interpretation boundary

The dataset records observed input and output pairs only. It does not reveal the mathematical form of any hidden function, the gradients of those functions, or the location of a global optimum. Strategy labels, rankings and conclusions are derived interpretations of the recorded observations and should be evaluated separately from the raw data.

## Week 10 significance

Week 10 added a useful mixture of positive, negative and repeatability evidence. Functions 2 and 3 improved relative to Week 09. Function 5 returned exactly `4394.868042481448` again at the repeated Week 09 input, providing direct evidence of repeatability at that tested point. Functions 4, 6, 7 and 8 declined, while Function 1 remained effectively unresolved near zero.

This combination made Week 10 particularly useful for distinguishing between immediate objective improvement and information gained from an unsuccessful or repeated query.