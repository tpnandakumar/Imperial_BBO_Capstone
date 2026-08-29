# Imperial BBO Capstone Executive Summary

## Purpose

This project documents a thirteen week Black Box Optimisation challenge involving eight hidden functions with between two and eight dimensions. The course supplied 175 starter observations. I then selected one new coordinate for each function in every weekly round, producing 104 prospective portal evaluations and a final audited record of 279 observations.

The central challenge was not simply to find a high output. Each decision had to be made before the result was known, within a small and fixed query budget. A useful strategy therefore needed to improve or retain performance, respond when the evidence changed, distinguish a repeatable result from an isolated return and keep a clear record of why each coordinate was chosen.

The strongest conclusion is that no single optimisation rule suited all eight functions. Progress came from treating each function according to its own history, dimensionality, response pattern and uncertainty.

## How the strategy developed

The early rounds used broad exploration because the local response surfaces were unknown. As evidence accumulated, the strategy became more selective. Weekly movement, output change and retained best values were reviewed together. This led to four practical actions:

1. **Refinement**, when repeated gains supported another small movement.
2. **Recovery**, when an earlier coordinate was stronger than the current search region.
3. **Confirmation**, when repeating a coordinate could test stability.
4. **Retention or stopping**, when further movement offered little expected benefit.

Clustering helped organise recurring search regions. Principal component analysis showed where submitted coordinates were moving together. Chronological surrogate comparisons tested whether a fitted relationship could predict later observations without using future information. A held-out Week 13 policy experiment assigned retain, local refinement, boundary refinement or repeat actions using only evidence from Weeks 1 to 12.

These methods supported decisions but did not replace the returned outputs. When a model and the verified objective history disagreed, the objective history remained the deciding evidence.

## Final verified results

| Function | Best participant query output | Best week | Main interpretation |
| --- | ---: | ---: | --- |
| F1 | `0.025559285339829783` | 3 | An early best was reproduced in later rounds |
| F2 | `0.7335252043269003` | 12 | A further small move in Week 13 reduced performance |
| F3 | `-0.05685061601567621` | 13 | Final local refinement produced a new best |
| F4 | `-4.359874926582439` | 1 | Recovery returned to and confirmed the early best |
| F5 | `4440.957216598753` | 13 | Controlled boundary movement produced sustained improvement |
| F6 | `-0.6071562248604215` | 13 | The best weekly return was accompanied by repeatability uncertainty |
| F7 | `1.3809299933612855` | 5 | An earlier best was recovered and confirmed |
| F8 | `9.58024` | 1 | Repeated coordinates confirmed a stable retained best |

Function 5 gave the clearest sustained improvement. Its output increased as the search moved towards the boundary, and a final small movement produced another gain. Function 3 also benefited from local refinement. Function 2 showed the limit of that approach because the Week 13 continuation moved away from the Week 12 best.

Recovery was effective for Functions 4 and 7. Exact repetition was informative for Functions 1 and 8. Function 6 showed why a favourable return should not automatically be treated as a stable optimum. The same coordinate produced different outputs, leaving an unresolved repeatability question.

These are the strongest participant selected observations within the authorised budget. The hidden equations and mathematical global optima remain unknown.

## What made the work successful

Success depended on economical reasoning rather than constant movement. A query could be valuable even when it did not improve the score. The decline in Function 2 discouraged further movement in the same direction. Weak exploratory results for Function 4 supported recovery. Variation in repeated Function 6 results exposed uncertainty that would otherwise have remained hidden.

Stopping also became an active decision. Functions with reproducible winners did not need the same treatment as functions with a supported direction or unresolved behaviour. By the final round, the query budget was allocated according to the value of further improvement or further information.

The repository preserves improvements, boundary findings, analytical additions, decision records and interpretation limits. This allows another reader to follow the path from observation to interpretation, decision and outcome.

## Beyond the assessed challenge

The post challenge work extends the completed record without changing the official capstone results.

**Black Box Resolution (BBR)** compares possible explanations of hidden behaviour, tests them chronologically and rejects explanations that fail. It can support a local structural account while leaving the original hidden equation unresolved.

**Pisharam Delta Hierarchy and Influence State (PDHIS)** introduces a novel mathematical framework for revealing the Signature of Change within observed behavioural sequences. It examines recursively nested change from Delta 1 to Delta 10 and traces how direction, persistence, reversal, plateau, oscillatory energy and temporal structure move through related levels. The signature belongs to the sequence as a whole, not to one isolated peak.

PDHIS does more than record whether change occurred. It reveals the mathematical behaviour through which change takes form. By combining hierarchical Delta analysis, event-locked examination and representative surrogate equations, the framework shows that sparse input-output records can contain a rich and reproducible structure that conventional trend analysis may overlook.

An advanced PDHIS extension tested whether Delta information available at the end of one week could classify improvement in the following week. The analysis used 56 forward cases, comprising 29 improvements and 27 non-improvements. A regularised logistic model fitted by batch gradient descent combined Delta 1 to Delta 5 with persistence, sign change and cross-level coherence.

