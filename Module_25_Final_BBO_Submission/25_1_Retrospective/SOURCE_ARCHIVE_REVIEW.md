# Source archive review

This register records how historical course and capstone files were assessed before inclusion in the final retrospective. Numerical claims are checked against the submitted coordinates and returned BBO outputs. A historical file is not treated as final evidence merely because it contains a chart or uses optimisation terminology.

## Evidence hierarchy

1. Processed portal input and output files
2. Verified repository CSV files and exact-history tables
3. Executable analysis code and reproducible outputs
4. Contemporary weekly reflections and decision records
5. Later summaries and infographics
6. Generic course material and conceptual illustrations

Higher-ranked evidence takes precedence when values conflict.

## Archive Week 1-11.zip

This archive contains course Weeks 1 to 11, not BBO query rounds 1 to 11. It covers probability, simulations, validation, class imbalance, oversampling, KNN, decision trees, Naive Bayes and introductory Bayesian optimisation.

### Retained as learning context

- Validation, leakage prevention and time-aware evaluation principles
- Oversampling within training folds
- Hyperparameter selection and overfitting control
- Introductory Gaussian-process, UCB, PI and posterior-variance exercises
- Early neurology referral-triage applications

### Excluded from the BBO chronology

- Generic assignments, solution archives and course transcripts
- Neurology triage work that was not performed on the eight BBO functions
- Introductory Bayesian-optimisation exercises using known teaching functions
- Screenshots and decorative course images

These files explain prior learning but are not evidence of submitted BBO queries or returned black-box outputs.

## Archive 12-15.zip

This archive contains the beginning of the BBO work and documents the move from the supplied starter observations to the first participant-selected queries.

### Retained as historical evidence

- Imperial starter arrays and challenge instructions
- F1 to F8 optimisation progression plots
- F1 to F8 sampled search-space plots
- Week 1 output comparison
- Week 2 exploration and exploitation heatmap
- Relative query movement map
- Week 2 decision matrix
- Week 3 and Week 4 trajectory, ranking and query-selection records
- Contemporary reflections describing the transition from broad exploration to function-specific refinement

### Corrective decision

An early methodology draft says that no observations were available at the start. That statement is not used. Imperial supplied the initial data-point starters. The first weekly inputs were calculated from those observations, submitted through the portal and followed by returned outputs. This sequential cycle continued for 13 BBO rounds.

### Excluded or qualified

- Decorative optimisation posters and generated landscapes
- Saved webpage assets and interface screenshots
- Generic course diagrams not calculated from BBO data
- SVM and neural-network discussions without fitted models and validation outputs
- Duplicate images and draft documents

## Archive 16-19.zip

This archive contains exact processed portal records through BBO round 6, later reflections and a scientific-validation folder.

### Retained as primary evidence

- `Capstone Project - Week 5 Submission Processed.zip`
- `Capstone Project - Week 6 Submission Processed.zip`
- Exact portal `inputs.txt` and `outputs.txt` records
- Week 5 function analysis
- Week 6 strategy and technical justification
- Function 5 growth and exploration versus exploitation records
- Coverage, dispersion, transition, efficiency, limitations and traceability methods

### Numerical verification finding

The processed portal files take precedence over the later scientific-validation CSV files. Several summary CSV values do not reproduce the exact portal values. Some differences are rounding differences, while others are materially different observations. The affected figures must therefore be regenerated from the processed portal files or verified repository history.

The exact processed BBO round 1 outputs are F1 6.854713532414845e-19, F2 0.45494185399727516, F3 -0.10183633971746164, F4 -4.359874926582439, F5 1415.8763939603884, F6 -0.7001549808025808, F7 1.3199939052019112 and F8 9.58024.

### Excluded or qualified

- HEBO material is background unless executable BBO-specific code and results are present
- CNN, SVM and neural-network diagrams are methods considered, not fitted BBO models
- Language, tokenisation, prompting and decoding assignments are unrelated
- Generic literature figures, transcripts, installers and self-study solutions are excluded

## Archive 23-25.zip

This archive covers the Week 12 analysis, Week 13 input selection, reinforcement-learning reflection and final-submission preparation.

### Retained as primary evidence

- Exact Week 12 input and output CSV files
- Week 11 to Week 12 decision narrative
- PCA analysis of the observed coordinate paths
- Variance, correlation, redundancy and dimensional-attribution records
- State, action, feedback and reward framing used before Week 13
- Delayed-feedback and query-budget analysis
- Prospective Week 13 action policy

