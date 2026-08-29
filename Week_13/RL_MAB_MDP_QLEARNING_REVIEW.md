# RL, MAB, MDP and Q Learning Review

## Context

Module 24 introduced reinforcement learning, multi armed bandits, Markov decision processes and Q learning immediately before the final capstone stage. I applied these methods to the verified Week 1 to Week 12 history when selecting the Week 13 action for each function. The analysis was decision influencing, although the small continuous dataset did not justify claiming that a stable tabular Q function had been trained.

## Multi armed bandit view

The strongest connection is the exploration and exploitation problem. Each new query consumes a limited opportunity and returns a reward. As the final round approached, the value of broad exploration fell because there was no later query available to recover from a poor result.

This helps explain why repeated best points were reasonable for Functions 1, 4, 7 and 8, while Functions 3 and 5 still justified small moves because their recent evidence remained directional.

## MDP view

An MDP interpretation is useful if the state is defined as the accumulated knowledge about a function: historical best values, recent direction, boundary behaviour, repeatability and uncertainty. The action is the next submitted coordinate and the reward is the returned objective value.

The hidden function itself is not observed as a changing state. What changes after each query is the evidence available for the next decision.

## Q learning view

A literal tabular Q learning approach is poorly matched to this dataset. The coordinate space is continuous, the number of observations is small and most exact state action combinations are visited only once. Discretisation is possible, but it would introduce arbitrary bins and could discard the fine local structure that mattered in Functions 2, 3 and 5.

The useful contribution of Q learning was reward based action comparison and preference updating. This was combined with function specific evidence to select retention for Functions 1, 4, 7 and 8, local refinement for Functions 2 and 3, boundary refinement for Function 5 and repetition for uncertainty for Function 6.

## Executed experiment

The [Week 13 RL-Informed Decision Experiment](RL_DECISION_EXPERIMENT/SECTION_GUIDE.md) runs the final policy using only the committed Week 1 to Week 12 history. It records the state features, selected action and reason for all eight functions. The returned Week 13 outputs are then added to assess what followed each selected action.

## Final conclusion

The Module 24 methods materially informed the final strategy, especially the exploration and exploitation trade off. They did not replace the direct numerical evidence. The final decisions combined reward based reasoning with function specific history, PCA where informative, repeatability testing and local performance trends.

