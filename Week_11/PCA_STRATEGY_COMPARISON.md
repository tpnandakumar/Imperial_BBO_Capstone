# PCA Strategy Comparison for the Week 12 Decision

## Purpose

Module 23 introduces principal component analysis as a way of retaining important variation while simplifying a high dimensional representation. For the BBO capstone, the useful question is not whether PCA should automatically replace the existing optimisation strategy. The question is whether the accumulated query history contains lower dimensional structure that improves the next decision.

This review uses the verified Weeks 1 to 11 query history already analysed in `week_11_analysis.py`. PCA is compared with the observed objective history and the stronger historical regions before the Week 12 query set is selected.

## What PCA shows

The recorded query trajectories for Functions 3 to 8 are concentrated in relatively few principal directions.

| Function | PC1 explained variance | PC1 plus PC2 | Components for at least 90 percent |
| --- | ---: | ---: | ---: |
| Function 3 | `0.9824765956583574` | `0.9966917983027923` | 1 |
| Function 4 | `0.929457542635097` | `0.9990069305772716` | 1 |
| Function 5 | `0.9676115302998125` | `0.997726663010752` | 1 |
| Function 6 | `0.864773785020967` | `0.9866734368322968` | 2 |
| Function 7 | `0.8602299516486513` | `0.9692454132352497` | 2 |
| Function 8 | `0.9021092653998608` | `0.9666706798190747` | 1 |

The concentration is useful, but it has an important limitation. These principal directions describe where the submitted queries moved. They do not, by themselves, identify directions that maximise the hidden objective. The queries were selected adaptively, so their variance partly reflects the strategy that generated them.

## Comparison with objective evidence

### Function 1

Function 1 is two dimensional and does not need PCA for dimensional reduction. The point `0.600000,0.600000` returned `0.025559285339829783` in both Week 3 and Week 11. The repeat is stronger evidence for the next decision than a variance based transformation.

**Decision:** retain the confirmed point.

### Function 2

Function 2 is also two dimensional. Week 11 produced a new verified best of `0.5848554940277205` at `0.695000,0.950000`. The local evidence is more directly relevant than PCA.

The strongest earlier result was `0.5712475315739602` at `0.700000,0.950000`. The improvement after reducing the first coordinate by `0.005000` while retaining the second coordinate supports one further small test in that direction.

**Decision:** local refinement takes priority over PCA.

### Function 3

PC1 explains `0.9824765956583574` of the recorded query variance, but the best verified result remains `-0.06037987403160633` at `0.850000,0.150000,0.850000`. Week 11 moved close to that point at `0.840000,0.160000,0.840000` and recovered to `-0.06542982421105416`.

The objective evidence therefore supports returning to the exact stronger historical point rather than extrapolating along PC1.

**Decision:** historical best recovery takes priority, with PCA retained as structural context.

### Function 4

PC1 explains `0.929457542635097` of the recorded query variance. Week 11 produced a large recovery after moving towards the earlier strong region, but the best verified result remains `-4.359874926582439` at `0.600000,0.430000,0.420000,0.250000`.

The recovery is consistent with the broad structural movement identified by PCA, but the objective history gives a more precise target.

**Decision:** use the verified historical best rather than extend the principal direction beyond observed evidence.

### Function 5

PC1 explains `0.9676115302998125` of the recorded query variance. This agrees with the visible one direction tightening of the Function 5 search path. The objective evidence is unusually consistent: the value rose from `1415.8763939603884` in Week 1 to `4411.0387356061765` in Week 11 as the search concentrated near the boundary.

Week 9 and Week 10 both returned `4394.868042481448` at `0.120000,0.997000,0.999800,0.999800`. Week 11 then improved to `4411.0387356061765` at `0.110000,0.998000,0.999900,0.999900`.

Here PCA and objective evidence point in the same broad direction. A further small boundary refinement is justified, but it should remain within the permitted range.

**Decision:** use a PCA consistent boundary refinement.

### Function 6

Function 6 needs two components to retain at least 90 percent of the recorded query variance. The best verified result remains `-0.648848297397347` at `0.700000,0.200000,0.700000,0.700000,0.200000`. Week 11 recovered to `-0.7268715077444687` after moving back towards that basin.

The PCA result confirms that the trajectory is not well represented by a single direction. The direct objective evidence is therefore more useful for the immediate decision.

**Decision:** return to the verified best point.

### Function 7

Function 7 also requires two components for at least 90 percent of the recorded query variance. Its best verified output is `1.3809299933612855` at `0.040000,0.480000,0.260000,0.220000,0.420000,0.740000`. Week 11 remained close to that region and returned `1.3579108517237013`.

Because the best observed point is already known and the PCA structure is two dimensional rather than a single clear direction, the stronger evidence is to revisit the verified best.

**Decision:** use the verified best point.

### Function 8

PC1 explains `0.9021092653998608` of the recorded query variance, but Function 8 gives stronger direct evidence. The exact Week 1 input `0.060000,0.070000,0.030000,0.040000,0.410000,0.820000,0.500000,0.910000` returned `9.58024` again when repeated in Week 11.

The repeated best point is more informative for immediate optimisation than extrapolation along the principal component.

**Decision:** retain the confirmed best point.

## Strategy comparison

| Function | PCA contribution | Stronger evidence for Week 12 | Selected approach |
| --- | --- | --- | --- |
| Function 1 | Not required for 2D reduction | Exact repeated best | Confirmed best |
| Function 2 | Not required for 2D reduction | New local best and directional improvement | Small local refinement |
| Function 3 | Strong one direction query concentration | Exact stronger historical point | Historical best recovery |
| Function 4 | Strong one direction query concentration | Exact stronger historical point | Historical best recovery |
| Function 5 | Strong one direction concentration agrees with objective trend | New boundary best after plateau | PCA consistent boundary refinement |
| Function 6 | Two component structure | Exact stronger historical point | Historical best recovery |
| Function 7 | Two component structure | Exact stronger historical point | Confirmed productive point |
| Function 8 | Strong one direction query concentration | Exact repeated best | Confirmed best |

## Candidate Week 12 query set

The comparison supports the following candidate set for the twelfth round:

```text
Function 1
0.600000-0.600000

Function 2
0.690000-0.950000

Function 3
0.850000-0.150000-0.850000

Function 4
0.600000-0.430000-0.420000-0.250000

Function 5
0.100000-0.999000-1.000000-1.000000

Function 6
0.700000-0.200000-0.700000-0.700000-0.200000

Function 7
0.040000-0.480000-0.260000-0.220000-0.420000-0.740000

Function 8
0.060000-0.070000-0.030000-0.040000-0.410000-0.820000-0.500000-0.910000
```

## Interpretation

PCA changes the analysis without forcing the same decision for every function. It is most useful for showing that the higher dimensional query histories are concentrated in one or two directions. The objective values then determine whether those directions deserve to influence the next query.

For Function 5, the structural and objective evidence agree, so the principal direction supports a further controlled boundary refinement. For Functions 3, 4, 6, 7 and 8, direct historical performance gives a stronger immediate target than extrapolating along a principal component. Functions 1 and 2 are already two dimensional, so direct geometry remains clearer.

This comparison therefore uses PCA as a tested analytical option rather than as an automatic replacement for the existing optimisation strategy.