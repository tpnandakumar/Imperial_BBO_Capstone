# Imperial BBO Method and Experiment Register

This register controls what appears in the dashboard code laboratory. A method is marked **Verified and linked** only when its week, code or reflection and role can be traced in the official repository. Methods remembered as completed but not yet traceable are retained as **Performed but source path unresolved** rather than assigned to an invented week.

## Confirmed evolution

1. Weeks 1 to 9: exploration, exploitation, refinement and recovery.
2. Week 10: KMeans hyperparameter comparison and clustering interpretation.
3. Week 11: PCA comparison after the Week 11 outputs.
4. Week 12: PCA update and final sequential decision development.
5. Weeks 12 to 13: RL, MAB, MDP and Q-learning interpretation.

## Week 10 HPO record

The confirmed Week 10 HPO tested `k=2` and `k=3` for every function. KMeans used `n_init=50` and `random_state=42`. Silhouette score selected the exploratory partition. This was a decision aid applied to ten weekly observations per function, not proof that the hidden function contained exactly two or three natural clusters.

## Evidence still to recover

The following experiments must be mapped from their original reflection, code and saved output before the dashboard presents them as completed weekly evidence:

- Linear regression
- Logistic regression
- Polynomial regression
- Kernel methods
- Support vector regression
- Gaussian process modelling
- Decision trees
- Random forest
- Bootstrap validation
- CNN

For each, the required evidence is the week introduced, exact code path, data available at the time, parameter search, saved output, interpretation and influence on the following query.
