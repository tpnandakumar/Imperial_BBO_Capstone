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
- **Read by Week:** thirteen compact chronological chapters with Home, Previous and Next controls
- **Read by Function:** eight complete function trajectories with page controls and tabbed evidence
- **Scientific Atlas:** interactive trajectories, heat map and maxima view
- **BBR and Strategy:** Black Box Resolution, the resolution loop and optimisation trade-offs
- **Evidence:** filterable record of all 104 participant queries

The interface uses dynamic viewport scaling, compact page tabs, responsive pastel styling, Plotly hover evidence and restrained motion. It is designed for desktop, smaller laptops and mobile screens without turning the visual book into one continuous scroll. Motion is disabled automatically when the browser reports a reduced-motion accessibility preference.
