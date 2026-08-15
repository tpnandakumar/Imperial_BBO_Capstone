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

The `PGC` and `PFRAMOS` directories contain supplementary research that developed from questions raised during the capstone. They support the project but do not replace the weekly assessed record. See [Extended Research and Validation](EXTENDED_RESEARCH_AND_VALIDATION.md).

## Project overview

The challenge contains eight hidden objective functions with dimensionalities ranging from two to eight variables. One query vector is submitted for each function during every optimisation round. Because the mathematical form of each function is unknown, decisions are based on previously observed inputs and returned objective values.

The repository preserves the full optimisation history rather than presenting only the best final results. Unsuccessful queries are retained because they also provide evidence. A deterioration can rule out a direction, a repeated output can support stability, and a return to an earlier strong point can test reproducibility.

The strategy has developed gradually from broad exploration towards function specific refinement, recovery, controlled exploitation and boundary testing.

## Current position

Week 12 is the latest completed and verified round. No function deteriorated relative to Week 11. Functions 2, 3 and 5 reached new verified best values, Functions 4 and 7 recovered their historical best values, and Functions 1 and 8 repeated verified best values.

| Function | Week 11 output | Interpretation |
| --- | ---: | --- |
| F1 | 0.025559285339829783 | Exact repeat of verified best |
| F2 | 0.7335252043269003 | New verified best |
| F3 | -0.05985127532683556 | New verified best |
| F4 | -4.359874926582439 | Historical best recovered |
| F5 | 4427.343995806448 | New verified best near the boundary |
| F6 | -0.7078316130911375 | Improved, but below historical best |
| F7 | 1.3809299933612855 | Historical best recovered |
| F8 | 9.58024 | Exact repeat of verified best |

These results do not prove global optimality. They show that the Week 12 function specific decisions improved or retained performance relative to the immediately preceding round.

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

Later rounds use four broad actions rather than applying one treatment to every function:

- **Explore:** move to a meaningfully different region when earlier observations remain uninformative.
- **Refine:** make controlled local changes where evidence supports a productive neighbourhood.
- **Reassess or recover:** change direction after deterioration or move back towards a stronger historical basin.
- **Exploit or boundary test:** stay close to a well supported region while testing whether further improvement remains available.

Academic feedback also led to clearer checks for excessive exploitation. Later rounds consider plateau length, diminishing improvement, repeated local concentration, material deterioration, boundary concentration and weak wider search space coverage before continuing to tighten around a strong region.

## Module 21: transparency and interpretability

Module 21 corresponds to Week 09. The required documentation is stored separately so that the dataset and optimisation workflow can be reviewed directly.

- [Datasheet](Week_09/DATASHEET.md)
- [Model Card](Week_09/MODEL_CARD.md)
- [Week 09 supporting analysis](Week_09/README.md)

The Datasheet records provenance, composition, collection, preprocessing, quality assurance, bias, limitations, transparency and maintenance. The Model Card records the workflow, inputs, outputs, performance, assumptions, failure modes, human oversight and reproducibility, including an F1 to F8 performance summary and explicit workflow versioning.

## Component 22.1: clustering lens

[Week 10](Week_10/README.md) records the clustering based reflection used to prepare the Week 11 query set. The analysis does not claim statistically validated clusters from sparse data. It uses recurring local regions, distance between queries, stability of neighbouring outputs and boundary behaviour as practical cues.

The Week 10 documentation also records why weaker directions were stopped rather than continued automatically.

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

The weekly record shows the chronological development of the optimisation approach as additional observations became available. Later documentation adds validation and analysis while the submitted inputs and returned outputs preserve the underlying experimental record.

## Reproducibility and evidence

Raw submitted inputs and returned outputs remain the authoritative numerical record. Analysis scripts, CSV summaries, figures, rankings and strategy labels are derived material and are kept separate from those source observations.

Later rounds add stronger evidence trails through validation records, assumptions, decision cards, provenance material and reproducibility checks where relevant.

## Academic feedback and continuous improvement

Academic feedback informed the subsequent development of the optimisation approach. Later work introduced more concise comparisons between functions, clearer differentiation across F1 to F8, explicit recognition of adaptive sampling bias, stronger workflow versioning, concise performance summaries and clearer triggers for detecting plateaux, diminishing returns and excessive local concentration.

The repository records both the optimisation results and the progressive development of the methods used to obtain them.
