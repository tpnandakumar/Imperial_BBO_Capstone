# Week 10 Research Note

## Identification

- Course module: 21
- Capstone week: 10
- Optimisation round: 10
- Maintainer: Dr N T Pisharam
- Purpose: concise narrative account of the evidence, assumptions, decisions and next steps for this round

## 1. What was known before this round?

By the end of Week 09, the eight hidden functions showed clearly different optimisation profiles. Function 5 remained the dominant performer and had improved to 4394.868042481448. Functions 7 and 8 were stable positive performers, Function 2 remained positive but had declined from its Week 08 value, Function 4 had improved while remaining negative, Functions 3 and 6 remained uncertain within negative regions, and Function 1 continued to return a value effectively equal to zero.

This evidence supported a differentiated Week 10 strategy rather than applying the same search rule to every function.

## 2. What evidence changed the strategy?

Week 09 reinforced the value of exploiting Function 5 but also indicated diminishing returns near its best known boundary region. Functions 2, 7 and 8 remained suitable for cautious refinement because their broader regions still appeared productive. Function 4 justified one further local test after moving towards a less negative result. Functions 3 and 6 lacked a stable improvement direction and therefore required reassessment. Function 1 remained the principal exploration target because repeated local evidence did not reveal a useful signal.

The resulting Week 10 submission deliberately separated exploitation, refinement, reassessment and exploration.

## 3. What assumptions were made?

The Week 10 strategy depended on several explicit assumptions:

1. larger objective values were preferable for every function;
2. repeated local improvement suggested useful neighbouring structure;
3. an unchanged result at an identical query provided evidence of repeatability;
4. a small decline in a previously productive region did not automatically invalidate that region;
5. broader movement was justified where repeated outputs remained effectively uninformative;
6. the hidden functions could be locally irregular, so no local trend was treated as proof of global behaviour.

These assumptions guided query selection but also limited the certainty of the conclusions.

## 4. Why were the Week 10 queries chosen?

### Function 1

A broader two-dimensional move was chosen because the previous region repeatedly returned values near zero. Continued local refinement would have added little information.

### Function 2

A controlled local refinement was selected because the function remained positive despite its Week 09 decline. The aim was to test whether the productive region could be recovered.

### Function 3

A nearby alternative was chosen because the function remained negative but showed enough local variation to justify further targeted investigation.

### Function 4

A local movement was selected after the Week 09 improvement. The purpose was to test whether the favourable direction persisted rather than assume it would continue.

### Function 5

The Week 09 best input was repeated exactly. This was a deliberate stability test before making further boundary adjustments.

### Function 6

A nearby alternative was tested because recent results remained negative and the local direction was uncertain.

### Function 7

A small refinement was used to preserve a productive positive region while testing whether a marginal gain remained available.

### Function 8

Only a minimal local adjustment was made because the function was already high and stable, making large movement unnecessarily risky.

## 5. What did Week 10 show?

Function 2 improved to 0.5311818841205426 and Function 3 improved to -0.08697581687486715. Function 5 reproduced its Week 09 maximum exactly, supporting repeatability at that point. Function 1 remained effectively near zero despite broader exploration. Functions 4, 6, 7 and 8 declined, although the changes in Functions 7 and 8 were small.

The most important lesson was that not every informative query improves the objective value. The Function 5 repeat confirmed stability, while the Function 4 decline ruled out an immediate continuation in that direction.

## 6. What should the next round investigate?

Week 11 should preserve the strongest validated evidence while changing direction where the Week 10 result weakened confidence.

- Keep Function 5 within a very small neighbourhood of the stable boundary point.
- Confirm the improved Function 2 region.
- Continue targeted refinement of Function 3.
- Redirect Functions 4 and 6 rather than continue the same local movement.
- Retain conservative adjustments for Functions 7 and 8.
- Continue broad exploration for Function 1.

## Transparency and reproducibility

This note should be read alongside:

- [Week 10 section guide](SECTION_GUIDE.md)
- [week_10_inputs.csv](week_10_inputs.csv)
- [week_10_results.csv](week_10_results.csv)
- [week_10_analysis_summary.csv](week_10_analysis_summary.csv)
- [week_10_analysis.py](week_10_analysis.py)
- [generate_week_10_figures.py](generate_week_10_figures.py)

The note records the reasoning behind the round. The CSV files preserve the evidence, while the Python scripts reproduce the comparisons and figures.

