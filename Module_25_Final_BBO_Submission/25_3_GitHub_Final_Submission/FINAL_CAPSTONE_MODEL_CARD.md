# Final Capstone Model Card

## Model description

### Purpose

The capstone system is a human-supervised sequential optimisation workflow for eight independent hidden objective functions. It selects one query vector per function from the evidence available at each round, records the portal output, and updates the next decision without access to the hidden equations or gradients.

### Input

The workflow uses:

- course-supplied starter coordinates and objective values;
- verified weekly query vectors and returned outputs;
- the known input dimension and `[0,1]` coordinate bounds;
- recent improvement, deterioration and distance moved;
- stronger historical coordinates and repeated measurements;
- boundary behaviour, clustering summaries and PCA trajectory evidence; and
- function-specific exploration, refinement, recovery, repeat and stopping considerations.

### Output

The prospective output is one valid coordinate vector for each of F1 to F8. The analytical outputs include best-observed coordinates, chronological comparisons, repeatability findings, action classifications, figures and an evidence record explaining why each query was selected.

### Model architecture

This is not one fitted predictive model. It is a decision architecture with four layers:

1. **Evidence layer:** preserves the 175 starter observations and 104 portal evaluations.
2. **Analytical layer:** calculates within-function rankings, movement, repeated coordinates, clustering, PCA and chronological surrogate diagnostics.
3. **Policy layer:** selects among exploration, local refinement, controlled exploitation, recovery, repetition and stopping.
4. **Human review layer:** checks feasibility, provenance, uncertainty and whether the proposed action is justified before portal submission.

No single optimisation rule was imposed on all functions. K-means clustering used Week 10 evidence to inform Week 11 by comparing `k=2` and `k=3`, with `n_init=50`, `random_state=42` and silhouette-score selection. PCA described coordinated movement. Polynomial Ridge and Gaussian-process comparisons were evaluated chronologically. The Week 13 policy experiment used only Weeks 1 to 12 to select action types before the final outputs were revealed.

## Performance

Performance is measured within each function because the eight objectives use different numerical scales. The primary metric is the strongest objective value produced by the 13 participant-selected queries. Supporting measures include comparison with the starter-data maximum, whether the best query value was reproduced, whether Week 13 improved on Week 12, movement from the previous query and chronological surrogate error where a surrogate was evaluated.

| Function | Best participant-query output | Best query week or weeks | Final assessment |
| --- | ---: | --- | --- |
| F1 | `0.025559285339829783` | 3, 11, 12, 13 | Winner reproduced repeatedly |
| F2 | `0.7335252043269003` | 12 | Week 13 local step deteriorated |
| F3 | `-0.05685061601567621` | 13 | New final-round best |
| F4 | `-4.359874926582439` | 1, 12, 13 | Historical winner recovered and reproduced |
| F5 | `4440.957216598753` | 13 | New final-round best after boundary refinement |
| F6 | `-0.6071562248604215` | 13 | New best, but repeated-coordinate variability remained |
| F7 | `1.3809299933612855` | 5, 12, 13 | Historical winner recovered and reproduced |
| F8 | `9.58024` | 1, 11, 12, 13 | Winner reproduced repeatedly |

Within the participant-query record, Round 13 produced new best values for F3, F5 and F6. Four established query winners were retained. F2 provided a useful negative result because a further local movement reduced performance. F5 showed the strongest sustained improvement, rising from `1415.8763939603884` in Week 1 to `4440.957216598753` in Week 13. The course-supplied starter maxima remained stronger for F3, F4 and F8, which is shown explicitly in the final notebook.

The final figures can be regenerated with `python Week_13/generate_week_13_figures.py`. The numerical summary is stored in [`Week_13/week_13_analysis_summary.csv`](../../Week_13/week_13_analysis_summary.csv).

## Limitations

- Only 13 prospective queries were available per function.
- Sampling was adaptive rather than random or space-filling.
- Coverage became increasingly local, especially in higher dimensions.
- The equations, gradients, true optima and noise mechanisms remained hidden.
- A best observed coordinate is not proof of a global optimum.
- F2, F3 and F6 returned different outputs at identical recorded coordinates. F6 showed the largest range. The available data cannot distinguish stochasticity, an unobserved process, rounding beyond the recorded precision or evaluator inconsistency.
- Clustering and PCA describe the sampled trajectory, not the hidden objective surface.
- Surrogate validation is restricted to the observed chronology and cannot validate behaviour in unsampled regions.
- The workflow was developed for this synthetic challenge and has not been externally validated for clinical or operational deployment.

## Trade-offs

### Exploration versus exploitation

Exploration could locate a new productive region but consumed one of only 13 queries. Exploitation could improve a credible local trend but risked missing a stronger region or continuing beyond a turning point. The balance shifted from broader early searches towards function-specific refinement, recovery, repeat or stopping as evidence accumulated.

### Immediate score versus information

A query that failed to set a record could still reject a hypothesis. F2's final decline, F4's weak exploratory region and F6's repeated-coordinate variability all informed later interpretation. The workflow therefore valued information as well as immediate reward.

### Model complexity versus interpretability

Surrogates, clustering and PCA organised sparse evidence, but complex models could create false confidence. Direct objective history and reproducible coordinates were preferred when they provided a clearer decision.

### Retention versus continued search

Repeating or retaining F1, F4, F7 and F8 protected established results and tested reproducibility, but reduced opportunities to explore. Continued search was reserved for F2, F3, F5 and F6 where improvement or useful information remained plausible.

## Intended use and safeguards

The model card supports interpretation and reproduction of the official thirteen-round capstone. It does not authorise autonomous query submission or transfer to clinical practice. All portal submissions were human-reviewed. Exact inputs and outputs remain separate from inferred surfaces, and post-capstone Black Box Resolution work is labelled separately so that it cannot be mistaken for evidence available during the challenge.
