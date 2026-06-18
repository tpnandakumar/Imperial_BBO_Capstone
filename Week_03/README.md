# Week 3

## Introduction
The Week 3 optimisation round built upon the evidence gathered during Weeks 1 and 2. Earlier observations had identified substantial differences in performance across the eight black-box functions, allowing query selection to become increasingly informed by measured outputs rather than purely exploratory sampling. Functions demonstrating strong performance in previous rounds were investigated through local refinement, while weaker-performing functions were assigned exploratory query points to reduce uncertainty and improve understanding of the search space.

The primary objective of Week 3 was to evaluate whether previously identified high-performing regions continued to produce favourable outputs while simultaneously assessing whether alternative regions could yield improvements for functions that had performed poorly. This required balancing exploitation of promising areas against exploration of less understood regions. As additional observations became available, optimisation decisions could increasingly be guided by evidence rather than intuition, reflecting the core principles of Bayesian optimisation.

The Week 3 results provided further insight into the behaviour of the underlying objective functions. Several functions showed meaningful changes in performance relative to previous rounds, highlighting both the benefits of local refinement and the value of exploratory sampling. These observations contributed to a more detailed understanding of the search landscape and supported increasingly informed query selection decisions for future optimisation rounds.

## Figure 1 – Week 3 Results

<img width="1536" height="1024" alt="figure 1" src="https://github.com/user-attachments/assets/68f4b369-92d2-4aab-b853-7601d29a3d11" />

Figure 1 summarises the progression of function outputs across the first three optimisation rounds and highlights how observed performance influenced future query selection. The results demonstrate that the functions exhibit markedly different behaviours, reinforcing the need for an adaptive optimisation strategy rather than a uniform search approach.

Function 5 remained the dominant performer throughout all three weeks. Its output increased from 1415.876 in Week 1 to 2308.149 in Week 2 and further to 2840.990 in Week 3. This consistent improvement suggests that the optimisation process successfully identified a highly rewarding region of the search space. The continued gains observed following local refinement provide strong evidence that exploitation was appropriate for this function and that further investigation of neighbouring regions may continue to yield improvements.

Function 4 produced the largest change in output magnitude across the optimisation process. Although the function remained negative, performance improved substantially from -23.120 in Week 2 to -14.554 in Week 3. This large response to a relatively small query adjustment suggests that the surrounding search landscape may contain regions of rapid variation. Consequently, Function 4 became an important candidate for further exploration because nearby evaluations may reveal significant improvements.

Functions 2, 7 and 8 demonstrated declining trends across successive optimisation rounds. Function 8 remained strongly positive despite a gradual reduction in output, indicating that the previously identified region may still contain useful information but could be approaching a local optimum. Functions 2 and 7 also declined, suggesting that the search direction selected during previous rounds may require adjustment. These observations highlight the importance of monitoring performance trajectories rather than relying solely on absolute output values.

Functions 1, 3 and 6 provided additional evidence regarding the structure of the search space. Function 1 remained close to zero across all rounds, suggesting limited evidence of a highly rewarding region near the sampled locations. Functions 3 and 6 remained negative but showed relatively small changes compared with Functions 4 and 5, indicating that further exploration may be required before reliable conclusions can be drawn regarding their underlying response surfaces.

Overall, the Week 3 results demonstrate the value of combining exploitation and exploration within a Bayesian optimisation framework. Strongly performing functions such as Function 5 benefited from continued local refinement, while Functions 4 and 6 provided evidence that potentially informative regions may still exist outside previously sampled areas. The observed variation across functions reinforces the importance of adapting query selection according to empirical evidence rather than applying a single optimisation strategy uniformly across the entire search space.

## Figure 2 – Comparison of Week 2 and Week 3 Performance

<img width="1536" height="1024" alt="fig 2" src="https://github.com/user-attachments/assets/79e791a4-e425-4ee1-8d19-6b885534db71" />

Figure 2 focuses on Function 5, the strongest-performing function across all optimisation rounds. The trajectory demonstrates a consistent increase in output from Week 1 to Week 3, providing strong evidence that the optimisation process successfully identified and refined a highly rewarding region of the search space.

