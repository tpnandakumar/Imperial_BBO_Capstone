# Week_02

## Objectives

- Refine query selection using Week 1 observations
- Balance exploration and exploitation
- Investigate promising regions of the search space
- Improve objective function performanc

# Week 2 Query Selection Methodology

## Introduction

The objective of Week 2 was to use the information obtained from Week 1 to select improved query points for each black-box function.

Unlike Week 1, where decisions were based on the initial observations supplied by Imperial, Week 2 decisions were based on the outputs generated from my own Week 1 submissions.

The aim was to balance exploration and exploitation.

* Exploitation involved remaining close to regions that had already demonstrated strong performance.
* Exploration involved moving to substantially different regions when previous results were weak or uninformative.

---

## Step 1: Review Week 1 Results

The Week 1 outputs were:

| Function | Week 1 Output |
| -------- | ------------: |
| F1       |      0.000000 |
| F2       |      0.454942 |
| F3       |     -0.101836 |
| F4       |     -4.359875 |
| F5       |   1415.876394 |
| F6       |     -0.700155 |
| F7       |      1.319994 |
| F8       |      9.580240 |

These outputs formed the evidence base for Week 2 decision making.

---

## Step 2: Rank Functions by Performance

The functions were ranked from highest output to lowest output.

```python
import pandas as pd

results = {
    "F1": 0.000000,
    "F2": 0.454942,
    "F3": -0.101836,
    "F4": -4.359875,
    "F5": 1415.876394,
    "F6": -0.700155,
    "F7": 1.319994,
    "F8": 9.580240
}

df = pd.DataFrame(
    results.items(),
    columns=["Function","Output"]
)

df = df.sort_values(
    "Output",
    ascending=False
)

df["Rank"] = range(1,9)

print(df)
```

This produced:

| Rank | Function |      Output |
| ---- | -------- | ----------: |
| 1    | F5       | 1415.876394 |
| 2    | F8       |    9.580240 |
| 3    | F7       |    1.319994 |
| 4    | F2       |    0.454942 |
| 5    | F1       |    0.000000 |
| 6    | F3       |   -0.101836 |
| 7    | F6       |   -0.700155 |
| 8    | F4       |   -4.359875 |

---

## Step 3: Classify Search Behaviour

A simple ranking-based classification was used.

```python
def classify(rank):

    if rank <= 2:
        return "Exploitation"

    elif rank <= 4:
        return "Mixed"

    else:
        return "Exploration"
```

Result:

| Function | Classification |
| -------- | -------------- |
| F5       | Exploitation   |
| F8       | Exploitation   |
| F7       | Mixed          |
| F2       | Mixed          |
| F1       | Exploration    |
| F3       | Exploration    |
| F6       | Exploration    |
| F4       | Exploration    |

---

## Step 4: Apply Exploration or Exploitation

### Exploitation

For the strongest performers, the next query remained close to the successful region.

The objective was to determine whether the surrounding neighbourhood produced even higher values.

Applied to:

* Function 5
* Function 8

### Mixed Strategy

For moderate performers, the next query remained near the successful region but moved sufficiently to gather additional information.

Applied to:

* Function 2
* Function 7

### Exploration

For weak performers, local refinement was unlikely to generate substantial improvement.

Therefore a larger movement was used to investigate a different region of the search space.

Applied to:

* Function 1
* Function 3
* Function 4
* Function 6

---

## Step 5: Select Week 2 Query Points

The final query points were selected manually using the exploration–exploitation framework.

### Function 5

Week 1:

```text
0.210000-0.870000-0.900000-0.900000
```

Week 2:

```text
0.180000-0.900000-0.950000-0.950000
```

Reason:

The strongest performer in Week 1. The query remained close to the successful region.

---

### Function 8

Week 1:

```text
0.060000-0.070000-0.030000-0.040000-0.410000-0.820000-0.500000-0.910000
```

Week 2:

```text
0.080000-0.080000-0.050000-0.050000-0.450000-0.850000-0.550000-0.950000
```

Reason:

Second strongest performer. Local refinement around a promising region.

---

### Function 7

Week 1:

```text
0.050000-0.500000-0.250000-0.220000-0.420000-0.740000
```

Week 2:

```text
0.080000-0.550000-0.300000-0.250000-0.450000-0.780000
```

Reason:

Positive output. Moderate movement while remaining near the successful region.

---

### Function 2

Week 1:

```text
0.720000-0.940000
```

Week 2:

```text
0.760000-0.900000
```

Reason:

Positive output. Small adjustment around the previous solution.

---

### Function 1

Week 1:

```text
0.740000-0.740000
```

Week 2:

```text
0.300000-0.300000
```

Reason:

The Week 1 output was effectively zero. A completely different region was explored.

---

### Function 3

Week 1:

```text
0.530000-0.640000-0.250000
```

Week 2:

```text
0.750000-0.250000-0.750000
```

Reason:

Negative output. Alternative region explored.

---

### Function 6

Week 1:

```text
0.750000-0.180000-0.700000-0.720000-0.040000
```

