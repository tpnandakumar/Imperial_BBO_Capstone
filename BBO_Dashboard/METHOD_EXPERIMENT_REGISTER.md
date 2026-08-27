# Imperial BBO Method and Experiment Register

This register distinguishes the course teaching chronology from the BBO evidence chronology. It is controlled by the module-to-capstone crosswalk in `COURSE_CAPSTONE_TOPIC_MAP.md`.

## Correct course-linked sequence

1. Module 12 used starter evidence and informed Week 1: Bayesian optimisation.
2. Module 13 analysed Week 1 and informed Week 2: logistic regression.
3. Module 14 analysed Week 2 and informed Week 3: support vector machines and kernels.
4. Module 15 analysed Week 3 and informed Week 4: neural networks and function approximation.
5. Module 16 analysed Week 4 and informed Week 5: deeper neural architectures.
6. Module 17 analysed Week 5 and informed Week 6: convolutional neural networks.
7. Break week: no BBO round and no renumbering.
8. Module 18 analysed Week 6 and informed Week 7: hyperparameters and hyperparameter tuning.
9. Module 19 analysed Week 7 and informed Week 8: attention, prompting and transformer foundations.
10. Module 20 analysed Week 8 and informed Week 9: scaling, emergence and transformer refinement.
11. Module 21 analysed Week 9 and informed Week 10: transparency and interpretability.
12. Module 22 analysed Week 10 and informed Week 11: clustering.
13. Module 23 analysed Week 11 and informed Week 12: principal component analysis.
14. Module 24 analysed Week 12 and informed Week 13: reinforcement learning.
15. Module 25: retrospective and repository submission.

## Analysis-week and submission-week distinction

An experiment stored with Week 10 outputs may have been used to choose the Week 11 input. The dashboard therefore records the course-linked capstone week, the evidence cut-off or repository folder, and the later submission informed by that evidence. These values must not be collapsed into a single week label.

## HPO and clustering example

HPO was taught in Module 18 while Week 6 evidence was available and informed Week 7. Later, during Module 22 clustering, KMeans settings were compared using evidence available through Week 10 to inform Week 11. The confirmed comparison tested `k=2` and `k=3`, with `n_init=50` and `random_state=42`, and selected by silhouette score.

The accurate statement is:

> Hyperparameter optimisation was introduced in Module 18 while preparing Week 7 and later applied to the Module 22 clustering analysis that used Week 10 evidence to inform Week 11.

## Evidence classes

- **Course-linked**: confirmed by the printed course record.
- **Decision-influencing**: saved evidence shows that the result affected a later submission.
- **Retrospective**: constructed after the event to compare or demonstrate a method.
- **To verify**: remembered or plausible, but the BBO-specific source code or output has not yet been indexed.

Course attendance alone is not evidence that a method was used to select a competition coordinate.