The output increased from 1415.876 in Week 1 to 2308.149 in Week 2, representing an improvement of approximately 63.0%. A further increase to 2840.990 was achieved in Week 3, corresponding to an additional gain of 532.841 and confirming that the direction selected during Week 2 remained beneficial. Across the three optimisation rounds, the total improvement exceeded 1425 output units, representing an overall gain of approximately 100.7%.

An important observation is that improvement occurred without any reversal in performance. Each successive query generated a higher output than the previous evaluation. This behaviour suggests that the sampled region contains a relatively smooth local improvement pathway rather than a highly unstable landscape. Consequently, local exploitation was justified because neighbouring evaluations consistently produced superior objective values.

The accompanying input trajectory also provides useful insight. Between Weeks 1 and 3, the first parameter decreased slightly while the remaining three parameters increased progressively. Although the available observations are insufficient to determine formal feature importance, the consistency of the resulting output improvements suggests that this general search direction is associated with increasingly favourable outcomes. Additional evaluations would be required before attributing improvement to any individual variable.

From a Bayesian optimisation perspective, Function 5 provides evidence that exploitation can be highly effective once a promising region has been identified. Rather than allocating resources uniformly across the search space, optimisation effort was concentrated around a region that had already demonstrated strong performance. The resulting improvements validate the Week 2 decision to continue local refinement rather than abandoning the region in favour of broader exploration.

Overall, Figure 2 demonstrates a successful exploitation pathway. The absence of performance deterioration, combined with substantial cumulative improvement, suggests that Function 5 remains the strongest candidate for continued refinement in future optimisation rounds. These results illustrate how evidence-driven query selection can efficiently identify and develop high-performing regions within an unknown black-box search space.


## Figure 3 – Query Selection Strategy

<img width="1536" height="1024" alt="fig 3" src="https://github.com/user-attachments/assets/5721f4ad-26d9-4029-a8af-71ad431098b4" />

Figure 3 presents a decision matrix developed using the Week 3 outputs and observed performance trends across the optimisation process. The matrix combines output quality with confidence derived from trend stability, allowing functions to be grouped according to their suitability for exploitation, monitoring or further exploration.

Function 8 occupied the high-confidence exploitation region. Although its output was substantially lower than Function 5, it remained consistently positive across all optimisation rounds and demonstrated relatively stable behaviour. This suggests that the sampled region contains a reliable source of positive performance and may justify continued local refinement. Function 5 also occupied an exploitation-oriented region because it produced the highest output by a considerable margin. However, its lower confidence score reflected the possibility that the steep improvements observed across successive rounds could indicate a rapidly changing response surface. Consequently, continued exploitation remains appropriate, but careful monitoring is required to detect any future performance plateau.

Functions 2 and 7 were classified within the monitor or mixed-strategy region. Both functions continued to produce positive outputs but exhibited declining performance trends. These results suggest that the current search direction may no longer be optimal. Rather than committing fully to exploitation or abandoning the regions entirely, a balanced strategy involving moderate exploratory movement appears more appropriate. This would allow additional information to be gathered while retaining the possibility of recovering performance.

Functions 1, 3, 4 and 6 were positioned within the exploration region. Their outputs remained weak or negative, providing limited evidence that the currently sampled locations were close to high-performing regions. Function 4 was particularly noteworthy because it demonstrated substantial output variation despite remaining negative overall. This behaviour suggests that neighbouring regions may contain important structural information about the search landscape and therefore warrant further investigation. The remaining functions provided insufficient evidence to justify local refinement and would benefit more from broader exploratory movements.

The decision matrix illustrates an important principle of Bayesian optimisation: query selection should be influenced not only by current performance but also by the confidence associated with that performance. High outputs alone do not necessarily justify exploitation if uncertainty remains substantial, while low outputs may still provide valuable information if they reveal regions of rapid change. By considering both output quality and trend stability, the matrix provides a structured framework for allocating future evaluations efficiently.

