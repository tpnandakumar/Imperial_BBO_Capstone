# Model Card for the Bayesian Black Box Optimisation Workflow

**Author:** Dr N T Pisharam  
**Capstone week:** 10  
**Optimisation round:** 10  
**Model name:** Pisharam Bayesian Black Box Optimisation Workflow  
**Model type:** Human supervised sequential optimisation workflow  
**Document status:** Week 10 model card

## 1. Purpose

This model card documents the decision process used for Week 10 of the Imperial Bayesian Black Box Optimisation capstone. The task was to select one query vector for each of eight hidden objective functions using only the history of submitted points and returned values.

The workflow did not attempt to reconstruct the hidden functions. Its purpose was narrower: review the evidence available for each function, decide whether the next move called for exploration, refinement, reassessment or exploitation, and record the reasoning behind that choice.

## 2. Why the workflow changed by Week 10

The early rounds contained too little information to justify narrow local search across every function. By Week 10, the eight functions had developed clearly different histories. Function 5 had a strong and persistent high value. Function 1 remained effectively near zero. Functions 2, 3, 4, 6, 7 and 8 showed different mixtures of improvement, deterioration and local stability.

For that reason, Week 10 used a function specific strategy rather than one rule for all eight functions.

## 3. Inputs to the decision process

The workflow used:

- the full history of submitted query vectors;
- the returned objective values;
- each function's dimensionality;
- the permitted input range from 0 to 1;
- the six decimal place submission requirement;
- the latest change in objective value;
- recent local behaviour;
- the longer term direction of travel.

The stored CSV files remain the authoritative record. Rankings and strategy labels are derived interpretations.

## 4. Week 10 strategy

| Function | Treatment | Reason |
|---|---|---|
| Function 1 | Explore | Previous outputs remained effectively near zero |
| Function 2 | Refine | Positive region with scope for a controlled local move |
| Function 3 | Refine | Opportunity to improve within a negative region |
| Function 4 | Reassess | Earlier local behaviour remained uncertain |
| Function 5 | Exploit and confirm | Highest known result justified a repeatability check |
| Function 6 | Reassess | Recent local movement did not justify simple continuation |
| Function 7 | Refine | Positive region with modest local variation |
| Function 8 | Refine | Stable high value with scope for a cautious local move |

## 5. Exact Week 10 inputs

| Function | Input |
|---|---|
| Function 1 | `0.450000,0.650000` |
| Function 2 | `0.700000,0.955000` |
| Function 3 | `0.280000,0.875000,0.315000` |
| Function 4 | `0.290000,0.730000,0.690000,0.210000` |
| Function 5 | `0.120000,0.997000,0.999800,0.999800` |
| Function 6 | `0.260000,0.780000,0.260000,0.840000,0.300000` |
| Function 7 | `0.060000,0.500000,0.250000,0.220000,0.430000,0.740000` |
| Function 8 | `0.050000,0.050000,0.050000,0.050000,0.470000,0.875000,0.575000,0.985000` |

## 6. Exact Week 10 outputs

| Function | Output |
|---|---:|
| Function 1 | `2.8950706668499033e-23` |
| Function 2 | `0.5311818841205426` |
| Function 3 | `-0.08697581687486715` |
| Function 4 | `-13.483642655031158` |
| Function 5 | `4394.868042481448` |
| Function 6 | `-1.2283806967341901` |
| Function 7 | `1.285160161342515` |
| Function 8 | `9.4646525` |

## 7. Week 09 to Week 10 change

| Function | Week 09 | Week 10 | Exact change |
|---|---:|---:|---:|
| Function 1 | `-1.4546199699251391e-58` | `2.8950706668499033e-23` | `2.895070666849903300000000000E-23` |
| Function 2 | `0.47297842839949866` | `0.5311818841205426` | `0.05820345572104394` |
| Function 3 | `-0.1156707106126581` | `-0.08697581687486715` | `0.02869489373779095` |
| Function 4 | `-11.788939969158545` | `-13.483642655031158` | `-1.694702685872613` |
| Function 5 | `4394.868042481448` | `4394.868042481448` | `0` |
| Function 6 | `-1.1733030029888645` | `-1.2283806967341901` | `-0.0550776937453256` |
| Function 7 | `1.314307996450604` | `1.285160161342515` | `-0.029147835108089` |
| Function 8 | `9.4709436` | `9.4646525` | `-0.0062911` |

