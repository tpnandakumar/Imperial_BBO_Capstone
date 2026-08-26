# Imperial BBO Challenge Dashboard

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
- Code laboratory: controlled reproduction and variation of PCA, movement and output experiments
- Chapter Summary: shared conclusion for both visual-book reading routes
- Extend and Evolve: clearly separated bridge to the post-BBO Advanced Next Stage
- Round dashboard: function and round controls, history, submission, strategy, PCA and diagnostics
- Weekly progress: comparable progress across all eight functions
- Capstone retrospective: evidence organised around the five required discussion areas
- Assessment evidence: filterable and downloadable Week 1 to Week 13 records

The visual design uses a restrained pastel palette. Each function has a consistent colour across its cards and charts, while dark text and uncluttered panels preserve readability.

## Three reading routes

The dashboard can be read chronologically by Week, followed by function from F1 to F8, or explored as a small code laboratory. Official reproductions use the saved competition evidence. Interactive variations are labelled clearly and never overwrite or masquerade as official results.

The dashboard deliberately excludes all post-capstone BBD research.

The `data` folder contains the official starter evidence and Week 1 to Week 13 evaluator record required by the dashboard.
