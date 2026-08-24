# Final Capstone Synthesis

## Would I continue optimising if another round were available?

Yes, but not by applying the same decision to all eight functions.

The final thirteen round record shows that the search had not reached a uniform stopping point. Some functions had become stable enough that another query would mainly test repeatability. Others still showed evidence that further improvement might be available. The correct decision is therefore function specific rather than a single yes or no for the whole portfolio.

## Why the answer is yes overall

Round 13 still produced new overall best values for Functions 3, 5 and 6. That is direct evidence that useful improvement remained available at the end of the formal competition. A blanket decision to stop after Round 12 would therefore have left measurable performance on the table.

Function 5 is the clearest example. The sequence of controlled boundary refinements continued to improve the objective and Round 13 reached `4440.957216598753`, above the Week 12 value of `4427.343995806448`. The direction was still productive, although the remaining margin for movement had become very small because the coordinates were already concentrated at or near the upper boundary.

Function 3 also improved again, reaching `-0.05685061601567621`, which became its strongest observed value. Function 6 improved to `-0.6071562248604215`, also its strongest observed value, although repeated use of the same coordinate had produced different outputs across the history. That variability means another query could still be informative, but it would need to be interpreted carefully.

## Why I would not continue all functions in the same way

Functions 1, 4, 7 and 8 finished by exactly retaining their strongest observed values. Repeating those points again would add little optimisation value unless the purpose was specifically to test stability or reproducibility.

Function 2 gives the strongest argument against automatic continued exploitation. Week 12 reached `0.7335252043269003`, but the final Round 13 result fell to `0.6413430885133908`. The previous local refinement had been productive, yet the next move did not maintain that gain. Another round would therefore need to return towards the Week 12 optimum or reopen local exploration rather than continue the same directional step.

This final contrast is important. The project did not finish with one universal rule. It finished with different stopping conditions for different functions.

## Function specific continuation decision

| Function | Further optimisation? | Reason |
| --- | --- | --- |
| F1 | No, unless testing repeatability | Strongest value was repeatedly reproduced and no new directional evidence appeared |
| F2 | Yes | Final deterioration suggests the local step crossed away from the stronger Week 12 region, so a controlled recovery or neighbourhood test remains justified |
| F3 | Yes | Round 13 produced a new best, so the local region still contained useful improvement |
| F4 | No, unless testing the surrounding basin | Historical best was recovered and retained without evidence of a better direction |
| F5 | Yes, cautiously | Round 13 produced another new best and the boundary trend remained productive, but very little feasible movement remains |
| F6 | Yes, mainly to resolve uncertainty | Round 13 produced a new best, but identical coordinates have returned different values, so repeatability and response variability need further testing |
| F7 | No, unless probing the neighbourhood | Historical best was recovered and retained, with no evidence that further tightening would improve it |
| F8 | No, unless testing stability | The same best value was reproduced repeatedly and further exploitation has little expected information gain |

## Decision rule

If another round were available, I would therefore continue optimisation for Functions 2, 3, 5 and 6, while stopping routine optimisation for Functions 1, 4, 7 and 8.

The continuation rule would be:

1. continue when the latest round creates a new best or exposes unresolved uncertainty;
2. stop when repeated best values are stable and no credible new direction remains;
3. reverse or reopen local search when a final exploitation step deteriorates;
4. separate optimisation value from validation value, because a repeated query can still be useful even when it is unlikely to improve the objective.

## Final interpretation

The main lesson from the capstone is that stopping is itself an optimisation decision. A strong result is not enough to justify stopping if the latest evidence still shows improvement. Equally, continued querying is not justified simply because more budget exists.

If an additional round were available, my decision would therefore be yes at portfolio level, but only for the functions where the expected information or performance gain still exceeds the value of stopping. That conclusion follows directly from the final round evidence and is more defensible than either unconditional continuation or unconditional termination.