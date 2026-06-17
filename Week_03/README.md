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

Overall, Figure 3 demonstrates how empirical observations can be translated into practical optimisation decisions. The framework supports continued exploitation of strong-performing functions while directing exploratory effort towards uncertain or poorly understood regions. This balanced allocation of resources helps maximise information gain and performance improvement simultaneously, which is a central objective of Bayesian optimisation.


## Figure 4 – Learning from Exploration and Exploitation

## Reflection

## Conclusion

## Contents