The round produced three improvements, four declines and one unchanged result. That mixture is more useful than a simple success count because it shows which local assumptions held and which did not.

## 8. Repeatability test

Function 5 used exactly the same input in Weeks 09 and 10:

`0.120000,0.997000,0.999800,0.999800`

Both submissions returned:

`4394.868042481448`

This is direct repeatability evidence for that exact tested point. It does not prove that the surrounding region is stable or that the global optimum has been found.

## 9. What Week 10 taught us

Function 2 improved, supporting another controlled local refinement. Function 3 also improved, although its output remained negative. Function 4 deteriorated substantially, so continuing in the same direction would have ignored the new evidence. Function 6 also declined and required reassessment.

Functions 7 and 8 stayed positive but fell slightly. That supported cautious refinement rather than a larger move. Function 1 remained unresolved because the change in sign occurred at a magnitude that was still effectively near zero.

The Function 5 repeat was useful for a different reason. It did not improve the objective value, but it reduced uncertainty about whether the strongest known point could be reproduced.

## 10. Decision process

The practical sequence was:

```text
Review verified history
        |
Assess each function separately
        |
Choose explore, refine, reassess or exploit
        |
Generate candidate query
        |
Check dimensions, bounds and precision
        |
Human review
        |
Submit
        |
Record returned value
        |
Compare with previous evidence
```

The workflow remains human supervised. Strategy labels support the decision but do not replace judgement.

## 11. Evaluation

The workflow is evaluated within each function rather than by comparing raw values across functions. The main checks are:

- best value observed so far;
- exact change from the previous round;
- whether recent movement improved or worsened the result;
- whether a repeated point behaves consistently;
- whether the chosen strategy matches the available evidence;
- compliance with dimensionality, range and precision requirements.

Because the eight functions use different numerical scales, cross function ranking is descriptive only.

## 12. Computational implementation

`week_10_analysis.py` validates the stored inputs, reads the Week 09 and Week 10 outputs, calculates exact changes using `Decimal`, ranks the functions and writes the analytical summary.

`generate_week_10_figures.py` prepares the historical series, writes the figure data summary and generates the Week 10 figures in the weekly folder.

The source CSV files are not replaced by these derived outputs.

## 13. Reproducibility

From the repository root:

```bash
python Week_10/week_10_analysis.py
python Week_10/generate_week_10_figures.py
```

The authoritative numerical files are `week_10_inputs.csv` and `week_10_results.csv`.

## 14. Strengths

The main strengths are straightforward:

- decisions are tied to recorded observations;
- different functions can follow different strategies;
- exact competition values are retained;
- successful and unsuccessful moves both influence the next decision;
- the reasoning can be checked against the stored data.

## 15. Limitations

Ten observations per function remain sparse, especially in the higher dimensional search spaces. The hidden functions are unknown, so local improvement cannot be treated as evidence of global structure. A repeated point can demonstrate repeatability at that point, but not across a wider region.

The workflow also contains human judgement. Strategy classifications are therefore interpretations of the evidence rather than outputs from a fixed statistical model.

## 16. Intended use

This workflow is intended for the Imperial BBO capstone, for documenting sequential optimisation under uncertainty, and for analysing how query choices change as evidence accumulates.

It is not evidence that the hidden functions have been identified, that a global optimum has been proved, or that this approach is superior to established optimisation methods without direct comparison.

## 17. Week 10 conclusion

Week 10 was useful because it tested several different assumptions in the same round. Functions 2 and 3 supported continued refinement. Function 5 confirmed repeatability at the strongest known point. Function 4 showed clearly that its tested direction should be changed. Functions 6, 7 and 8 called for more cautious movement, while Function 1 remained an exploration problem.

That evidence made the Week 11 decision more selective and more defensible than a simple continuation of the previous search direction.

## References

Imperial College Business School. Black Box Optimisation Capstone Challenge.

Rasmussen, C. E. and Williams, C. K. I. *Gaussian Processes for Machine Learning*. MIT Press.

Frazier, P. I. *A Tutorial on Bayesian Optimization*. arXiv:1807.02811.