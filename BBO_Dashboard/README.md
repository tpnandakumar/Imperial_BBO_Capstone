# Imperial BBO Challenge Dashboard

> “Life is a stone. Sculpt yourself a masterpiece.”  
> Dr N T Pisharam, [*Be and Become*](https://honeycombpublications.com/books/be-and-become/), [Honeycomb Publications](https://honeycombpublications.com/)

The quotation frames the dashboard as a visual story of development. It opens the journey and returns in the post-BBO chapter, where Method, Methodology, Modulation, Modification, Magnificence and Masterpiece describe how the work was progressively shaped.

This Streamlit dashboard presents only the official thirteen-round Imperial BBO Challenge record.

## Run locally

From the project root:

```bash
python -m pip install -r BBO_Dashboard/requirements.txt
streamlit run BBO_Dashboard/streamlit_app.py
```

## Dashboard pages

- Visual home: direct Week 01 to Week 13 and F1 to F8 navigation
- Week story: all eight inputs and outputs for a selected competition round
- Function story: complete thirteen-week input, output and coordinate history for F1 to F8
- Code laboratory: controlled reproduction and variation of HPO, PCA, movement and output experiments
- Methods and Evolution: verified method chronology with a separate evidence-recovery register for experiments whose source files still need locating
- Chapter Summary: shared conclusion for both visual-book reading routes
- Extend and Evolve: clearly separated bridge to the post-BBO Advanced Next Stage
- Round dashboard: function and round controls, history, submission, strategy, PCA and diagnostics
- Weekly progress: comparable progress across all eight functions
- Capstone retrospective: evidence organised around the five required discussion areas
- Assessment evidence: filterable and downloadable Week 1 to Week 13 records

The visual design uses a restrained pastel palette. Each function has a consistent colour across its cards and charts, while dark text and uncluttered panels preserve readability.

## Three reading routes

The dashboard can be read chronologically by Week, followed by function from F1 to F8, or explored as a small code laboratory. Official reproductions use the saved competition evidence. Interactive variations are labelled clearly and never overwrite or masquerade as official results.

Hyperparameter optimisation is treated as a core Week 10 experiment and runs on the genuine Weeks 1 to 10 function-specific evidence. The official reproduction compares KMeans `k=2` and `k=3`, with `n_init=50` and `random_state=42`, and selects the exploratory partition by silhouette score. Broader cluster searches and polynomial Ridge tuning are clearly labelled as interactive or post-hoc extensions rather than original Week 10 submissions.

The dashboard deliberately excludes all post-capstone BBD research.

The `data` folder contains the official starter evidence and Week 1 to Week 13 evaluator record required by the dashboard.
