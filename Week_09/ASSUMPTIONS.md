# Week 09 Assumptions Register

## Identification

- Course module: 21
- Capstone week: 09
- Optimisation round: 9
- Maintainer: Dr N T Pisharam

## Purpose

This register makes the assumptions behind Week 09 analysis and query selection explicit. It supports transparency, later review and future Assumption Audit development.

## Assumptions

| ID | Assumption | Basis | Risk if false | Treatment |
|---|---|---|---|---|
| A09-01 | Larger objective values are preferable | Challenge convention and prior analysis | Strategy direction would be reversed | Retained |
| A09-02 | Returned outputs correspond correctly to submitted inputs | Portal workflow | All comparisons would be unreliable | Checked against weekly records |
| A09-03 | Small local changes are appropriate in repeatedly productive regions | F5, F7 and F8 trajectories | Local optimum or boundary trap may be missed | Use cautious refinement and retain exploration |
| A09-04 | An effectively zero F1 output indicates an uninformative region | Repeated near-zero results | A narrow optimum may exist nearby | Broader exploration rather than abandonment |
| A09-05 | Movement towards a less negative value is an improvement | Maximisation objective | Scale or noise may distort interpretation | Compare across multiple rounds |
| A09-06 | Recent decline does not necessarily invalidate a productive region | Sequential noisy search | Resources may be spent on a weakening region | Reassess confidence after each round |
| A09-07 | Historical observations remain relevant to the next query | Stationarity assumed within the challenge | Non-stationarity would weaken prior evidence | Monitor for abrupt inconsistent changes |
| A09-08 | Human review reduces unsupported or duplicated recommendations | Supervised workflow | Human bias may still influence decisions | Preserve explicit rationale and alternatives |
| A09-09 | Function scales are not directly comparable | Observed output ranges differ substantially | Cross-function ranking may mislead | Use ranks only descriptively |
| A09-10 | The small dataset can guide local decisions but cannot prove global optimality | Black box constraints | Overconfidence and premature convergence | State uncertainty and preserve exploration |

## Assumptions changed from earlier rounds

By Week 09, the earlier expectation that all functions required broad exploration was no longer justified. Evidence supported differentiated treatment. F5 had sufficient repeated evidence for exploitation, while F1 still required broad exploration. F2, F4, F7 and F8 supported refinement, and F3 and F6 required reassessment.

## Review trigger

An assumption must be reviewed if:

- a new output contradicts the established trajectory;
- repeated local refinement produces no improvement;
- a supposedly stable function changes sharply;
- a data correction alters the historical comparison;
- a strategy label no longer matches the evidence.

## Linked records

- [DATASHEET.md](DATASHEET.md)
- [DECISION_CARD.md](DECISION_CARD.md)
- [VALIDATION.md](VALIDATION.md)
