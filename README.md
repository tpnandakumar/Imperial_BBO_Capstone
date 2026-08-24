# Imperial BBO Capstone

## Bayesian Black Box Optimisation Portfolio

**Author:** Dr Nandakumar Theekkootu Pisharam  
**Programme:** Imperial College Business School Artificial Intelligence and Machine Learning Programme  
**Repository status:** Public  
**Default branch:** `main`

## Project summary

This project explored how to find strong solutions for eight unknown mathematical functions when only a limited number of evaluations were available. Across thirteen rounds, I submitted new coordinates, examined the returned results and changed the search strategy according to the evidence. Early rounds explored broadly, while later rounds focused on promising regions, recovered from unsuccessful moves and tested whether further improvement remained possible. The final round produced new best results for Functions 3, 5 and 6, while several other functions retained their strongest earlier results. The repository preserves the full decision trail, including unsuccessful trials, analysis, code, figures and final conclusions.

## Assessment navigation

The assessed BBO history is preserved chronologically in `Week_01` through `Week_13`. Module 25 is the final assessment stage and is kept separate from the thirteen optimisation rounds.

### Final assessment hub

- [Module 25: Final BBO Capstone Submission](Module_25_Final_BBO_Submission/README.md)
- [25.1 Retrospective Evidence Map](Module_25_Final_BBO_Submission/25_1_Retrospective/EVIDENCE_MAP.md)
- [25.2 Successful Optimisation Strategies Evidence Map](Module_25_Final_BBO_Submission/25_2_Successful_Optimisation_Strategies/EVIDENCE_MAP.md)
- [25.3 Repository Audit](Module_25_Final_BBO_Submission/25_3_GitHub_Final_Submission/REPOSITORY_AUDIT.md)
- [Final Capstone Datasheet](Module_25_Final_BBO_Submission/25_3_GitHub_Final_Submission/FINAL_CAPSTONE_DATASHEET.md)
- [Final Capstone Model Card](Module_25_Final_BBO_Submission/25_3_GitHub_Final_Submission/FINAL_CAPSTONE_MODEL_CARD.md)
- [Final Reproducibility Guide](Module_25_Final_BBO_Submission/25_3_GitHub_Final_Submission/FINAL_REPRODUCIBILITY.md)
- [Final Verified Winner Summary](Module_25_Final_BBO_Submission/Final_13_Round_Evidence/FINAL_RESULTS_SUMMARY.csv)

### Key analytical stages

- [Week 09: Module 21 analysis](Week_09/README.md)
- [Week 09 Datasheet](Week_09/DATASHEET.md)
- [Week 09 Model Card](Week_09/MODEL_CARD.md)
- [Week 10: clustering and strategy refinement](Week_10/README.md)
- [Week 11: PCA comparison and Week 12 decision pathway](Week_11/README.md)
- [Week 12: verified outcome and capstone reflection](Week_12/README.md)
- [Component 23.1 reflection](Week_12/COMPONENT_23_1_CAPSTONE_REFLECTION.md)
- [Week 13: final round analysis](Week_13/README.md)
- [Week 13 final strategy outcome](Week_13/FINAL_STRATEGY_OUTCOME.md)
- [Week 13 final capstone synthesis](Week_13/FINAL_CAPSTONE_SYNTHESIS.md)
- [Week 13 RL, MAB, MDP and Q-learning review](Week_13/RL_MAB_MDP_QLEARNING_REVIEW.md)

## Project overview

The challenge contains eight hidden objective functions with dimensionalities from two to eight variables. One query vector was submitted for each function during every optimisation round. Because the mathematical form of each function was unknown, decisions were based on previously observed inputs and returned objective values.

The repository preserves the complete optimisation history rather than presenting only the strongest final values. Unsuccessful queries remain part of the evidence because deterioration can reject a direction, repeated results can support stability and recovery to an earlier point can test whether a previously strong basin remains useful.

## Final thirteen-round position

