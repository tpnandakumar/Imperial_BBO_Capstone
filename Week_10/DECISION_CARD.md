# Week 10 Decision Card

## Decision context

Week 10 produced a mixed but strategically useful result. The purpose of this card is to record how the verified Week 10 evidence informed the next query decision without rewriting the historical observations after later results became known.

## Evidence summary

| Function | Week 10 output | Week 10 evidence | Decision after Week 10 |
| --- | ---: | --- | --- |
| Function 1 | 2.8950706668499033e-23 | Still effectively zero | Explore |
| Function 2 | 0.5311818841205426 | Improved | Confirm and refine |
| Function 3 | -0.08697581687486715 | Improved within negative region | Targeted refinement |
| Function 4 | -13.483642655031158 | Substantial deterioration | Reassess and change direction |
| Function 5 | 4394.868042481448 | Exact repeat of Week 09 leading value | Precise exploitation |
| Function 6 | -1.2283806967341901 | Declined | Reassess |
| Function 7 | 1.285160161342515 | Positive but lower | Conservative refinement |
| Function 8 | 9.4646525 | Stable positive region, small decline | Conservative refinement |

## Portfolio decision

The Week 10 evidence did not support a single optimisation strategy across all eight functions. The next submission therefore required a portfolio approach.

Function 5 had the strongest evidence for exploitation because its leading output repeated exactly at the same input. Function 2 justified continued local work because the latest movement improved the objective. Function 3 also supported targeted refinement, although its output remained negative.

Functions 4 and 6 required a change in direction because their Week 10 movements were unsuccessful. Continuing automatically along the same local path would have ignored the new evidence. Functions 7 and 8 remained productive but their small declines favoured conservative rather than aggressive movement. Function 1 remained unresolved and therefore retained an exploratory role.

## Information value

The Week 10 decision was influenced by information gain as well as immediate objective value. The Function 5 repeat reduced uncertainty about the reproducibility of the tested point. The Function 4 decline provided evidence against continuing the same local direction. The Function 2 and Function 3 improvements strengthened their respective local search hypotheses.

This distinction is important because a sequential optimisation query can be valuable even when it does not improve the objective, provided that it changes the evidence available for the next decision.

## Verified Week 11 query selected after Week 10

| Function | Week 11 query |
| --- | --- |
| Function 1 | 0.600000,0.600000 |
| Function 2 | 0.695000,0.950000 |
| Function 3 | 0.840000,0.160000,0.840000 |
| Function 4 | 0.620000,0.420000,0.440000,0.250000 |
| Function 5 | 0.110000,0.998000,0.999900,0.999900 |
| Function 6 | 0.720000,0.190000,0.700000,0.710000,0.150000 |
| Function 7 | 0.045000,0.485000,0.255000,0.220000,0.420000,0.745000 |
| Function 8 | 0.060000,0.070000,0.030000,0.040000,0.410000,0.820000,0.500000,0.910000 |

## Decision boundary

This card records the reasoning supported by the Week 10 evidence. It does not claim that the selected Week 11 queries were mathematically optimal. The hidden functions remained unknown, and the final query choices were human supervised decisions made under a limited query budget.