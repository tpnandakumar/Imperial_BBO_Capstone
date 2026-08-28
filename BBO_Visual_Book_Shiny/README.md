# Imperial BBO Visual Book, Shiny edition

This is the reader-facing presentation layer for the Imperial BBO capstone. It reads the audited `279`-observation evidence file and does not modify any official input or output.

## What happens when this link opens

GitHub can display this page and the source code, but it cannot execute the Shiny application inside a repository page. Open the public Visual Book from the main repository README, or launch it locally using the two commands below. The opening cover then provides the full visual navigation without requiring the reader to browse folders.

## Run locally

From the repository root:

```bash
python -m pip install -r BBO_Visual_Book_Shiny/requirements.txt
python -m shiny run BBO_Visual_Book_Shiny/app.py
```

Open the local address printed by Shiny.

## Reading routes

- **Cover:** the opening quote and two-book gateway
- **Imperial BBO Capstone:** entry to the official thirteen-week optimisation book, verified totals and best retained values
- **Above and Beyond BBO:** a second gateway separating the Above BBO BBR Book from the Beyond BBO PDHIS Book
- **Read by Week:** thirteen compact chronological chapters with Home, Previous and Next controls
- **Read by Function:** eight complete function trajectories with page controls and tabbed evidence
- **Scientific Atlas:** interactive trajectories, heat map and maxima view
- **Resolution:** Black Box Resolution, competing explanations and the recurring Evaluate, Resolve, Explore or Exploit, Extend, Optimise, Evolve and Experiment cycle
- **BBR:** the resolution loop, competing explanations and optimisation trade-offs
- **Beyond BBO:** a dedicated post-challenge chapter for Delta of BBO, with a landing page and separate pages for Delta meanings, the Lotus hierarchy, selectable Delta trajectories, chronological predictability, F1 to F8 relationships and evidence limits
- **PDHIS:** Pisharam Delta Hierarchy and Influence State, the framework used in Delta of BBO to study recursively nested change from Delta 1 to Delta 10. Its central visual idea is **Delta as the Signature of Change**: a structured, recurring and directionally coherent pattern across related Delta levels, rather than one isolated peak. Each graph includes a plain-English interpretation and an **Explain graph** dialogue. Delta to the power n remains extendable when the preceding level changes materially and enough evidence remains. Chronological testing, randomisation and evidence limits distinguish candidate signals from confirmed predictors.
- **Evidence:** filterable record of all 104 participant queries

The interface uses dynamic viewport scaling, compact page tabs, responsive pastel styling, Plotly hover evidence and restrained motion. It is designed for desktop, smaller laptops and mobile screens without turning the visual book into one continuous scroll. Motion is disabled automatically when the browser reports a reduced-motion accessibility preference.
