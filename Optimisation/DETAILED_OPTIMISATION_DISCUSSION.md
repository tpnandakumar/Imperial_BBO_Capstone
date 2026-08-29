# Detailed Optimisation Discussion

## Purpose

This chapter explains how optimisation decisions were made across the thirteen-round Imperial BBO challenge and how the supporting parameters were examined. It separates methods used during the live challenge from retrospective modelling completed after the final submission. That distinction matters because a later result must not be used to make an earlier decision appear better informed than it was.

The challenge involved eight hidden functions with different dimensions, output scales and behaviour. Only one new query per function could be submitted in each round. The true equations, gradients and global optima were unavailable. Optimisation therefore meant choosing the next input from the evidence already observed, recording the returned output, and adapting the next decision to the behaviour of that function.

## Optimisation framework

The working model was a sequential decision framework rather than one fixed predictive equation. Five actions were available:

1. **Explore** a different region when the evidence was sparse or unconvincing.
2. **Refine** a promising region using a smaller coordinate movement.
3. **Recover** an earlier strong point after later movement reduced performance.
4. **Replicate** a coordinate when the stability of its returned output needed checking.
5. **Stop or retain** when further movement lacked support and the strongest observed result should be protected.

Each function was assessed separately. A numerical change that was small for one function could be substantial for another, and raw outputs were not compared across functions. The principal outcome test remained the value returned by the hidden function.

## Parameters examined

| Parameter or analytical choice | Values or alternatives considered | Selection evidence | Role in the project |
| --- | --- | --- | --- |
| Coordinate direction | Positive, negative, recovery or unchanged movement by coordinate | Earlier outputs, proximity to strong observations, recent direction and boundary position | Live decision parameter |
| Coordinate step size | Broad exploration followed by smaller local changes where improvement persisted | Chronological response, remaining query budget and distance from the current best | Live decision parameter |
| K-means cluster count | `k = 2` and `k = 3` for each function | Highest silhouette score, with inertia and neighbouring outputs used as supporting checks | Live exploratory evidence at Week 10 |
| K-means restart count | `n_init = 50` | Stable repeated initialisation within the bounded comparison | Live clustering setting |
| Principal components retained | One or two components where needed to describe at least 90 per cent of observed query variance | Explained variance, coordinate loadings and agreement with objective history | Live structural comparison before Week 12 |
| Polynomial surrogate degree | Degrees 1, 2 and 3 | Lowest expanding-window normalised root mean squared error | Retrospective model comparison |
| Ridge regularisation | Alpha from `0.000001` to `10` | Lowest chronological validation error within each function | Retrospective model comparison |
| F5 Matérn 2.5 length scale | Candidate settings assessed through weekly walk-forward validation | Lowest chronological validation error on the completed record | Post-capstone representative surrogate |
| F7 quadratic Ridge alpha | Candidate regularisation settings including `0.000001` | Lowest weekly walk-forward validation error | Post-capstone representative surrogate |

## Chronological development

### Early rounds: exploration and local comparison

The first rounds concentrated on learning how each function responded to coordinate movement. The dimensionality ranged from two to eight inputs, so an exhaustive search was not possible. Decisions were based on the direction and size of earlier changes, the location of the strongest observed points and whether nearby inputs produced similar behaviour.

Broad movement was retained where no productive region had emerged. Smaller steps were used where the recent sequence showed consistent improvement. This was particularly important for Function 5, where directional refinement continued to raise the output. The same rule was not imposed on functions whose results had plateaued or reversed.

### Middle rounds: refinement, recovery and replication

As the evidence accumulated, the optimisation shifted from general exploration towards function-specific decisions. Recovery became important when an exploratory move performed worse than an earlier point. Replication was used when the stability of an output needed confirmation.

This stage showed that movement itself is not evidence of progress. Functions 4 and 7 ultimately benefited from returning to earlier strong coordinates. Function 6 demonstrated why repeated-coordinate behaviour must be inspected rather than assumed. These observations shaped the later balance between improvement and protection of the retained best.

### Week 10: K-means comparison

K-means clustering was introduced as an exploratory view of the accumulated input locations. Candidate cluster counts were restricted to two and three because only ten live observations per function were available at that stage. Fifty restarts were used with a fixed random state to reduce dependence on one initial allocation.

The chosen cluster count was the candidate with the higher silhouette score. Inertia, nearest-neighbour distance, distance from the strongest point and neighbouring output behaviour were retained as supporting evidence. For example, the recorded comparison selected three clusters for Function 1 with a silhouette score of `0.586983`, two for Function 3 with `0.827687`, and two for Function 5 with `0.569486`. These partitions described the submitted query neighbourhoods. They did not prove that the hidden response surfaces contained the same number of natural clusters.

Function 5 provided the clearest practical clustering case. Its high-output observations concentrated near a boundary point, and the Week 9 input was repeated in Week 10 with the same returned value. This supported cautious exploitation. Other functions retained exploratory or recovery decisions when cluster membership was not supported by the objective history.

The complete live analysis is recorded in the [Week 10 clustering discussion](../Week_10/CLUSTERING_ANALYSIS.md), with all tested settings in the [clustering optimisation table](../BBO_Dashboard/hpo_results/week10_clustering_hpo_all_results.csv).

### Weeks 11 and 12: principal component comparison

Principal component analysis was used to describe how the submitted coordinates had moved. It was not treated as a direct model of the hidden objective. For Functions 3, 4, 5 and 8, the first principal component accounted for more than 90 per cent of the observed query variance through Week 11. Functions 6 and 7 required two components to retain at least 90 per cent.

The important decision was whether this structural pattern agreed with the returned outputs. For Function 5, the dominant movement direction and the improving objective values supported another controlled boundary refinement. For Functions 3, 4, 6, 7 and 8, an exact historical strong point gave a more defensible target than extrapolation along a principal component. Functions 1 and 2 were already two-dimensional, so direct geometry and objective history were clearer.

