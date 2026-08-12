# Week 10 Assumptions

## Purpose

This document states the assumptions used in the Week 10 analysis and separates observed evidence from interpretation.

## 1. Historical observations are informative

Previously submitted query vectors and returned objective values are treated as useful evidence for subsequent query selection. This does not imply that the hidden response surfaces are smooth or that nearby inputs must produce nearby outputs.

## 2. Each function requires independent interpretation

The eight objective functions operate on different scales and have different dimensionalities. A high numerical output for one function is therefore not treated as directly comparable with the output of another. Progress is assessed mainly within each function across successive rounds.

## 3. Local refinement requires evidence

Local movement is reasonable only where the history suggests a productive region. Week 10 illustrates why this remains conditional. Function 2 improved after local refinement, while Function 4 deteriorated substantially after its Week 10 movement.

## 4. Repeated queries can provide information

Repeating a previously successful input can be useful when the purpose is to test repeatability rather than search a new region. Function 5 used the same Week 09 input in Week 10 and returned exactly `4394.868042481448` again. This supports repeatability at that tested point but does not establish stability across the surrounding region.

## 5. A negative result can still change the next decision

A deterioration in objective value is not an optimisation gain, but it can narrow the plausible next directions. The Week 10 declines in Functions 4 and 6 therefore supported reassessment.

## 6. Near zero does not imply an optimum

Function 1 returned `2.8950706668499033e-23`. Its historical outputs remained extremely close to zero, so the Week 10 result is treated as unresolved behaviour rather than evidence that an optimum has been located.

## 7. Stable positive regions still require caution

Functions 7 and 8 remained positive but declined slightly in Week 10. Their histories support conservative refinement, not unrestricted movement or a claim that either region contains a global optimum.

## 8. The hidden functions remain unknown

No analytical equation, derivative, Hessian, exact optimum or complete response surface is available. All conclusions remain conditional on the finite set of observed query and output pairs.

## 9. Human review remains part of the workflow

Computational summaries support the analysis, but final interpretation and query selection remain human supervised. Strategy labels such as explore, refine, reassess and exploit are decision aids derived from the evidence, not properties supplied by the competition platform.

## 10. Chronology of the record

Week 10 is interpreted from the evidence and methods recorded for that stage of the capstone. Later research developments are documented separately so that the sequence of decisions remains clear.

## Review

These are working assumptions for sequential decision making. New observations can strengthen, weaken or overturn them as the optimisation record develops.