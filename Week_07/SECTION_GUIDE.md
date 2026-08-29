# Week_07

## Bayesian Black Box Optimisation Portfolio
### Week 07 Analysis

## 1. Introduction

Week 07 was a useful test of whether the Week 06 directions were robust. The answer was mixed. F5 improved strongly again, several negative functions recovered, and F2 fell sharply after its previous gain. That combination changed how I approached the next round.

## 2. Week 7 Results

| Function | Week 7 output |
| --- | ---: |
| F1 | -1.4546199699251391e-58 |
| F2 | 0.239929 |
| F3 | -0.091169 |
| F4 | -10.745961 |
| F5 | 4278.816638 |
| F6 | -1.119713 |
| F7 | 1.154336 |
| F8 | 9.494760 |

F5 rose from `3922.765223` to `4278.816638`. F3, F4 and F6 all improved from Week 06, although they remained negative. F2 fell from `0.571248` to `0.239929`. F7 and F8 also declined, but both remained positive.

## 3. Comparison with Week 6

The largest practical change was F4's recovery from `-31.203478` to `-10.745961`. F3 also moved much closer to zero. These improvements showed that changing direction in weak functions could be worthwhile. F2 gave the opposite lesson because its Week 06 gain did not persist.

## 4. Query Selection Strategy

I kept F5 as the principal exploitation target. F3, F4 and F6 had earned further attention because the new directions improved their results. F2 needed reassessment. F7 and F8 remained suitable for cautious local work because their declines were modest relative to their established positive regions.

## 5. Exploration and Exploitation

The round reinforced the need for different levels of commitment. F5 justified close exploitation. F7 and F8 justified refinement. F2 required a more cautious reset, while F1 still offered almost no useful signal. The improving negative functions remained exploratory but now had clearer directions to test.

## 6. Reflection on Week 8 Selection

The Week 07 result made me less interested in simply following the previous week's winner or loser. What mattered was whether the latest movement had changed the evidence. F4's recovery supported further work around the revised direction, while F2's fall argued for stepping away from its Week 06 path.

## 7. Functional Ranking

F5 remained first, followed by F8, F7 and F2. F1 was effectively zero. F3, F6 and F4 remained negative. The ranking was stable at the top, but the changes within the lower functions were strategically important.

## 8. High Performing Regions

F5 remained the clearest high performing region. F8 and F7 retained positive local regions despite small declines. The recovery in F3 and F4 did not establish high performing regions, but it did identify directions worth testing again.

## 9. Decision Matrix

| Function | Week 7 reading | Week 8 approach |
| --- | --- | --- |
| F1 | Effectively zero | Explore |
| F2 | Sharp decline | Reassess |
| F3 | Strong recovery | Refine cautiously |
| F4 | Large recovery | Continue revised direction |
| F5 | Strong further gain | Exploit |
| F6 | Improved but negative | Refine cautiously |
| F7 | Positive with decline | Conservative refinement |
| F8 | Stable positive region | Conservative refinement |

## 10. Information Gained

F2 was the clearest warning against assuming that a previous improvement would continue. F4 showed the value of changing direction after a poor result. Together they made the strategy more responsive to the latest evidence rather than to ranking alone.

## 11. Computational Analysis

The numerical comparisons and figures were used to check trends and organise the eight functions. They supported, rather than replaced, the judgement used for the next query set.

## 12. Repository Record

This README preserves the Week 07 interpretation. The displayed values remain those recorded for the round, including the higher precision value retained for F1.

## 13. Conclusion

Week 07 strengthened F5, recovered several difficult functions and exposed instability in F2. The next round therefore combined continued exploitation with selective recovery and reassessment.

## 14. Automation Decision

No automated optimiser controlled the Week 08 query selection. Computational summaries informed a manually supervised decision.

## 15. References

Imperial College Business School, Black Box Optimisation Capstone materials.
