# Stage 2: Required Capstone Component 25.1

## Retrospective on the BBO Capstone Project: Section B

### 1. Initial codebase and repository

The 13-week BBO challenge began with course-supplied starter data for eight unknown functions. For each function, `initial_inputs.npy` contained coordinates already evaluated and `initial_outputs.npy` contained the corresponding results. The number of starter observations increased with dimensionality, from 10 points for each two-dimensional function to 40 points for the eight-dimensional function. These data were the common starting evidence. The hidden equations, gradients and locations of the optima were not disclosed.

I built the starting codebase from scratch specifically for this challenge. It was not copied from a public optimisation repository or taken from my previous work. I chose this approach because I needed a transparent structure that could preserve the exact history of eight functions with different dimensions while allowing the method to change as evidence accumulated. The course guidance recommended Bayesian optimisation and explained how NumPy could be used to load and append data, but the weekly analysis, comparison scripts, candidate selection, figures and decision records were developed during my project. Established Python libraries were used where appropriate rather than rewriting standard numerical methods.

The weekly cycle was simple but demanding. I analysed all input-output pairs available for each function, selected one new coordinate per function and entered the eight numerical strings into the BBO portal. Once processed, the portal returned the submitted inputs and their black-box outputs. I appended those eight observations to the accumulated evidence, examined improvement and deterioration, then calculated the following week's inputs. This continued until the Week 13 outputs were received. The repository therefore records an adaptive sequence of 104 authorised queries, not a set of results generated retrospectively.