Overall, Figure 3 demonstrates how empirical observations can be translated into practical optimisation decisions. The matrix indicates that Functions 5 and 8 are the strongest candidates for continued refinement, Functions 2 and 7 require strategic monitoring, and Functions 1, 3, 4 and 6 warrant additional exploration. By allocating future evaluations according to both performance and confidence, optimisation resources can be directed towards regions most likely to improve objective values while continuing to reduce uncertainty within the search space. This balanced allocation of resources reflects the central objective of Bayesian optimisation: maximising information gain while efficiently identifying high-performing solutions.


## Figure 4 – Learning from Exploration and Exploitation

<img width="1536" height="1024" alt="figure 4" src="https://github.com/user-attachments/assets/f4a026ab-0501-455e-9ae4-9984dd3461e0" />

## Figure 4 – Learning from Exploration and Exploitation

<img width="1536" height="1024" alt="fig 4" src="PASTE_IMAGE_LINK_HERE" />

Figure 4 summarises the complete query selection workflow used throughout the Black-Box Optimisation challenge. The process evolved from broad exploratory sampling in Week 1 towards increasingly informed and targeted optimisation decisions in subsequent weeks. Each round of observations reduced uncertainty about the search space and provided additional evidence to guide future query selection.

The Week 1 queries focused primarily on exploration because no information was available regarding the behaviour of the eight objective functions. A combination of designed and broadly distributed query points was used to obtain initial coverage of the search space. The resulting outputs provided the first empirical evidence regarding function behaviour and identified potentially promising regions for further investigation.

Week 2 represented a transition towards a mixed exploration–exploitation strategy. Functions demonstrating strong performance, particularly Functions 5, 7 and 8, became candidates for local refinement, while weaker-performing functions were assigned broader exploratory movements. This balanced approach enabled performance improvement while continuing to reduce uncertainty regarding poorly understood regions of the search space.

By Week 3, sufficient evidence had accumulated to support more targeted refinement. Function 5 demonstrated consistent improvement across all three optimisation rounds, providing strong evidence that a high-performing region had been identified. At the same time, Functions 3, 4 and 6 continued to provide valuable information regarding less favourable regions and highlighted areas where further exploration remained necessary. These observations demonstrated that both successful and unsuccessful evaluations contribute useful information within a Bayesian optimisation framework.

An important lesson from the challenge was that optimisation is fundamentally a sequential learning process. Early exploratory evaluations may produce weak objective values, but they reduce uncertainty and improve understanding of the search landscape. As additional observations become available, confidence in promising regions increases and query selection can become progressively more targeted. Consequently, exploration and exploitation should not be viewed as competing objectives but as complementary mechanisms that jointly improve optimisation performance.

The workflow also highlights the importance of balancing risk and reward. Excessive exploitation risks premature convergence to a local optimum before the wider search space has been sufficiently explored. Conversely, excessive exploration may delay identification of high-performing solutions. The iterative process illustrated in Figure 4 seeks to balance these competing objectives by continuously adapting query selection according to the evidence available at each stage.

Overall, Figure 4 demonstrates how Bayesian optimisation combines exploration, exploitation and iterative learning to improve decision quality over time. The challenge showed that effective optimisation depends not only on identifying strong-performing regions but also on systematically reducing uncertainty across the search space. This evidence-driven process provides a practical framework for solving complex optimisation problems when objective functions are expensive to evaluate and their underlying structure is unknown.

## Reflection on Week 4 Query Selection Strategy


The first three rounds of the Black-Box Optimisation (BBO) challenge transformed the problem from a largely exploratory exercise into a progressively evidence-driven optimisation process. During Week 1, very little was known about the behaviour of the eight unknown functions, requiring broad exploration across the search space. As additional observations accumulated during Weeks 2 and 3, emerging performance patterns enabled more informed query selection. Rather than viewing the task purely as optimisation, it became increasingly useful to interpret the search process as a combination of optimisation, classification, and information acquisition. The objective was no longer simply to locate high-performing query points, but to understand the underlying structure of the search landscape sufficiently well to guide future evaluations efficiently.

