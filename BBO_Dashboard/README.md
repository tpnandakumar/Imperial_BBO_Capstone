# Imperial BBO Challenge Dashboard

This Streamlit dashboard presents only the official thirteen-round Imperial BBO Challenge record.

## Run locally

From the project root:

```bash
python -m pip install -r BBO_Dashboard/requirements.txt
streamlit run BBO_Dashboard/streamlit_app.py
```

## Dashboard pages

- Overview: challenge scale, process and final winners
- Round dashboard: function and round controls, history, submission, strategy, PCA and diagnostics
- Weekly progress: comparable progress across all eight functions
- Function explorer: output and coordinate movement for one function
- Capstone retrospective: evidence organised around the five required discussion areas
- Assessment evidence: filterable and downloadable Week 1 to Week 13 records

The dashboard deliberately excludes all post-capstone BBD research.

The `data` folder contains the official starter evidence and Week 1 to Week 13 evaluator record required by the dashboard.