The public record is available in the [Imperial BBO Capstone repository](https://github.com/tpnandakumar/Imperial_BBO_Capstone). It preserves unsuccessful trials as well as successful ones because both affected later decisions.

### 2. How the approach changed across the 13 weeks

My initial approach was deliberately cautious. In Week 1, I identified the strongest supplied observation for each function and made a manually supervised local adjustment. This produced the first outputs from coordinates I had selected myself. Thereafter, the search became function-specific rather than applying one optimiser or step size to all eight functions.

| Week | Development of the approach |
| --- | --- |
| 1 | Loaded the supplied arrays, identified each best starter observation and submitted nearby local probes. |
| 2 | Used the first returned outputs to separate promising functions from those needing wider exploration. F5 became the clearest exploitation target. |
| 3 | Compared direction as well as value. F5 improved again, F1 produced its first visible positive result and declines in F2, F7 and F8 warned against mechanical continuation. |
| 4 | Used different movement sizes by function. F2, F3 and F8 recovered, while F4 deteriorated, demonstrating that simple momentum was unreliable. |
| 5 | Continued controlled exploitation of F5 and found a strong F7 point, while poor results elsewhere justified changing direction. |
| 6 | Pushed several coordinates aggressively towards boundaries. F5 improved, but deterioration in other functions showed the cost of overextending a weak trend. |
| 7 | Retained the productive F5 direction and moderated movements elsewhere. F5 reached another new best. |
| 8 | Shifted from broad movement to more structured local probing around historically stronger regions. F5 improved to `4359.384134322703`. |
| 9 | Tightened the search and formalised reproducible summaries, figure data and validation checks. F5 improved again to `4394.868042481448`. |
| 10 | Used clustering to examine recurring local regions, productive basins and failed basins. Hyperparameter checks, including repeated initialisations, tested whether the structural interpretation was stable. |
| 11 | Used PCA to examine variance, correlated coordinate movement and redundancy in the higher-dimensional search paths. The objective outputs remained the primary decision evidence. F1, F4, F5, F6 and F8 improved relative to Week 10. |
| 12 | Combined the full history, movement size, previous best status and PCA evidence. F2, F3 and F5 achieved new bests, while F1, F4, F7 and F8 reproduced earlier winners. |
| 13 | Used a predominantly exploitative final portfolio: retain confirmed winners, make small local changes for F2 and F3, continue the evidenced F5 boundary direction and repeat F6 to investigate variability. |

The codebase developed alongside this reasoning. Early scripts mainly loaded, ranked and compared observations. Later folders added authoritative input and result CSV files, automated validation of dimensions and bounds, exact change calculations, clustering and PCA analyses, reproducible figure generation, model cards, datasheets and decision records. This progression made the project more auditable without rewriting early decisions as if later methods had already been available.

The most significant change was abandoning a common search rule in favour of a separate strategy for each function. That decision allowed sustained exploitation of F5, recovery of strong earlier coordinates for F4, F7 and F8, and cautious late refinement of F2 and F3. The later validation pipeline also had an important effect on decision quality because it prevented rounded, reconstructed or dimensionally invalid values from entering the final comparisons.

### 3. Final results and performance trajectory

The final outcome was mixed in an informative way. Week 13 produced new overall best outputs for F3, F5 and F6. F1, F4, F7 and F8 retained established best values. F2's strongest result remained its Week 12 output because the final local movement reduced performance.

| Function | Strongest verified output | Best week or weeks | Final interpretation |
| --- | ---: | --- | --- |
| F1 | `0.025559285339829783` | 3, 11, 12, 13 | Winner repeatedly confirmed |
| F2 | `0.7335252043269003` | 12 | Week 13 crossed away from the stronger local point |
| F3 | `-0.05685061601567621` | 13 | Final local adjustment produced a new best |
| F4 | `-4.359874926582439` | 1, 12, 13 | Early winner recovered and retained |
| F5 | `4440.957216598753` | 13 | Sustained boundary refinement produced a new best |
| F6 | `-0.6071562248604215` | 13 | New best, with response variability at an identical coordinate |
| F7 | `1.3809299933612855` | 5, 12, 13 | Earlier winner recovered and confirmed |
| F8 | `9.58024` | 1, 11, 12, 13 | Early winner repeatedly confirmed |

F5 showed the clearest optimisation trajectory, rising from `1415.8763939603884` in Week 1 to `4440.957216598753` in Week 13, a gain of `3025.0808226383646`. Its improvement was not produced by a single large jump. It emerged through repeated, controlled movement as the first coordinate decreased and the remaining coordinates approached the upper boundary.

The other functions show why final score alone is insufficient. F4 and F8 were strongest early, became worse during exploration and were later recovered. F2 peaked in Week 12 at `0.690000,0.950000`; moving the first coordinate by only `0.005000` reduced the Week 13 output by `0.0921821158135095`. F6 returned three different outputs from the identical coordinate in Weeks 3, 12 and 13. This established response variability but did not reveal whether its cause was stochasticity, hidden state or evaluator behaviour.

These are the best verified observations within the authorised query budget. They do not prove that the global mathematical optima were found.

### 4. Trade-offs and decision quality

The central trade-off was exploration against exploitation. Early exploration was necessary because the supplied observations were sparse, particularly in the higher-dimensional spaces. However, every exploratory query used one of only 13 opportunities per function. Exploitation protected productive evidence but risked becoming trapped around a local maximum.

I eventually used four practical actions: explore, refine, recover and retain. F5 justified progressive refinement because repeated movement produced repeated gains. F4 required recovery after broad exploration moved far below its Week 1 result. F1, F7 and F8 eventually justified retention because their winning coordinates could be reproduced. F2 demonstrated that even a very small exploitative step can overshoot a narrow productive region.

Clustering was useful for describing recurring neighbourhoods, but sparse adaptively sampled data can create unstable or misleading groups. PCA helped identify concentrated movement and coordinate relationships, but high explained variance in the submitted path did not imply that the same direction increased the hidden objective. I therefore treated both methods as decision support, not as substitutes for returned outputs.

The final round had a different risk profile because there was no later competition query available to repair a poor experiment. This justified freezing F1, F4, F7 and F8, cautiously refining F2 and F3, extending the supported F5 direction and repeating F6. The Week 13 results confirmed that this portfolio approach was preferable to one universal rule, even though the F2 move did not succeed.

Before selecting the Week 13 inputs, I carried out substantial reinforcement learning analysis of the 12-week history. Each candidate coordinate was treated as an action, its expected or previously observed output as a reward and the accumulated function history as the decision state. Multi-armed bandit reasoning helped determine where the final query should explore, exploit or preserve a known winner. The MDP view made the process explicitly sequential because each returned output altered the state of knowledge and therefore the value of the next action. Q-learning concepts supported reward updating and comparison of candidate actions, while the small continuous dataset made a stable tabular Q-function inappropriate. The resulting hybrid policy materially informed the official Week 13 choices: retain established winners for F1, F4, F7 and F8; make controlled local moves for F2 and F3; continue the rewarded boundary direction for F5; and repeat F6 to investigate unresolved reward variability. This was applied RL-informed decision analysis, although it was not presented as a fully trained autonomous Q-learning agent.

![Week 13 RL-informed decision experiment](../../Week_13/RL_DECISION_EXPERIMENT/outputs/rl_week13_policy_snapshot.png)

*Figure 1. Executed state-action-reward experiment using the verified Week 1 to Week 12 history, followed by the returned Week 13 outcomes.*

### 5. Learning, surprises and future application

The greatest change in my thinking was moving from searching for one superior algorithm to managing eight different evidence problems. Dimensionality mattered, but observed behaviour mattered more. Some functions rewarded boundary movement, some had narrow local regions, some required recovery and one showed non-identical outputs at the same coordinate.

If starting again, I would establish the reproducible data pipeline, validation rules and experiment register in Week 1. I would separate performance queries from repeatability queries, calculate movement and uncertainty consistently, and predefine function-specific stopping rules. I would also use Bayesian surrogate models and acquisition functions more systematically from the beginning, while comparing them with transparent baselines and retaining human review where evidence was sparse.

The capstone has direct relevance to clinical neurology service development. Optimising a referral pathway, urgent-recall threshold or investigation policy also involves limited observations, unequal consequences and uncertain responses. The lesson is not to transfer a numerical winner blindly. It is to preserve provenance, test changes sequentially, distinguish improvement from random variation, protect high-risk cases and stop only when the evidence supports stopping. The final project therefore taught me to favour certainty over belief while remaining explicit about what the available data cannot establish.

What surprised me most was that identical coordinates did not always produce identical outputs. F6 returned three different values at the same point, whereas repeated winning coordinates for F1, F4, F7 and F8 reproduced their results exactly. I was also surprised that the most advanced-looking method was not automatically the most useful. Clustering, PCA and Gaussian process reasoning added structure, but the strongest decisions still came from combining those methods with the complete observed history and careful human judgement.
