# Week 10 Clustering Analysis

## Purpose

Week 10 introduced an explicit clustering perspective to the accumulated optimisation evidence. The purpose was not to claim that ten observations recover the hidden response surfaces. Instead, clustering was used as an exploratory decision aid to identify recurring neighbourhoods, compact high performing regions, weak regions, possible outliers and areas where further exploration remained necessary.

Only observations available by the end of Week 10 are used. Week 11 outputs are excluded. The Week 11 query vectors are recorded only as the subsequent decisions informed by the Week 10 evidence.

## Analytical principle

Each hidden function is analysed independently because the eight functions have different dimensionalities and output scales. Input coordinates are already bounded on [0,1], so Euclidean distance in input space provides a transparent measure of neighbourhood proximity within each function. Output values are interpreted within function, not compared across functions as though they shared a common scale.

The analysis considers four related signals:

1. proximity of query vectors in input space;
2. recurrence of strong or weak outputs within nearby observations;
3. concentration or dispersion of later queries as the search develops;
4. whether an apparently strong observation is supported by neighbouring evidence or remains isolated.

K means is treated as exploratory rather than definitive. Candidate cluster counts are restricted by the very small sample size, and silhouette scores are reported only when mathematically valid. Nearest neighbour distances and output ranks are retained alongside any K means assignment so that interpretation does not depend on a single algorithm.

## Week 10 interpretation

| Function | Week 10 evidence | Clustering interpretation | Decision consequence |
| --- | --- | --- | --- |
| Function 1 | Output remained effectively zero after movement | No convincing productive cluster | Continue broader exploration |
| Function 2 | Improved to 0.5311818841205426 | Emerging productive neighbourhood | Confirm and refine locally |
| Function 3 | Improved to -0.08697581687486715 | More favourable local grouping, still uncertain | Continue targeted refinement |
| Function 4 | Declined to -13.483642655031158 | Week 10 neighbourhood not supported | Change direction and reassess |
| Function 5 | Repeated 4394.868042481448 at the same boundary point | Strongest evidence of a stable high performing neighbourhood | Precise exploitation and boundary refinement |
| Function 6 | Declined to -1.2283806967341901 | Current local direction weakened | Reassess neighbourhood |
| Function 7 | Remained positive at 1.285160161342515 with a small decline | Productive but relatively flat neighbourhood | Conservative local refinement |
| Function 8 | Remained high at 9.4646525 with a small decline | Compact, stable positive neighbourhood | Cautious boundary testing |

## Function 5 as the clearest case

Function 5 provides the strongest clustering evidence at Week 10. The search had progressively concentrated near a high performing boundary region. Week 10 deliberately repeated the Week 09 point `0.120000,0.997000,0.999800,0.999800` and reproduced the output `4394.868042481448` exactly. This repeat does not prove a global optimum, but it strengthens the interpretation that the tested neighbourhood is stable and worth refining.

## Negative evidence and boundaries

Clustering was also used to interpret poor results. A weak observation is not automatically noise. If neighbouring queries repeatedly perform poorly, they help define a low performing region. Conversely, an isolated strong result is not automatically treated as a cluster centre. Repeated behaviour among nearby observations receives more weight than a single exceptional point.

This distinction is important for Functions 3, 4 and 6. Their negative outputs are not grouped merely because they share a sign. Input location, proximity and repeated behaviour are considered together.

## Data driven figures

Three figures were specified from the exact Weeks 1 to 10 history:

1. `week_10_clustering_figure_1_cluster_separation.png` reports exploratory K means separation by function using the best silhouette score from candidate partitions with k equal to 2 or 3.
2. `week_10_clustering_figure_2_function5_cluster.png` plots Function 5 output against normalised Euclidean distance from the Week 10 query. Bubble size increases with output, making the tightening high value neighbourhood visible directly.
3. `week_10_clustering_figure_3_decision_evidence.png` links Week 10 cluster evidence to the Week 11 query decision for all eight functions. Distances are normalised by the square root of dimensionality and Week 11 outputs are excluded.

The source values used to construct these figures are exported to `week_10_clustering_figure_source.csv`. The figure generator is stored as `generate_week_10_clustering_figures.py`, so the visual evidence can be regenerated directly from the repository record.

## Link to the Week 11 submission

The Week 10 clustering interpretation informed the next query set by changing both direction and step size. Supported neighbourhoods were refined, apparently flat regions were tested cautiously at their boundaries, and unresolved functions retained greater exploratory movement. This creates an auditable chain:

`Weeks 1 to 10 observations -> neighbourhood and cluster analysis -> interpretation -> exploration/refinement decision -> Week 11 query`

The Week 11 query is therefore a downstream decision record, not additional evidence used to construct the Week 10 clusters.

## Reproducibility

Run:

```bash
python Week_10/week_10_clustering_analysis.py
python Week_10/generate_week_10_clustering_figures.py
```

The analysis script calculates pairwise and nearest neighbour distances, performs conservative exploratory K means where the data permit, evaluates candidate partitions with silhouette score and exports a cluster evidence table. The figure generator uses the exact Weeks 1 to 10 input and output history and creates the three clustering visualisations plus their source table.

Expected analytical outputs:

- `Week_10/week_10_cluster_summary.csv`
- `Week_10/week_10_clustering_figure_source.csv`
- `Week_10/week_10_clustering_figure_1_cluster_separation.png`
- `Week_10/week_10_clustering_figure_2_function5_cluster.png`
- `Week_10/week_10_clustering_figure_3_decision_evidence.png`

## Limitations

Ten observations per function remain sparse, especially in four to eight dimensions. Adaptive sampling also means the observations are not independent or uniformly distributed. Apparent clusters may reflect the optimisation policy as well as the hidden function. K means assumes approximately compact groups and should not be interpreted as proof of natural cluster structure. For these reasons, clustering is used here as exploratory evidence for query selection, not as a claim that the global geometry or global optimum has been established.
