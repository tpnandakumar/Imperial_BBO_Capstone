# Week 09 Dataset

## Identification

- Course module: 21
- Capstone week: 09
- Optimisation round: 9
- Dataset state: completed Week 09 inputs and outputs
- Maintainer: Dr N T Pisharam
- Related context document: [DATASHEET.md](DATASHEET.md)

## Purpose

This document describes the data files contained in `Week_09`. The accompanying datasheet explains why the data was collected, how the queries were selected, the assumptions made and the appropriate uses of the data.

## Core files

| File | Role | Records |
|---|---|---:|
| `week_09_inputs.csv` | Submitted query vector for each hidden function | 8 |
| `week_09_results.csv` | Returned objective value for each hidden function | 8 |
| `week_09_analysis_summary.csv` | Rank, strategy and status derived from the outputs | 8 |
| `week_09_figure_data_summary.csv` | Structured values used to reproduce figures | See file |

## Schema

### `week_09_inputs.csv`

- `Function`: identifier from Function 1 to Function 8
- `Input`: comma-separated numeric vector, with each coordinate constrained to `[0,1]`

Function dimensions are:

| Function | Dimensions |
|---|---:|
| F1 | 2 |
| F2 | 2 |
| F3 | 3 |
| F4 | 4 |
| F5 | 4 |
| F6 | 5 |
| F7 | 6 |
| F8 | 8 |

### `week_09_results.csv`

- `Function`: function identifier
- `Output`: scalar objective value returned by the black box

### `week_09_analysis_summary.csv`

- `Function`
- `Output`
- `Rank`
- `Strategy`: Exploit, Refine, Explore or Reassess
- `Status`: Positive, Negative or Near Zero

## Week 09 observations

The Week 09 outputs were:

| Function | Output |
|---|---:|
| F1 | -1.4546199699251391e-58 |
| F2 | 0.47297842839949866 |
| F3 | -0.1156707106126581 |
| F4 | -11.788939969158545 |
| F5 | 4394.868042481448 |
| F6 | -1.1733030029888645 |
| F7 | 1.314307996450604 |
| F8 | 9.4709436 |

## Completeness and gaps

All eight functions have one Week 09 input and one corresponding output. The hidden function definitions, gradients, noise model and global optima are unavailable by design. The dataset is therefore complete for the submitted round but incomplete as a representation of the full search landscape.

## Transformations

Raw inputs and outputs are preserved. Derived files add ranking, status and strategy labels. No transformation is applied to the objective values in the core results file.

## Data quality checks

- Exactly eight function records are required.
- Input dimensionality must match the function specification.
- Every coordinate must lie within `[0,1]`.
- Submission coordinates use six decimal places.
- Every input must have one returned output.
- Derived summaries must agree with `week_09_results.csv`.

## Reproduction

Use `week_09_analysis.py` and `generate_week_09_figures.py` to reproduce the analysis and visual outputs. Interpretive context, limitations and collection rationale are documented in [DATASHEET.md](DATASHEET.md).
