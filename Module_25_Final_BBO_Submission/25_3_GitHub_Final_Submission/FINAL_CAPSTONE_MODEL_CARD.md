# Final Capstone Model Card

## System purpose

The capstone workflow is a human-supervised sequential optimisation process for eight independent hidden objective functions. Its purpose is to select one query vector per function from the evidence available at each round, then update the next decision after the returned objective values become known.

## Inputs

The final workflow draws on verified historical query vectors and outputs, function dimensionality, recent improvement or deterioration, stronger historical regions, repeated coordinates, local distance, boundary behaviour, clustering-informed regional structure, PCA-informed trajectory structure and final exploration versus exploitation reasoning.

## Decision framework

No single optimisation rule is assumed to suit all eight functions. The workflow chooses among broad exploration, local refinement, controlled exploitation, recovery to a stronger historical basin, boundary testing and stopping according to the evidence for each objective.

Clustering and PCA are supporting analytical methods. They organise the observed search history but do not reveal the hidden functions directly. Reinforcement-learning, multi-armed-bandit, MDP and Q-learning concepts are used in the final stage as decision lenses for sequential reward and exploration versus exploitation, not as a claim that a trained RL agent generated the historical queries.

## Final observed performance

Round 13 produced new overall best values for F3, F5 and F6. F1, F4, F7 and F8 retained their strongest verified values. F2 declined from its Week 12 peak, leaving Week 12 as its strongest verified coordinate.

The final winner table is stored in `../Final_13_Round_Evidence/FINAL_RESULTS_SUMMARY.csv`.

## Strengths

The workflow preserves the chronology of the experiment, retains unsuccessful queries as evidence, treats functions separately, separates direct objective evidence from structural interpretation and records exact numerical values. It also provides explicit reasons for changing direction and for stopping.

## Failure modes and safeguards

A local trend can reverse, as shown by F2 in Week 13. A productive region can be missed if exploration continues too long after a strong basin has been identified, as the F4 history illustrates. Boundary concentration can encourage excessive exploitation, so continued movement is justified only while returned values continue to improve. F6 shows that identical recorded inputs need not return identical values, so deterministic repeatability cannot be assumed universally.

## Human oversight

Final query selection remains human-supervised. Code calculates comparisons, validates dimensions and values, performs structural analyses and generates figures, but the scripts do not independently submit queries to the Imperial evaluator.

## Reproducibility

The closing analysis is reproduced from the repository root with:

```bash
python Week_13/week_13_analysis.py
python Week_13/generate_week_13_figures.py
```

The analysis reads the committed weekly source files and produces the Week 13 derived summaries and figures. The source inputs and returned values are not modified by the workflow.

## Intended interpretation

The model card supports claims about the observed thirteen-round optimisation process and the strongest verified coordinates found within it. It does not claim access to the hidden mathematical objectives or prove global optima.

## Post-capstone research boundary

SOC and the Advanced Extension Series begin after the assessed thirteen-round experiment. Their surrogate predictions and extension candidates are separately labelled and must not be interpreted as historical capstone outputs.
