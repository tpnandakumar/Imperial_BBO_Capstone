# Module 25 Figure Status

## Week 13 analytical figures

The final Week 13 figure-generation script defines four evidence-based analytical figures:

1. `week_13_figure_1_final_change.png` shows the objective change from Week 12 to Week 13.
2. `week_13_figure_2_normalised_progress.png` shows within-function normalised performance across the thirteen rounds.
3. `week_13_figure_3_function_5_trajectory.png` shows the Function 5 optimisation trajectory.
4. `week_13_figure_4_latest_best_round.png` shows the latest round in which each final best was observed.

These PNG files are generated outputs rather than authoritative source data. They are reproduced from committed input and result evidence by `Week_13/generate_week_13_figures.py`. The final repository audit workflow now checks that all four are generated successfully and are non-empty.

## Module 25 reflection infographics

The final 25.1 and 25.2 reflection infographics are intentionally not fixed yet because the assessment prompts and rubrics remain locked. Their numerical and analytical sources are already mapped in `INFOGRAPHIC_SOURCE_MAP.md`.

Once the prompts unlock, each final infographic should answer a specific part of the assessment, use verified capstone evidence, contain an embedded caption and avoid visible rubric labels. Any normalisation or derived measure used in a graphic must be stated explicitly.

## Audit finding

The Week 13 PNG files are not currently stored as static repository artefacts. This is deliberate at this preparation stage because they are reproducibly generated from the committed source evidence. If the final 25.3 rubric explicitly requires figures to be present as files rather than reproducible outputs, the generated PNGs should be committed before submission.
