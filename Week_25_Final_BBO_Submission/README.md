# Week 25: Final BBO Submission

## Final thirteen round analysis and optimisation synthesis

This section is the final BBO submission synthesis for the course week following completion of Round 13. It does **not** create a fourteenth BBO round and it does not alter the historical Week 01 to Week 13 record.

Its purpose is to bring the complete capstone together in one place: what each function did, which optimisation strategies were used, why each strategy was chosen, how it was applied, when the strategy changed, what evidence caused that change, and where the final thirteen round search finished.

The post capstone **Advanced Extension Series** and **SOC, the Surrogate Optimisation Competition**, remain separate research extensions and are not presented as part of the assessed thirteen round outcome.

## 1. Final capstone position

All thirteen BBO rounds are complete. The final Week 13 submission produced new overall best values for F3, F5 and F6. F1, F4, F7 and F8 retained their strongest observed values. F2 finished below its Week 12 peak.

| Function | Strongest verified output after 13 rounds | Final interpretation |
| --- | ---: | --- |
| F1 | `0.025559285339829783` | Strongest observed coordinate retained |
| F2 | `0.7335252043269003` | Week 12 remains the strongest verified result |
| F3 | `-0.05685061601567621` | New overall best in Week 13 |
| F4 | `-4.359874926582439` | Strongest observed basin recovered and retained |
| F5 | `4440.957216598753` | New overall best in Week 13 |
| F6 | `-0.6071562248604215` | New overall best in Week 13, with repeatability uncertainty |
| F7 | `1.3809299933612855` | Strongest observed coordinate retained |
| F8 | `9.58024` | Strongest observed coordinate retained |

These are the strongest verified observations in the available thirteen round record. They are not claims of mathematical global optimality.

## 2. Overall strategy development

The optimisation process did not use one fixed method from beginning to end. The strategy changed as evidence accumulated.

The broad progression was:

**Initial local search -> broader exploration -> function specific refinement -> recovery from weak directions -> clustering based structural review -> hyperparameter informed refinement -> PCA comparison -> controlled exploitation and boundary testing -> reinforcement learning informed final decision review**

The central principle was that each hidden function had to be treated as a separate search problem. A strategy that was productive for F5 was not automatically suitable for F3, F6 or F8.

## 3. When exploration was used

Exploration was used when the available evidence was weak, when recent movements had deteriorated, when too much of the search had become concentrated in one neighbourhood, or when a function had not yet revealed a stable productive region.

Exploration was particularly important early in the capstone for F1, F3, F4 and F6. It was also reopened later when local exploitation ceased to provide useful information.

The purpose of exploration was not movement for its own sake. A new region was useful only if it reduced uncertainty, rejected an unproductive direction or identified a better basin.

## 4. When exploitation was used

Exploitation was used when repeated evidence supported a productive neighbourhood. Instead of making large movements, the next query was placed close to a strong historical point to test whether the response could be improved or reproduced.

F5 became the clearest exploitation problem because its output improved repeatedly as the search moved towards a narrow boundary region. F2, F7 and F8 also received local refinement when their strongest regions became clearer.

Exploitation was stopped or reduced when gains diminished, a movement caused material deterioration, or repeated local queries stopped adding useful information.

## 5. Clustering and local region analysis

Clustering was used as a structural lens rather than as proof that the sparse observations formed statistically definitive clusters. The analysis examined whether strong observations were repeatedly concentrated in similar coordinate regions, whether neighbouring points had similar outputs, and whether weak regions could be separated from productive basins.

This helped distinguish functions with a stable local region from functions where the apparent optimum moved as new evidence arrived. It also supported the decision to refine some functions while reopening exploration in others.

## 6. Hyperparameter optimisation and model settings

Hyperparameter choices were treated as part of the analytical method rather than as automatic optimisation of the hidden objective. Where clustering or model based analysis was used, settings such as the number of clusters, initialisation count and random state were chosen to obtain a stable analytical representation of the observed data.

The purpose was to test the robustness of the interpretation, not to suggest that tuning an analytical model directly revealed the hidden BBO optimum.

## 7. PCA and dimensional structure

