# Post-BBO Black Box Resolution Infographics

This folder presents the post-capstone Black Box Resolution work as a concise visual story. BBR investigates the behaviour of the hidden functions using the completed Week 1 to Week 13 record. It does not alter the official submissions and does not claim exact recovery of the Imperial equations.

## Figures

1. **BBR-1: From optimisation to Black Box Resolution**  
   Shows how 13 rounds, 8 functions and 104 official evaluations became evidence for chronological system identification.

2. **BBR-2: Function-specific findings**  
   Summarises the best completed function-specific model for F4 to F8 and the strongest measured finding for each function.

3. **BBR-3: Predictive evidence**  
   Compares the best normalised walk-forward MAE for F4 to F8. Lower values indicate better chronological prediction within the observed output range of that function.

4. **BBR-4: Repeatability boundary**  
   Contrasts zero-range repeated evaluations for F4 and F8 with the non-identical repeated outputs recorded for F6.

## Values used

| Function | Best completed model | Normalised walk-forward MAE | Repeatability or structural evidence |
| --- | --- | ---: | --- |
| F4 | Matérn 2.5 Gaussian Process | 0.021834 | One coordinate tested three times, output range 0.0 |
| F5 | Matérn 2.5 Gaussian Process | 0.001616 | Strongest linear direction x2, coefficient +17,750.44 |
| F6 | Static coordinate Gaussian Process | 0.044100 | Two repeat groups, maximum range 0.100675; within-coordinate MAE floor 0.030852 |
| F7 | Full 27-term quadratic | 0.034870 | The 20-term model was approximately 0.45% worse |
| F8 | Ordinary linear regression | 0.016539 | Four identical repeats; gradient cosine approximately 0.936764 |

## Evidence boundary

These figures report the best-supported explanations over the observed historical region. They do not establish the original hidden equation, behaviour across unobserved regions or a proven global optimum.

Both editable SVG and presentation-ready PNG versions are provided. Figure numbers and captions are embedded inside each artwork so that the evidence boundary is retained when a figure is copied into the Component 25.2 reflection.