### Superseded historical figures

The Week 24 reinforcement-learning figures state that Week 13 outputs were pending. They are valid prospective records but are not final outcome figures. The current Week 13 repository analysis supersedes them by holding out Week 13 outputs until after action selection, evaluating each selected action against the returned reward and reporting the final outcomes.

### Methodological qualification

- PCA describes the sampled query path, not the hidden objective surface
- Clustering is retained only as an exploratory diagnostic
- The bandit and Markov decision interpretations describe the sequential structure
- A converged tabular Q-learning policy is not claimed because the action space is continuous and the dataset is sparse
- Repeated coordinates are distinguished from unsuccessful movement because they test reproducibility and preserve verified reference points

### Excluded or superseded

- Generic PCA applications to neurological referral assessment
- Course transcripts, solution archives and career reflections
- Advertising and appointment-reminder reinforcement-learning examples
- Course-page and meeting screenshots
- The older discussion document whose figures pre-date the returned Week 13 outputs
- Conceptual figures without a capstone calculation

## Archive 20-22(1).zip

This archive covers the transition from the Round 9 documentation record to the Week 10 clustering analysis and Week 11 query decision.

### Retained as historical evidence

- Round 9 datasheet and model-card documentation
- Week 10 clustering reflection and contemporary decision rationale
- Exact distinction between a compact productive neighbourhood and an isolated strong observation
- K-means comparison for k = 2 and k = 3
- Silhouette score, nearest-neighbour distance and distance-to-best checks
- Function-specific Week 11 decisions based on the Week 10 evidence
- Documentation of adaptive-sampling bias, sparse coverage and higher-dimensional limitations

### Numerical and visual qualification

Several archived clustering infographics contain rounded or inconsistent values. They are historical presentation material rather than the authoritative numerical record. The current repository clustering figures are regenerated from the exact recovered history using `random_state=42`, `n_init=50`, candidate k values of 2 and 3, and explicit provenance files.

K-means is treated as an exploratory partitioning tool. Apparent clusters may reflect the adaptive query policy as well as the hidden function. Silhouette score is therefore interpreted alongside output history and distance measures, not as evidence of a recovered objective surface.

### Excluded from the final scientific figure set

- Generic language-model scaling and transformer assignments
- Fairness, interpretability and unrelated model-card coursework
- Course webpage assets, transcripts and solution archives
- Conceptual clustering diagrams not calculated from the verified BBO history
- Archived figures containing values that do not match the exact portal record

### Module 25 transcript note

The Module 25 introduction suggests considering an ablation study when discussing which parts of a strategy helped or hindered performance. This is advisory rather than an explicit completion requirement. Hyperparameter comparisons and function-specific outcome tests already provide component-level evidence, but a formal ablation would remain a useful repository extension if time permits.

## Archive capstone data.zip

This is the highest-priority primary-data archive. It contains the original starter arrays and the cumulative portal input and output records for all 13 BBO rounds.

### Starter-data verification

The supplied starting data contain 175 observations in total:

- F1: 10 observations in 2 dimensions
- F2: 10 observations in 2 dimensions
- F3: 15 observations in 3 dimensions
- F4: 30 observations in 4 dimensions
- F5: 20 observations in 4 dimensions
- F6: 20 observations in 5 dimensions
- F7: 30 observations in 6 dimensions
- F8: 40 observations in 8 dimensions

These are the initial data points supplied by the course. They are distinct from the 13 subsequent queries selected for each function through the portal.

### Query-history verification

The cumulative Week 13 files contain 104 function-level query and output records, comprising 13 rounds for each of eight functions. All inputs and outputs agree with the repository history. Weeks 12 and 13 match the dedicated repository CSV files with no discrepancies. Four values in the Weeks 1 to 11 CSV differ from the text representation only at approximately 1e-15 to 5e-13 because of floating-point CSV serialisation. They are numerically equivalent and do not change any calculation, ranking or conclusion.

### Evidence decision

The starter NumPy arrays and cumulative portal records are authoritative for numerical reconstruction. Templates, executable installers, theory notes and unrelated clinical coursework within the archive are excluded from the BBO evidence base.

## Final inclusion rule

The final retrospective uses verified values from all 13 BBO rounds. Scientific figures must identify their source data, calculation, interpretation and limitation. Earlier graphics may be preserved as historical records, but final GitHub and discussion-board figures are regenerated when chronology, values or captions are outdated.
