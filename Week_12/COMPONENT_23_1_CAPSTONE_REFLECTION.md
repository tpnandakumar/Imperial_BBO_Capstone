# Component 23.1 Capstone Reflection Record

## Strategy maturation

The strategy developed from broad exploration into function specific decision making. Early rounds tested wide areas because little was known about the hidden surfaces. Later rounds used each function's own history to distinguish productive regions from weak directions. By Week 11, the choice was no longer simply whether to explore or exploit. It included confirmation, local refinement, historical recovery and controlled boundary testing.

Week 11 provided a strong outcome test. All eight functions improved relative to Week 10. Functions 2 and 5 reached new verified best values, Functions 1 and 8 reproduced earlier best values, and Functions 3, 4 and 6 recovered after weaker rounds. These results supported the regional strategy while also showing why the eight functions should not be treated as one comparable numerical scale.

## Variation, correlation and redundancy

Principal component analysis was used to examine how the submitted coordinates had moved together. For Functions 3, 4, 5 and 8, more than 90 per cent of observed query variance lay in the first principal component. Functions 6 and 7 required two components to reach the same threshold.

This concentration does not establish the effective dimensionality of the unknown objective functions. The query history was created adaptively, so its variance partly reflects earlier strategic choices. A narrow trajectory may reveal a productive direction, but it may also show that other directions were sampled less often.

The PCA findings were therefore compared with returned objective values. Function 5 offered the clearest agreement. Its coordinates had become concentrated near the upper boundary, and successive controlled moves continued to improve the result. For Functions 3, 4, 6 and 7, verified historical performance gave a stronger immediate target than extrapolation along a principal direction.

## Simplification and continued exploration

Simplification became appropriate when several observations supported the same conclusion. Functions 1 and 8 had repeatable best points. Functions 4 and 7 had identifiable historical best points that could be tested directly. Function 5 had a sustained boundary trend. In these cases, reducing unnecessary movement protected reliable evidence.

Continued exploration remained valuable where uncertainty could affect the final decision. Function 6 was the clearest example. Returning to its earlier coordinates improved the Week 12 result from `-0.7268715077444687` to `-0.7078316130911375`, but it did not reproduce its stronger historical value. This exception prevented the strategy from assuming that every return to a previous point would behave identically.

## Exploration and exploitation balance

The Week 12 submission balanced several actions within one round. Functions 1 and 8 repeated confirmed best points. Function 2 made a small local refinement and improved from `0.5848554940277205` to `0.7335252043269003`. Functions 3, 4, 6 and 7 returned to stronger historical regions. Function 5 made another controlled boundary refinement and improved from `4411.0387356061765` to `4427.343995806448`.

No function deteriorated relative to Week 11. Functions 2, 3 and 5 reached new verified best values. Functions 4 and 7 recovered their historical best values, while Functions 1 and 8 repeated verified best values exactly. The outcome supports measured exploitation where improvement has been repeated, but it does not prove global optimality.

## Final strategic reasoning

The most important lesson is that method selection must follow evidence. PCA clarified variance, coordinate relationships and redundancy, but objective performance remained the deciding test. Historical recovery was useful for some functions, exact repetition strengthened reliability for others, and controlled local movement remained productive for Functions 2 and 5.

The final round should continue this function specific approach. Strong regions can be exploited where gains remain repeatable, while uncertainty should be preserved where the evidence is incomplete. This maintains a clear audit trail from observation to interpretation, decision and outcome.
