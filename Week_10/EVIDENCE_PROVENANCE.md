# Week 10 Evidence and Provenance Matrix

## Purpose

This document connects the principal Week 10 analytical claims to the verified records from which they were derived. It is intended to make the assessment trail explicit and to distinguish direct observations from interpretation.

## Evidence hierarchy

Primary evidence consists of submitted query vectors and returned objective values. Derived evidence consists of exact comparisons, rankings and reproducible summaries generated from those records. Interpretive evidence consists of strategy labels and decisions based on the primary and derived evidence.

## Provenance matrix

| Claim | Primary evidence | Derived evidence | Interpretation |
| --- | --- | --- | --- |
| Function 1 remained unresolved near zero | Week 09 output `-1.4546199699251391e-58`; Week 10 output `2.8950706668499033e-23` | Exact Week 09 to Week 10 change `2.895070666849903300000000000E-23` | Continue exploration rather than treating the sign change as a meaningful optimum |
| Function 2 improved | Week 09 output `0.47297842839949866`; Week 10 output `0.5311818841205426` | Exact change `0.05820345572104394` | Confirm and refine the productive local direction |
| Function 3 improved | Week 09 output `-0.1156707106126581`; Week 10 output `-0.08697581687486715` | Exact change `0.02869489373779095` | Continue targeted refinement while recognising that the output remains negative |
| Function 4 Week 10 movement was unsuccessful | Week 09 output `-11.788939969158545`; Week 10 output `-13.483642655031158` | Exact change `-1.694702685872613` | Reassess and change direction rather than continue the same movement |
| Function 5 repeated the Week 09 result exactly | Week 09 input and Week 10 input both `0.120000,0.997000,0.999800,0.999800`; both outputs `4394.868042481448` | Exact change `0` | Evidence of repeatability at the exact tested point, supporting precise exploitation |
| Function 6 declined | Week 09 output `-1.1733030029888645`; Week 10 output `-1.2283806967341901` | Exact change `-0.0550776937453256` | Reassess the local direction |
| Function 7 remained positive but declined | Week 09 output `1.314307996450604`; Week 10 output `1.285160161342515` | Exact change `-0.029147835108089` | Conservative refinement rather than aggressive movement |
| Function 8 remained positive but declined slightly | Week 09 output `9.4709436`; Week 10 output `9.4646525` | Exact change `-0.0062911` | Monitor and refine cautiously |

## Source locations

The Week 10 submitted vectors are stored in [week_10_inputs.csv](week_10_inputs.csv). Week 10 returned values are stored in [week_10_results.csv](week_10_results.csv). Week 09 returned values used for comparison are stored in `../Week_09/week_09_results.csv`.

The reproducible Week 10 comparison is produced by [week_10_analysis.py](week_10_analysis.py) and recorded in [week_10_analysis_summary.csv](week_10_analysis_summary.csv). Figure source data are recorded separately in [week_10_figure_data_summary.csv](week_10_figure_data_summary.csv).

## Decision provenance chain

```text
Verified Week 09 evidence
        |
        v
Week 10 query hypothesis
        |
        v
Verified Week 10 submitted query
        |
        v
Verified Week 10 returned result
        |
        v
Exact comparison and validation
        |
        v
Interpretation and strategy classification
        |
        v
Verified Week 11 query decision
```

The chain records how evidence informed the next decision. It does not imply that the hidden functions were known or that any selected query was mathematically optimal.

## Provenance boundary

Later research developments are not used as retrospective evidence for Week 10 unless they are explicitly documented as contemporaneous inputs to the Week 10 decision. This preserves the chronology of the capstone and prevents later methods from being attributed to earlier optimisation rounds.