# Figure 4 – Query Selection Workflow

<img width="1536" height="1024" alt="figure 4" src="https://github.com/user-attachments/assets/7289ac8b-5d9e-4f84-aeed-6cc1a31ac11b" />

# Functional Ranking Evolution

As evidence accumulated across successive iterations, the relative ranking of the functions became increasingly stable. Function 5 consistently remained the strongest-performing function, while Function 8 maintained a stable second position throughout the optimisation process. In contrast, Function 4 consistently produced the weakest outputs despite displaying substantial variability between iterations. The stability of the rankings suggests that the optimisation process was gradually revealing meaningful structure within the search space rather than producing random fluctuations. This increasing consistency improved confidence that future query allocation could be guided by observed performance trends.

# Figure 14 – Function Ranking Evolution Across Weeks 1–3

<img width="1536" height="1024" alt="Fig 15" src="https://github.com/user-attachments/assets/3201612e-d1bf-49b6-af33-da5d9fbb1942" />

# Functional Output Progression

Analysis of output trajectories provided additional evidence regarding the behaviour of individual functions. Function 5 demonstrated the strongest and most consistent improvement, increasing from approximately 1416 in Week 1 to 2841 in Week 3. Functions 2, 7 and 8 remained positive but showed declining performance across successive iterations. Functions 1, 3, 4 and 6 remained weak or negative, suggesting that the currently sampled regions were unlikely to contain high-performing optima. These trends helped identify which functions should be prioritised for exploitation and which required further exploration.

# Figure 1 – Function Output Progression (Weeks 1–3)

<img width="1536" height="1024" alt="figure 1" src="https://github.com/user-attachments/assets/ad00b0a9-da86-4a5f-9eb7-e497a16f4c93" />

# Identifying Exploitation and Boundary Regions

Several functions exhibited behaviour that revealed important characteristics of the search landscape. Function 5 demonstrated a clear and consistent upward trajectory, suggesting that successive query modifications were moving closer to a high-performing region. By contrast, Function 4 exhibited substantial output fluctuations despite relatively modest changes in the query location. Such behaviour resembles a boundary or transition region, where small movements in the input space generate large output changes. Boundary regions are particularly valuable because they often provide the greatest information gain regarding the shape of the underlying response surface. Function 8 demonstrated a third optimisation pattern, remaining highly stable across all iterations and suggesting the possibility of a local plateau or convergence region.

# Figure 13 – Three Distinct Optimisation Behaviours Observed

<img width="1536" height="1024" alt="fig 14" src="https://github.com/user-attachments/assets/f38c13e6-3e9c-4ea0-9993-c7ef03b2b2e6" />

# Function 5 and Influential Variables

Function 5 provided the strongest evidence regarding influential variables. Across three iterations, performance improved from approximately 1416 to 2308 and then to 2841. Examination of the corresponding query points suggested that decreasing the first variable while increasing the remaining variables consistently improved performance. Although the underlying function remains unknown, the consistency of this trend suggests that these dimensions exert substantial influence on the objective value. Consequently, Function 5 represented the strongest candidate for continued exploitation during Week 4.

# Figure 2 – Function 5 Improvement Trajectory

# Decision Matrix and Resource Allocation

To formalise query selection, functions were grouped according to both output quality and confidence derived from observed trend stability. High-output functions with stable trends were considered suitable candidates for exploitation, while low-output functions with unstable behaviour were prioritised for exploration. Functions displaying moderate performance but relatively stable behaviour were assigned to a monitoring category. This framework ensured that query allocation was influenced not only by observed outputs but also by the confidence associated with those outputs. Such balancing of performance and uncertainty is a central principle of Bayesian optimisation.

# Figure 3 – Week 3 Decision Matrix

<img width="1536" height="1024" alt="fig 3" src="https://github.com/user-attachments/assets/3de62987-0e17-4222-a601-10ce02ab26b3" />

# Surrogate Modelling and Neural Network Considerations

