# Detailed Results Discussion for the Imperial BBO Capstone

## Summary

The Imperial BBO Capstone tested a sequential approach to eight hidden functions over thirteen rounds. The model did not assume that one search rule would suit every function. Instead, each weekly decision used the evidence available at that point to choose among exploration, local refinement, recovery, replication and retention. This approach produced new participant-query best results for Functions 3, 5 and 6 in the final round, while several other functions retained or reconfirmed strong earlier results.

The main conclusion is practical. Black box optimisation improves when the search responds to the behaviour of each function rather than applying the same movement everywhere. Returned objective values remained the primary evidence. Clustering, principal component analysis and local surrogate work helped organise or interpret that evidence, but they did not replace direct evaluation by the hidden functions.

## Overall outcome

The complete record contains 175 starter observations and 104 participant-selected queries. One query was submitted for each of the eight functions in every round. The final participant-query best values were:

| Function | Best output | Winning week or weeks | Main interpretation |
| --- | ---: | --- | --- |
| F1 | `0.025559285339829783` | 3, 11, 12 and 13 | A strong point was found early and later reconfirmed |
| F2 | `0.7335252043269003` | 12 | A further small move in Week 13 reduced performance |
| F3 | `-0.05685061601567621` | 13 | The final adjustment produced a new participant-query best |
| F4 | `-4.359874926582439` | 1, 12 and 13 | Recovery returned to an earlier strong point and confirmed it |
| F5 | `4440.957216598753` | 13 | Sustained directional refinement produced continuing improvement |
| F6 | `-0.6071562248604215` | 13 | The final round improved the observed best, although repeatability remained important |
| F7 | `1.3809299933612855` | 5, 12 and 13 | Recovery and repetition reconfirmed an earlier best |
| F8 | `9.58024` | 1, 11, 12 and 13 | Repetition confirmed a stable retained result within the observed record |

These are maxima from participant-selected queries. They are not claims about the unknown mathematical global optima.

## Function-level interpretation

### F1: early discovery followed by confirmation

F1 reached its strongest participant-query value in Week 3. The same result appeared again in Weeks 11, 12 and 13. Later repetition did not improve the retained maximum, but it showed that returning to the same point reproduced the result in the recorded evaluations. For this function, the important learning was not that continuous movement always helps. Once a strong point had been identified, retention and confirmation became more defensible than unsupported exploration.

### F2: a local move can still be harmful

F2 achieved its best result in Week 12. A further nearby move in Week 13 produced a lower output. This is a useful warning against treating small coordinate changes as automatically safe. Local refinement should continue only while the evidence remains favourable. The Week 13 outcome supports a stopping rule based on the retained best rather than an assumption that every additional small move will improve it.

### F3: late improvement remained possible

F3 produced a new participant-query best in Week 13. The result shows why the final round still had value for a function whose earlier evidence had not settled into a convincing plateau. Careful adjustment remained justified because the recent trajectory continued to support another test. The result does not establish the hidden optimum, but it demonstrates that late improvement can occur when the search remains responsive to function-specific evidence.

### F4: recovery was more valuable than novelty

F4's strongest result first appeared in Week 1 and was recovered in Weeks 12 and 13. Later exploratory movement did not surpass that point. Returning to the earlier coordinates therefore became the strongest evidence-based decision. This function illustrates recovery as an active optimisation strategy. Recovery is not simply a failure to explore. It protects a known strong result after later trials have weakened the case for continued movement.

### F5: the clearest sustained improvement

F5 showed the strongest continuing progression in the capstone. Its output rose from `1415.876394` in Week 1 to `4440.957217` in Week 13. The trajectory supported movement in a consistent direction, and the final result continued that pattern. F5 therefore provides the clearest example of successful exploitation after earlier exploration. It also shows why search behaviour should remain function-specific. The directional refinement that helped F5 would not have been justified for functions that had plateaued, reversed or shown unstable outputs.

### F6: improvement and repeatability must be read together

F6 reached its strongest participant-query output in Week 13, but repeated coordinates did not always return identical values elsewhere in its record. The best observed result therefore needs to be interpreted alongside measurement or process variability. Replication was essential because one returned value could not automatically be treated as a stable property of the coordinate. This finding strengthens the case for recording repeated evaluations and separating observed maxima from certainty about the underlying function.

### F7: recovery and retention protected the best result

F7 first reached its strongest result in Week 5 and repeated it in Weeks 12 and 13. The later rounds did not produce a higher value, but they confirmed the usefulness of returning to the earlier strong point. F7 supports the same broad lesson as F4 while following a different numerical trajectory. When later exploration has not improved the record, recovery and retention can be more rational than continued movement.

### F8: a stable retained maximum

F8's strongest participant-query output appeared in Week 1 and was repeated in Weeks 11, 12 and 13. The repeated result supports the decision to retain the point. It also demonstrates that an optimisation campaign can end with confirmation rather than a new maximum. A final round is still informative when it tests whether an earlier strong result remains reproducible.

## What the model taught us

The sequential model was most useful as a decision framework rather than as a single fitted equation. Five lessons emerged.

1. Exploration is valuable when the available evidence does not yet identify a promising region.
2. Local refinement is useful when recent movement produces consistent improvement, as seen most clearly in F5.
3. Recovery protects an earlier strong point after later movement performs poorly, as shown by F4 and F7.
4. Replication helps distinguish a stable result from variable output, which was particularly important for F6.
5. Stopping is a positive decision when additional movement lacks evidential support, as the F2 result illustrates.

Clustering helped describe recurring coordinate regions. Principal component analysis helped examine whether coordinates moved together. These methods added structure to the decision process, but neither supplied the hidden objective function or guaranteed improvement. Their value came from supporting a transparent judgement based on the chronological record.

## Limitations

The query budget was small relative to the dimensionality and possible complexity of the eight functions. Only one new point per function was evaluated in each round. The objective equations, gradients and true global optima were not available. Function outputs also differed greatly in scale, so raw values cannot be compared directly across functions. Normalised plots show timing and direction within a function, not equivalent performance between functions.

The results may also contain local plateaux, unobserved better regions and function-specific variability. Repeated outputs at the same coordinates strengthen the evidence for stability when they agree, but disagreement requires caution. Post-capstone surrogate and PDHIS analyses extract additional mathematical structure from the completed sequence, yet they do not change the official thirteen-round results.

## Practical conclusion

The capstone demonstrates that an effective black box search is not defined by constant movement. It is defined by choosing the next action in response to the evidence. F5 rewarded persistent refinement. F3 and F6 improved late. F4 and F7 rewarded recovery. F1 and F8 rewarded confirmation. F2 showed when another move should not be mistaken for progress.

The strongest overall lesson is therefore the value of adaptive, function-specific decision-making. The model helped organise those decisions, preserve the chronological evidence and explain why a query was selected. The returned objective values determined whether the decision succeeded.

## Supporting evidence

- [Results summary and three evidence routes](../SECTION_GUIDE.md)
- [Verified final result summary](../../Module_25_Final_BBO_Submission/Final_13_Round_Evidence/FINAL_RESULTS_SUMMARY.csv)
- [Executable final capstone notebook](../../Module_25_Final_BBO_Submission/25_3_GitHub_Final_Submission/FINAL_CAPSTONE_NOTEBOOK.ipynb)
- [Final strategy outcome](../../Week_13/FINAL_STRATEGY_OUTCOME.md)
- [Successful optimisation strategies evidence](../../Module_25_Final_BBO_Submission/25_2_Successful_Optimisation_Strategies/EVIDENCE_MAP.md)

