# Executive Capstone Reflection

## Introduction

This project began as a thirteen week Black Box Optimisation challenge involving eight hidden functions with between two and eight dimensions. The task was simple to describe but difficult to complete well. Each week allowed one new query per function. I selected the input coordinates, submitted them through the course portal and received an output without seeing the equation behind the function. The limited query budget made every decision important. A poorly chosen point could use a full week without adding useful information, while an apparently strong result still required confirmation before it could be trusted.

The completed record contains 279 observations. Of these, 175 were supplied at the start of the course and 104 came from the thirteen weekly rounds. The project developed from a practical optimisation exercise into a disciplined investigation of evidence, uncertainty and sequential decision making. The later Black Box Resolution work and the Pisharam Delta Hierarchy and Influence State analysis extended the research after the assessed challenge, while keeping the official results unchanged.

## 1. Starting position and analytical foundation

The starting point was the course supplied evidence for eight functions, each operating on a different scale and within a different number of dimensions. I developed the analysis around this evidence rather than assuming that one general strategy would suit every function. The public repository became the working record for the project. It stores the weekly inputs, returned outputs, analysis files, figures, decision notes and final reproducibility material.

The first requirement was dependable data handling. Coordinates had to remain within the permitted interval from zero to one, retain the required precision and match the correct dimensionality for each function. I also needed a consistent way to compare new results with earlier observations. The workflow therefore separated the authoritative portal outputs from later calculations and interpretations. This distinction became increasingly important as the analysis grew more sophisticated.

At the beginning, broad exploration was reasonable because the response surfaces were unknown. I reviewed the starter observations, compared promising regions and selected new coordinates that could provide useful information. I did not treat raw outputs from different functions as directly comparable because their scales varied greatly. Each function was judged against its own history.