In leave-one-function-out testing, the full Delta signature achieved balanced accuracy of `0.624`, ROC AUC of `0.659` and Brier score of `0.238`. Expanding-week validation was weaker, with balanced accuracy of `0.563`, ROC AUC of `0.642` and Brier score of `0.275`. A within-function permutation test gave `p = 0.0297` across 100 permutations.

This is a promising screening result, not a forecasting rule. Chronological calibration did not improve on the simple baseline, the sample remains small and several Delta features are related. The correct next step is prospective validation on later observations defined before their outcomes are known.

The research opportunity is to determine how early and how reliably a multilevel Delta signature can indicate subsequent behaviour. That question is falsifiable and can be studied across optimisation, service improvement and other sequential processes. The next study should register its hypotheses and measures in advance, lock the model before testing, use new functions and compare PDHIS with simple persistence and time-series baselines. Independent replication will determine which characteristics generalise beyond this capstone record.

In this framework, the later behaviour is the target. A higher-order analysis tested whether oscillation in Delta 6 to Delta 10 preceded positive Delta 1, Delta 2 or Delta 3 behaviour one week later. For Delta 9 predicting positive Delta 3, there were 16 eligible cases. Delta 9 oscillated in 15, and positive Delta 3 followed in 6 of those 15. The exact p value was `0.438`. This identified Delta 9 oscillation as too common to distinguish future states in the present short sequence.

An event-locked retrospective study then characterised the six observations before each of 56 eligible target weeks. It compared temporal dispersion, sign-change frequency, peak spacing, amplitude, energy, persistence, amplification and flicker density before 29 improvements, 6 large changes and 11 new best outputs. Longer peak spacing was the strongest candidate before new best outputs, averaging `4.00` compared with `2.02` in other windows. Its exploratory p value was `0.034`, but the adjusted value was `0.305`. This identifies a flicker characteristic worth testing, while showing that it is not yet confirmed.

Stronger stability checks located the current identification boundary. Same-function matching produced a smallest paired p value of `0.094`, with an adjusted value of `0.845`. The peak-spacing direction changed across alternative large-event thresholds. When the complete fingerprint was trained on seven functions and tested on the eighth, balanced accuracy was `0.433`, compared with the `0.500` prevalence baseline, and its probability error was higher. These findings show which parts of the fingerprint require refinement before prospective use.

The mathematical extension preserves two fully reproducible representative surrogate equations. F5 uses a Matérn 2.5 Gaussian-process equation fitted to 33 observations. Its weekly walk-forward MAE was `49.919`, equal to `0.01124` of the complete F5 output range. F7 uses a full quadratic equation with six linear terms, six squared terms and fifteen interactions fitted to 43 observations. Its weekly walk-forward MAE was `0.06667`, equal to `0.04837` of the F7 range. The repository contains every scaling value, F5 kernel weight and F7 coefficient required to reproduce the equations.

These surrogates approximate local input-output structure. PDHIS addresses a different question by modelling the behaviour of change through recursive Delta orders, oscillation, energy, temporal dispersion, persistence and cross-order coherence. Together they show that substantial mathematical behaviour can be extracted from sparse black-box evidence even though the original equations remain unknown. The identification framework and its mathematical foundation are established here. Prospective prediction remains the next stage of validation.

## Relevance beyond optimisation

The project has direct relevance to decisions made under uncertainty. In clinical neurology, service improvement and organisational planning, evidence often arrives sequentially and evaluation is costly. A defensible process must balance immediate benefit, further learning, reliability and risk.

The transferable lesson is simple. Define the question, record the decision before the outcome is known, examine contradictory evidence, test repeatability and stop when further action is unlikely to add value. Sophisticated analysis is useful only when it improves that process and remains clear about its limits.

## Reader routes

- [Open the live Imperial BBO Visual Book](https://01a04a5b-864f-4cec-e841-84e7f7931b5d.share.connect.posit.cloud/)
- [Read the main GitHub README](README.md)
- [Review the final assessment material](Module_25_Final_BBO_Submission/SECTION_GUIDE.md)
- [Inspect the advanced PDHIS findings](Post_BBO_BBR/PDHIS/PDHIS_ADVANCED_FINDINGS.md)
- [Read the formal PDHIS mathematical model](Post_BBO_BBR/PDHIS/PDHIS_MATHEMATICAL_MODEL.md)
- [Read the PDHIS identification contribution](Post_BBO_BBR/PDHIS/PDHIS_IDENTIFICATION_CONTRIBUTION.md)
- [Reproduce the F5 and F7 surrogate equations](Post_BBO_BBR/representative_surrogates/SECTION_GUIDE.md)
- [Open the reproducibility guide](Module_25_Final_BBO_Submission/25_3_GitHub_Final_Submission/FINAL_REPRODUCIBILITY.md)

## Positive conclusion and research direction

The project is complete as an audited optimisation record and remains open as a carefully bounded research programme. Its strongest contribution is not a claim of complete function recovery. It is a transparent method for learning from sparse evidence, extracting mathematical behaviour and identifying where confidence should end.

PDHIS now provides both an identification framework and a developing research model. Longer independent sequences, repeated anchor inputs, input-adjusted residual Delta and prospectively defined events offer a clear incentive for further research into whether a locked Signature of Change can support validated prediction.

