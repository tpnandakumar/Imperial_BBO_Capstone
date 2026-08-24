# Week 13 Strategy Model Card

## System

Human supervised sequential optimisation workflow for eight independent black box objectives.

## Final decision inputs

The final analysis draws on:

- complete Weeks 1 to 12 objective history;
- confirmed best points and repeatability evidence;
- local directional changes;
- clustering and historical region recovery;
- PCA as a structural comparison method;
- exploration and exploitation reasoning introduced in Module 24.

## Decision principle

No single method is assumed to be optimal across all eight functions. The strongest available evidence is selected separately for each objective.

## Final observed performance

Round 13 produced new overall best values for Functions 3, 5 and 6, retained established best values for Functions 1, 4, 7 and 8, and declined from the Week 12 best for Function 2.

## Strengths

The workflow preserves chronology, separates structural analysis from objective evidence, records unsuccessful moves, and retains exact numerical source values.

## Limitations

The query budget is small, the search spaces are continuous, and the hidden functions are unknown. Function 6 also shows that repeated evaluation at the same recorded coordinate can return different values. The workflow therefore identifies the strongest observed evidence rather than a proven global optimum.
