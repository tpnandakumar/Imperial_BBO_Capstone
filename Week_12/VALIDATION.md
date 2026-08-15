# Week 12 Validation Record

## Verified source record

The authoritative Week 12 source files are:

- `week_12_inputs.csv`
- `week_12_results.csv`

The analysis validates eight functions, their required dimensions, the coordinate range from 0 to 1, exact stored inputs and exact returned outputs.

## Reproducible checks

`week_12_analysis.py` performs exact decimal comparison before converting coordinates to floating point values for PCA. The conversion is limited to numerical decomposition and plotting.

The script compares Week 12 with Week 11 within each function, checks the previous best output and writes two derived files:

- `week_12_analysis_summary.csv`
- `week_12_pca_summary.csv`

`generate_week_12_figures.py` then creates the figure data summary and four analytical figures.

## Limitation

The sample contains only twelve adaptively selected observations per function. PCA findings describe the observed query path and must not be presented as proof of the hidden objective surface, global optimality or the correct Week 13 query.
