# Week 10 Assumptions

## Purpose

This document makes the assumptions underlying the Week 10 analysis explicit. The aim is to distinguish observed evidence from the reasoning used to select and interpret optimisation strategies.

## 1. Historical observations are informative

The workflow assumes that previously submitted query vectors and returned objective values contain useful information for subsequent query selection. This does not imply that the hidden response surfaces are smooth or that nearby inputs must produce nearby outputs.

## 2. Each function requires independent interpretation

The eight objective functions operate on different scales and have different dimensionalities. A high numerical output for one function is therefore not treated as directly comparable with the numerical output of another. Progress is assessed primarily within each function across successive rounds.

## 3. Local refinement requires evidence

Local movement is assumed to be reasonable only where historical observations suggest a productive region. Week 10 provides evidence that this assumption must remain conditional. Function 2 improved after local refinement, whereas Function 4 deteriorated substantially following its Week 10 movement.

## 4. Repeated queries can provide information

Repeating a previously successful input can be justified when the purpose is to test repeatability rather than to search a new region. Function 5 used the same Week 09 input in Week 10 and returned exactly `4394.868042481448` again. The observation supports repeatability at that tested point. It does not prove stability throughout the surrounding region.

## 5. A negative result can still provide information

A deterioration in objective value is not interpreted as a useful optimisation gain, but it can narrow the set of plausible next directions. The Week 10 declines in Functions 4 and 6 therefore informed reassessment rather than being treated as successful optimisation.

## 6. Near zero does not imply an optimum

Function 1 returned `2.8950706668499033e-23`. Because its historical outputs remained extremely close to zero, the Week 10 result is treated as unresolved behaviour rather than evidence that an optimum has been located.

## 7. Stable positive regions still require caution

Functions 7 and 8 remained positive but declined slightly in Week 10. The workflow assumes that established positive performance can justify conservative refinement, but not unrestricted movement or a claim that the region contains a global optimum.

## 8. The hidden functions remain unknown

No analytical equation, derivative, Hessian, exact optimum or complete response surface is available. All conclusions are conditional on the finite set of observed query and output pairs.

## 9. Human review remains part of the workflow

Computational summaries support the analysis, but final interpretation and query selection remain human supervised. Strategy labels such as explore, refine, reassess and exploit are decision aids derived from evidence, not properties supplied by the competition platform.

## 10. Later methods are not applied retrospectively

Research frameworks developed after a given optimisation round should not be described as having generated that round unless contemporaneous evidence supports the claim. Week 10 documentation therefore distinguishes the methods and reasoning recorded for Week 10 from later developments in PGC, PFRAMOS or other research extensions.

## Review condition

These assumptions should be reconsidered whenever new returned outputs contradict the behaviour expected from the current strategy. They are working assumptions for sequential decision making, not statements about the true hidden functions.