This comparison prevented principal component analysis from becoming an automatic rule. Explained variance described the path taken by the queries, while the hidden-function outputs determined whether that path was useful. The full values and function-level decisions are available in the [PCA strategy comparison](../Week_11/PCA_STRATEGY_COMPARISON.md) and [Week 12 PCA evidence record](../Week_12/PCA_EVIDENCE.md).

### Final rounds: controlled refinement and retention

The final decisions reflected the evidence boundary for each function. Function 5 continued to support refinement and rose from `1415.876394` in Week 1 to `4440.957217` in Week 13. Function 3 also improved in the final round. Function 2 reached its strongest participant-query result in Week 12, then declined after another small move in Week 13. This demonstrated that a small step is not automatically a safe step.

For Functions 1, 4, 7 and 8, retention or recovery protected strong earlier findings. Function 6 achieved its strongest observed participant-query output in Week 13, although its repeated-coordinate variation remained part of the interpretation. The final strategy was therefore mixed by design. Refinement, recovery, replication and stopping were selected according to the behaviour of each function.

## Retrospective surrogate optimisation

After the thirteen-round challenge, polynomial Ridge surrogates were compared using expanding-window validation. For each weekly prediction, the model used only the starter data and observations available before that week. Polynomial degrees 1 to 3 and Ridge alpha values from `0.000001` to `10` were compared using normalised root mean squared error.

This retrospective comparison tested how model complexity and regularisation behaved across the recorded chronology. It did not alter any earlier query. The complete settings and errors are preserved in the [surrogate optimisation results](../BBO_Dashboard/hpo_results/posthoc_surrogate_hpo_all_results.csv), and the calculation is implemented in the [hyperparameter optimisation code](../BBO_Dashboard/hpo_engine.py).

Two representative post-capstone equations were then retained for deeper study:

- **Function 5:** a Matérn 2.5 surrogate with standardised length scale `10.0` and diagonal noise `0.00000001`. Its weekly walk-forward mean absolute error was `49.918573`, equal to `0.011241` of the complete observed F5 output range.
- **Function 7:** a quadratic surrogate with 27 terms and Ridge alpha `0.000001`. Its weekly walk-forward mean absolute error was `0.066669`, equal to `0.048373` of the complete observed F7 output range.

These equations approximate the sampled input-output evidence. They are not the original hidden equations and should not be extrapolated beyond the observed domain without new validation. Their full specifications, scaling values, weights and coefficients are available in the [representative surrogate record](../Post_BBO_BBR/representative_surrogates/SECTION_GUIDE.md).

## What worked

The strongest optimisation lesson was that the action should follow the function rather than a universal search rule. Sustained refinement worked for Function 5 because both direction and returned output remained favourable. Recovery protected the strongest evidence for Functions 4 and 7. Replication supported retention for Functions 1 and 8 and exposed the need for caution in Function 6. Stopping became a positive optimisation choice when another move lacked support.

K-means and principal component analysis were useful when they were treated as decision aids. They helped organise neighbourhoods and movement patterns, but the hidden-function outputs retained priority. Chronological validation strengthened the later surrogate work because it avoided evaluating a model on information that would not have been available at the prediction point.

## What did not work consistently

No method produced improvement for every function. Small coordinate movements sometimes reduced performance. A compact cluster did not necessarily identify a high-output region. A dominant principal component described the sampled path but did not automatically identify an improving direction. Higher-degree polynomial models could fit more structure while remaining unstable under sparse chronological validation.

These findings are useful negative evidence. They explain why the final framework includes recovery, replication and stopping rather than treating continuous movement or increasing model complexity as progress.

## Limitations

The live query budget provided only thirteen participant-selected observations per function. The observations were adaptive, not independent or uniformly distributed. Dimensionality reached eight inputs, leaving large areas of the bounded domain unobserved. The hidden equations, gradients and true optima remained unknown. Function 6 also showed that repeated coordinates may return different values.

For these reasons, cluster structure, principal components and surrogate equations must be read within the sampled evidence. They support interpretation and disciplined query selection, but they do not prove global geometry or global optimality. The representative surrogates were refitted to the complete evidence after chronological comparison, so they describe the recorded domain rather than providing independent prospective validation.

## Conclusion

The optimisation process developed from broad exploration into a controlled, function-specific framework. Its strength lies in the evidence trail: every live decision can be traced to information available at that time, and later modelling is clearly labelled as retrospective. The final results support a practical combination of exploration, refinement, recovery, replication and stopping. Clustering, principal component analysis and surrogate validation add technical depth while preserving the central principle that returned objective values decide whether an optimisation step succeeded.

## Reproducibility and evidence

- [Hyperparameter optimisation code](../BBO_Dashboard/hpo_engine.py)
- [Complete Week 10 clustering settings](../BBO_Dashboard/hpo_results/week10_clustering_hpo_all_results.csv)
- [Complete retrospective surrogate settings](../BBO_Dashboard/hpo_results/posthoc_surrogate_hpo_all_results.csv)
- [Week 10 clustering analysis](../Week_10/CLUSTERING_ANALYSIS.md)
- [PCA strategy comparison](../Week_11/PCA_STRATEGY_COMPARISON.md)
- [Week 12 PCA evidence](../Week_12/PCA_EVIDENCE.md)
- [F5 Matérn 2.5 and F7 quadratic surrogate details](../Post_BBO_BBR/representative_surrogates/SECTION_GUIDE.md)
- [Final model card](../Module_25_Final_BBO_Submission/25_3_GitHub_Final_Submission/FINAL_CAPSTONE_MODEL_CARD.md)