Throughout the optimisation process, I considered the potential use of surrogate models to approximate the unknown functions. A neural network surrogate was not trained because the available dataset remained relatively small compared with the dimensionality of several functions. Under these circumstances, highly flexible models are vulnerable to overfitting and may produce unreliable gradient estimates. Nevertheless, surrogate modelling remains conceptually important because it provides a mechanism for estimating local response behaviour and identifying promising search directions. If additional observations were available, neural network surrogates could potentially be used to estimate gradients through backpropagation and guide future query refinement.

# Neural Network Hyperparameter Figure 3

<img width="1274" height="1536" alt="3" src="https://github.com/user-attachments/assets/62c4081c-d312-4307-afe3-b20f5ab3f80f" />


# Optimisation as a Classification Problem

The optimisation problem can also be interpreted as a classification task. Rather than predicting exact output values, the objective becomes distinguishing between favourable and unfavourable regions of the search space. Logistic regression could provide simple linear decision boundaries, while Support Vector Machines (SVMs) can capture more complex non-linear separations. In this context, support vectors become particularly important because they identify regions near decision boundaries where uncertainty is highest. Sampling near these boundaries can provide substantial information gain and improve understanding of the search landscape.

# Figure 18 – SVM Classification Boundaries for Functions 3 and 7

<img width="1535" height="1025" alt="Figure 18" src="https://github.com/user-attachments/assets/7cb09c49-bfa3-463a-8270-bba134d4a6bf" />

# Model Complexity versus Interpretability

Among the candidate modelling approaches, SVMs or simple surrogate models currently represent the most appropriate compromise between predictive flexibility and interpretability. Logistic regression may be overly restrictive because the observed function behaviours appear highly non-linear, whereas neural networks would likely require substantially more observations before reliable training becomes possible. At this stage of the optimisation process, interpretability remains important because understanding why a region appears promising is often as valuable as accurately predicting future outputs. This creates a practical trade-off between model complexity and transparency.

# Figure 5 – Model Complexity versus Interpretability Trade-Off

<img width="1536" height="1024" alt="fig 5" src="https://github.com/user-attachments/assets/82b0fdd4-86dd-4d83-b3ef-8d5696d44fb9" />


# Information Gain and Exploration Strategy

An important lesson from Week 3 was that high outputs alone should not determine future query allocation. Regions exhibiting high uncertainty or rapid output variation may provide greater information gain than regions with already stable performance. Function 4 illustrates this principle particularly well. Although its outputs remained negative, the large fluctuations observed across iterations suggest that neighbouring regions may contain valuable information regarding the underlying response surface. Consequently, exploration decisions should be driven not only by expected performance improvement but also by the expected information gained from additional evaluations.

# Figure 15 – Information Gain Map

<img width="1536" height="1024" alt="fig 16" src="https://github.com/user-attachments/assets/00a0e6a1-1710-4756-9d13-07f6a24e786c" />

# Final Week 4 Query Selection

The final Week 4 strategy combined evidence from output trajectories, classification boundaries, uncertainty estimates, information gain considerations and optimisation behaviour. Function 5 was selected for continued exploitation because it demonstrated strong and consistent improvement. Function 4 was prioritised for exploration because of its high uncertainty and potential information gain. Function 8 was monitored with minimal query allocation because its behaviour suggested a stable plateau region. Functions 2 and 7 were assigned a balanced monitoring strategy, while Functions 1, 3 and 6 continued to receive exploratory attention. This allocation sought to maximise both performance improvement and learning efficiency.

# Figure 16 – Week 4 Query Selection Decision Tree

<img width="1024" height="1536" alt="fig17" src="https://github.com/user-attachments/assets/79481f11-9cc0-4684-bea7-7996965b89b3" />


## Computational Analysis and Coding Implementation

The optimisation workflow was supported by computational analysis performed in Python. Weekly function outputs were organised into structured data tables, enabling systematic comparison of performance across optimisation rounds. Quantitative measures including output differences, percentage change, function rankings and trend direction were calculated to support evidence-based query selection. These calculations provided an objective framework for identifying candidate regions for exploitation, monitoring stable functions and prioritising exploratory evaluations in uncertain regions of the search space.

