# Smart Advanced Continuation and Stopping Policy

## Explore, Exploit, Extend

The post-capstone optimisation extension is organised around three linked actions: **Explore, Exploit and Extend**.

**Explore** is used where uncertainty remains high enough to justify learning more about the local landscape. **Exploit** is used where a strong region is already supported and the best use of the next query is to refine or confirm it. **Extend** is used when the latest evidence still shows improvement, so the search should continue beyond the formal competition limit as a research exercise until a justified stopping point is reached.

Functions 2, 3, 5 and 6 remain active optimisation targets. Functions 1, 4, 7 and 8 are treated as frozen reference functions unless new evidence gives a reason to reopen them.

## Decision cycle

```text
Explore -> Exploit -> Extend -> Stop
```

The process can move backwards when evidence requires it. A failed exploitation step can reopen exploration, while a new improving direction can reopen extension.

## Function-specific policy

| Function | Mode | Continue until | Current stopping location |
| --- | --- | --- | --- |
| F1 | Exploit, then stop | No routine continuation required | `0.600000,0.600000` |
| F2 | Explore, exploit, extend | Local bracket around the peak is resolved | strongest verified point in the bracket, currently `0.690000,0.950000` |
| F3 | Exploit, extend | first reversal is followed by local refinement that fails to improve | strongest verified point in the final local bracket |
| F4 | Exploit, then stop | No routine continuation required | `0.600000,0.430000,0.420000,0.250000` |
| F5 | Exploit, extend | first confirmed non-improving step or lower boundary | strongest verified boundary point before reversal |
| F6 | Explore first | response variability is sufficiently characterised | strongest replicated response estimate |
| F7 | Exploit, then stop | No routine continuation required | `0.040000,0.480000,0.260000,0.220000,0.420000,0.740000` |
| F8 | Exploit, then stop | No routine continuation required | `0.060000,0.070000,0.030000,0.040000,0.410000,0.820000,0.500000,0.910000` |

## Portfolio stopping rule

A function moves from Extend to Stop when one of the following is satisfied:

1. a local peak is bracketed and smaller moves on both sides do not improve it;
2. successive gains become negligible and no justified nearby direction remains;
3. a boundary is reached and no other coordinate direction has evidence for further gain;
4. repeated evaluations show that apparent differences are smaller than response variability;
5. another query would add less useful information than retaining the strongest verified point.

This policy is post-capstone research. It does not alter the official Week 01 to Week 13 record.