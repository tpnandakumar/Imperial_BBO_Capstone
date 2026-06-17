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

The Week 1 results revealed substantial heterogeneity across the eight black-box functions, indicating that the sampled regions differed considerably in their underlying response characteristics. Function 5 produced an output that was substantially larger than all other functions, providing the first evidence that a potentially high-performing region of the search space had been identified. Functions 7 and 8 also returned positive outputs, suggesting that further local investigation may be worthwhile. In contrast, Functions 3, 4 and 6 generated negative outputs, indicating that the sampled locations were unlikely to represent favourable regions of the search space. These observations provided the first empirical evidence regarding function behaviour and reduced uncertainty sufficiently to support more informed query selection. Consequently, Week 1 marked the transition from purely exploratory sampling towards an evidence-driven exploration-exploitation strategy that could adapt according to observed performance.

# Figure 2

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/195993df-cff4-4af7-9b01-bc3a3597ffc6" />

Figure 2. Week 2 Performance Summary showing outputs for all eight functions and highlighting evidence of both successful exploitation and continued exploration. Function 5 remained the strongest performer, confirming the value of refining previously successful regions, while Functions 3, 4 and 6 continued to exhibit negative outputs, indicating that broader exploration remained necessary to reduce uncertainty and identify alternative high-performing regions.

## Interpretation of Week 2 Results and Implications for Query Selection

The Week 2 outputs provided important evidence about the behaviour of the eight black-box functions. Function 5 remained the dominant performer, producing an output of 2308.149. This was substantially higher than all other functions and suggested that the sampled region contained a highly rewarding region of the search space. As a result, Function 5 became the strongest candidate for continued exploitation.

Function 8 also remained important because it produced a stable positive output of 9.524. Although this was much smaller than Function 5, it provided evidence that the previously identified region was still productive. This supported further cautious local refinement rather than abandoning the region.

Function 4 produced the weakest Week 2 result, deteriorating to -23.120. This suggested that the sampled region was unlikely to contain a favourable local optimum. Therefore, Function 4 required broader exploration in the next optimisation round rather than continued local refinement.

Functions 3 and 6 also produced negative outputs, indicating that their current regions remained weak. In contrast, Functions 2 and 7 produced positive but modest outputs, suggesting that they should be monitored using a mixed strategy rather than treated as either clear exploitation or full exploration candidates. The variation in outputs across the eight functions also highlighted the heterogeneous nature of the optimisation problem. Different regions of the search space appeared to exhibit substantially different response behaviours, suggesting that a single optimisation strategy would be unlikely to perform well across all functions. Instead, query selection needed to be adapted according to observed performance. Strongly performing functions could justify local refinement, whereas poorly performing functions required broader exploration to gather additional information and reduce uncertainty. This reinforced the importance of evidence-driven decision making rather than applying a uniform search strategy.

My Week 2 strategy leaned slightly more towards exploitation, although exploration remained an important component. For Functions 5, 7 and 8, I selected query points close to the original locations because these functions produced the strongest outputs. By exploiting these regions, I aimed to refine the search around potentially high-performing areas and determine whether further improvement could be achieved through local refinement. Remaining close to successful regions reduced the risk of abandoning potentially valuable areas of the search space prematurely.

At the same time, exploration continued to play an important role. Functions 3, 4 and 6 generated negative outputs, indicating that the sampled locations were unlikely to represent high-performing regions. For these functions, I selected points in substantially different areas of the search space to gain additional information and reduce uncertainty. Function 1 produced an output that was effectively zero, providing little evidence that the original region was worth pursuing. Consequently, a larger exploratory movement was considered more appropriate than local refinement. This exploratory behaviour was important because poor outputs are still informative within a black-box optimisation setting. Identifying regions that are unlikely to contain high-performing solutions helps reduce uncertainty and narrows the search space available for future iterations. Consequently, exploration was not viewed as a failure to find good solutions, but as a mechanism for improving understanding of the underlying objective functions. This information is expected to improve the efficiency of subsequent query selection and support more informed optimisation decisions as additional evidence becomes available.

# Figure 3 – Exploration versus Exploitation Strategy
<img width="1632" height="963" alt="image" src="https://github.com/user-attachments/assets/e055353c-f059-4b06-93ad-23a12f200ec0" />

