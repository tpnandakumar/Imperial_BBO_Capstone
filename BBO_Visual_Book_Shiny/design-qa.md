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
