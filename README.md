# Imperial BBO Capstone

## Bayesian Black Box Optimisation Portfolio

**Author:** Dr Nandakumar Theekkootu Pisharam  
**Programme:** Imperial College Business School Artificial Intelligence and Machine Learning Programme  
**Repository status:** Public  
**Default branch:** `main`

## Assessment navigation

The assessed capstone work is organised through the weekly BBO folders. Each completed round preserves the submitted inputs, returned outputs, analysis, figures and the reasoning used to select the next queries.

Key assessment links:

- [Week 09: Module 21 analysis](Week_09/README.md)
- [Week 09 Datasheet](Week_09/DATASHEET.md)
- [Week 09 Model Card](Week_09/MODEL_CARD.md)
- [Week 10: Component 22.1 clustering and strategy refinement](Week_10/README.md)
- [Week 11: PCA comparison and Week 12 decision pathway](Week_11/README.md)
- [Week 12: verified outcome and capstone reflection](Week_12/README.md)
- [Component 23.1: completed capstone reflection](Week_12/COMPONENT_23_1_CAPSTONE_REFLECTION.md)
- [Week 13: final round analysis](Week_13/README.md)
- [Week 25: Final BBO Submission synthesis](Week_25_Final_BBO_Submission/README.md)

The Week 25 section is a final synthesis of the completed thirteen round BBO record. It is not an additional optimisation round. It brings together the function specific evidence, strategies used, reasons for changing strategy, final stopping logic and the relationship between the assessed capstone and the later research extension.

The `PGC` and `PFRAMOS` directories contain supplementary research that developed from questions raised during the capstone. They support the project but do not replace the weekly assessed record. See [Extended Research and Validation](EXTENDED_RESEARCH_AND_VALIDATION.md).

## Project overview

The challenge contains eight hidden objective functions with dimensionalities ranging from two to eight variables. One query vector is submitted for each function during every optimisation round. Because the mathematical form of each function is unknown, decisions are based on previously observed inputs and returned objective values.

The repository preserves the full optimisation history rather than presenting only the best final results. Unsuccessful queries are retained because they also provide evidence. A deterioration can rule out a direction, a repeated output can support stability, and a return to an earlier strong point can test reproducibility.

The strategy developed from broad exploration towards function specific refinement, recovery, controlled exploitation, boundary testing, PCA comparison and final reward based decision review.

## Current position

All thirteen rounds are complete. The final round produced new overall best values for Functions 3, 5 and 6. Functions 1, 4, 7 and 8 retained their strongest observed values exactly. Function 2 finished below its Week 12 peak.

| Function | Final output | Final interpretation |
| --- | ---: | --- |
| F1 | 0.025559285339829783 | Best retained exactly |
| F2 | 0.6413430885133908 | Below Week 12 best of 0.7335252043269003 |
| F3 | -0.05685061601567621 | New overall best |
| F4 | -4.359874926582439 | Best retained exactly |
| F5 | 4440.957216598753 | New overall best |
| F6 | -0.6071562248604215 | New overall best |
| F7 | 1.3809299933612855 | Best retained exactly |
| F8 | 9.58024 | Best retained exactly |

The final record does not prove global optimality. It identifies the strongest values observed within the thirteen submitted rounds and records the evidence used to interpret them.

## Function dimensionality

| Function | Dimensions |
| --- | ---: |
| Function 1 | 2 |
| Function 2 | 2 |
| Function 3 | 3 |
| Function 4 | 4 |
| Function 5 | 4 |
| Function 6 | 5 |
| Function 7 | 6 |
| Function 8 | 8 |

Every coordinate lies between 0 and 1 and is submitted to six decimal places.

## Strategy framework

Later rounds used four broad actions rather than applying one treatment to every function:

- **Explore:** move to a meaningfully different region when earlier observations remain uninformative.
- **Refine:** make controlled local changes where evidence supports a productive neighbourhood.
- **Reassess or recover:** change direction after deterioration or move back towards a stronger historical basin.
- **Exploit or boundary test:** stay close to a well supported region while testing whether further improvement remains available.

