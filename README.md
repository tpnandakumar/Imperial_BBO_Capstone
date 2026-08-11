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
- [Week 11: latest completed optimisation round](Week_11/README.md)

The `PGC` and `PFRAMOS` directories contain supplementary research that developed from questions raised during the capstone. They support the project but do not replace the weekly assessed record. See [Extended Research and Validation](EXTENDED_RESEARCH_AND_VALIDATION.md).

## Project overview

The challenge contains eight hidden objective functions with dimensionalities ranging from two to eight variables. One query vector is submitted for each function during every optimisation round. Because the mathematical form of each function is unknown, decisions are based on previously observed inputs and returned objective values.

The repository preserves the full optimisation history rather than presenting only the best final results. Unsuccessful queries are retained because they also provide evidence. A deterioration can rule out a direction, a repeated output can support stability, and a return to an earlier strong point can test reproducibility.

The strategy has developed gradually from broad exploration towards function specific refinement, recovery, controlled exploitation and boundary testing.

## Current position

Week 11 is the latest completed and fully documented round. Every function improved relative to Week 10.

| Function | Week 11 output | Interpretation |
| --- | ---: | --- |
| F1 | 0.025559285339829783 | Recovered the confirmed narrow positive peak |
| F2 | 0.5848554940277205 | New best through a local probe |
| F3 | -0.06542982421105416 | Improved through local refinement |
| F4 | -4.868852987697114 | Strong recovery after the Week 10 decline |
| F5 | 4411.0387356061765 | New verified best near the boundary |
| F6 | -0.7268715077444687 | Recovered towards the strongest known basin |
| F7 | 1.3579108517237013 | Improved through tight local refinement |
| F8 | 9.58024 | Returned to the best verified value |

These results do not prove global optimality. They show that the Week 11 function specific decisions improved on the immediately preceding round.

Week 12 should only be added once its submitted inputs and returned outputs have been verified.

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

Earlier weekly documents are preserved as historical records. They show how the reasoning changed over time and should not be rewritten simply to make the earlier strategy appear more advanced than it was at the time.

## Reproducibility and evidence

Raw submitted inputs and returned outputs remain the authoritative numerical record. Analysis scripts, CSV summaries, figures, rankings and strategy labels are derived material and are kept separate from those source observations.

Later rounds add stronger evidence trails through validation records, assumptions, decision cards, provenance material and reproducibility checks where relevant.

## Academic feedback and continuous improvement

Academic feedback has been incorporated into later work rather than used to rewrite the historical record. The main changes include more concise comparisons between functions, clearer differences between F1 to F8, explicit recognition of adaptive sampling bias, stronger workflow versioning, concise performance summaries and clearer triggers for detecting plateaux, diminishing returns and excessive local concentration.

The repository is intended to show both the optimisation results and the development of the method used to obtain them.
