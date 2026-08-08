# Model Card for the Bayesian Black Box Optimisation Workflow

**Author:** Dr N T Pisharam  
**Capstone week:** 10  
**Optimisation round:** 10  
**Model name:** Pisharam Bayesian Black Box Optimisation Workflow  
**Model type:** Human supervised, LLM assisted sequential optimisation workflow  
**Document status:** Week 10 full model card

## 1. Executive Summary

This model card documents the optimisation workflow used for Week 10 of the Imperial Bayesian Black Box Optimisation capstone. The workflow supports sequential selection of one query vector for each of eight hidden objective functions using only the evidence accumulated from prior submissions and the objective values returned by the competition platform.

By Week 10, the workflow had moved beyond broad exploratory search and was using function specific strategies. Function 5 was tested through exact repetition of the Week 09 best known input, Functions 2, 3, 7 and 8 were refined locally, Functions 4 and 6 were reassessed after mixed earlier behaviour, and Function 1 continued broader exploration because its outputs remained effectively near zero.

The Week 10 results reinforced the value of differentiated decision making. Functions 2 and 3 improved, Function 5 reproduced its best known result exactly, Function 1 remained unresolved, and Functions 4, 6, 7 and 8 declined. These outcomes informed the Week 11 strategy and provided additional evidence about local stability, diminishing returns and the need for directional change in some functions.

## 2. Model Overview

The workflow is a human supervised, LLM assisted decision support process for black box optimisation under limited observations. It does not know the mathematical form of the eight objective functions and does not claim to reconstruct them. Instead, it uses the cumulative history of submitted query vectors and returned objective values to guide the next set of candidate queries.

The workflow treats each function independently because dimensionality, numerical scale and observed behaviour differ substantially across the eight objectives. Historical evidence is used to decide whether a function should be explored, refined, reassessed or exploited.

## 3. Model Purpose

The primary purpose of the workflow is to improve query selection under uncertainty while preserving a transparent record of why each decision was made.

A secondary purpose is to support reproducibility. Exact inputs, outputs, changes, strategy labels and analytical scripts are stored so that the reported Week 10 reasoning can be reconstructed from the repository.

## 4. Scope

The workflow is scoped to the Imperial BBO capstone and the evidence available within that project. It is not presented as a general purpose replacement for Bayesian optimisation, Gaussian process optimisation or other established methods.

Its role is structured decision support for a small sequential dataset with hidden objectives and a strict query budget.

## 5. Model Architecture

The workflow follows a repeated evidence cycle:

```text
Verified optimisation history
        |
        v
Function specific trend review
        |
        v
Candidate strategy selection
        |
        v
Candidate query generation
        |
        v
Human review and constraint checking
        |
        v
Official submission
        |
        v
Returned objective values
        |
        v
Exact comparison and strategy update
```

The cyclical structure ensures that each new round incorporates the latest evidence without altering earlier observations.

## 6. Model Inputs

The primary inputs are:

- historical query vectors for all eight functions;
- historical returned objective values;
- dimensionality of each function;
- allowed input range from zero to one;
- six decimal place submission requirement;
- week to week changes in objective values;
- recent local search direction;
- longer term performance trends.

Derived summaries may be used to support interpretation, but the raw observations remain authoritative.

## 7. Model Outputs

The principal output is one recommended query vector for each function for the next optimisation round.

Supporting outputs include exact change calculations, function rankings, strategy classifications, local trend interpretations, information gain summaries and figures showing progression and comparison. These supporting outputs explain the decision process but are not competition returned values.

## 8. Development History

The workflow evolved as evidence accumulated across successive rounds. Early decisions placed greater emphasis on exploration because little was known about the hidden response surfaces. Later rounds allowed more selective local refinement and exploitation where repeated evidence supported those choices.

By Week 10, the workflow had enough historical context to test repeatability deliberately. Function 5 was held at the exact Week 09 best known input rather than moved automatically. The identical returned value provided evidence of repeatability at that tested point.

