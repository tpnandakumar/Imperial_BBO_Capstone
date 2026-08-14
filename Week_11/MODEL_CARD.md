# Week 11 Model Card

## Model purpose

The Week 11 optimisation workflow is a human supervised sequential decision process for eight hidden objective functions. It uses verified historical inputs and outputs to decide whether each function should be repeated, refined, recovered towards an earlier strong region or explored differently.

## Week 11 role

Week 11 is primarily an outcome test of the strategy developed in Week 10. The Week 10 analysis used clustering, regional proximity and historical performance to choose the Week 11 queries. Once the Week 11 outputs were returned, the workflow was extended with principal component analysis to prepare the Week 12 decision.

## Inputs

The workflow uses:

- verified query vectors from the previous rounds;
- verified returned objective values;
- function dimensionality;
- distance to stronger historical points;
- repeated observations;
- local improvement or deterioration;
- principal component structure of the accumulated query trajectories for Functions 3 to 8.

## Outputs

The workflow produces:

- a function specific interpretation of the Week 11 result;
- comparison with Week 10;
- identification of new, repeated or recovered strong regions;
- a PCA based description of query trajectory concentration;
- a strategy comparison for the Week 12 query decision.

## Week 11 performance

Every Week 11 objective improved relative to Week 10.

| Function | Week 10 output | Week 11 output | Interpretation |
| --- | ---: | ---: | --- |
| Function 1 | `2.8950706668499033e-23` | `0.025559285339829783` | Prior best reproduced |
| Function 2 | `0.5311818841205426` | `0.5848554940277205` | New verified best |
| Function 3 | `-0.08697581687486715` | `-0.06542982421105416` | Recovery towards stronger region |
| Function 4 | `-13.483642655031158` | `-4.868852987697114` | Large recovery |
| Function 5 | `4394.868042481448` | `4411.0387356061765` | New verified best |
| Function 6 | `-1.2283806967341901` | `-0.7268715077444687` | Clear recovery |
| Function 7 | `1.285160161342515` | `1.3579108517237013` | Strong positive region retained |
| Function 8 | `9.4646525` | `9.58024` | Prior best reproduced |

## PCA extension

Centred PCA was applied to the accumulated input histories for Functions 3 to 8 after the Week 11 outputs were available. The analysis found that the recorded query paths were concentrated in one or two principal directions.

This was treated as structural evidence, not as a direct optimiser. The principal components describe variation in submitted coordinates. They do not automatically identify directions that maximise the hidden functions.

For Week 12, PCA was therefore compared with direct objective evidence. Function 5 was the clearest case where structural concentration and objective improvement pointed in the same direction. For several other functions, the known historical best point was stronger evidence than principal component extrapolation.

## Human supervision

Final strategy classification and query selection remain human supervised. Numerical scripts validate the data, calculate exact changes, measure distances and perform PCA, but they do not independently submit queries.

## Strengths

The Week 11 workflow has several practical strengths:

- it treats each function separately;
- it preserves exact numerical evidence;
- it distinguishes repeated performance from new improvement;
- it uses unsuccessful earlier moves to support recovery decisions;
- it compares a newly introduced analytical method with existing evidence rather than adopting it automatically;
- it keeps the final submission decision separate from the supporting calculations.

## Limitations

The optimisation history is small and adaptively sampled. PCA results can be influenced by the search strategy that generated the coordinates. The workflow cannot identify gradients, prove global optima or guarantee that a local improvement will continue.

The eight functions also operate on different scales. Cross function numerical ranking should therefore not be interpreted as a common performance measure.

## Reproducibility

The main reproducible files are:

- `week_11_inputs.csv`
- `week_11_results.csv`
- `week_11_analysis.py`
- `week_11_analysis_summary.csv`
- `generate_week_11_figures.py`
- `week_11_figure_data_summary.csv`
- `PCA_STRATEGY_COMPARISON.md`
- `WEEK_12_DECISION_RECORD.md`

The Week 11 analysis and figure scripts can be run from the repository root. The source input and output files remain unchanged by those calculations.

## Responsible interpretation

The Week 11 record supports statements about the observed queries and returned values only. It does not reveal the hidden mathematical functions. Later results can strengthen or weaken the Week 12 strategy, but they do not alter what was known when the Week 12 queries were selected.