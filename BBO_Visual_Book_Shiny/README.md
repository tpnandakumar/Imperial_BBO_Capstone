# Imperial BBO Visual Book, Shiny edition

This is the enhanced presentation layer for the Imperial BBO capstone. It reads the same audited `279`-observation evidence file as the verified Streamlit dashboard and does not modify any official input or output.

## Run locally

From the repository root:

```bash
python -m pip install -r BBO_Visual_Book_Shiny/requirements.txt
python -m shiny run BBO_Visual_Book_Shiny/app.py
```

Open the local address printed by Shiny.

## Reading routes

- **Cover:** entry page and verified campaign totals
- **Read by Week:** thirteen animated chronological chapters
- **Read by Function:** eight complete function trajectories
- **Scientific Atlas:** interactive trajectories, heat map and maxima view
- **Strategy Loop:** exploration, exploitation and feedback-led development
- **Evidence:** filterable record of all 104 participant queries

The interface uses responsive pastel styling, Plotly hover evidence and restrained motion. Motion is disabled automatically when the browser reports a reduced-motion accessibility preference.
