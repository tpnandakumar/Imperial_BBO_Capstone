# Delta of BBO: PDHIS Analysis of the Eight Functions

The latest extension adds [regularised logistic classification, chronological validation, leave-one-function-out testing, permutation analysis, coefficient stability and influence-state summaries](PDHIS_ADVANCED_FINDINGS.md). These results are exploratory and do not replace the original Delta evidence or establish a validated forecasting rule.

A further [higher-order pointer analysis](PDHIS_HIGH_ORDER_POINTERS.md) tests whether oscillation in Delta 6 to Delta 10 precedes positive Delta 1, Delta 2 or Delta 3 behaviour one week later. It defines the later low-order Delta as the target and keeps every predictor within the information available at the prediction week.

The [event-locked flicker study](PDHIS_EVENT_LOCKED_FLICKERS.md) looks backwards from known event and non-event weeks. It characterises the preceding six observations through temporal dispersion, sign-change frequency, peak spacing, energy, amplitude, persistence, amplification, Delta 2 energy and flicker density.

The [matched event atlas and stability analysis](PDHIS_MATCHED_EVENT_ATLAS.md) exploits the existing evidence further through same-function matching, event-threshold sensitivity and leave-one-function-out transfer testing. These stronger checks do not confirm the initial flicker candidate.

This analysis applies the Pisharam Delta Hierarchy and Influence States
(PDHIS) to the eight hidden functions in the completed BBO challenge.
"Delta of BBO" refers to this specific application. PDHIS is the analytical
framework; the weekly outputs of F1 to F8 are the observed sequences to which
the hierarchy is applied.

PDHIS is used to identify the earliest observable occurrence of structured
change. It tests whether a developing Delta sequence can distinguish
vector-directed change, an approaching plateau, reversal or oscillation from
irregular fluctuation. It then evaluates whether that sequence has
chronological predictive value for the direction and trajectory of subsequent
functional change.

Within the wider resolution process, PDHIS supplies evidence to the recurring
cycle: Evaluate, Resolve, Explore or Exploit, Extend, Optimise, Evolve,
Experiment and Evaluate again. Explore and Exploit remain bidirectionally
linked choices rather than fixed consecutive stages.

PDHIS did not originate from inspecting the final BBO outcomes. The Delta
prediction work had already been developed through the separate PIMF and PMOS
research project. The present analysis consolidates that earlier hierarchy,
extends it consistently from Delta 1 to Delta 10 and evaluates it against the
complete BBO record.

The official record remains unchanged. The source contains thirteen genuine
weekly portal outputs for every function. The values and tests in this folder
are newly calculated from that fixed record, while the underlying Delta
prediction concept predates the completed challenge analysis.

## Questions

1. What patterns appear from Delta 1 through Delta 10?
2. Does a Delta order relate to the next output or the next output change?
3. Are any apparent relationships stronger than shuffled chronology?
4. How quickly does usable evidence decline at higher Delta orders?
5. Do coordinate movements and output movements carry the same information?
6. Can the timing and propagation of a Delta series predict direction or
   trajectory rather than simply describe past variation?

## Method

Outputs are range-normalised separately within each function before comparing
functions. Finite differences are then calculated recursively from Delta 1 to
Delta 10. Predictive associations are strictly chronological: a Delta ending
at Week t is compared only with the output or output change at Week t+1.

Pooled Spearman correlations are calculated after within-function
standardisation. Directional hit rates exclude exact zero changes.
Randomisation validation shuffles the next changes within each function while
preserving the marginal distribution. Two thousand permutations are used.
Benjamini-Hochberg correction controls the false-discovery rate across the ten
Delta-order tests.

These calculations assess association and limited short-horizon predictability.
They do not recover the hidden equations, establish causality or prove a global
optimum.

## Meaning of the Delta hierarchy