Week 2:

```text
0.250000-0.750000-0.300000-0.300000-0.800000
```

Reason:

Negative output. Broad exploration performed.

---

### Function 4

Week 1:

```text
0.600000-0.430000-0.420000-0.250000
```

Week 2:

```text
0.200000-0.800000-0.800000-0.800000
```

Reason:

Weakest performer. Largest exploratory movement.

---

## Mathematical Documentation

The movement from Week 1 to Week 2 can be expressed as:

```text
Week 2 Query = Week 1 Query + Movement Vector
```

where:

```text
Movement Vector = Week 2 Query − Week 1 Query
```

The size of the movement was quantified using Euclidean distance:

```python
distance = np.linalg.norm(
    week2_query - week1_query
)
```

Small distances represented exploitation.

Large distances represented exploration.

---

## Conclusion

Week 2 was not random.

The process consisted of:

1. Reviewing Week 1 outputs.
2. Ranking functions according to performance.
3. Classifying functions as exploitation, mixed or exploration.
4. Selecting new query points consistent with that classification.
5. Submitting the new query points to the BBO portal.

Strong performers were refined locally, while weak performers were moved to substantially different regions of the search space. This provided a structured exploration–exploitation strategy for the second optimisation round.

## Results

# The input

| Function   | Query                                                                     |
| ---------- | ------------------------------------------------------------------------- |
| Function 1 | `0.300000-0.300000`                                                       |
| Function 2 | `0.760000-0.900000`                                                       |
| Function 3 | `0.750000-0.250000-0.750000`                                              |
| Function 4 | `0.200000-0.800000-0.800000-0.800000`                                     |
| Function 5 | `0.180000-0.900000-0.950000-0.950000`                                     |
| Function 6 | `0.250000-0.750000-0.300000-0.300000-0.800000`                            |
| Function 7 | `0.080000-0.550000-0.300000-0.250000-0.450000-0.780000`                   |
| Function 8 | `0.080000-0.080000-0.050000-0.050000-0.450000-0.850000-0.550000-0.950000` |

and

# The Output

| Function   |        Output |
| ---------- | ------------: |
| Function 1 |    `0.000000` |
| Function 2 |    `0.412137` |
| Function 3 |   `-0.133256` |
| Function 4 |  `-23.120154` |
| Function 5 | `2308.148703` |
| Function 6 |   `-2.070246` |
| Function 7 |    `1.069658` |
| Function 8 |    `9.524100` |


## Strategy Summary

Week 2 focused on balancing exploration and exploitation. Query selection was informed by Week 1 observations while maintaining sufficient exploration to avoid premature convergence on local optima.

## Reflection

# Week 2 Reflection and Discussion with Figures & Analysis

Week 2 marked a transition from broad exploratory sampling towards a more evidence-driven optimisation strategy. During Week 1, the objective was to gather information about the behaviour of the eight black-box functions because no prior knowledge of the response surfaces was available. Once the Week 1 outputs became available, it became possible to identify which functions appeared promising and which regions were producing poor results.

Figure 1. Week 1 Function Outputs.
<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/9b1bbfe4-b35f-43da-b2b1-18e0d72f18bb" />


The Week 1 results showed substantial variation across the functions. Function 5 produced a markedly larger output than any other function, while Functions 7 and 8 also returned positive values. In contrast, Functions 3, 4 and 6 generated negative outputs, suggesting that the sampled regions were unlikely to be close to an optimum. These observations provided the first evidence base for decision making and shifted the optimisation process from purely exploratory sampling towards a more balanced exploration–exploitation framework.

# DIgure 2

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/195993df-cff4-4af7-9b01-bc3a3597ffc6" />
Figure 2. Week 2 Performance Summary showing outputs for all eight functions and highlighting high-performing and low-performing regions. Function 5 remained the strongest performer, while Functions 3, 4 and 6 continued to exhibit negative outputs.

My Week 2 strategy leaned slightly more towards exploitation, although exploration remained an important component. For Functions 5, 7 and 8, I selected query points close to the original locations because these functions produced the strongest outputs. By exploiting these regions, I aimed to refine the search around potentially high-performing areas and determine whether further improvement could be achieved through local refinement. Remaining close to successful regions reduced the risk of abandoning potentially valuable areas of the search space prematurely.

At the same time, exploration continued to play an important role. Functions 3, 4 and 6 generated negative outputs, indicating that the sampled locations were unlikely to represent high-performing regions. For these functions, I selected points in substantially different areas of the search space to gain additional information and reduce uncertainty. Function 1 produced an output that was effectively zero, providing little evidence that the original region was worth pursuing. Consequently, a larger exploratory movement was considered more appropriate than local refinement.

# Figure 3 – Exploration versus Exploitation Strategy
<img width="1632" height="963" alt="image" src="https://github.com/user-attachments/assets/e055353c-f059-4b06-93ad-23a12f200ec0" />

## Evidence-Based Query Selection