The calculations presented in this report are fully reproducible using the accompanying Python script `week3_analysis.py`. The script calculates output changes, percentage improvements, function rankings and Week 4 strategy allocations directly from the observed optimisation results.

### Script Output

Running `week3_analysis.py` produces:

- Function rankings based on Week 3 outputs
- Week-to-week output changes
- Percentage improvements
- Week 4 strategy recommendations
- Exportable CSV summary table

### Output Change Calculation
Observed output changes were calculated directly from the optimisation results. For Function 5, the output increased from 2308.15 in Week 2 to 2840.99 in Week 3.

**Output Change**
Δy = 2840.99 − 2308.15

Δy = 532.84

**Percentage Improvement**
%Δ = ((2840.99 − 2308.15) / 2308.15) × 100

%Δ = 23.09%

This substantial improvement supported the decision to continue exploiting the Function 5 search region during Week 4 query selection.

### Function Ranking Calculation

Functions were ranked according to observed output values after each optimisation round. At Week 3, Function 5 produced the highest output (2840.99), followed by Function 8 (9.44), while Functions 4 and 6 remained negative. These rankings were used to guide resource allocation between exploitation, monitoring and exploration activities.

### Python Implementation

All calculations were implemented in Python using the pandas library. The accompanying script `week3_analysis.py` stores optimisation outputs, calculates week-to-week changes, computes percentage improvements, ranks functions according to observed performance and assigns Week 4 query strategies based on the evidence collected during Weeks 1–3. The script also exports the processed results to a CSV file, allowing the analysis to be reproduced and independently verified.

```python
df["Change_W2_to_W3"] = df["Week3"] - df["Week2"]

df["Percent_Change_W2_to_W3"] = (
    df["Change_W2_to_W3"] / df["Week2"].abs()
) * 100

df["Week3_Rank"] = df["Week3"].rank(
    ascending=False,
    method="min"
)
```
### Computational Contribution to Query Selection

The computational analysis transformed raw optimisation outputs into interpretable performance metrics. By combining output changes, percentage improvements, ranking information and observed trend stability, the analysis provided objective support for the Week 4 exploitation, exploration and monitoring decisions. This reduced reliance on subjective judgement and ensured that query allocation remained evidence driven.

All calculations were implemented in Python using the pandas and numpy libraries. Visualisations were produced using matplotlib. The accompanying script `week3_analysis.py` calculates week-to-week output changes, percentage improvements, function rankings and strategy allocations directly from the observed optimisation results.

Neural networks were not trained during this stage of the optimisation process. They are discussed as potential future surrogate models once additional observations become available. At the current stage, simpler interpretable approaches such as SVM classification and ranking analysis were considered more appropriate given the limited number of observations.

# Conclusion

Overall, the most important insight from this iteration is that optimisation, classification, surrogate modelling and information acquisition represent complementary perspectives on the same underlying problem. Effective query selection requires balancing exploitation of known high-performing regions against exploration of uncertain areas that may contain better solutions. As additional evaluations accumulate, increasingly sophisticated models may become justified. However, model complexity should be introduced only when supported by sufficient evidence and data. The Week 4 strategy therefore reflects not only a search for better outputs but also a systematic effort to improve understanding of the search landscape itself.


## Contents

1. Introduction
2. Week 3 Results
3. Comparison of Week 2 and Week 3 Performance
4. Query Selection Strategy
5. Learning from Exploration and Exploitation
6. Reflection on Week 4 Query Selection Strategy
7. Functional Ranking Evolution
8. Identifying Exploitation and Boundary Regions
9. Function 5 and Influential Variables
10. Decision Matrix and Resource Allocation
11. Surrogate Modelling and Neural Network Considerations
12. Optimisation as a Classification Problem
13. Model Complexity versus Interpretability
14. Information Gain and Exploration Strategy
15. Final Week 4 Query Selection
16. Computational Analysis and Coding Implementation
17. Conclusion
