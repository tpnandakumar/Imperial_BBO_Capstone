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
- Round dashboard: function and round controls, history, submission, strategy, PCA and diagnostics
- Weekly progress: comparable progress across all eight functions
- Capstone retrospective: evidence organised around the five required discussion areas
- Assessment evidence: filterable and downloadable Week 1 to Week 13 records

The visual design uses a restrained pastel palette. Each function has a consistent colour across its cards and charts, while dark text and uncluttered panels preserve readability.

The dashboard deliberately excludes all post-capstone BBD research.

The `data` folder contains the official starter evidence and Week 1 to Week 13 evaluator record required by the dashboard.
