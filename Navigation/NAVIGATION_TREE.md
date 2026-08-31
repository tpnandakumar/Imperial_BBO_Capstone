# Imperial BBO Repository Navigation Tree

This page provides a practical route through the repository. It highlights the folders and files most useful to assessors, technical readers and readers exploring the later research. Generated images and intermediate artefacts remain available in their original folders but are not all repeated here.

## 1. Start here

- [Main README](../README.md)
- [Detailed Executive Summary](../Executive_Summary/DETAILED_EXECUTIVE_SUMMARY.md)
- [Final assessment submission](../Module_25_Final_BBO_Submission/25_3_GitHub_Final_Submission/)
  - [Final notebook](../Module_25_Final_BBO_Submission/25_3_GitHub_Final_Submission/FINAL_CAPSTONE_NOTEBOOK.ipynb)
  - [Final datasheet](../Module_25_Final_BBO_Submission/25_3_GitHub_Final_Submission/FINAL_CAPSTONE_DATASHEET.md)
  - [Final model card](../Module_25_Final_BBO_Submission/25_3_GitHub_Final_Submission/FINAL_CAPSTONE_MODEL_CARD.md)
  - [Reproducibility guide](../Module_25_Final_BBO_Submission/25_3_GitHub_Final_Submission/FINAL_REPRODUCIBILITY.md)
