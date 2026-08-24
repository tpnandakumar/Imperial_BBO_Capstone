# Smart Advanced Continuation and Stopping Policy

## Explore, Exploit, Extend

The post-capstone optimisation extension is organised around three linked actions: **Explore, Exploit and Extend**.

**Explore** is used where uncertainty remains high enough to justify learning more about the local landscape. **Exploit** is used where a strong region is already supported and the best use of the next query is to refine or confirm it. **Extend** is used when the latest evidence still shows improvement, so the search should continue beyond the formal competition limit as a research exercise until a justified stopping point is reached.

The key principle is that continuation should be selective. Functions 2, 3, 5 and 6 remain active optimisation targets. Functions 1, 4, 7 and 8 are treated as frozen reference functions unless new evidence later gives a reason to reopen them.

## Decision cycle

```text
Explore
Identify unresolved uncertainty or an untested nearby direction
        ↓
Exploit
Refine the strongest supported region
        ↓
Extend
Continue only while improvement or useful information remains available
        ↓
Stop
Retain the strongest verified point when further querying is no longer justified
```

The stopping decision is therefore part of the optimisation process rather than an administrative end point.

## Function-specific policy

| Function | Mode | Why | Continue until | Stop location |
| --- | --- | --- | --- | --- |
| F1 | Exploit, then stop | Best point repeatedly reproduced | No routine continuation required | `0.600000,0.600000` |
| F2 | Explore, exploit, extend | Week 12 best is bracketed by weaker neighbours | Local bracket around the peak is resolved | Best verified point inside the resolved bracket, currently centred near `0.690000,0.950000` |
| F3 | Exploit, extend | Final step still improved | First confirmed reversal is followed by local refinement that fails to improve | Best verified point inside the final local bracket |
| F4 | Exploit, then stop | Historical best recovered and repeated | No routine continuation required | `0.600000,0.430000,0.420000,0.250000` |
| F5 | Exploit, extend | Boundary refinement continued to improve through Round 13 | First confirmed non-improving step, or the first-coordinate lower boundary if improvement continues | Best verified boundary point reached before reversal, or the boundary itself |
| F6 | Explore first, then exploit if justified | Same coordinate produced different outputs | Response variability is characterised well enough to distinguish signal from variation | Point with the strongest replicated response estimate |
| F7 | Exploit, then stop | Historical best recovered and repeated | No routine continuation required | `0.040000,0.480000,0.260000,0.220000,0.420000,0.740000` |
| F8 | Exploit, then stop | Best point repeatedly reproduced | No routine continuation required | `0.060000,0.070000,0.030000,0.040000,0.410000,0.820000,0.500000,0.910000` |

## Function 2

Function 2 should continue because the strongest local result is already bracketed by weaker neighbours:

| First coordinate | Second coordinate | Output |
| ---: | ---: | ---: |
| `0.695000` | `0.950000` | `0.5848554940277205` |
| `0.690000` | `0.950000` | `0.7335252043269003` |
| `0.685000` | `0.950000` | `0.6413430885133908` |

A local quadratic interpolation places the estimated stationary point near `0.6894136686090656`, giving a six-decimal research candidate of `0.689414,0.950000`.

The extension should continue until smaller two-sided tests fail to improve the same central region. At that point the bracket is resolved and the best verified point inside it should be retained.

## Function 3

Function 3 ended with continued improvement:

```text
0.840000,0.160000,0.840000  ->  -0.06542982421105416
0.850000,0.150000,0.850000  ->  -0.05985127532683556
0.855000,0.145000,0.855000  ->  -0.05685061601567621
```

The next research step is therefore `0.860000,0.140000,0.860000`. If it improves, extend again with an equal or smaller step. If it declines, the search should form a local bracket between the last improving point and the first declining point, then refine inside that interval.

The stop point is the best verified coordinate inside that final bracket after further smaller moves fail to improve it.

## Function 5

Function 5 produced the clearest sustained trend:

- Week 11: `4411.0387356061765`
- Week 12: `4427.343995806448`
- Week 13: `4440.957216598753`

The last three coordinates are already at, or effectively at, the upper boundary. The extension should therefore vary only the first coordinate while keeping the others fixed at `1.000000`.

The next research candidate is `0.080000,1.000000,1.000000,1.000000`. If improvement continues, reduce the first coordinate further in progressively cautious steps. Stop at the first confirmed non-improving move and retain the best preceding point. If improvement persists all the way to `0.000000`, then the lower boundary itself becomes the natural stopping location.

## Function 6

Function 6 requires a different strategy because the same coordinate produced different outputs. The point `0.700000,0.200000,0.700000,0.700000,0.200000` returned different values across repeated evaluations.

The first extension step is therefore replication, not movement. Further directional optimisation should begin only after repeated measurements give a usable estimate of central tendency and response spread.

The search stops when nearby replicated points do not improve the estimated mean response beyond the observed variation. The retained point should then be the coordinate with the strongest replicated response estimate, not simply the single highest isolated observation.

## Portfolio stopping rule

A function moves from **Extend** to **Stop** when one of the following is satisfied:

1. a local peak is bracketed and smaller moves on both sides do not improve it;
2. successive gains become negligible and no justified nearby direction remains;
3. a boundary is reached and no other coordinate direction has evidence for further gain;
4. repeated evaluations show that apparent differences are smaller than the response variability;
5. another query would add less useful information than simply retaining the strongest verified point.

This creates a full optimisation lifecycle:

```text
Explore -> Exploit -> Extend -> Stop
```

The process can also move backwards when the evidence requires it. A failed exploitation step can trigger renewed exploration, while a newly discovered improving direction can reopen extension. The aim is not to maximise the number of queries. The aim is to continue only while each additional query has a defensible expected value.