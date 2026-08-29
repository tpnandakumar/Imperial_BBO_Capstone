# Visual Book design QA

Date: 2026-08-28

## Reference issues

The five supplied screenshots showed:

1. BBR evidence separated from its controls by a large empty region and clipped at the bottom.
2. A PDHIS graph embedded in the page and clipped by the available viewport.
3. The Delta meaning table cut off at the bottom.
4. A spreadsheet-style evidence widget with unexplained filter boxes and an internal scrollbar.
5. Reader-facing wording that introduced the legacy Streamlit edition and caused confusion.

## Live verification

Verified on the public Posit deployment at a 1363 by 936 pixel viewport.

- BBR method evidence ended at y=460 and remained fully visible. The page had no overflow.
- PDHIS trajectory contained no inline Plotly graph. Open graph and Explain graph controls were visible.
- The centred graph viewer occupied y=44 to y=792. Its 360-pixel graph was fully visible.
- The explanation dialog was compact, centred and 204 pixels high.
- All ten Delta meaning rows fitted between y=169 and y=359 with no internal scrolling.
- Evidence displayed six rows, no filter inputs, no internal scrolling and a visible `Rows 1 to 6 of 104` pager.
- Repository displayed two concise explanation cards and no reader-facing Streamlit reference.

## Result

final result: passed

## Final completion check

Date: 2026-08-29

The live public deployment was checked again at a 1280 by 720 pixel viewport after the reader-facing revisions.

- PDHIS expanded correctly on first use and displayed the full name in the page heading.
- The Delta trajectory page kept its controls, launch panel and interpretation above the bottom edge.
- The centred graph viewer displayed a 1085 by 360 pixel Plotly graph without page or modal scrolling.
- The Delta meaning table showed all ten rows, followed by the explanation controls, with no internal scrollbar.
- Evidence showed six rows and its visible pager. No spreadsheet filter boxes or table scrollbar appeared.
- The BBR method ended at y=372, leaving all evidence visible within the 720 pixel viewport.
- Repository wording identified Shiny as the live reader-facing edition and linked to the public GitHub record.
- Graph explanations were checked for natural British English, distinct interpretation guidance and evidence limits.
- A changed PDHIS selection could leave a completed Plotly graph inside a hidden Shiny output container. The graph-stage visibility rule now keeps every generated graph visible, including F5 Delta 2.

Final completion result: passed.

## Advanced analysis and repository check

Date: 2026-08-29

- The Advanced model page displayed its grouped validation graph at 1085 by 360 pixels in the centred graph viewer.
- The graph remained visible after changing PDHIS selections and required no page or modal scrolling.
- The explanation dialogue defined balanced accuracy, both validation methods, the prevalence baseline and the exploratory permutation result.
- The interpretation stated that chronological probability calibration did not beat the baseline and that prospective validation is required.
- The Repository page displayed separate links to the executive summary, the GitHub README and the complete repository.
- The three repository cards collapsed to one column at the existing mobile breakpoint.

Advanced analysis completion result: passed locally. Public deployment verification follows the checked push to `main`.

## Event-locked flicker study

Date: 2026-08-29

- The flicker page states that the analysis is retrospective and that the six-observation fingerprint precedes the known target week.
- The graph compares nine temporal characteristics across improvement, large-change and new-best targets.
- The explanation reports the exploratory and adjusted results separately and does not describe the candidate peak-spacing result as confirmed.
- The supporting static figure was inspected for readable labels, complete axes and unclipped annotations.

Event-locked analysis completion result: passed locally.

## Matched event atlas

Date: 2026-08-29

- Same-function matching, threshold sensitivity and held-out-function results are reported separately.
- The Visual Book explanation states that the candidate fingerprint was not confirmed.
- Standardised paired differences keep characteristics with different units comparable in the graph.
- The supporting three-panel figure was inspected for readable labels, complete axes and unclipped annotations.

Matched atlas completion result: passed locally.
