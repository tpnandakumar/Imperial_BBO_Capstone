# Imperial BBO Data and Analytical Resources

> “Life is a stone. Sculpt yourself a masterpiece.”  
> Dr N T Pisharam, *Be and Become*

The quotation frames the project as a story of development. It opens the journey and returns in the post-BBO chapter, where Method, Methodology, Modulation, Modification, Magnificence and Masterpiece describe how the work was progressively shaped.

This folder preserves the canonical dataset and analytical resources used to reproduce the official thirteen-round Imperial BBO Challenge record. The public interactive edition is the [Shiny Visual Book](../BBO_Visual_Book_Shiny/README.md).

## Open the Visual Book

From the project root:

```bash
python -m pip install -r BBO_Visual_Book_Shiny/requirements.txt
python -m shiny run BBO_Visual_Book_Shiny/app.py
```

The same reader-facing edition is available through the [live Imperial BBO Visual Book](https://01a04a5b-864f-4cec-e841-84e7f7931b5d.share.connect.posit.cloud/).

## Resources preserved here

- `data/complete_internal_evidence.csv`: the canonical 279-observation record
- `CAPSTONE_WEEK_STORY.csv`: the verified Week 1 to Week 13 chronology
- `hpo_results/`: the retained clustering and surrogate experiment results
- `METHOD_EXPERIMENT_REGISTER.md`: the method and evidence register
- `run_hpo_experiment.py` and `hpo_engine.py`: supporting analytical code

The Shiny Visual Book reads the canonical evidence from this folder and presents it through the Week, Function, Scientific Atlas, Repository, BBR and PDHIS routes.

## Three reading routes

The Visual Book can be read chronologically by Week, followed by function from F1 to F8, or explored through its scientific and post-capstone routes. Official reproductions use the saved competition evidence. Interactive views never overwrite or masquerade as official results.

The Week 10 clustering analysis used genuine Weeks 1 to 10 evidence to inform the Week 11 submission. Its HPO comparison tested KMeans `k=2` and `k=3`, with `n_init=50` and `random_state=42`, selecting by silhouette score. Broader cluster searches and polynomial Ridge tuning are labelled as interactive or post-hoc extensions.

The assessment-facing chronology is presented as Week 1 to Week 13, showing the focus, what was done, what the evidence showed and how it shaped the following decision.

The `data` folder contains the official starter evidence and Week 1 to Week 13 evaluator record required by the Shiny Visual Book, final notebook, assessment figures and reproducibility checks.
