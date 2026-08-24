# RL, MAB, MDP and Q Learning Review

## Context

Module 24 introduced reinforcement learning, multi armed bandits, Markov decision processes and Q learning immediately before the final capstone stage. These methods provide useful ways to examine sequential decisions, but the BBO data do not justify claiming that a literal reinforcement learning agent generated the final coordinates.

## Multi armed bandit view

The strongest connection is the exploration and exploitation problem. Each new query consumes a limited opportunity and returns a reward. As the final round approached, the value of broad exploration fell because there was no later query available to recover from a poor result.

This helps explain why repeated best points were reasonable for Functions 1, 4, 7 and 8, while Functions 3 and 5 still justified small moves because their recent evidence remained directional.

## MDP view

An MDP interpretation is useful if the state is defined as the accumulated knowledge about a function: historical best values, recent direction, boundary behaviour, repeatability and uncertainty. The action is the next submitted coordinate and the reward is the returned objective value.

The hidden function itself is not observed as a changing state. What changes after each query is the evidence available for the next decision.

## Q learning view

A literal tabular Q learning approach is poorly matched to this dataset. The coordinate space is continuous, the number of observations is small and most exact state action combinations are visited only once. Discretisation is possible, but it would introduce arbitrary bins and could discard the fine local structure that mattered in Functions 2, 3 and 5.

The useful contribution of Q learning is therefore conceptual: compare actions by the reward they produced and update the preference for future actions. The capstone already follows this logic through repeated evidence based revision, but without claiming a stable learned Q function.

## Final conclusion

The Module 24 methods strengthen the interpretation of the final strategy, especially the exploration and exploitation trade off. They do not replace the direct numerical evidence. The strongest final decisions came from combining reward based reasoning with function specific history, PCA where informative, repeatability testing and local performance trends.