PDHIS treats change as a recursive Lotus hierarchy. Delta 1 is the direct
change in the observed function. Delta 2 is the change of Delta 1, or the
change of change. Delta 3 is the change of Delta 2, and the same definition
continues recursively:

`Delta^n y(t) = Delta^(n-1) y(t) - Delta^(n-1) y(t-1)`

The first levels have the clearest practical interpretation. Delta 1 describes
direction and magnitude. Delta 2 describes acceleration, curvature and the
development of a plateau or reversal. Delta 3 examines whether that second
order behaviour is itself changing. Higher levels describe increasingly
complex repeated transitions and may expose oscillation, improvement,
deterioration or instability that is less visible in the raw output.

| Level | Recursive definition | Practical meaning | Forward cases in the BBO record |
|:--:|:--|:--|--:|
| Delta 1 | `y(t) - y(t-1)` | Direct observed change: direction and magnitude. | 88 |
| Delta 2 | `Delta 1(t) - Delta 1(t-1)` | Change of change: acceleration, curvature, emerging plateau or reversal. | 80 |
| Delta 3 | `Delta 2(t) - Delta 2(t-1)` | Whether acceleration, plateau or reversal is itself changing. | 72 |
| Delta 4 | `Delta 3(t) - Delta 3(t-1)` | Persistence, reversal or developing oscillation in the third-order pattern. | 64 |
| Delta 5 | `Delta 4(t) - Delta 4(t-1)` | Medium-order transition used to test whether a repeated pattern propagates. | 56 |
| Delta 6 | `Delta 5(t) - Delta 5(t-1)` | Deeper recursive change, interpreted through coherence with lower levels. | 48 |
| Delta 7 | `Delta 6(t) - Delta 6(t-1)` | Higher-order propagation or instability already present in the change sequence. | 40 |
| Delta 8 | `Delta 7(t) - Delta 7(t-1)` | Deep repeated change, treated as exploratory as chronological evidence narrows. | 32 |
| Delta 9 | `Delta 8(t) - Delta 8(t-1)` | Penultimate practical level in this record, requiring strong cross-level consistency. | 24 |
| Delta 10 | `Delta 9(t) - Delta 9(t-1)` | Current practical cap for the thirteen-week record and hypothesis generation. | 16 |
| Delta n | `Delta (n-1)(t) - Delta (n-1)(t-1)` | Extend only when the preceding Delta changes materially and sufficient evidence remains. | Depends on record length |

Delta 10 is used as the current practical cap rather than a universal maximum.
The working theory is that ten levels will usually be sufficient, while Delta
to the power n remains an active extension. A further level is considered when
the preceding Delta shows a material change and enough chronological evidence
remains for testing.

A higher-order Delta cannot mathematically occur before its preceding Delta,
because it is calculated from consecutive values of that preceding level. It
may nevertheless make a developing pattern more visible. Higher orders also
describe change at progressively deeper recursive levels and rapidly reduce
the available sample. Irregular variation already present may therefore become
more prominent in the remaining pattern. An apparent early signal must be
tested against shuffled chronology and future observations before it can be
described as predictive. Directional or vector prediction is a further
question and is not established by magnitude change alone.

One active PDHIS hypothesis is that genuine vector-directed change will show
coherent propagation across related Delta levels. Chaotic noise should be more
likely to generate unstable, non-persistent or directionally inconsistent
patterns. This distinction may help separate propagated functional change from
random fluctuation, but it must be evaluated prospectively through persistence,
directional agreement, permutation testing and performance on unseen events.

## Evidence boundary

Every finite-difference order removes one observation. With thirteen weeks,
Delta 10 can be calculated, but only two forward cases remain per function.
High-order results are therefore displayed for completeness and hypothesis
generation, not treated as validated predictive mechanisms.

## Reproduction

```bash
python Post_BBO_BBR/PDHIS/generate_pdhis_analysis.py
```

The script produces four CSV evidence tables and twenty numbered JPG
infographics with embedded captions.