- [Live Visual Storyboard](https://01a04a5b-864f-4cec-e841-84e7f7931b5d.share.connect.posit.cloud/)

## 2. Repository tree

- **Imperial BBO Capstone**
  - [README.md](../README.md): single authoritative project overview and assessment route
  - [Executive_Summary](../Executive_Summary/)
    - [DETAILED_EXECUTIVE_SUMMARY.md](../Executive_Summary/DETAILED_EXECUTIVE_SUMMARY.md)
  - [BBO_Dashboard](../BBO_Dashboard/): audited dataset, optimisation code and hyperparameter results
    - [Complete 279-observation evidence](../BBO_Dashboard/data/complete_internal_evidence.csv)
    - [Hyperparameter optimisation engine](../BBO_Dashboard/hpo_engine.py)
    - [Hyperparameter results](../BBO_Dashboard/hpo_results/)
  - [BBO_Visual_Book_Shiny](../BBO_Visual_Book_Shiny/): source for the public Shiny Visual Storyboard
    - [Application source](../BBO_Visual_Book_Shiny/app.py)
    - [Narration scripts](../BBO_Visual_Book_Shiny/NARRATION_SCRIPTS.md)
    - [Visual and narration assets](../BBO_Visual_Book_Shiny/www/)
  - [Results](../Results/)
    - [Tables and numerical results](../Results/Tables_and_Numerical_Results/TABLES_AND_NUMERICAL_RESULTS.md)
    - [Graphs and infographics](../Results/Graphs_and_Infographics/GRAPHS_AND_INFOGRAPHICS.md)
    - [Detailed results discussion](../Results/Discussion/DETAILED_RESULTS_DISCUSSION.md)
  - [Optimisation](../Optimisation/)
    - [Detailed optimisation discussion](../Optimisation/DETAILED_OPTIMISATION_DISCUSSION.md)
  - [Module_25_Final_BBO_Submission](../Module_25_Final_BBO_Submission/)
    - [25.1 Retrospective evidence](../Module_25_Final_BBO_Submission/25_1_Retrospective/)
    - [25.2 Successful optimisation strategies](../Module_25_Final_BBO_Submission/25_2_Successful_Optimisation_Strategies/)
    - [25.3 Final GitHub submission](../Module_25_Final_BBO_Submission/25_3_GitHub_Final_Submission/)
    - [Final thirteen-round evidence](../Module_25_Final_BBO_Submission/Final_13_Round_Evidence/)
  - **Weekly chronological record**
    - [Week 1](../Week_01/)
    - [Week 2](../Week_02/)
    - [Week 3](../Week_03/)
    - [Week 4](../Week_04/)
    - [Week 5](../Week_05/)
    - [Week 6](../Week_06/)
    - [Week 7](../Week_07/)
    - [Week 8](../Week_08/)
    - [Week 9](../Week_09/)
    - [Week 10](../Week_10/)
    - [Week 11](../Week_11/)
    - [Week 12](../Week_12/)
    - [Week 13](../Week_13/)
  - **Above and Beyond**
    - [Black Box Resolution](../Post_BBO_BBR/)
      - [BBR mathematical models for F1 to F8](../Post_BBO_BBR/BBR_MATHEMATICAL_MODELS_F1_TO_F8.md)
      - [Representative F5 and F7 surrogates](../Post_BBO_BBR/representative_surrogates/)
      - [BBR infographics and evidence values](../Post_BBO_BBR/infographics/)
    - [Pisharam Delta Hierarchy and Influence State](../Post_BBO_BBR/PDHIS/)
      - [PDHIS mathematical model](../Post_BBO_BBR/PDHIS/PDHIS_MATHEMATICAL_MODEL.md)
      - [PDHIS findings](../Post_BBO_BBR/PDHIS/PDHIS_FINDINGS.md)
      - [Event-locked flicker study](../Post_BBO_BBR/PDHIS/PDHIS_EVENT_LOCKED_FLICKERS.md)
      - [Matched event atlas](../Post_BBO_BBR/PDHIS/PDHIS_MATCHED_EVENT_ATLAS.md)
      - [PDHIS infographics](../Post_BBO_BBR/PDHIS/infographics/)
  - **Supporting material**
    - [Experiments](../Experiments/)
    - [Figures](../Figures/)
    - [Notebooks](../Notebooks/)
    - [Reports](../Reports/)
    - [References](../References/)
    - [Templates](../Templates/)
    - [Visualisations](../Visualisations/)
    - [Repository validation tools](../tools/)

## 3. Suggested reading routes

### Assessment route

[Main README](../README.md) → [Final notebook](../Module_25_Final_BBO_Submission/25_3_GitHub_Final_Submission/FINAL_CAPSTONE_NOTEBOOK.ipynb) → [Datasheet](../Module_25_Final_BBO_Submission/25_3_GitHub_Final_Submission/FINAL_CAPSTONE_DATASHEET.md) → [Model card](../Module_25_Final_BBO_Submission/25_3_GitHub_Final_Submission/FINAL_CAPSTONE_MODEL_CARD.md) → [Reproducibility guide](../Module_25_Final_BBO_Submission/25_3_GitHub_Final_Submission/FINAL_REPRODUCIBILITY.md)

### Results route

[Results summary](../README.md#results) → [Tables and numerical results](../Results/Tables_and_Numerical_Results/TABLES_AND_NUMERICAL_RESULTS.md) → [Graphs and infographics](../Results/Graphs_and_Infographics/GRAPHS_AND_INFOGRAPHICS.md) → [Detailed discussion](../Results/Discussion/DETAILED_RESULTS_DISCUSSION.md)

### Visual route

[Live Visual Storyboard](https://01a04a5b-864f-4cec-e841-84e7f7931b5d.share.connect.posit.cloud/) → [Visual Storyboard source](../BBO_Visual_Book_Shiny/) → [Figure register](../Module_25_Final_BBO_Submission/25_1_Retrospective/ACADEMIC_FIGURE_REGISTER.md)

### Research route

[Black Box Resolution](../Post_BBO_BBR/) → [BBR equations](../Post_BBO_BBR/BBR_MATHEMATICAL_MODELS_F1_TO_F8.md) → [PDHIS](../Post_BBO_BBR/PDHIS/) → [PDHIS mathematical model](../Post_BBO_BBR/PDHIS/PDHIS_MATHEMATICAL_MODEL.md)