## 9. Week 10 Strategy

| Function | Week 10 treatment | Rationale |
|---|---|---|
| Function 1 | Explore | Prior outputs remained effectively near zero |
| Function 2 | Refine | Positive region with evidence supporting local improvement |
| Function 3 | Refine | Opportunity to improve within a negative region |
| Function 4 | Reassess | Earlier direction remained uncertain |
| Function 5 | Exploit and confirm | Highest known result required a repeatability check |
| Function 6 | Reassess | Recent local behaviour did not justify direct continuation |
| Function 7 | Refine | Positive region with modest local structure |
| Function 8 | Refine | Stable high performing region with cautious local movement |

## 10. Week 10 Inputs

| Function | Exact input |
|---|---|
| Function 1 | `0.450000,0.650000` |
| Function 2 | `0.700000,0.955000` |
| Function 3 | `0.280000,0.875000,0.315000` |
| Function 4 | `0.290000,0.730000,0.690000,0.210000` |
| Function 5 | `0.120000,0.997000,0.999800,0.999800` |
| Function 6 | `0.260000,0.780000,0.260000,0.840000,0.300000` |
| Function 7 | `0.060000,0.500000,0.250000,0.220000,0.430000,0.740000` |
| Function 8 | `0.050000,0.050000,0.050000,0.050000,0.470000,0.875000,0.575000,0.985000` |

## 11. Week 10 Outputs

| Function | Exact output |
|---|---:|
| Function 1 | `2.8950706668499033e-23` |
| Function 2 | `0.5311818841205426` |
| Function 3 | `-0.08697581687486715` |
| Function 4 | `-13.483642655031158` |
| Function 5 | `4394.868042481448` |
| Function 6 | `-1.2283806967341901` |
| Function 7 | `1.285160161342515` |
| Function 8 | `9.4646525` |

## 12. Week 09 to Week 10 Performance

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

## 13. Decision Making Framework

The workflow reviews each function across three levels of evidence: the latest movement, the recent local trajectory and the longer term optimisation history. Candidate points are then selected according to whether the evidence supports continued movement, reduced step size, direction change, confirmation or broader exploration.

The final query remains subject to human review. This prevents a derived strategy label from being treated as an automatic instruction when the broader evidence suggests caution.

## 14. Exploration and Exploitation

Week 10 deliberately retained both exploration and exploitation. Function 5 represented the strongest exploitation case, while Function 1 remained the clearest exploration case. The remaining functions occupied intermediate states where local refinement or reassessment was more appropriate.

This mixed allocation reduced the risk of committing the entire query budget to previously successful regions while still preserving the strongest known result.

## 15. Repeatability Assessment

Function 5 returned `4394.868042481448` in both Week 09 and Week 10 at the exact same input, `0.120000,0.997000,0.999800,0.999800`.

This supports repeatability at that specific tested point. It does not prove that the surrounding region is stable, that the global optimum has been found or that the function is deterministic everywhere.

## 16. Model Performance

Week 10 performance was mixed. Functions 2 and 3 improved. Function 5 remained unchanged at the highest known value. Function 1 changed sign but remained effectively near zero. Functions 4, 6, 7 and 8 declined.

The workflow therefore provided useful information even when numerical improvement was absent. Negative movements helped identify directions that should not be continued automatically, while the Function 5 repeat strengthened confidence in the tested location.

## 17. Evaluation Metrics

Evaluation uses best so far value within each function, exact change from the preceding round, direction of recent movement, stability of repeated or neighbouring observations, consistency between evidence and selected strategy, dimensionality and range compliance, and preservation of exploration where uncertainty remains high.

Cross function ranking is treated as descriptive because the objective scales differ.

## 18. Information Gain

Information gain is interpreted qualitatively from how much a new observation changes understanding of the search direction. Function 5 provided strong information about repeatability. Function 2 strengthened confidence in its local region. Function 3 supplied a favourable directional signal. Function 4 ruled against automatic continuation in the Week 10 direction.