Round 13 produced new overall best values for Functions 3, 5 and 6. Functions 1, 4, 7 and 8 retained their strongest verified values. Function 2 ended below its Week 12 peak, so the Week 12 coordinate remains its strongest verified point.

| Function | Strongest verified output | Best week or weeks | Final interpretation |
| --- | ---: | --- | --- |
| F1 | `0.025559285339829783` | 3, 11, 12, 13 | Best repeatedly confirmed |
| F2 | `0.7335252043269003` | 12 | Week 13 local refinement deteriorated |
| F3 | `-0.05685061601567621` | 13 | New overall best |
| F4 | `-4.359874926582439` | 1, 12, 13 | Historical best recovered and retained |
| F5 | `4440.957216598753` | 13 | New overall best after sustained boundary refinement |
| F6 | `-0.6071562248604215` | 13 | New overall best with repeatability uncertainty |
| F7 | `1.3809299933612855` | 5, 12, 13 | Historical best recovered and retained |
| F8 | `9.58024` | 1, 11, 12, 13 | Best repeatedly confirmed |

These are the strongest observations in the thirteen-round record. They are not claims of mathematical global optimality.

## Strategy evolution

The search developed from broad exploration into function-specific decision making. Later rounds used four main actions:

- **Explore:** move to a meaningfully different region when existing evidence remained weak.
- **Refine:** make controlled local changes where a productive neighbourhood had emerged.
- **Recover or reassess:** change direction after deterioration or return towards a stronger historical basin.
- **Exploit or test a boundary:** remain close to a well-supported region while improvement continued.

Week 10 added clustering as a practical lens for recurring local regions and switching signals. Week 11 compared PCA with direct objective evidence and used dimensional structure only where it improved the decision. The final rounds used exploration versus exploitation, reward and stopping concepts from Module 24 to interpret the remaining query budget.

## What worked and what did not

F5 provides the clearest sustained exploitation success, rising from `1415.8763939603884` in Week 1 to `4440.957216598753` in Week 13 as the search approached a productive boundary. F3 also benefited from late local refinement. Recovery was valuable for F4 and F7, while repeated best points supported stopping for F1 and F8.

F2 provides useful negative evidence. The Week 12 local best improved sharply, but the next small move in Week 13 reduced the result. F6 adds a different limitation because the same recorded coordinate returned different outputs in Weeks 3, 12 and 13. These results show why optimisation and stopping decisions must remain function-specific.

## Reproducibility

A clean environment can reproduce the final assessment analysis with:

```bash
python -m pip install -r requirements-final.txt
python tools/repository_audit.py
python Week_13/week_13_analysis.py
python Week_13/generate_week_13_figures.py
```

The repository audit checks the required Module 25 evidence files, Week 01 to Week 13 navigation, internal Markdown links and common unfinished placeholder markers. The Week 13 analysis reconstructs the complete thirteen-round history from committed evidence and calculates the final comparisons. Objective values remain stored exactly as supplied, and exact Week 12 to Week 13 changes are calculated with decimal arithmetic. Figure generation uses floating-point conversion only for visualisation.

A GitHub Actions workflow also runs the repository audit and final Week 13 reproducibility sequence on changes affecting the final assessment record.

See the [Final Reproducibility Guide](Module_25_Final_BBO_Submission/25_3_GitHub_Final_Submission/FINAL_REPRODUCIBILITY.md) for the assessment-facing route.

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

## Extended research and post-capstone boundary

The `PGC` and `PFRAMOS` directories contain supplementary research that developed from questions raised during the capstone. They support the project but do not replace the weekly assessed record. See [Extended Research and Validation](EXTENDED_RESEARCH_AND_VALIDATION.md).

The [Advanced Extension Series](Advanced_Extension_Series/README.md) begins only after the official thirteen-round experiment. Its first analytical stage is [SOC: Surrogate Optimisation Competition](Advanced_Extension_Series/SOC_Surrogate_Optimisation_Competition/README.md). SOC is post-capstone research. It was not used to generate the Week 01 to Week 13 outputs and does not retrospectively alter the assessed record.