Figure 3 summarises the decision framework used to select Week 2 query points. Rather than applying a uniform search strategy across all functions, query selection was adapted according to the evidence generated during Week 1. Functions demonstrating strong performance were assigned to exploitation-focused refinement, while functions producing weak or negative outputs were assigned to broader exploratory movements. This approach sought to balance performance improvement with uncertainty reduction, ensuring that promising regions were investigated further without neglecting potentially valuable areas elsewhere in the search space.

## Evidence-Based Query Selection

The Week 2 query points were selected according to the amount of evidence available from Week 1.
Functions producing strong positive outputs (F5 and F8) were treated as promising regions of the search space. These functions were assigned an exploitation strategy, where only small movements were made to investigate the local neighbourhood around successful points.
Functions producing moderate positive outputs (F2 and F7) were assigned a mixed strategy. Query points remained relatively close to previous locations while introducing moderate movement to gather additional information.
Functions producing weak, zero or negative outputs (F1, F3, F4 and F6) were assigned an exploration strategy. Larger movements were used because there was insufficient evidence that the previously sampled regions contained high-performing solutions.
This approach balanced performance improvement with information gathering and provided a structured framework for selecting Week 2 query points.

The allocation of functions to exploitation, mixed and exploration categories was based on the strength of evidence available rather than the magnitude of output alone. Function 5 provided the strongest evidence of a potentially high-performing region and therefore justified local refinement. Functions 2 and 7 produced positive but less decisive results, making a balanced strategy more appropriate. In contrast, Functions 1, 3, 4 and 6 provided limited evidence that their sampled regions contained favourable solutions, increasing the value of exploratory sampling. This evidence-based allocation reduced the likelihood of overcommitting resources to uncertain regions while maintaining opportunities to discover superior solutions elsewhere in the search space.

The central trade-off during Week 2 was between maximising immediate performance gains and reducing uncertainty about the search space. Exploitation focused on refining regions that had already demonstrated strong performance, increasing the probability of achieving improved objective values. However, excessive exploitation risks premature convergence to a local optimum because only a small portion of the search landscape has been explored. Conversely, exploration sacrifices short-term performance in order to gather information about previously untested regions. Although exploratory queries may produce weaker outputs, they reduce uncertainty and improve understanding of the underlying response surface. This information can become highly valuable in later optimisation rounds.

The Week 2 strategy therefore balanced both objectives. Strong-performing functions such as F5 and F8 were refined through cautious local exploitation, while weaker-performing functions such as F3, F4 and F6 were assigned broader exploratory movements to reduce uncertainty and investigate alternative regions of the search space. This adaptive approach sought to maximise both learning and performance improvement while reducing the risk of overlooking superior regions elsewhere in the search space.

More broadly, the strategy reflected a key principle of Bayesian optimisation: decisions should be guided by the information available at the time rather than by a fixed search rule. As additional observations become available, confidence in the underlying response surface increases and query selection can become progressively more targeted. Consequently, the Week 2 approach represented an intermediate stage between initial exploration and more informed optimisation, where both information gain and objective improvement remained important considerations. 

The Week 1 outputs represented the first empirical observations of the underlying objective functions and therefore formed the evidence base for all Week 2 decisions. Prior to receiving these outputs, there was little justification for favouring one region of the search space over another. Once performance differences became visible, query selection could be guided by measured outcomes rather than intuition alone. The substantial variation between functions demonstrated that different regions of the search space exhibited markedly different behaviours. Consequently, applying the same optimisation strategy to every function would have been inefficient. Instead, query selection was adapted according to observed performance, allowing stronger functions to be exploited while weaker functions were explored more aggressively..

Class discussions also influenced my thinking. Topics relating to regression modelling, feature relationships and uncertainty highlighted the importance of interpreting available evidence carefully. These discussions encouraged a balanced approach that incorporated both exploration and exploitation rather than committing exclusively to one strategy. The concept of uncertainty reduction was particularly relevant because the optimiser had only a limited number of observations from which to infer the underlying behaviour of the functions.

