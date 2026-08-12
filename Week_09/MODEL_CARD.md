# Model Card for the Bayesian Black Box Optimisation Workflow

**Author:** Dr N T Pisharam  
**Capstone week:** 09  
**Optimisation round:** 9  
**Model name:** Pisharam Bayesian Black Box Optimisation Workflow  
**Model type:** Human supervised sequential optimisation workflow  
**Document status:** Week 09 model card

## 1. Purpose

This model card documents the decision process used for Week 09 of the Imperial Bayesian Black Box Optimisation capstone. The task was to select one query vector for each of eight hidden objective functions using the observations accumulated over the previous rounds.

The workflow was not an autonomous system and did not know the mathematical form of the functions. Its role was to organise the evidence, compare recent performance with earlier results and support a reasoned choice between exploration, refinement, reassessment and exploitation.

## 2. Development by Week 09

By Round 9, the search had become more selective. Function 5 had developed a strong upward trajectory and justified further exploitation. Function 1 remained effectively near zero and still required exploration. Functions 2, 3, 4, 6, 7 and 8 showed mixed local behaviour, so each required a different degree of refinement or reassessment.

This was the point at which a uniform search rule was clearly no longer appropriate.

## 3. Inputs to the workflow

The decision process used:

- all previously submitted query vectors;
- all returned objective values;
- each function's dimensionality;
- the permitted coordinate range from 0 to 1;
- the six decimal place submission requirement;
- the latest weekly change;
- the recent local trajectory;
- the longer term history of each function.

The stored source files remain authoritative. Rankings and strategy labels are interpretations derived from them.

## 4. Week 09 strategy profile

| Function | Week 09 output | Strategy |
|---|---:|---|
| Function 1 | `-1.4546199699251391e-58` | Explore |
| Function 2 | `0.47297842839949866` | Refine |
| Function 3 | `-0.1156707106126581` | Reassess |
| Function 4 | `-11.788939969158545` | Refine |
| Function 5 | `4394.868042481448` | Exploit |
| Function 6 | `-1.1733030029888645` | Reassess |
| Function 7 | `1.314307996450604` | Refine |
| Function 8 | `9.4709436` | Refine |

The profile reflects the evidence available at the time. Function 5 had the clearest case for exploitation, while Function 1 remained unresolved. The remaining functions required more cautious treatment.

## 5. Exact Week 09 inputs

| Function | Input |
|---|---|
| Function 1 | `0.350000,0.700000` |
| Function 2 | `0.725000,0.945000` |
| Function 3 | `0.255000,0.855000,0.295000` |
| Function 4 | `0.310000,0.710000,0.670000,0.230000` |
| Function 5 | `0.120000,0.997000,0.999800,0.999800` |
| Function 6 | `0.240000,0.760000,0.240000,0.820000,0.280000` |
| Function 7 | `0.058000,0.495000,0.248000,0.218000,0.425000,0.742000` |
| Function 8 | `0.050000,0.050000,0.050000,0.050000,0.468000,0.872000,0.572000,0.982000` |

## 6. Exact Week 09 outputs

| Function | Output |
|---|---:|
| Function 1 | `-1.4546199699251391e-58` |
| Function 2 | `0.47297842839949866` |
| Function 3 | `-0.1156707106126581` |
| Function 4 | `-11.788939969158545` |
| Function 5 | `4394.868042481448` |
| Function 6 | `-1.1733030029888645` |
| Function 7 | `1.314307996450604` |
| Function 8 | `9.4709436` |

## 7. Week 08 to Week 09 change

| Function | Week 08 | Week 09 | Change |
|---|---:|---:|---:|
| Function 1 | `-1.4546199699251391e-58` | `-1.4546199699251391e-58` | `0` |
| Function 2 | `0.5672775862793291` | `0.47297842839949866` | `-0.09429915787983044` |
| Function 3 | `-0.0991107637427902` | `-0.1156707106126581` | `-0.0165599468698679` |
| Function 4 | `-12.305008897187289` | `-11.788939969158545` | `0.516068928028744` |
| Function 5 | `4359.384134322703` | `4394.868042481448` | `35.483908158745` |
| Function 6 | `-1.1197178425911847` | `-1.1733030029888645` | `-0.0535851603976798` |
| Function 7 | `1.3346391663186332` | `1.314307996450604` | `-0.0203311698680292` |
| Function 8 | `9.47621` | `9.4709436` | `-0.0052664` |

Function 5 improved again and Function 4 also moved in a favourable direction. Functions 2, 3, 6, 7 and 8 declined, while Function 1 remained unchanged at an effectively zero value.

## 8. Decision process

The practical sequence was:

```text
Review accumulated observations
        |
Assess recent movement for each function
        |
Choose exploration, refinement, reassessment or exploitation
        |
Generate candidate query
        |
Check dimensions, bounds and precision
        |
Human review
        |
Submit and record the returned value
```

The purpose of this structure was to keep each decision tied to the evidence available at that point in the capstone.

## 9. How performance was judged

Because the true functions and optima were unknown, performance was judged within each function over time. The main checks were:

- best value observed so far;
- change from the previous round;
- direction of recent movement;
- consistency of neighbouring or repeated points where available;
- whether the chosen strategy matched the observed history;
- compliance with dimensionality, bounds and submission precision.

Cross function ranking was treated as descriptive because the eight objectives operate on different numerical scales.

## 10. What Week 09 showed

Function 5 remained the strongest optimisation pathway and improved by `35.483908158745`. Function 4 improved by becoming less negative. Function 2 remained positive but lost part of its Week 08 gain. Functions 3 and 6 deteriorated and required reassessment. Functions 7 and 8 remained positive but slipped slightly. Function 1 provided no new useful signal.

The mixed result was important because it reinforced the need for function specific decisions rather than continuing every local movement automatically.

## 11. Strengths

The workflow's main strengths at Week 09 were its traceability and adaptability. Each query could be related to the preceding evidence, and different functions were allowed to follow different search strategies.

The weekly record also made unsuccessful moves visible rather than hiding them. That matters because a deterioration can change the next decision even when it does not improve the objective value.

## 12. Limitations

Nine observations per function remained sparse, particularly for the higher dimensional objectives. Local improvements did not establish global structure, and the workflow could not prove that any observed best value represented a global optimum.

The process also relied on human interpretation. Strategy labels therefore describe the reasoning applied to the observations rather than outputs from a fixed statistical model.

## 13. Intended use

The workflow is intended for the Imperial BBO capstone and for documenting sequential optimisation under uncertainty. It can be used to examine how query choices changed as evidence accumulated.

It is not suitable for claiming recovery of the hidden functions, proof of a global optimum or superiority over other optimisation methods without direct comparative evidence.

## 14. Reproducibility

The Week 09 repository contains the submitted inputs, returned results, analysis code, figure generation code and supporting documentation required to reconstruct the reported comparisons.

The authoritative source files are `week_09_inputs.csv` and `week_09_results.csv`.

## 15. Week 09 conclusion

Week 09 sharpened the distinction between functions that justified continued local work and those that needed a change in direction. Function 5 remained the clearest exploitation target. Function 4 improved. Functions 2, 3 and 6 required more caution after deterioration, while Functions 7 and 8 remained positive but showed small declines. Function 1 still required exploration.

That evidence set up Week 10 as a more deliberate test of local refinement, reassessment and repeatability.

## References

Imperial College Business School. Black Box Optimisation Capstone Challenge.

Rasmussen, C. E. and Williams, C. K. I. *Gaussian Processes for Machine Learning*. MIT Press.

Frazier, P. I. *A Tutorial on Bayesian Optimization*. arXiv:1807.02811.