PCA was introduced later as a comparison tool for understanding coordinate relationships, variance and redundancy. It was particularly useful for asking whether several coordinates were moving together and whether a lower dimensional representation offered a useful summary of the search history.

PCA did not replace direct function specific evidence. Its role was to compare structural patterns and help determine whether the next move should follow a dominant direction, remain local, or reject a simplified representation when important coordinate information would be lost.

## 8. Reinforcement learning, MAB, MDP and Q learning lens

The final stage used reinforcement learning concepts as a decision framework rather than claiming that a fully trained reinforcement learning agent had generated the historical queries.

The eight functions could be viewed as repeated sequential decision problems in which each query produced a reward signal. Multi armed bandit ideas clarified the exploration versus exploitation trade off. Markov decision process reasoning helped frame the current evidence state, possible actions and returned reward. Q learning concepts provided a way to think about whether a repeated action or a new direction had greater expected value based on previous outcomes.

This final lens strengthened the stopping decision because continuing to query a stable function has an opportunity cost when another function still shows improvement or uncertainty.

## 9. Function 1: plateau identification and stopping

F1 was difficult because many observations were extremely close to zero. A strong positive response emerged at `0.600000-0.600000`, producing `0.025559285339829783`.

The strategy moved from exploration to local validation once that coordinate clearly separated itself from the near zero observations. Returning to the same coordinate reproduced the strongest value, supporting the interpretation that this was the best verified region in the available search.

Further routine movement was not justified at the end of Round 13 because the strongest coordinate had already been reproduced and alternative regions had been materially weaker. The correct capstone action was therefore to retain the verified winner rather than continue moving without new evidence.

## 10. Function 2: local optimisation and final recovery question

F2 showed a productive region around the second coordinate near `0.95`, but the exact optimum within that neighbourhood remained sensitive to the first coordinate.

The search alternated between local refinement and recovery after weaker moves. Week 12 produced the strongest verified result at `0.690000-0.950000`, with an output of `0.7335252043269003`. Week 13 moved to `0.685000-0.950000` and returned `0.6413430885133908`.

That deterioration is useful evidence. It suggests that the Week 12 neighbourhood was stronger than the final movement and that the search had begun to bracket a local optimum. The correct interpretation is not that F2 failed, but that the final step helped identify where further local refinement would be most informative if more evaluations were available.

## 11. Function 3: directional recovery and late improvement

F3 initially produced consistently negative outputs and required wider exploration. Several early directions were rejected because they moved further away from zero.

A stronger region later emerged around coordinates in which the first and third variables were high and the second variable was low. The search progressively refined this structure. Week 13 at `0.855000-0.145000-0.855000` returned `-0.05685061601567621`, the strongest verified F3 result in the thirteen round history.

Because the final round still improved the objective, F3 had not shown the same stopping evidence as F1, F4, F7 or F8. It therefore became a natural candidate for post capstone extension research.

## 12. Function 4: basin recovery and confirmation

F4 provided its strongest verified value very early at `0.600000-0.430000-0.420000-0.250000`, returning `-4.359874926582439`.

Broader exploratory movements produced substantially poorer outputs. This created strong evidence that the original local basin was more productive than the distant regions tested. The strategy therefore changed from exploration back to recovery and local confirmation.

Returning to the strongest coordinate reproduced the best value. By the end of Round 13, routine further movement was not justified without a new structural reason to reopen the search.

## 13. Function 5: sustained exploitation and boundary extension

F5 showed the clearest and most sustained optimisation trajectory in the capstone. The output increased from `1415.8763939603884` in Week 1 through `2308.1487028593933`, `2840.9903787629305`, `3238.333368768757`, `3682.2110623386798`, `3922.7652233497042`, `4278.816638076986`, `4359.384134322703`, `4394.868042481448`, `4411.0387356061765`, `4427.343995806448` and finally `4440.957216598753`.

The evidence supported increasingly controlled exploitation. The first coordinate moved down while the remaining coordinates moved towards the upper boundary. Because improvement continued, boundary testing remained justified rather than being treated as premature overfitting.

Week 13 still produced a new best, so the capstone ended while the direction remained productive. This is why F5 is one of the strongest candidates for the Advanced Extension Series.