Information gain scores stored elsewhere in the repository are project interpretation values rather than competition returned measurements.

## 19. Robustness

Robustness in this workflow means avoiding unsupported large movements, preserving strong known points where appropriate and changing direction when recent evidence becomes adverse.

Week 10 improved the robustness of later decision making because it supplied both a repeat observation and several clear tests of local movement.

## 20. Human Oversight

The workflow does not submit queries autonomously. Human review remains required before each official submission. The reviewer checks whether the recommendation agrees with the evidence, whether input dimensions are correct and whether all coordinates satisfy the permitted range and precision requirements.

## 21. Computational Implementation

`week_10_analysis.py` validates input dimensions and ranges, reads Week 09 and Week 10 results, calculates exact changes using `Decimal`, ranks functions and exports the Week 10 analytical summary.

`generate_week_10_figures.py` prepares the verified historical series, exports figure data and generates Week 10 analytical figures directly into the weekly folder.

## 22. Reproducibility

The Week 10 workflow can be reproduced from the repository root with:

```bash
python Week_10/week_10_analysis.py
python Week_10/generate_week_10_figures.py
```

The stored CSV values remain authoritative. Plotting conversions do not replace the original numerical records.

## 23. Strengths

The principal strengths of the workflow are transparency, function specific strategy selection, exact preservation of competition values and the ability to adapt after both favourable and unfavourable observations.

The Week 10 repeatability test for Function 5 also shows that the workflow can use a query for confirmation rather than treating every round as a requirement to move.

## 24. Limitations

The hidden mathematical functions remain unknown. Ten observations per function provide only sparse coverage, especially in higher dimensions. Local trends may not generalise to other regions, and no global optimum can be confirmed from the available evidence.

The workflow also includes human interpretation and LLM assistance, so some strategy judgements are qualitative rather than outputs from a fixed statistical model.

## 25. Risks

The main risks are premature exploitation, overinterpretation of sparse local evidence, assuming smoothness where none has been demonstrated and confusing derived analytical labels with observed competition data.

These risks are reduced through exact data preservation, explicit strategy labels, repeated comparison and human review.

## 26. Intended Uses

The workflow is intended for educational analysis of the Imperial BBO capstone, sequential optimisation under uncertainty, reproducible experiment tracking and reflection on exploration versus exploitation.

It may also be used as a case study for how a decision support workflow evolves as evidence accumulates.

## 27. Unsuitable Uses

The workflow should not be used to claim that the hidden functions have been identified, that a global optimum has been proven or that the method is superior to established optimisation algorithms without comparative evidence.

It is not suitable for direct deployment in clinical, financial or other safety critical decision making without independent validation.

## 28. Responsible Interpretation

Later frameworks or research extensions should not be described as though they were used in earlier rounds unless the contemporaneous repository record supports that claim. This protects the chronology of the capstone and distinguishes observed evidence from later methodological development.

Similarly, PGC and PFRAMOS are supplementary research streams arising from the wider project. Their later capabilities should not be used to reinterpret Week 10 outcomes retrospectively.

## 29. Week 10 Conclusion

Week 10 was valuable because it tested several different strategic assumptions at once. Functions 2 and 3 justified further refinement, Function 5 demonstrated repeatability at its best known point, Function 1 remained unresolved, and Functions 4, 6, 7 and 8 supplied evidence that local continuation should be cautious or redirected.

The resulting evidence supported a more selective Week 11 submission and strengthened the overall experimental record by showing that confirmation, refinement, reassessment and exploration can all have legitimate roles within the same optimisation round.

## References

Imperial College Business School. Artificial Intelligence and Machine Learning Programme, Black Box Optimisation Capstone Challenge.

Rasmussen, C. E. and Williams, C. K. I. Gaussian Processes for Machine Learning. MIT Press.

Frazier, P. I. A Tutorial on Bayesian Optimization. arXiv:1807.02811.