The Week 2 query points were selected according to the amount of evidence available from Week 1.
Functions producing strong positive outputs (F5 and F8) were treated as promising regions of the search space. These functions were assigned an exploitation strategy, where only small movements were made to investigate the local neighbourhood around successful points.
Functions producing moderate positive outputs (F2 and F7) were assigned a mixed strategy. Query points remained relatively close to previous locations while introducing moderate movement to gather additional information.
Functions producing weak, zero or negative outputs (F1, F3, F4 and F6) were assigned an exploration strategy. Larger movements were used because there was insufficient evidence that the previously sampled regions contained high-performing solutions.
This approach balanced performance improvement with information gathering and provided a structured framework for selecting Week 2 query points.

The central trade-off during Week 2 was between maximising short-term gains and reducing uncertainty. Excessive exploitation can cause an optimiser to become trapped in a local optimum, particularly when only limited information is available. Conversely, excessive exploration may waste evaluations in regions that have little potential for improvement. The challenge was therefore to balance both objectives. Strongly performing functions were refined cautiously, while weakly performing functions were explored more aggressively. This approach aimed to maximise learning while preserving opportunities for performance improvement.

The Week 1 outputs had the greatest influence on my decision-making process. They provided the first meaningful evidence regarding the behaviour of the functions and demonstrated the value of data-driven decision making. Rather than relying on intuition alone, the observed outputs enabled decisions to be grounded in measurable performance. The large variation between functions reinforced the importance of adapting the strategy according to available evidence rather than applying a uniform approach to all functions.

Class discussions also influenced my thinking. Topics relating to regression modelling, feature relationships and uncertainty highlighted the importance of interpreting available evidence carefully. These discussions encouraged a balanced approach that incorporated both exploration and exploitation rather than committing exclusively to one strategy. The concept of uncertainty reduction was particularly relevant because the optimiser had only a limited number of observations from which to infer the underlying behaviour of the functions.

From a modelling perspective, fitting a simple linear regression model at this stage would likely violate several assumptions. The most obvious issue is linearity. Black-box optimisation problems often involve complex response surfaces with peaks, valleys and interactions between variables. Such behaviour is unlikely to be represented adequately by a straight-line relationship. The extremely small sample size also limits the reliability of any fitted model. With only a small number of observations available, estimates would be highly uncertain and potentially unstable.

Similarly, while logistic regression could potentially be used if outputs were categorised into high-performing and low-performing regions, there is currently insufficient evidence to define meaningful decision boundaries. At this stage, the available observations are too sparse to determine whether such boundaries exist. Additional optimisation rounds will be required before reliable classification behaviour can be assessed.

# Insert Figure 4 – Dimensionality versus Output
<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/7fb66c4c-9225-447a-89c3-1bb982cc2b02" />

The dimensionality of each function also influenced the Week 2 decision-making process. Functions F1 and F2 contained only two dimensions, meaning that a single observation represented a relatively larger proportion of the search space. In contrast, Functions F7 and F8 contained six and eight dimensions respectively, creating substantially larger search spaces in which local information becomes increasingly sparse. As dimensionality increases, the volume of the search space grows rapidly and the probability of sampling near an optimum by chance decreases. Consequently, optimisation decisions for higher-dimensional functions require greater caution because individual observations provide less information about the overall landscape. This increases uncertainty and strengthens the need to balance exploration with exploitation. The positive outputs observed for Functions F7 and F8 suggested that potentially valuable regions had been identified despite their higher dimensionality. Therefore, these functions were refined cautiously rather than abandoned. In contrast, negative outputs from Functions F3, F4 and F6 provided little evidence that their current regions were promising, justifying more exploratory movements. These observations reinforced the importance of adapting optimisation behaviour according to both observed performance and problem dimensionality rather than applying the same strategy uniformly across all functions.

Although there was insufficient data to calculate feature importance formally, considering the potential influence of individual dimensions helped structure my decision-making process. Rather than selecting points randomly, I considered whether local refinement or broader exploration was more appropriate for each function. This encouraged a systematic and evidence-based approach to query selection. As more observations become available, feature-level analysis is expected to play an increasingly important role in guiding optimisation decisions.

Overall, Week 2 marked the transition from purely exploratory sampling towards evidence-driven optimisation. The Week 1 observations provided the first meaningful information about the behaviour of the eight black-box functions and allowed query selection to be guided by measured performance rather than intuition alone. Strong-performing functions such as F5, F7 and F8 were refined through local exploitation, while weaker-performing functions were assigned broader exploratory movements to reduce uncertainty and investigate alternative regions of the search space.The results demonstrate that optimisation decisions should adapt as new evidence becomes available. Rather than applying a uniform strategy across all functions, query selection was tailored according to both observed performance and problem dimensionality. This balanced approach improved the efficiency of the search process while maintaining sufficient exploration to avoid premature convergence on potentially suboptimal regions. Consequently, Week 2 established a more structured optimisation framework that will support future Bayesian optimisation decisions as additional observations become available.

## Contents

This folder contains:
- Query submissions
- Results
- Reflections
- Figures
- Analysis notes
