# SOE Experiment 001: Week 11 Validation

## 1. Objective

This experiment evaluated whether the Strategic Optimisation Engine, version 1.0, could improve the Week 10 results by using the complete Weeks 1 to 10 optimisation history.

## 2. Experimental basis

The engine treated each black box function separately. It combined exact historical best point recovery, local trust region probes, best basin recovery and one controlled boundary directed exploration for Function 5.

The experiment used the verified Week 11 submission recorded in `week_11_inputs.csv`. The returned values are preserved exactly in `week_11_results.csv`.

## 3. Week 11 strategy

| Function | Strategy |
|---|---|
| Function 1 | Exploit confirmed narrow peak |
| Function 2 | Local trust region probe |
| Function 3 | Local refinement |
| Function 4 | Local recovery probe |
| Function 5 | Boundary directed probe |
| Function 6 | Best basin recovery |
| Function 7 | Tight trust region refinement |
| Function 8 | Exploit confirmed best |

## 4. Results

Every Week 11 output improved relative to Week 10.

| Function | Week 10 output | Week 11 output | Exact change |
|---|---:|---:|---:|
| Function 1 | 2.8950706668499033e-23 | 0.025559285339829783 | 0.02555928533982978299997104929 |
| Function 2 | 0.5311818841205426 | 0.5848554940277205 | 0.0536736099071779 |
| Function 3 | -0.08697581687486715 | -0.06542982421105416 | 0.02154599266381299 |
| Function 4 | -13.483642655031158 | -4.868852987697114 | 8.614789667334044 |
| Function 5 | 4394.868042481448 | 4411.0387356061765 | 16.1706931247285 |
| Function 6 | -1.2283806967341901 | -0.7268715077444687 | 0.5015091889897214 |
| Function 7 | 1.285160161342515 | 1.3579108517237013 | 0.0727506903811863 |
| Function 8 | 9.4646525 | 9.58024 | 0.1155875 |

## 5. Interpretation

The experiment supports the use of a structured decision framework for the final stages of the capstone. Historical best point recovery was effective for Functions 1 and 8. Recovery towards earlier high performing regions produced substantial gains for Functions 4 and 6. Local refinement improved Functions 2, 3 and 7. The controlled Function 5 boundary probe established a new confirmed best output of `4411.0387356061765`.

These findings validate the Week 11 decision process within this competition. They do not establish that the engine is universally superior to Bayesian optimisation or other established methods.

## 6. Reproducibility

The original engine code is stored in `strategic_optimisation_engine_v1.py`. The exact submitted inputs, returned outputs and Week 10 comparison are stored as CSV files in this directory.

The source datasets and scripts are authoritative. No values have been rounded or truncated.
