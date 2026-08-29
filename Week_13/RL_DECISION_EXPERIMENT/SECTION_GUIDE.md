# Week 13 RL-Informed Decision Experiment

## Purpose

This experiment runs the reinforcement-learning analysis used to prepare the official Week 13 inputs. It uses only the verified Week 1 to Week 12 history to choose an action type for each function. The Week 13 outputs are introduced only after action selection to evaluate the policy.

The state is the accumulated evidence for a function, including its current reward, historical best, recent reward change, repeatability and boundary position. The action is one of four supervised policies: retain a winner, make a local refinement, continue a boundary refinement or repeat a point to investigate uncertainty. The black-box output is the reward.

This is an executed RL-informed policy experiment. It does not claim that the small continuous dataset is sufficient to train a stable tabular Q-function.

## Run

From the repository root:

```bash
python Week_13/RL_DECISION_EXPERIMENT/run_rl_decision_experiment.py
```

## Outputs

- `outputs/rl_week13_policy_results.csv`: state, selected action and Week 13 validation outcome
- `outputs/rl_week13_policy_snapshot.png`: visual state-action-reward evidence
- `outputs/rl_week13_reward_snapshot.png`: Week 12 to Week 13 reward change

## Evidence boundary

The action selection uses data only through Week 12. Week 13 results are held out until the policy has selected an action. The experiment supports the decision process but does not prove that any observed coordinate is a global optimum.