Academic feedback also led to clearer checks for excessive exploitation. Later rounds considered plateau length, diminishing improvement, repeated local concentration, material deterioration, boundary concentration and weak wider search space coverage before continuing to tighten around a strong region.

## Module 21: transparency and interpretability

Module 21 corresponds to Week 09. The required documentation is stored separately so that the dataset and optimisation workflow can be reviewed directly.

- [Datasheet](Week_09/DATASHEET.md)
- [Model Card](Week_09/MODEL_CARD.md)
- [Week 09 supporting analysis](Week_09/README.md)

The Datasheet records provenance, composition, collection, preprocessing, quality assurance, bias, limitations, transparency and maintenance. The Model Card records the workflow, inputs, outputs, performance, assumptions, failure modes, human oversight and reproducibility, including an F1 to F8 performance summary and explicit workflow versioning.

## Component 22.1: clustering lens

[Week 10](Week_10/README.md) records the clustering based reflection used to prepare the Week 11 query set. The analysis does not claim statistically validated clusters from sparse data. It uses recurring local regions, distance between queries, stability of neighbouring outputs and boundary behaviour as practical cues.

The Week 10 documentation also records why weaker directions were stopped rather than continued automatically.

## Final analytical progression

Week 11 added PCA as a structural comparison method. Week 12 tested a function specific combination of confirmed best points, local refinement, historical recovery and boundary movement. Week 13 then completed the process by evaluating the final actions through the complete thirteen round history and the exploration versus exploitation ideas introduced in Module 24.

The final analysis also identified an important exception to simple repeatability assumptions. Function 6 returned different values at the same recorded coordinate across Weeks 3, 12 and 13, so fixed input repeatability cannot be assumed for every objective.

## Week 25 final synthesis

[Week 25: Final BBO Submission](Week_25_Final_BBO_Submission/README.md) provides the assessment facing synthesis of the complete BBO project. It explains, function by function, what strategy was used, why it was chosen, how the strategy was applied, when the decision changed and what evidence caused the change.

It also records the final stopping logic and separates the assessed thirteen round BBO record from the post capstone Advanced Extension Series.

## Advanced Extension Series

The [Advanced Extension Series](Advanced_Extension_Series/README.md) begins only after the official capstone sequence. Its first analytical stage is [SOC 1: Surrogate Optimisation Competition](Advanced_Extension_Series/SOC_Surrogate_Optimisation_Competition/README.md).

SOC makes several surrogate model families compete independently for Functions 1 to 8 using held out predictive performance. It is a post capstone research competition and does not alter the original Week 01 to Week 13 record.

## Weekly record

| Round | Documentation |
| --- | --- |
| Week 01 | [README](Week_01/README.md) |
| Week 02 | [README](Week_02/README.md) |
| Week 03 | [README](Week_03/README.md) |
| Week 04 | [README](Week_04/README.md) |
| Week 05 | [README](Week_05/README.md) |
| Week 06 | [README](Week_06/README.md) |
| Week 07 | [README](Week_07/README.md) |
| Week 08 | [README](Week_08/README.md) |
| Week 09 | [README](Week_09/README.md) |
| Week 10 | [README](Week_10/README.md) |
| Week 11 | [README](Week_11/README.md) |
| Week 12 | [README](Week_12/README.md) |
| Week 13 | [README](Week_13/README.md) |

The weekly record shows the chronological development of the optimisation approach as additional observations became available. Later documentation adds validation and analysis while the submitted inputs and returned outputs preserve the underlying experimental record.

## Reproducibility and evidence

Raw submitted inputs and returned outputs remain the authoritative numerical record. Analysis scripts, CSV summaries, figures, rankings and strategy labels are derived material and are kept separate from those source observations.

Later rounds add stronger evidence trails through validation records, assumptions, decision cards, provenance material and reproducibility checks where relevant.

## Academic feedback and continuous improvement

Academic feedback informed the subsequent development of the optimisation approach. Later work introduced more concise comparisons between functions, clearer differentiation across F1 to F8, explicit recognition of adaptive sampling bias, stronger workflow versioning, concise performance summaries and clearer triggers for detecting plateaux, diminishing returns and excessive local concentration.

The repository records both the optimisation results and the progressive development of the methods used to obtain them.
