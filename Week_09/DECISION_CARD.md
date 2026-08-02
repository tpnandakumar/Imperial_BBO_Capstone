# Week 09 Decision Card

## Identification

- Course module: 21
- Capstone week: 09
- Optimisation round: 9
- Decision owner: Dr N T Pisharam

## Decision objective

Select one valid query vector for each hidden function using the strongest available evidence while balancing performance, robustness, uncertainty and the limited query budget.

## Decision framework

Each function was assessed using:

1. recent output movement;
2. best-so-far evidence;
3. stability of the surrounding region;
4. uncertainty and information value;
5. risk of premature convergence;
6. expected value of exploration versus refinement.

## Function decisions

### Function 1

- Evidence: repeated output effectively equal to zero.
- Interpretation: current region remained uninformative.
- Decision: broader exploration.
- Risk: another low-information query.
- Alternative considered: continued local refinement, rejected because repeated nearby evidence did not show progress.

### Function 2

- Evidence: positive output, but lower than Week 08.
- Interpretation: productive region remained plausible, although the latest direction was weaker.
- Decision: cautious local refinement near the stronger region.
- Risk: overreacting to one decline or drifting away from the best-known area.

### Function 3

- Evidence: negative output and a small decline.
- Interpretation: current local direction lacked confirmation.
- Decision: reassess with a nearby alternative rather than a large jump.
- Risk: continued sampling of an unproductive basin.

### Function 4

- Evidence: improved from Week 08 while remaining negative.
- Interpretation: local movement appeared favourable.
- Decision: continue controlled refinement.
- Risk: mistaking movement towards zero for evidence of a broader optimum.

### Function 5

- Evidence: highest output and continued Week 08 to Week 09 improvement.
- Interpretation: strongest validated productive region.
- Decision: exploit through very small local adjustment.
- Risk: diminishing returns and boundary overconcentration.

### Function 6

- Evidence: negative output and slight decline.
- Interpretation: local structure remained uncertain.
- Decision: reassess nearby alternatives.
- Risk: excessive local search without information gain.

### Function 7

- Evidence: strong positive output with a small decline.
- Interpretation: region remained stable and productive.
- Decision: cautious refinement.
- Risk: degrading a reliable result through unnecessary movement.

### Function 8

- Evidence: high and stable positive output with minimal decline.
- Interpretation: region remained reliable.
- Decision: minimal local refinement.
- Risk: spending query budget where marginal gain may be limited.

## Portfolio allocation

| Strategy | Functions | Rationale |
|---|---|---|
| Exploit | F5 | Strongest repeated performance |
| Refine | F2, F4, F7, F8 | Productive or improving regions |
| Reassess | F3, F6 | Negative and recently weaker |
| Explore | F1 | Persistently uninformative region |

## Confidence statement

Confidence was highest for the direction of F5, moderate for F4, F7 and F8, and lower for F1, F2, F3 and F6. Confidence refers to the appropriateness of the strategy, not certainty that the next query will improve the objective value.

## Human oversight

No query was approved solely from automated output. Candidate coordinates were checked against prior submissions, dimensionality, bounds, strategy and potential duplication before final submission.

## Linked documentation

- [DATASET.md](DATASET.md)
- [DATASHEET.md](DATASHEET.md)
- [MODEL_CARD.md](MODEL_CARD.md)
- [VALIDATION.md](VALIDATION.md)
- [ASSUMPTIONS.md](ASSUMPTIONS.md)