## 14. Function 6: optimisation under response variability

F6 required a different interpretation because the same recorded coordinate `0.700000-0.200000-0.700000-0.700000-0.200000` produced different returned values across the history.

The coordinate returned `-0.648848297397347` in Week 3, `-0.7078316130911375` in Week 12 and `-0.6071562248604215` in Week 13. The Week 13 value is the strongest verified F6 output, but the repeated input behaviour means that simple deterministic repeatability cannot be assumed.

The optimisation strategy therefore has two objectives: find a strong region and understand whether observed variation is genuine response variability, evaluation noise or another unobserved effect. F6 should not be declared globally resolved from one highest observation alone.

## 15. Function 7: local winner and reproducibility

F7 identified a strong local region relatively early. The coordinate `0.040000-0.480000-0.260000-0.220000-0.420000-0.740000` produced `1.3809299933612855`, the strongest verified F7 result.

Subsequent nearby movements were useful because they tested whether further local refinement could improve that value. They did not. Returning to the stronger coordinate confirmed the advantage of the earlier point.

By the final round the evidence supported retaining the verified winner rather than continuing routine local movement.

## 16. Function 8: stability and stopping

F8 began with a strong result of `9.58024` at `0.060000-0.070000-0.030000-0.040000-0.410000-0.820000-0.500000-0.910000`.

Several exploratory and local variants produced slightly lower values. Returning to the original strong coordinate reproduced `9.58024` in later rounds.

This repeated recovery is strong stopping evidence within the sampled search. The function was therefore treated as stable rather than consuming further query budget without a clear reason to expect improvement.

## 17. Why the strategies changed over time

The strategy changed because new outputs altered the evidence. Improvements encouraged controlled exploitation. Deterioration triggered reassessment or recovery. Repeated best values supported stopping. Continuing improvement at a boundary justified extension. Structural methods such as clustering and PCA were used when the accumulated history was large enough to make cross round comparison useful.

The method was therefore adaptive rather than predetermined.

## 18. Final stopping logic

The thirteen round capstone did not end because every hidden function had been mathematically solved. It ended because the authorised competition sequence ended.

The evidence nevertheless supports function specific stopping decisions:

- F1, F4, F7 and F8 had strong verified coordinates with repeated or recovered support.
- F2 had a clear best local point but the final movement deteriorated, leaving a narrow recovery question.
- F3 and F5 were still improving in the final round.
- F6 produced a new best but retained unresolved repeatability uncertainty.

This distinction is important. A rational optimiser should not continue every function merely because additional computational effort is possible.

## 19. What would happen with another optimisation opportunity

If further genuine evaluations were available, the continuation decision would be selective rather than universal.

F2, F3, F5 and F6 would remain active. F1, F4, F7 and F8 would remain frozen unless new evidence justified reopening them.

The continuation lifecycle is:

**Explore -> Exploit -> Extend -> Eliminate -> Validate -> Winner -> Stop**

The aim is one defensible winning coordinate for each function, not one function defeating the others.

## 20. Post capstone research boundary

The post capstone work is intentionally separated from the assessed BBO record.

The **Advanced Extension Series** continues the optimisation question beyond Round 13. Its first analytical stage is **SOC, the Surrogate Optimisation Competition**, in which several surrogate models compete independently for F1 to F8 using held out predictive performance.

SOC and later Optimisation Extension runs are research extensions. They do not rewrite the official thirteen round evidence and do not present surrogate predictions as genuine Imperial outputs.

## 21. Final conclusion

The main achievement of the capstone is not a single optimisation technique. It is the progressive development of an evidence based search strategy under uncertainty.

The work moved from local judgement to structured comparison, clustering, parameter tuning, PCA, explicit exploration versus exploitation reasoning, recovery, boundary testing and final sequential decision analysis. Just as importantly, weak results were retained as evidence because they helped reject directions and define stopping points.

The thirteen round record therefore shows both optimisation performance and the development of the reasoning used to obtain it. The final stage does not claim that every hidden function has been solved. It shows which coordinates are strongest in the verified record, why they were selected, which functions should stop, and which questions remain scientifically worth extending beyond the assessed capstone.