The repository is available at [Imperial BBO Capstone](https://github.com/tpnandakumar/Imperial_BBO_Capstone). It now includes a reader friendly Shiny Visual Book as well as the complete technical record. This makes the work open to inspection without requiring a reader to reproduce every calculation before understanding the main story.

## 2. Weekly development, modification and feedback

The strategy changed as new evidence arrived. The early rounds focused on exploration and broad comparison. I examined which coordinate movements produced improvement, which regions appeared unproductive and whether any functions showed a stable direction. By the middle rounds, the evidence supported a more selective approach. Some functions benefited from continued movement, while others required recovery towards an earlier point or confirmation of an existing best result.

The analysis became more structured each week. Weekly summaries recorded the submitted coordinates, returned outputs, movement from the previous round and the best value retained so far. This prevented a poor recent result from obscuring a stronger earlier observation. It also made the reasoning behind each new query easier to audit.

Clustering was introduced to examine whether the submitted points formed recurring regions. This helped identify areas that had been revisited and supported recovery decisions when recent exploration had performed poorly. Clustering did not reveal the hidden equations, and sparse observations limited the strength of any conclusion. Its value was practical. It organised the observed search history and helped distinguish a productive region from an isolated result.

Principal component analysis was later used to examine how coordinates moved together. For Functions 3, 4, 5 and 8, more than 90 per cent of the observed query variance lay in the first principal component. Functions 6 and 7 required two components to reach the same threshold. I interpreted this cautiously because the query history was created by my earlier decisions. A concentrated search path could indicate an important direction, but it could also mean that other directions had received less attention.

Function 5 provided the clearest agreement between coordinate structure and objective performance. Its queries moved towards the upper boundary and the returned output continued to improve. This supported controlled continuation in the same broad direction. Other functions required different decisions. Functions 1 and 8 benefited from exact repetition of strong coordinates. Functions 4 and 7 supported recovery to earlier best points. Function 6 showed variability when a coordinate was repeated, which raised a repeatability concern that could not be resolved within the remaining budget.

Feedback came through the returned outputs rather than a conventional evaluator. Every result therefore had to be interpreted in context. An improvement supported the latest decision but did not prove that the same movement should continue indefinitely. A decline could indicate overshooting, local curvature, variability or simply an unproductive direction. The next query was chosen by considering the full history rather than reacting to one result in isolation.

## 3. Final results and what I would change

The final retained participant query results showed that several different strategies had been successful. Function 1 retained a best output of `0.025559285339829783`, first reached in Week 3 and confirmed again in later weeks. Function 2 reached `0.7335252043269003` in Week 12, but a further small change in Week 13 reduced the output. Function 3 achieved its best value of `-0.05685061601567621` in the final week. Function 4 recovered and confirmed its Week 1 best of `-4.359874926582439`.

Function 5 showed the strongest sustained improvement and finished with `4440.957216598753` in Week 13. Function 6 also recorded its strongest weekly result in Week 13 at `-0.6071562248604215`, although repeated coordinate behaviour remained uncertain. Function 7 retained `1.3809299933612855`, first achieved in Week 5 and later confirmed. Function 8 repeatedly returned its best value of `9.58024`, demonstrating the value of confirmation when further movement offered little clear benefit.

These results are the strongest values observed within the participant query budget. They do not establish the mathematical global optima. That distinction is central to the final interpretation. The project demonstrates improvement, recovery and confirmation within a sparse sequential experiment, rather than complete knowledge of the hidden functions.

If I were starting again, I would create one consistent experimental register from the first week. Each proposed query would include its purpose, expected outcome, uncertainty and stopping condition before submission. I would reserve specific rounds for repeatability checks, particularly for functions such as Function 6. I would also scale movement according to dimensionality and separate exploratory proposals from refinement proposals before choosing the final coordinate.

Earlier chronological validation would strengthen the use of clustering, surrogate models and dimensionality reduction. Any model used to guide a decision should be tested only on information that would have been available at that point. This would reduce the risk of allowing later observations to influence an apparently successful earlier strategy.

## 4. Main trade-offs and decisions

The most important trade-off was between exploration and exploitation. Exploration gathered information about unfamiliar regions but risked moving away from a strong known point. Exploitation refined a promising area but could miss a better region elsewhere. Confirmation offered a third choice. Repeating a coordinate tested stability, although it used a scarce weekly query without exploring a new point.

The balance changed over time. Early uncertainty justified broader movement. Later evidence supported smaller, function specific actions. Function 5 continued to reward controlled boundary movement, so exploitation remained worthwhile. Functions 1 and 8 had repeatable best points, making confirmation more valuable than further exploration. Function 2 illustrated the danger of continuing a local move after a strong improvement. Its Week 13 decline showed that a small step is not automatically a safe step.

There was also a trade-off between analytical complexity and decision value. Clustering, principal component analysis and chronological surrogate testing added useful perspectives, but none replaced the returned objective values. A method was retained only when it clarified a practical choice. When model structure and observed performance disagreed, the verified output history took priority.

Stopping was another active decision. Continuing every function until the final week would have treated the available budget as something that had to be spent, rather than a resource that should be justified. Some functions had reached stable points where another move offered limited expected value. Others still had a supported direction or unresolved uncertainty. The final strategy therefore combined continuation, recovery, retention and confirmation rather than applying one rule to all eight functions.

## 5. Learning, wider application and post challenge development

The strongest lesson was that evidence should determine the method. Dimensionality, output scale, repeatability and recent behaviour all affected what counted as a sensible next step. A technique that helped one function could be unnecessary or misleading for another. This changed my view of optimisation from a search for one superior algorithm into a process of disciplined adaptation.

The work also showed the importance of separating observation from interpretation. A chart can reveal movement, a cluster can organise similar points and a principal component can summarise variance. None of these, on its own, explains the hidden function. Clear boundaries around each claim made the final conclusions more credible and the repository more useful to other readers.

After the formal capstone, I extended this principle through Black Box Resolution, or BBR. BBR compares possible explanations of hidden behaviour, tests them chronologically and rejects those that fail. Its purpose is not to claim recovery of the original equation. It seeks the best supported local account of the evidence while retaining uncertainty.

The Pisharam Delta Hierarchy and Influence State framework, known as PDHIS, examined recursively nested change from Delta 1 to Delta 10. This introduced Delta as the Signature of Change. The aim was to identify whether direction, persistence, reversal, plateau or oscillation formed a coherent pattern across related Delta levels. The analysis found promising relationships at Delta 2, Delta 4 and Delta 5, but none passed the adjusted false discovery threshold. The result is therefore a structured research direction rather than a validated forecasting rule.

These lessons have wider professional value. In clinical neurology, service improvement and organisational decision making, evidence often arrives sequentially and remains incomplete. Decisions must balance immediate benefit, further learning, reliability and risk. A good process records why an action was taken, checks the outcome and changes course when the evidence no longer supports the original plan.

## Conclusion

The capstone progressed from broad exploration to a transparent, function specific decision process. The final results came from several forms of reasoning: continued improvement for Function 5, local refinement for Functions 2 and 3, recovery for Functions 4 and 7, confirmation for Functions 1 and 8, and cautious interpretation of variability for Function 6. No single technique produced every success.

The lasting achievement is therefore not only the set of retained outputs. It is the development of a reproducible way to move from observation to interpretation, decision, outcome and review. The repository, Visual Book, BBR work and PDHIS analysis now present that process at different levels of detail while preserving the official evidence. The project has strengthened my ability to make careful decisions under uncertainty and to explain both what the evidence supports and where its limits remain.
