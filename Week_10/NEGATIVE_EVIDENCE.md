# Week 10 Negative Evidence and Failed Hypotheses

## Why negative evidence is recorded

Sequential optimisation is not evaluated only by counting improved objective values. A query that performs worse can still provide useful evidence by weakening a local hypothesis, identifying an unproductive direction or showing that a previously plausible strategy requires revision.

Week 10 contains several examples where the returned value did not improve but materially changed the next decision.

## Function 4

Week 09 returned `-11.788939969158545`. The Week 10 query returned `-13.483642655031158`, an exact change of `-1.694702685872613`.

The working hypothesis that the Week 10 movement could improve the local region was therefore weakened by the returned evidence. The appropriate response was not to describe the query as successful, but to change direction and reassess Function 4 before the next submission.

This was the clearest negative result in Week 10 and had high decision value because it argued against automatic continuation of the same local trajectory.

## Function 6

Week 09 returned `-1.1733030029888645`. Week 10 returned `-1.2283806967341901`, an exact change of `-0.0550776937453256`.

The deterioration was smaller than for Function 4, but it still failed to support continued movement in the same direction. Function 6 was therefore moved from local continuation towards reassessment.

## Function 7

Week 09 returned `1.314307996450604`. Week 10 returned `1.285160161342515`, an exact change of `-0.029147835108089`.

The result remained positive, so the evidence did not justify abandoning the region. It did, however, weaken the case for a larger move in the same direction. The resulting decision was conservative refinement.

## Function 8

Week 09 returned `9.4709436`. Week 10 returned `9.4646525`, an exact change of `-0.0062911`.

The small deterioration suggested a relatively stable positive region but did not support aggressive local movement. The negative evidence therefore changed the degree of exploitation rather than the overall classification of the region.

## Function 5 as a non-improving but informative query

Function 5 did not improve numerically in Week 10. The exact Week 09 query was repeated and returned exactly `4394.868042481448` again.

This is different from the negative cases above. The absence of improvement was expected because the purpose of the repeat was to test the behaviour of the established point. The result reduced uncertainty about repeatability at that exact query and therefore supplied information even though the objective value did not increase.

## Experimental lesson

Week 10 demonstrates three distinct outcomes:

1. **Improvement**, as observed for Functions 2 and 3.
2. **Negative evidence**, as observed most clearly for Functions 4 and 6.
3. **Information without objective improvement**, as demonstrated by the repeated Function 5 query.

Separating these outcomes prevents the analysis from treating every non-improving query as equivalent. It also makes the reasoning behind the Week 11 strategy auditable.

## Limitation

A single unsuccessful query does not prove that an entire region is poor. It provides evidence against the tested point and, depending on the surrounding history, may weaken a local search hypothesis. The interpretation therefore remains conditional on the finite observations available at Week 10.