# Week 08 Dataset

## Metadata

- **Course module:** 20
- **Capstone week:** 08
- **Optimisation round:** 8
- **Dataset version:** 08.1
- **Related datasheet:** [DATASHEET.md](DATASHEET.md)
- **Maintainer:** Dr N T Pisharam
- **Repository:** `tpnandakumar/Imperial_BBO_Capstone`

## Purpose

This file describes the data artefacts used for Capstone Week 08. It explains what data are present, how they are organised and how they support reproduction of the Week 08 analysis. The accompanying [DATASHEET.md](DATASHEET.md) explains why the data were created, how they were collected, the assumptions behind the query strategy and the appropriate conditions of use.

## Dataset scope

The Week 08 dataset records the eighth submitted query round for eight hidden objective functions together with the returned objective values and the analytical artefacts used to compare Week 08 with earlier rounds.

The function dimensionalities are:

| Function | Input dimensions |
|---|---:|
| F1 | 2 |
| F2 | 2 |
| F3 | 3 |
| F4 | 4 |
| F5 | 4 |
| F6 | 5 |
| F7 | 6 |
| F8 | 8 |

All query coordinates are constrained to the interval `[0,1]` and are represented to six decimal places in the capstone submission format.

## Core files

The Week 08 folder contains the following principal artefacts:

- `README.md`: narrative Week 08 analysis and interpretation.
- `week_08_inputs.csv`: submitted query coordinates for Functions 1 to 8.
- `week_08_results.csv`: returned Week 08 objective values.
- `week_08_analysis.py`: programmatic comparison and analytical calculations.
- `generate_week_08_figures.py`: reproducible figure generation.

The repository may also contain generated figures and linked image assets referenced from the Week 08 README.

## Record structure

### Input data

The input dataset contains one submitted query per function for the Week 08 round. Each row should identify the function and preserve the required dimensionality and six decimal place precision.

### Output data

The results dataset contains one returned objective value per function. Week 08 outputs recorded in the repository analysis are:

| Function | Week 08 output |
|---|---:|
| F1 | -1.4546199699251391e-58 |
| F2 | 0.5672775862793291 |
| F3 | -0.0991107637427902 |
| F4 | -12.305008897187289 |
| F5 | 4359.384134322703 |
| F6 | -1.1197178425911847 |
| F7 | 1.3346391663186332 |
| F8 | 9.47621 |

## Data relationships

The input and output files are paired by function identifier:

```text
week_08_inputs.csv
        ↓ function identifier
week_08_results.csv
        ↓
week_08_analysis.py
        ↓
README.md and generated figures
```

The input file explains what was submitted. The results file records what the black box returned. The datasheet explains the rationale, collection process, assumptions and limitations behind both.

## Derived data

Derived values include:

- Week 07 to Week 08 absolute changes.
- Relative improvements where meaningful.
- Function performance rankings.
- Exploration, refinement and exploitation classifications.
- Query priority and information gain interpretations.

Derived values must remain traceable to the original Week 08 inputs and outputs.

## Known gaps and limitations

- The hidden objective functions are not available.
- Gradients, internal parameters and response surface equations are unknown.
- Only one submitted query per function is available for the Week 08 round.
- Comparisons across functions must account for their different scales.
- A high objective value does not by itself prove that a global optimum has been reached.
- The dataset supports sequential optimisation analysis, not causal inference.

## Reproduction

1. Confirm that the Week 08 input and result CSV files are present.
2. Run `week_08_analysis.py` to reproduce analytical summaries.
3. Run `generate_week_08_figures.py` to regenerate figures.
4. Compare generated outputs with the interpretations in `README.md`.
5. Consult [DATASHEET.md](DATASHEET.md) before reusing or interpreting the data.

## Intended use

This dataset is intended for:

- documenting the Week 08 BBO submission;
- reproducing Week 08 calculations and figures;
- comparing Week 08 with earlier and later rounds;
- supporting transparent query selection for Week 09;
- teaching and research on sequential black box optimisation.

It is not intended to establish the true functional form of any hidden objective function or to support claims beyond the available observations.