From a modelling perspective, fitting a simple linear regression model at this stage would be inappropriate for several reasons. Linear regression assumes that the relationship between inputs and outputs can be approximated by a linear function. However, black-box optimisation problems frequently exhibit highly non-linear response surfaces containing local optima, sharp gradients and complex interactions between variables. Such behaviour cannot be adequately represented by a simple straight-line model. Furthermore, the available dataset consisted of only a small number of observations for each function, resulting in a very low sample-to-dimension ratio, particularly for the higher-dimensional functions. Under these conditions, parameter estimates would be highly unstable and predictions would be associated with substantial uncertainty. Consequently, linear regression would provide limited insight into the true structure of the search space at this stage of the optimisation process.

Similarly, logistic regression would require the outputs to be converted into discrete categories such as high-performing and low-performing regions. At this stage, there was insufficient evidence to define reliable classification boundaries because only a small number of observations had been collected. Any threshold used to separate good and poor regions would therefore be largely arbitrary and vulnerable to sampling noise. In addition, the optimisation objective is inherently continuous rather than categorical, meaning that converting outputs into classes would discard potentially valuable information regarding relative performance. Additional optimisation rounds and a larger evidence base would be required before classification-based approaches could be meaningfully evaluated.

# Insert Figure 4 – Dimensionality versus Output
<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/7fb66c4c-9225-447a-89c3-1bb982cc2b02" />

The dimensionality of each function also influenced the Week 2 decision-making process. Functions F1 and F2 contained only two dimensions, meaning that a single observation represented a relatively larger proportion of the search space. In contrast, Functions F7 and F8 contained six and eight dimensions respectively, creating substantially larger search spaces in which local information becomes increasingly sparse. As dimensionality increases, the volume of the search space grows rapidly and the probability of sampling near a high-performing region by chance decreases. This phenomenon is commonly referred to as the "curse of dimensionality", where the amount of information provided by each observation becomes increasingly small relative to the size of the search space. Consequently, optimisation decisions for higher-dimensional functions require greater caution because individual observations provide less information about the overall landscape. This increases uncertainty and strengthens the need to balance exploration with exploitation. The positive outputs observed for Functions F7 and F8 suggested that potentially valuable regions had been identified despite the increased search complexity associated with higher dimensionality. Therefore, these functions were refined cautiously rather than abandoned. In contrast, negative outputs from Functions F3, F4 and F6 provided little evidence that their current regions were promising, justifying more exploratory movements. These observations reinforced the importance of adapting optimisation behaviour according to both observed performance and problem dimensionality rather than applying the same strategy uniformly across all functions.

Although the available data were insufficient to quantify the effect of dimensionality formally, Figure 4 highlights an important optimisation challenge. As dimensionality increases, observations become increasingly sparse relative to the size of the search space. Consequently, each function evaluation provides less information about the underlying response surface, making uncertainty estimation more important. This observation reinforced the value of Bayesian optimisation principles, where query selection seeks to balance information gain and performance improvement. Rather than searching the entire space uniformly, Bayesian optimisation concentrates evaluations in regions that are expected to provide either the greatest improvement in objective value or the greatest reduction in uncertainty. As additional observations become available, dimensionality-aware analysis and uncertainty modelling are expected to play a greater role in guiding future optimisation decisions.

Overall, Week 2 marked a clear transition from exploratory sampling towards evidence-driven optimisation. The Week 1 observations provided the first meaningful information about the behaviour of the eight black-box functions and enabled query selection to be guided by measured performance rather than intuition alone. Strong-performing functions such as F5, F7 and F8 were refined through cautious local exploitation, while weaker-performing functions were assigned broader exploratory movements to reduce uncertainty and investigate alternative regions of the search space. The results demonstrate that optimisation decisions should adapt as new evidence becomes available. Rather than applying a uniform strategy across all functions, query selection was tailored according to both observed performance and problem dimensionality. This adaptive approach improved the efficiency of the search process while maintaining sufficient exploration to reduce the risk of premature convergence on local optima. These observations are consistent with the broader objective of Bayesian optimisation, which seeks to maximise information gain while minimising the number of expensive function evaluations required to understand the search landscape.

## Contents

This folder contains:
- Query submissions
- Results
- Reflections
- Figures
- Analysis notes
