# Scientific Story Infographic Register

The 20 story infographics supplement the 20 existing scientific figures. Each image is a compressed JPG with an embedded title, evidence statement, interpretation, limitation, caption and source statement. The individual images are stored in `scientific_story_infographics/`; ten side-by-side discussion-board plates are stored in `scientific_story_pairs/`.

| Story | Scientific content | Primary evidence | Interpretation boundary |
|---:|---|---|---|
| S01 | Starter observations and query budget | 175 starter observations, 104 portal queries | Dimensional coverage is not uniform |
| S02 | Complete weekly trajectories | All 104 portal returns | Within-function normalisation does not compare objective magnitude |
| S03 | Weekly record heatmap | New best event by function and week | Record frequency does not measure gain size |
| S04 | Observed maxima and minima | All 279 verified observations | Observed extrema are not global extrema |
| S05 | F1 projected response landscape | All F1 inputs and outputs | Interpolation inside the sampled projection only |
| S06 | F2 three-dimensional response terrain | All F2 inputs and outputs | Interpolation inside the sampled projection only |
| S07 | F3 projected response landscape | All F3 inputs and outputs | Other coordinates vary outside the displayed projection |
| S08 | F4 three-dimensional response terrain | All F4 inputs and outputs | Other coordinates vary outside the displayed projection |
| S09 | F5 projected response landscape | All F5 inputs and outputs | Productive boundary direction does not prove a boundary optimum |
| S10 | F6 three-dimensional response terrain | All F6 inputs and outputs | Repeat variability restricts deterministic interpretation |
| S11 | F7 projected response landscape | All F7 inputs and outputs | Other coordinates vary outside the displayed projection |
| S12 | F8 three-dimensional response terrain | All F8 inputs and outputs | Other coordinates vary outside the displayed projection |
| S13 | Query-movement heatmap | Consecutive L1 coordinate distances | Equal L1 distance has different geometry by dimension |
| S14 | Boundary-proximity heatmap | Minimum distance from each query to 0 or 1 | Proximity does not establish a boundary optimum |
| S15 | Week 10 clustering validation | Silhouette scores for k=2 and k=3 | Clusters may reflect adaptive sampling |
| S16 | PCA variance concentration | PC1 variance from each 13-query path | PCA describes the sampled path, not reward sensitivity |
| S17 | Week 13 reward changes | Exact Week 12 to Week 13 portal returns | Changes are normalised across incompatible scales |
| S18 | Repeatability audit | Identical-coordinate output groups | Too few repeats to estimate a complete noise distribution |
| S19 | Measured strengths and deviations | F5 gain, recoveries, F2 loss and F6 repeat range | One query per round limits causal attribution |
| S20 | Stopping and continuation map | Final function-specific evidence state | Status would change if new evidence became available |

## Side-by-side discussion plates

- `Stories_01_02.jpg`
- `Stories_03_04.jpg`
- `Stories_05_06.jpg`
- `Stories_07_08.jpg`
- `Stories_09_10.jpg`
- `Stories_11_12.jpg`
- `Stories_13_14.jpg`
- `Stories_15_16.jpg`
- `Stories_17_18.jpg`
- `Stories_19_20.jpg`

The generation scripts are `generate_scientific_story_infographics.py` and `build_paired_story_plates.py`.
