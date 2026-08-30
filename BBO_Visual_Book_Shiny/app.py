from __future__ import annotations

import base64
from pathlib import Path

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from shiny import App, Inputs, Outputs, Session, reactive, render, ui
from shinywidgets import output_widget, render_widget


APP_DIR = Path(__file__).resolve().parent
ROOT = APP_DIR.parent
DATA_FILE = ROOT / "BBO_Dashboard" / "data" / "complete_internal_evidence.csv"
PDHIS_ORDER_FILE = ROOT / "Post_BBO_BBR" / "PDHIS" / "PDHIS_PREDICTABILITY_BY_ORDER.csv"
PDHIS_FUNCTION_FILE = ROOT / "Post_BBO_BBR" / "PDHIS" / "PDHIS_FUNCTION_RELATIONSHIPS.csv"
PDHIS_ADVANCED_METRICS_FILE = ROOT / "Post_BBO_BBR" / "PDHIS" / "PDHIS_LOGISTIC_METRICS.csv"
PDHIS_ADVANCED_COEFFICIENTS_FILE = ROOT / "Post_BBO_BBR" / "PDHIS" / "PDHIS_LOGISTIC_COEFFICIENTS.csv"
PDHIS_FLICKER_ASSOCIATIONS_FILE = ROOT / "Post_BBO_BBR" / "PDHIS" / "PDHIS_EVENT_LOCKED_FLICKER_ASSOCIATIONS.csv"
PDHIS_MATCHED_RESULTS_FILE = ROOT / "Post_BBO_BBR" / "PDHIS" / "PDHIS_MATCHED_EVENT_RESULTS.csv"
PDHIS_FLICKER_LOFO_FILE = ROOT / "Post_BBO_BBR" / "PDHIS" / "PDHIS_FLICKER_LOFO_METRICS.csv"
EXECUTIVE_SUMMARY_FILE = ROOT / "Executive_Summary" / "DETAILED_EXECUTIVE_SUMMARY.md"
EXECUTIVE_SUMMARY_TEXT = EXECUTIVE_SUMMARY_FILE.read_text(encoding="utf-8")


def embedded_jpeg(name: str) -> str:
    payload = base64.b64encode((APP_DIR / "www" / name).read_bytes()).decode("ascii")
    return f"data:image/jpeg;base64,{payload}"


GATEWAY_ART = embedded_jpeg("imperial-bbo-rhino-gateway.jpg")

DIMENSIONS = {1: 2, 2: 2, 3: 3, 4: 4, 5: 4, 6: 5, 7: 6, 8: 8}
PASTELS = ["#64b6ac", "#8da9db", "#b497d6", "#f2b880", "#e58aa5", "#7db6d8", "#8bc49a", "#c69bd2"]
WEEK_CONTEXT = {
    1: ("Opening exploration", "Establish benchmarks and begin mapping unfamiliar response surfaces."),
    2: ("Function-specific strategy", "Exploit supported directions while preserving exploration where uncertainty remains."),
    3: ("Ranking and movement", "Use change, rank and coordinate movement to organise the next decision."),
    4: ("Selective refinement", "Protect productive trajectories while continuing to test weaker functions."),
    5: ("Reassessment", "Reduce commitment to deteriorating directions and preserve the clearest gains."),
    6: ("Validation", "Test whether the developing strategy remains defensible."),
    7: ("Responsive redirection", "Change direction when new evidence contradicts the earlier ranking."),
    8: ("Selective continuation", "Continue productive regions while reducing commitment to weakening directions."),
    9: ("Transparency and repeatability", "Add explicit evidence records and repeated-coordinate testing."),
    10: ("Clustering and recovery", "Use recurring regions, distance, stability and plateaux to select the next actions."),
    11: ("PCA and method comparison", "Compare coordinate structure with direct objective evidence."),
    12: ("Outcome validation", "Test repetition, refinement, recovery and boundary movement."),
    13: ("Final evaluation", "Balance controlled risk, repeatability and sequential-decision reflection before stopping."),
}

DELTA_MEANINGS = [
    ("Δ1", "y(t) - y(t-1)", "Direct observed change: its direction and magnitude."),
    ("Δ2", "Δ1(t) - Δ1(t-1)", "Change of change: acceleration, curvature, an emerging plateau or reversal."),
    ("Δ3", "Δ2(t) - Δ2(t-1)", "Whether the second-order behaviour is itself changing."),
    ("Δ4", "Δ3(t) - Δ3(t-1)", "Persistence, reversal or a developing oscillation in the third-order pattern."),
    ("Δ5", "Δ4(t) - Δ4(t-1)", "Whether a repeated-change pattern continues to propagate."),
    ("Δ6", "Δ5(t) - Δ5(t-1)", "Deeper recursive change, interpreted only with the lower Delta levels."),
    ("Δ7", "Δ6(t) - Δ6(t-1)", "Higher-order propagation or instability already present in the sequence."),
    ("Δ8", "Δ7(t) - Δ7(t-1)", "Deep repeated change, increasingly exploratory as evidence narrows."),
    ("Δ9", "Δ8(t) - Δ8(t-1)", "A high-order pattern requiring strong consistency across lower levels."),
    ("Δ10", "Δ9(t) - Δ9(t-1)", "The practical cap for this thirteen-week record, used to develop questions for later testing."),
]

PDHIS_EXPLANATIONS = {
    "hierarchy": (
        "The Lotus hierarchy: building the Signature of Change",
        "Each ring asks how the preceding Delta level changed. Read outwards from direct change at Δ1 to increasingly nested change. "
        "A Signature of Change develops through consistent direction, persistence and movement across related Delta levels. "
        "Higher levels contain fewer usable comparisons, so their interpretation is stronger when the lower levels support it."
    ),
    "trajectory": (
        "Reading a Delta trajectory: the Signature of Change",
        "The horizontal zero line separates positive from negative recursive change. A sign switch marks a reversal at the selected level; "
        "a movement towards zero can indicate a plateau; repeated alternating signs can indicate oscillation. Magnitude shows the size of the change, "
        "not its importance. The Signature of Change comes from the shape, persistence and agreement between these movements. "
        "The curve describes observed change. Later observations are needed to test its predictive value."
    ),
    "orders": (
        "Testing whether the Signature of Change predicts",
        "The lines show chronological association between each Delta order and the following output or following change. The shaded shuffled range is a noise reference. "
        "A value outside that range suggests that part of the Delta signature may carry forward information. It is not a confirmed forecasting rule unless it also "
        "survives multiple-testing correction and later prospective data."
    ),
    "functions": (
        "Comparing the Signature of Change across functions",
        "Each cell compares one function and one Delta order. Blue indicates a negative relationship with the following change, rose a positive relationship, "
        "and pale cells little observed relationship. Repeated colour across neighbouring Delta orders is more consistent with a coherent signature than one isolated cell. "
        "The number n is the available sample size; small n means greater uncertainty."
    ),
    "evidence": (
        "Where the Signature of Change reaches its evidence boundary",
        "Bars show how many forward comparisons remain at each Delta order. The second line shows adjusted evidence after controlling false discoveries. "
        "Evidence falls at higher orders because every recursive difference removes an observation. This graph prevents an intricate visual signature from being mistaken "
        "for statistical confirmation: no order currently crosses the confirmation threshold."
    ),
    "advanced": (
        "Reading the advanced Delta model",
        "The grouped bars compare regularised logistic classification with the prevalence baseline. Balanced accuracy gives equal weight to improvement and non-improvement. "
        "Leave-one-function-out testing asks whether the pattern transfers to a function excluded from fitting. Expanding-week testing preserves the order in which evidence arrived. "
        "The earlier Delta signature is the predictor and the later behaviour is the target."
    ),
    "flicker": (
        "Reading the event-locked flicker study",
        "Each cell compares a characteristic measured during the six observations before a known target week. Positive values mean the characteristic was stronger before events; negative values mean it was weaker. "
        "The outcome is already known, so this retrospective study discovers candidate fingerprints rather than proving advance prediction."
    ),
    "atlas": (
        "Reading the matched event atlas",
        "Each event is paired with the nearest non-event window from the same function. The heat map shows the standardised paired difference. "
        "The stability checks ask whether the earlier candidate survives closer controls, alternative event thresholds and transfer to a function excluded from fitting."
    ),
    "model": (
        "Reading the PDHIS mathematical model",
        "The hierarchy begins with the observed output and applies recursive finite differences from first-order Delta to tenth-order Delta. "
        "The descriptive state adds oscillation, energy, temporal dispersion, persistence and cross-order coherence. A separate prospective layer tests whether that state predicts a genuinely later target."
    ),
}


def load_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    complete = pd.read_csv(DATA_FILE)
    assessed = complete[complete.source.str.startswith("week_")].copy()
    assessed["week"] = assessed.source.str.removeprefix("week_").astype(int)
    assessed = assessed.sort_values(["function", "week"]).reset_index(drop=True)
    if len(complete) != 279 or len(assessed) != 104:
        raise ValueError("The canonical evidence file does not contain the expected 279 observations and 104 weekly queries.")
    return complete, assessed


COMPLETE, EVIDENCE = load_data()


def load_pdhis_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    order_metrics = pd.read_csv(PDHIS_ORDER_FILE)
    function_metrics = pd.read_csv(PDHIS_FUNCTION_FILE)
    if len(order_metrics) != 10 or len(function_metrics) != 80:
        raise ValueError("PDHIS evidence must contain ten Delta orders for each of eight functions.")
    return order_metrics, function_metrics


PDHIS_ORDERS, PDHIS_FUNCTIONS = load_pdhis_data()


def load_pdhis_advanced_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    metrics = pd.read_csv(PDHIS_ADVANCED_METRICS_FILE)
    coefficients = pd.read_csv(PDHIS_ADVANCED_COEFFICIENTS_FILE)
    if len(metrics) != 12 or len(coefficients) != 8:
        raise ValueError("Advanced PDHIS evidence must contain twelve validation rows and eight coefficients.")
    return metrics, coefficients


PDHIS_ADVANCED_METRICS, PDHIS_ADVANCED_COEFFICIENTS = load_pdhis_advanced_data()


def load_pdhis_flicker_data() -> pd.DataFrame:
    associations = pd.read_csv(PDHIS_FLICKER_ASSOCIATIONS_FILE)
    if len(associations) != 27:
        raise ValueError("The event-locked flicker evidence must contain twenty-seven feature and target comparisons.")
    return associations


PDHIS_FLICKER_ASSOCIATIONS = load_pdhis_flicker_data()


def load_pdhis_matched_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    matched = pd.read_csv(PDHIS_MATCHED_RESULTS_FILE)
    transfer = pd.read_csv(PDHIS_FLICKER_LOFO_FILE)
    if len(matched) != 27 or len(transfer) != 2:
        raise ValueError("The matched event atlas evidence is incomplete.")
    return matched, transfer


PDHIS_MATCHED_RESULTS, PDHIS_FLICKER_TRANSFER = load_pdhis_matched_data()


def format_number(value: float) -> str:
    value = float(value)
    if value == 0:
        return "0"
    if abs(value) < 0.001 or abs(value) >= 10000:
        return f"{value:.6e}"
    return f"{value:.6f}"


def winning_rows(frame: pd.DataFrame = EVIDENCE) -> pd.DataFrame:
    return frame.loc[frame.groupby("function").output.idxmax()].sort_values("function")


def book_heading(kicker: str, title: str, text: str) -> ui.Tag:
    return ui.div(
        ui.div(kicker, class_="chapter-kicker"),
        ui.h1(title),
        ui.p(text, class_="chapter-lead"),
        class_="book-heading reveal",
    )


def stat_box(title: str, value: str, note: str, colour: str) -> ui.Tag:
    return ui.div(
        ui.span(title), ui.strong(value), ui.tags.small(note),
        class_="stat-card reveal", style=f"--accent:{colour}",
    )


def page_toolbar(home_id: str, up_id: str, previous_id: str, next_id: str) -> ui.Tag:
    return ui.div(
        ui.input_action_button(home_id, "Home", class_="btn-home"),
        ui.input_action_button(up_id, "Up one level", class_="btn-soft"),
        ui.input_action_button(previous_id, "Previous", class_="btn-soft"),
        ui.input_action_button(next_id, "Next", class_="btn-accent"),
        class_="top-toolbar",
    )


def numbered_buttons(prefix: str, values: range, label_prefix: str) -> ui.Tag:
    return ui.div(
        *[
            ui.input_action_button(f"{prefix}_{value}", f"{label_prefix}{value}", class_="index-button")
            for value in values
        ],
        class_="numbered-index",
    )


def graph_actions(open_id: str, explain_id: str) -> ui.Tag:
    return ui.div(
        ui.input_action_button(open_id, "Open graph", class_="btn-accent"),
        ui.input_action_button(explain_id, "Explain graph", class_="btn-soft"),
        class_="graph-actions",
    )


def explanation_dialog(title: str, summary: str, points: list[str]) -> ui.Tag:
    return ui.modal(
        ui.div(
            ui.p(summary, class_="explanation-lead"),
            ui.tags.ul(*[ui.tags.li(point) for point in points]),
            class_="explanation-dialog",
        ),
        title=title,
        easy_close=True,
        footer=ui.modal_button("Close explanation", class_="btn-accent"),
        class_="explanation-modal",
    )


def delta_meanings_table() -> ui.Tag:
    rows = []
    for index, (level, definition, meaning) in enumerate(DELTA_MEANINGS, start=1):
        cases = int(PDHIS_ORDERS.loc[PDHIS_ORDERS.order == index, "forward_cases"].iloc[0])
        rows.append(ui.tags.tr(ui.tags.td(level), ui.tags.td(definition), ui.tags.td(meaning), ui.tags.td(str(cases))))
    return ui.div(
        ui.tags.table(
            ui.tags.thead(ui.tags.tr(ui.tags.th("Level"), ui.tags.th("Recursive definition"), ui.tags.th("Practical meaning"), ui.tags.th("Forward cases"))),
            ui.tags.tbody(*rows),
            class_="delta-table",
        ),
        class_="delta-table-wrap",
    )


def home_best_cards() -> ui.Tag:
    winners = winning_rows()
    cards = []
    for row in winners.itertuples():
        cards.append(
            ui.input_action_button(
                f"home_function_{int(row.function)}",
                ui.TagList(
                    ui.span(f"F{int(row.function)}", class_="best-function"),
                    ui.strong(format_number(row.output)),
                    ui.tags.small(f"Best after 13 weeks  |  Week {int(row.week)}"),
                ),
                class_="home-best-card",
                style=f"--accent:{PASTELS[int(row.function) - 1]}",
            )
        )
    return ui.div(*cards, class_="home-best-grid")


def plot_layout(fig: go.Figure, title: str = "") -> go.Figure:
    fig.update_layout(
        autosize=True,
        title=dict(text=title, x=0.02, xanchor="left", font=dict(size=14, color="#263f5a")),
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(255,255,255,0.68)",
        font=dict(family="Inter, Arial, sans-serif", size=11, color="#425b70"),
        margin=dict(l=36, r=16, t=44, b=32),
        hoverlabel=dict(bgcolor="white", font_size=11),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    )
    fig.update_xaxes(gridcolor="rgba(95,125,145,0.12)", zeroline=False)
    fig.update_yaxes(gridcolor="rgba(95,125,145,0.12)", zeroline=False)
    return fig


app_ui = ui.page_navbar(
    ui.nav_panel(
        "Cover",
        ui.div(
            ui.div(
                ui.div("THE IMPERIAL BBO VISUAL LIBRARY", class_="hero-kicker"),
                ui.tags.blockquote("“Life is a stone. Sculpt yourself a masterpiece.”"),
                ui.p("Dr N T Pisharam  |  Be and Become", class_="gateway-attribution"),
                class_="gateway-quote reveal",
            ),
            ui.div(
                ui.span(ui.strong("BBO"), ui.tags.small("Maximum"), class_="peak-label peak-bbo"),
                ui.span(ui.strong("BBR"), ui.tags.small("Maximum"), class_="peak-label peak-bbr"),
                ui.span(ui.strong("PDHIS"), ui.tags.small("Maximum"), class_="peak-label peak-pdhis"),
                class_="gateway-maxima",
                aria_label="Three maxima: BBO, BBR and PDHIS",
            ),
            ui.div(
                ui.input_action_button(
                    "open_bbo_book",
                    ui.TagList(ui.span("BOOK I", class_="route-kicker"), ui.strong("Imperial BBO Capstone"), ui.tags.small("The official thirteen-week optimisation record")),
                    class_="gateway-book mint-route",
                ),
                ui.input_action_button(
                    "open_above_beyond",
                    ui.TagList(ui.span("BOOKS II AND III", class_="route-kicker"), ui.strong("Above and Beyond BBO"), ui.tags.small("Above: BBR  |  Beyond: PDHIS")),
                    class_="gateway-book lavender-route",
                ),
                class_="gateway-books",
            ),
            class_="book-page gateway-page",
        ),
    ),
    ui.nav_panel(
        "Imperial BBO",
        ui.div(
            page_toolbar("bbo_home", "bbo_up", "bbo_previous", "bbo_next"),
            ui.tags.section(
                ui.div("IMPERIAL COLLEGE LONDON  |  BLACK BOX OPTIMISATION", class_="hero-kicker"),
                ui.h1("Thirteen weeks. Eight hidden functions."),
                ui.p("A visual book of 104 decisions, their returned results and the analytical methods used to decide what came next."),
                ui.div(ui.span("279 recorded observations"), ui.span("104 participant queries"), ui.span("2 to 8 dimensions"), ui.span("13 rounds"), class_="hero-tags"),
                class_="hero reveal",
            ),
            ui.div(
                stat_box("Functions", "8", "Each maximised independently", PASTELS[0]),
                stat_box("Weekly queries", "104", "One per function per round", PASTELS[1]),
                stat_box("Starter evidence", "175", "Course-supplied observations", PASTELS[2]),
                stat_box("Final dataset", "279", "Audited canonical rows", PASTELS[3]),
                class_="stat-grid",
            ),
            ui.div(ui.h2("Best values retained after thirteen weeks"), ui.p("Select a function to open its complete evidence page."), class_="home-best-heading"),
            home_best_cards(),
            ui.div(
                ui.input_action_button("open_readme", "Project overview", class_="route-button mint-route"),
                ui.input_action_button("open_weeks", "Week 1 to Week 13", class_="route-button blue-route"),
                ui.input_action_button("open_functions", "Function F1 to F8", class_="route-button lavender-route"),
                ui.input_action_button("open_atlas", "Scientific Atlas", class_="route-button peach-route"),
                ui.input_action_button("open_repository", "Repository", class_="route-button mint-route"),
                class_="home-route-grid",
            ),
            class_="book-page cover-page",
        ),
    ),
    ui.nav_panel(
        "README",
        ui.div(
            page_toolbar("readme_home", "readme_up", "readme_previous", "readme_next"),
            book_heading("PROJECT OVERVIEW", "Black Box Optimisation Capstone", "A concise guide to the challenge, the evidence and the reproducible analytical record."),
            ui.div(
                ui.div(ui.h2("The challenge"), ui.p("Eight hidden functions, ranging from two to eight dimensions, were optimised over thirteen weekly rounds. The course supplied 175 starter observations. We then submitted one new input per function each week and received the corresponding black-box output through the portal."), class_="reading-panel"),
                ui.div(ui.h2("The record"), ui.p("The repository preserves 279 observations, including 104 weekly participant queries. It documents the movement from broad exploration to function-specific optimisation, validation, repeat testing and final evaluation."), class_="reading-panel"),
                ui.div(ui.h2("How to read"), ui.p("Use Week by Week for the chronological campaign, Function by Function for all thirteen results from one function, Scientific Atlas for comparison, and Resolution for BBR and the earlier Delta prediction framework."), class_="reading-panel"),
                class_="readme-grid",
            ),
            class_="book-page",
        ),
    ),
    ui.nav_panel(
        "Read by Week",
        ui.div(
            page_toolbar("week_home", "week_up", "previous_week", "next_week"),
            book_heading("BOOK I  |  CHRONOLOGICAL READING", "The thirteen-round story", "Move through the campaign one round at a time. Each chapter combines the submitted evidence with the documented purpose of that stage."),
            numbered_buttons("choose_week", range(1, 14), "W"),
            ui.input_slider("week", None, 1, 13, 1, step=1),
            ui.div(
                ui.output_ui("week_chapter"),
                ui.div(
                    ui.input_radio_buttons("week_view", None, {"outputs": "Outputs and retained best", "movement": "Coordinate movement"}, selected="outputs", inline=True),
                    ui.input_switch("week_cumulative", "Cumulative best", True),
                    class_="view-switcher",
                ),
                ui.div(
                    ui.h2("View the selected Week graph"),
                    ui.p("Open the graph in a separate full-screen viewer. Close it to return to this Week without losing your place."),
                    graph_actions("open_week_graph", "explain_week_graph"),
                    class_="graph-launch-panel",
                ),
                class_="evidence-spread compact-page-body",
            ),
            class_="book-page",
        ),
    ),
    ui.nav_panel(
        "Read by Function",
        ui.div(
            page_toolbar("function_home", "function_up", "previous_function", "next_function"),
            book_heading("BOOK II  |  FUNCTION READING", "Eight distinct optimisation stories", "Select a function to examine its trajectory, winning week, coordinate movement and complete evidence record."),
            numbered_buttons("choose_function", range(1, 9), "F"),
            ui.input_select("function", None, {str(i): f"F{i}" for i in DIMENSIONS}, selected="1"),
            ui.div(
                ui.div(ui.output_ui("function_summary"), class_="summary-slot"),
                ui.div(
                    ui.input_radio_buttons("function_view", None, {"output": "Output and rate of change", "coordinates": "Coordinate movement", "record": "Thirteen-week record"}, selected="output", inline=True),
                    ui.input_switch("show_best", "Cumulative best", True),
                    ui.input_switch("show_starter", "Starter points", False),
                    class_="view-switcher",
                ),
                ui.panel_conditional(
                    "input.function_view !== 'record'",
                    ui.div(
                        ui.h2("View the selected Function graph"),
                        ui.p("Open the graph in a separate full-screen viewer. Close it to return to this Function without losing your place."),
                        graph_actions("open_function_graph", "explain_function_graph"),
                        class_="graph-launch-panel",
                    ),
                ),
                ui.panel_conditional("input.function_view === 'record'", ui.card(ui.output_data_frame("function_table"), class_="table-page")),
                class_="evidence-spread compact-page-body",
            ),
            class_="book-page",
        ),
    ),
    ui.nav_panel(
        "Scientific Atlas",
        ui.div(
            page_toolbar("atlas_home", "atlas_up", "atlas_previous", "atlas_next"),
            book_heading("BOOK III  |  SCIENTIFIC ATLAS", "Compare the complete optimisation landscape", "The atlas scales unlike outputs for fair visual comparison while retaining the original values in hover labels and tables."),
            ui.div(
                ui.input_select("atlas_measure", "Comparison measure", {"relative": "Within-function relative progress", "raw": "Original returned output"}, selected="relative"),
                ui.input_select("atlas_view", "Atlas view", {"weekly": "Weekly trajectories", "heatmap": "Function by week heat map", "winners": "Winning week and result"}, selected="weekly"),
                class_="inline-controls",
            ),
            ui.div(
                ui.div(
                    ui.h2("Open the selected Atlas graph"),
                    ui.p("The comparison opens in a full-screen viewer and closes back to this page."),
                    graph_actions("open_atlas_graph", "explain_atlas_graph"),
                    class_="graph-launch-panel",
                ),
                ui.div(
                        stat_box("First winning week", str(int(winning_rows().week.min())), "Earliest retained maximum", PASTELS[4]),
                        stat_box("Last winning week", str(int(winning_rows().week.max())), "Latest retained maximum", PASTELS[5]),
                        stat_box("Functions peaking in Week 13", str(int((winning_rows().week == 13).sum())), "Final-round maxima", PASTELS[6]),
                        stat_box("Observed dimensions", "2 to 8", "Heterogeneous search spaces", PASTELS[7]),
                        class_="atlas-stats",
                ),
                class_="atlas-spread",
            ),
            class_="book-page",
        ),
    ),
    ui.nav_panel(
        "Executive Summary",
        ui.div(
            page_toolbar("executive_home", "executive_up", "executive_previous", "executive_next"),
            book_heading("EXECUTIVE READING", "Executive Summary", "Read the complete project account while listening to the matching three-part narration."),
            ui.div(
                ui.h2("Executive Summary: read and listen"),
                ui.p("Select HEAR ME above to play the complete three-part narration. The written Executive Summary appears below in the same order, so you can read and listen on this page."),
                ui.markdown(EXECUTIVE_SUMMARY_TEXT),
                class_="reading-panel executive-summary-reading",
            ),
            class_="book-page",
        ),
    ),
    ui.nav_panel(
        "Repository",
        ui.div(
            page_toolbar("repository_home", "repository_up", "repository_previous", "repository_next"),
            book_heading("REPRODUCIBLE RECORD", "Repository and live Visual Book", "The live book explains the results. The repository preserves the evidence, calculations and source code behind them."),
            ui.div(
                ui.div(
                    ui.h2("GitHub README"),
                    ui.p("Use the README as the contents page for the assessment record, weekly evidence, reproducibility guidance and later research."),
                    ui.a("Read the GitHub README", href="https://github.com/tpnandakumar/Imperial_BBO_Capstone#readme", target="_blank", class_="external-button"),
                    class_="reading-panel",
                ),
                ui.div(
                    ui.h2("Full repository"),
                    ui.p("Inspect the permanent record of 279 observations, weekly analyses, notebooks, figures, final submission and Visual Book source."),
                    ui.a("Open Imperial BBO Capstone on GitHub", href="https://github.com/tpnandakumar/Imperial_BBO_Capstone", target="_blank", class_="external-button"),
                    class_="reading-panel",
                ),
                ui.div(
                    ui.h2("PDHIS mathematical model"),
                    ui.p("Read the formal definitions for recursive Delta, oscillation, energy, temporal dispersion, coherence, event locking and prospective targets."),
                    ui.a("Read the PDHIS Mathematical Model", href="https://github.com/tpnandakumar/Imperial_BBO_Capstone/blob/main/Post_BBO_BBR/PDHIS/PDHIS_MATHEMATICAL_MODEL.md", target="_blank", class_="external-button"),
                    class_="reading-panel",
                ),
                ui.div(
                    ui.h2("BBR models for F1 to F8"),
                    ui.p("Read the complete Black Box Resolution method, positive and negative findings, model-family equations and function-by-function interpretation."),
                    ui.a("Read the BBR Mathematical Models", href="https://github.com/tpnandakumar/Imperial_BBO_Capstone/blob/main/Post_BBO_BBR/BBR_MATHEMATICAL_MODELS_F1_TO_F8.md", target="_blank", class_="external-button"),
                    class_="reading-panel",
                ),
                ui.div(
                    ui.h2("PDHIS identification contribution"),
                    ui.p("See what PDHIS identifies across F1 to F8 and how the validation boundary guides the next research stage."),
                    ui.a("Read the Identification Contribution", href="https://github.com/tpnandakumar/Imperial_BBO_Capstone/blob/main/Post_BBO_BBR/PDHIS/PDHIS_IDENTIFICATION_CONTRIBUTION.md", target="_blank", class_="external-button"),
                    class_="reading-panel",
                ),
                class_="repository-grid",
            ),
            class_="book-page",
        ),
    ),
    ui.nav_panel(
        "Above and Beyond",
        ui.div(
            page_toolbar("above_home", "above_up", "above_previous", "above_next"),
            book_heading("THE POST-CHALLENGE LIBRARY", "Above and Beyond BBO", "Choose Above for Black Box Resolution (BBR), or Beyond for Pisharam Delta Hierarchy and Influence State (PDHIS)."),
            ui.div(
                ui.input_action_button(
                    "open_above_bbr",
                    ui.TagList(ui.span("ABOVE BBO", class_="route-kicker"), ui.strong("BBR: Black Box Resolution"), ui.tags.small("Resolve hidden structure through competing explanations, chronological tests and falsification")),
                    class_="gateway-book rose-route",
                ),
                ui.input_action_button(
                    "open_beyond_pdhis",
                    ui.TagList(ui.span("BEYOND BBO", class_="route-kicker"), ui.strong("PDHIS: Pisharam Delta Hierarchy and Influence State"), ui.tags.small("Study Delta 1 to Delta 10, trajectory, predictability and the limits of the evidence")),
                    class_="gateway-book lavender-route",
                ),
                class_="gateway-books post-bbo-gateway",
            ),
            class_="book-page gateway-page",
        ),
    ),
    ui.nav_panel(
        "Resolution",
        ui.div(
            page_toolbar("resolution_home", "resolution_up", "resolution_previous", "resolution_next"),
            book_heading("BOOK IV  |  RESOLUTION", "BBR: Black Box Resolution", "Investigate hidden structure by comparing explanations, testing them chronologically and rejecting those that fail."),
            ui.div(
                ui.input_radio_buttons(
                    "resolution_section", None,
                    {"overview": "Resolution home", "bbr": "BBR method"},
                    selected="bbr", inline=True,
                ),
                class_="resolution-index",
            ),
            ui.panel_conditional(
                "input.resolution_section === 'overview'",
                ui.div(
                    ui.input_action_button(
                        "open_resolution_bbr",
                        ui.TagList(ui.span("BBR", class_="route-kicker"), ui.strong("Black Box Resolution"),
                                   ui.tags.small("Competing explanations, chronological testing and rejection of failed models")),
                        class_="resolution-route mint-route",
                    ),
                    class_="resolution-route-grid",
                ),
            ),
            ui.panel_conditional(
                "input.resolution_section === 'bbr'",
                ui.div(
                    ui.div(
                        ui.div(ui.span("01"), ui.strong("Evaluate"), ui.p("Judge the returned evidence")),
                        ui.div(ui.span("02"), ui.strong("Resolve"), ui.p("Clarify what is known and uncertain")),
                        ui.div(ui.span("03"), ui.strong("Explore  ↔  Exploit"), ui.p("Choose information or refinement")),
                        ui.div(ui.span("04"), ui.strong("Extend"), ui.p("Widen the next question")),
                        ui.div(ui.span("05"), ui.strong("Optimise"), ui.p("Select the next coordinate")),
                        ui.div(ui.span("06"), ui.strong("Evolve"), ui.p("Adapt the method")),
                        ui.div(ui.span("07"), ui.strong("Experiment"), ui.p("Run the next reproducible test")),
                        class_="strategy-loop reveal",
                    ),
                    ui.p("Evaluate → Resolve → Explore ↔ Exploit → Extend → Optimise → Evolve → Experiment → Evaluate, then repeat.", class_="strategy-loop-caption"),
                    ui.input_action_button("explain_bbr", "What does BBR mean?", class_="btn-soft framework-explain-button"),
                    ui.div(
                        ui.a(
                            "BBR values and results",
                            href="https://github.com/tpnandakumar/Imperial_BBO_Capstone/blob/main/Post_BBO_BBR/infographics/BBR_EVIDENCE_VALUES.csv",
                            target="_blank",
                            class_="external-button bbr-values-link",
                        ),
                        ui.a(
                            "BBR equations for F1 to F8",
                            href="https://github.com/tpnandakumar/Imperial_BBO_Capstone/blob/main/Post_BBO_BBR/BBR_MATHEMATICAL_MODELS_F1_TO_F8.md",
                            target="_blank",
                            class_="external-button bbr-equations-link",
                        ),
                        ui.a(
                            "Complete BBR evidence library",
                            href="https://github.com/tpnandakumar/Imperial_BBO_Capstone/tree/main/Post_BBO_BBR",
                            target="_blank",
                            class_="external-button bbr-library-link",
                        ),
                        class_="bbr-resource-links",
                    ),
                    ui.div(
                        ui.div(
                            ui.h2("Black Box Resolution"),
                            ui.p("A structured investigation of a hidden function using recorded inputs and outputs. It compares explanations, tests chronological performance and rejects explanations that fail."),
                            ui.p("BBR may identify a best-supported local structure without claiming recovery of the original hidden equation or its global optimum."),
                            class_="reading-panel reveal compact-reading",
                        ),
                        ui.div(
                            ui.card(ui.card_header("Exploration"), ui.p("Broader movement purchased information about untested regions but risked leaving a strong local area."), class_="pastel-card mint"),
                            ui.card(ui.card_header("Exploitation"), ui.p("Smaller movement refined supported regions but could miss a separate and better optimum."), class_="pastel-card blue"),
                            ui.card(ui.card_header("Confirmation"), ui.p("Repeated coordinates tested stability, although every repeat consumed a scarce weekly evaluation."), class_="pastel-card lavender"),
                            class_="three-column",
                        ),
                        class_="bbr-evidence",
                    ),
                    class_="bbr-spread resolution-body",
                ),
            ),
            class_="book-page",
        ),
    ),
    ui.nav_panel(
        "Beyond BBO",
        ui.div(
            page_toolbar("pdhis_home", "pdhis_up", "pdhis_previous", "pdhis_next"),
            book_heading("BOOK V  |  BEYOND BBO", "PDHIS: Pisharam Delta Hierarchy and Influence State", "Delta of BBO examines recursively nested change across F1 to F8 and asks whether an early pattern carries information about later direction or trajectory."),
            ui.div(
                ui.input_radio_buttons(
                    "pdhis_view", None,
                    {"overview": "Delta home", "meanings": "Delta meanings", "hierarchy": "Lotus hierarchy", "trajectory": "Delta trajectory", "orders": "Predictability", "functions": "F1 to F8", "evidence": "Evidence boundary", "model": "Mathematical model", "advanced": "Advanced model", "flicker": "Flicker study", "atlas": "Matched atlas"},
                    selected="overview", inline=True,
                ),
                class_="resolution-index pdhis-page-index",
            ),
            ui.panel_conditional(
                "input.pdhis_view === 'overview'",
                ui.div(
                    ui.div(
                        ui.strong("Delta: the Signature of Change"),
                        ui.span("The Power of Change describes how behaviour develops across successive Delta levels. PDHIS looks for the earliest clear signature in its shape, persistence and direction, then tests whether that earlier signature can predict the later behaviour. The later behaviour is the target."),
                        class_="pdhis-rationale",
                    ),
                    ui.div(
                        stat_box("Delta hierarchy", "Δ1 to Δ10", "Calculated for F1 to F8", PASTELS[0]),
                        stat_box("Weekly evidence", "104", "Thirteen outputs per function", PASTELS[1]),
                        stat_box("Strongest candidates", "Δ2, Δ4, Δ5", "Inverse next-change relationships", PASTELS[2]),
                        stat_box("Confirmed orders", "0", "None reached FDR q below 0.05", PASTELS[4]),
                        class_="stat-grid compact pdhis-stats",
                    ),
                    ui.div(
                        *[
                            ui.input_action_button(f"open_pdhis_{key}", label, class_=f"resolution-route {colour}")
                            for key, label, colour in [
                                ("meanings", "Delta 1 to Delta 10: meaning table", "mint-route"),
                                ("hierarchy", "Lotus hierarchy: nested change", "blue-route"),
                                ("trajectory", "Delta trajectory: function and order", "lavender-route"),
                                ("orders", "Predictability: chronological tests", "peach-route"),
                                ("functions", "F1 to F8: relationship map", "rose-route"),
                                ("evidence", "Evidence boundary: what remains", "mint-route"),
                                ("model", "PDHIS mathematical model", "rose-route"),
                                ("advanced", "Advanced model: next-week improvement", "blue-route"),
                                ("flicker", "Event-locked flicker characterisation", "lavender-route"),
                                ("atlas", "Matched event atlas and stability", "peach-route"),
                            ]
                        ],
                        class_="pdhis-route-grid",
                    ),
                    class_="resolution-body pdhis-home-page",
                ),
            ),
            ui.panel_conditional(
                "input.pdhis_view !== 'overview'",
                ui.div(
                    ui.panel_conditional(
                        "input.pdhis_view === 'trajectory'",
                        ui.div(
                            ui.input_select("pdhis_function", "Function", {str(i): f"F{i}" for i in DIMENSIONS}, selected="1"),
                            ui.input_select("pdhis_order", "Delta level", {str(i): f"Delta {i}" for i in range(1, 11)}, selected="1"),
                            class_="inline-controls pdhis-trajectory-controls",
                        ),
                    ),
                    ui.panel_conditional(
                        "input.pdhis_view === 'meanings'",
                        ui.div(
                            delta_meanings_table(),
                            ui.div(
                                ui.input_select("delta_explain_level", "Explain a Delta level", {str(i): f"Delta {i}" for i in range(1, 11)}, selected="1"),
                                ui.input_action_button("explain_delta_level", "Open explanation", class_="btn-accent"),
                                class_="delta-explain-controls",
                            ),
                            class_="delta-meanings-page",
                        ),
                    ),
                    ui.panel_conditional(
                        "input.pdhis_view !== 'meanings'",
                        ui.div(
                            ui.h2(ui.output_text("pdhis_chart_title")),
                            ui.p("Open the graph in a centred viewer. Close it to return to this PDHIS page."),
                            graph_actions("open_pdhis_graph", "explain_pdhis_graph"),
                            class_="graph-launch-panel pdhis-graph-launch",
                        ),
                    ),
                    ui.div(ui.output_text("pdhis_interpretation"), class_="pdhis-note"),
                    class_="resolution-body pdhis-body",
                ),
            ),
            class_="book-page",
        ),
    ),
    ui.nav_panel(
        "Evidence",
        ui.div(
            page_toolbar("evidence_home", "evidence_up", "evidence_previous", "evidence_next"),
            book_heading("APPENDIX  |  VERIFIED EVIDENCE", "The complete participant-query record", "Filter all 104 weekly evaluations. The table is generated directly from the canonical 279-observation dataset."),
            ui.div(
                ui.input_select("evidence_function", "Function", {"all": "All functions", **{str(i): f"F{i}" for i in DIMENSIONS}}, selected="all"),
                ui.input_slider("evidence_weeks", "Week range", 1, 13, [1, 13], step=1),
                class_="inline-controls",
            ),
            ui.div(
                ui.output_ui("evidence_table"),
                ui.div(
                    ui.input_action_button("evidence_page_previous", "Previous rows", class_="btn-soft"),
                    ui.output_text("evidence_page_label"),
                    ui.input_action_button("evidence_page_next", "Next rows", class_="btn-accent"),
                    class_="evidence-pager",
                ),
                class_="evidence-card evidence-page-card",
            ),
            class_="book-page",
        ),
    ),
    ui.nav_control(
        ui.div(
            ui.tags.button("HEAR ME", id="hear_me", type="button", class_="btn hear-me-button", aria_label="Play natural narration for this section", title="Play natural narration for this section"),
            ui.tags.button("STOP", id="hear_stop", type="button", class_="btn hear-stop-button", aria_label="Stop narration", title="Stop narration"),
            ui.tags.span("", id="hear_me_status", class_="visually-hidden", aria_live="polite"),
            class_="hear-me-controls",
        )
    ),
    ui.nav_control(ui.input_action_button("global_home", "Home", class_="nav-home-button")),
    title=ui.div(ui.span("◈", class_="brand-mark"), ui.span("Imperial BBO Visual Book")),
    id="main_navigation", selected="Cover",
    navbar_options=ui.navbar_options(position="sticky-top", underline=False, collapsible=True),
    header=ui.tags.head(
        ui.tags.meta(name="description", content="Interactive visual book and scientific dashboard for the Imperial BBO capstone."),
        ui.include_css(APP_DIR / "www" / "styles.css"),
        ui.tags.style(f':root {{ --gateway-art: url("{GATEWAY_ART}"); }}'),
        ui.include_js(APP_DIR / "www" / "narration-player.js"),
    ),
    footer=ui.div("Official Week 1 to Week 13 evidence  |  279 observations  |  Reproducible Python application", class_="book-footer"),
    window_title="Imperial BBO Visual Book",
)


def server(input: Inputs, output: Outputs, session: Session) -> None:
    evidence_page = reactive.Value(0)

    @reactive.effect
    @reactive.event(input.global_home, input.bbo_home, input.above_home, input.week_home, input.function_home,
                    input.readme_home, input.executive_home, input.repository_home, input.atlas_home, input.resolution_home,
                    input.pdhis_home, input.evidence_home)
    def _go_home():
        ui.update_navs("main_navigation", selected="Cover")

    @reactive.effect
    @reactive.event(input.open_bbo_book)
    def _open_bbo_book(): ui.update_navs("main_navigation", selected="Imperial BBO")

    @reactive.effect
    @reactive.event(input.open_above_beyond)
    def _open_above_beyond(): ui.update_navs("main_navigation", selected="Above and Beyond")

    @reactive.effect
    @reactive.event(input.open_above_bbr)
    def _open_above_bbr():
        ui.update_radio_buttons("resolution_section", selected="bbr")
        ui.update_navs("main_navigation", selected="Resolution")

    @reactive.effect
    @reactive.event(input.open_beyond_pdhis)
    def _open_beyond_pdhis():
        ui.update_radio_buttons("pdhis_view", selected="overview")
        ui.update_navs("main_navigation", selected="Beyond BBO")

    @reactive.effect
    @reactive.event(input.open_readme)
    def _open_readme(): ui.update_navs("main_navigation", selected="README")

    @reactive.effect
    @reactive.event(input.open_weeks)
    def _open_weeks(): ui.update_navs("main_navigation", selected="Read by Week")

    @reactive.effect
    @reactive.event(input.open_functions)
    def _open_functions(): ui.update_navs("main_navigation", selected="Read by Function")

    @reactive.effect
    @reactive.event(input.open_atlas)
    def _open_atlas(): ui.update_navs("main_navigation", selected="Scientific Atlas")

    @reactive.effect
    @reactive.event(input.open_resolution)
    def _open_resolution():
        ui.update_radio_buttons("resolution_section", selected="bbr")
        ui.update_navs("main_navigation", selected="Resolution")

    @reactive.effect
    @reactive.event(input.open_pdhis)
    def _open_pdhis():
        ui.update_radio_buttons("pdhis_view", selected="overview")
        ui.update_navs("main_navigation", selected="Beyond BBO")

    @reactive.effect
    @reactive.event(input.open_resolution_bbr)
    def _open_resolution_bbr(): ui.update_radio_buttons("resolution_section", selected="bbr")

    @reactive.effect
    @reactive.event(input.open_repository)
    def _open_repository(): ui.update_navs("main_navigation", selected="Repository")

    @reactive.effect
    @reactive.event(input.deep_link_page)
    def _open_deep_link():
        if input.deep_link_page() == "executive-summary":
            ui.update_navs("main_navigation", selected="Executive Summary")
        elif input.deep_link_page() == "bbr":
            ui.update_navs("main_navigation", selected="Resolution")
            ui.update_radio_buttons("resolution_section", selected="bbr")

    @reactive.effect
    @reactive.event(input.bbo_up, input.bbo_previous, input.above_up, input.above_previous)
    def _gateway_up(): ui.update_navs("main_navigation", selected="Cover")

    @reactive.effect
    @reactive.event(input.bbo_next)
    def _bbo_next(): ui.update_navs("main_navigation", selected="README")

    @reactive.effect
    @reactive.event(input.readme_up, input.readme_previous, input.week_up, input.function_up,
                    input.atlas_up, input.evidence_up, input.executive_up, input.repository_up, input.repository_next)
    def _official_up(): ui.update_navs("main_navigation", selected="Imperial BBO")

    @reactive.effect
    @reactive.event(input.above_next)
    def _above_next():
        ui.update_radio_buttons("resolution_section", selected="bbr")
        ui.update_navs("main_navigation", selected="Resolution")

    @reactive.effect
    @reactive.event(input.resolution_up)
    def _resolution_up():
        ui.update_navs("main_navigation", selected="Above and Beyond")

    @reactive.effect
    @reactive.event(input.pdhis_up)
    def _pdhis_up():
        if input.pdhis_view() == "overview":
            ui.update_navs("main_navigation", selected="Above and Beyond")
        else:
            ui.update_radio_buttons("pdhis_view", selected="overview")

    @reactive.effect
    @reactive.event(input.readme_next)
    def _readme_next(): ui.update_navs("main_navigation", selected="Read by Week")

    @reactive.effect
    @reactive.event(input.atlas_previous)
    def _atlas_previous(): ui.update_navs("main_navigation", selected="Read by Function")

    @reactive.effect
    @reactive.event(input.atlas_next)
    def _atlas_next():
        ui.update_radio_buttons("resolution_section", selected="bbr")
        ui.update_navs("main_navigation", selected="Resolution")

    @reactive.effect
    @reactive.event(input.resolution_previous)
    def _resolution_previous():
        ui.update_navs("main_navigation", selected="Above and Beyond")

    @reactive.effect
    @reactive.event(input.resolution_next)
    def _resolution_next():
        ui.update_radio_buttons("pdhis_view", selected="overview")
        ui.update_navs("main_navigation", selected="Beyond BBO")

    pdhis_pages = ["overview", "meanings", "hierarchy", "trajectory", "orders", "functions", "evidence", "model", "advanced", "flicker", "atlas"]

    for page in pdhis_pages[1:]:
        @reactive.effect
        @reactive.event(input[f"open_pdhis_{page}"])
        def _open_pdhis_page(page=page):
            ui.update_radio_buttons("pdhis_view", selected=page)

    @reactive.effect
    @reactive.event(input.pdhis_previous)
    def _pdhis_previous():
        current = input.pdhis_view()
        index = pdhis_pages.index(current)
        if index == 0:
            ui.update_navs("main_navigation", selected="Above and Beyond")
        else:
            ui.update_radio_buttons("pdhis_view", selected=pdhis_pages[index - 1])

    @reactive.effect
    @reactive.event(input.pdhis_next)
    def _pdhis_next():
        current = input.pdhis_view()
        index = pdhis_pages.index(current)
        if index == len(pdhis_pages) - 1:
            ui.update_navs("main_navigation", selected="Evidence")
        else:
            ui.update_radio_buttons("pdhis_view", selected=pdhis_pages[index + 1])

    @reactive.effect
    @reactive.event(input.evidence_previous)
    def _evidence_previous():
        ui.update_radio_buttons("pdhis_view", selected="evidence")
        ui.update_navs("main_navigation", selected="Beyond BBO")

    @reactive.effect
    @reactive.event(input.evidence_next)
    def _evidence_next(): ui.update_navs("main_navigation", selected="Executive Summary")

    @reactive.effect
    @reactive.event(input.executive_previous)
    def _executive_previous(): ui.update_navs("main_navigation", selected="Evidence")

    @reactive.effect
    @reactive.event(input.executive_next)
    def _executive_next(): ui.update_navs("main_navigation", selected="Repository")

    @reactive.effect
    @reactive.event(input.repository_previous)
    def _repository_previous(): ui.update_navs("main_navigation", selected="Executive Summary")

    for value in range(1, 14):
        @reactive.effect
        @reactive.event(input[f"choose_week_{value}"])
        def _choose_week(value=value):
            ui.update_slider("week", value=value)

    for value in range(1, 9):
        @reactive.effect
        @reactive.event(input[f"choose_function_{value}"])
        def _choose_function(value=value):
            ui.update_select("function", selected=str(value))

    for value in range(1, 9):
        @reactive.effect
        @reactive.event(input[f"home_function_{value}"])
        def _open_home_function(value=value):
            ui.update_select("function", selected=str(value))
            ui.update_navs("main_navigation", selected="Read by Function")

    @reactive.effect
    @reactive.event(input.open_week_graph)
    def _open_week_graph():
        output_id = "week_movement_plot" if input.week_view() == "movement" else "week_rank_plot"
        title = f"Week {int(input.week())}: " + ("coordinate movement" if input.week_view() == "movement" else "outputs and retained best")
        ui.modal_show(
            ui.modal(
                ui.div(output_widget(output_id, height="clamp(300px, 56dvh, 600px)"), class_="graph-modal-stage"),
                title=title,
                size="xl",
                easy_close=True,
                footer=ui.modal_button("Close graph", class_="btn-accent"),
                class_="graph-viewer-modal",
            )
        )

    @reactive.effect
    @reactive.event(input.open_function_graph)
    def _open_function_graph():
        coordinate_view = input.function_view() == "coordinates"
        output_id = "coordinate_trajectory" if coordinate_view else "function_trajectory"
        title = f"F{int(input.function())}: " + ("coordinate movement" if coordinate_view else "output and rate of change")
        ui.modal_show(
            ui.modal(
                ui.div(output_widget(output_id, height="clamp(300px, 56dvh, 600px)"), class_="graph-modal-stage"),
                title=title,
                size="xl",
                easy_close=True,
                footer=ui.modal_button("Close graph", class_="btn-accent"),
                class_="graph-viewer-modal",
            )
        )

    @reactive.effect
    @reactive.event(input.open_atlas_graph)
    def _open_atlas_graph():
        view = input.atlas_view()
        output_id = f"atlas_{view}_plot"
        ui.modal_show(
            ui.modal(
                ui.div(output_widget(output_id, height="clamp(300px, 56dvh, 600px)"), class_="graph-modal-stage"),
                title="Scientific Atlas",
                size="xl",
                easy_close=True,
                footer=ui.modal_button("Close graph", class_="btn-accent"),
                class_="graph-viewer-modal",
            )
        )

    @reactive.effect
    @reactive.event(input.open_pdhis_graph)
    def _open_pdhis_graph():
        view = input.pdhis_view()
        if view not in PDHIS_EXPLANATIONS:
            return
        output_id = f"pdhis_{view}_plot"
        title = PDHIS_EXPLANATIONS[view][0]
        if view == "trajectory":
            title = f"F{int(input.pdhis_function())}, Delta {int(input.pdhis_order())} trajectory"
        ui.modal_show(
            ui.modal(
                ui.div(output_widget(output_id, height="clamp(300px, 56dvh, 600px)"), class_="graph-modal-stage"),
                title=title,
                size="xl",
                easy_close=True,
                footer=ui.modal_button("Close graph", class_="btn-accent"),
                class_="graph-viewer-modal",
            )
        )

    @reactive.effect
    @reactive.event(input.explain_week_graph)
    def _explain_week_graph():
        movement = input.week_view() == "movement"
        if movement:
            dialog = explanation_dialog(
                "How to read the Week coordinate graph",
                "Each line shows how one input coordinate changed for F1 to F8 in the selected week.",
                ["Large movement indicates exploration of a different region.", "Small movement indicates exploitation or local refinement.", "A move is evidence of the chosen strategy, not proof that the strategy improved the output."],
            )
        else:
            dialog = explanation_dialog(
                "How to read the Week output graph",
                "The graph compares the eight returned outputs in the selected week with the best values retained so far.",
                ["Each function has its own scale, so compare change within a function rather than raw height across functions.", "A new retained best marks improvement for that function.", "Repeated best values indicate confirmation or a plateau, depending on the submitted coordinate."],
            )
        ui.modal_show(dialog)

    @reactive.effect
    @reactive.event(input.explain_function_graph)
    def _explain_function_graph():
        coordinate_view = input.function_view() == "coordinates"
        if coordinate_view:
            dialog = explanation_dialog(
                f"How to read the F{int(input.function())} coordinate graph",
                "Each coloured line is one input coordinate across thirteen weekly submissions.",
                ["Broad movement indicates exploration.", "Small directed movement indicates exploitation or refinement.", "A flat coordinate means that dimension was retained while other dimensions changed."],
            )
        else:
            dialog = explanation_dialog(
                f"How to read the F{int(input.function())} output graph",
                "The weekly line shows returned output; the cumulative-best line keeps only the strongest result observed up to each week.",
                ["An upward step in cumulative best is a new improvement.", "A flat cumulative-best line means no later query beat the retained result.", "Rate of change shows week-to-week movement and may be volatile even when the retained best is stable."],
            )
        ui.modal_show(dialog)

    @reactive.effect
    @reactive.event(input.explain_atlas_graph)
    def _explain_atlas_graph():
        ui.modal_show(explanation_dialog(
            "How to read the Scientific Atlas",
            "The Atlas compares all eight functions without pretending that their raw output scales are directly comparable.",
            ["Relative progress rescales each function only against its own observed range.", "The heat map highlights timing and direction, not absolute magnitude between functions.", "The winning-week view shows when each retained participant-query maximum first or last appeared."],
        ))

    @reactive.effect
    @reactive.event(input.explain_pdhis_graph)
    def _explain_pdhis_graph():
        view = input.pdhis_view()
        title, summary = PDHIS_EXPLANATIONS.get(view, ("PDHIS graph", "This graph describes recursively nested change in the completed BBO record."))
        if view == "trajectory":
            order = int(input.pdhis_order())
            title = f"How to read F{int(input.pdhis_function())}, Delta {order}"
            comparison = (
                "Read Delta 1 beside the normalised output history because it is the direct change between consecutive weeks."
                if order == 1 else
                f"Read Delta {order} beside Delta {order - 1} and the lower levels to check whether the same interpretation continues through the hierarchy."
            )
            points = [
                comparison,
                "Crossing zero marks a change of direction at the selected level. Movement towards zero may indicate flattening, while alternating signs may indicate oscillation.",
                "Check whether the pattern persists across several observations before relating it to what happens next.",
            ]
        else:
            points = {
                "hierarchy": [
                    "Begin with direct change at Delta 1 and move outwards. Each ring shows how the preceding level changed.",
                    "Agreement across neighbouring levels gives a pattern more weight than a strong movement in one outer ring.",
                    "The number of usable comparisons falls at every level, so the outer rings require greater caution.",
                ],
                "orders": [
                    "The green line relates each Delta order to the following change. The purple line relates it to the following output.",
                    "The gold shuffled range shows relationships that can appear when chronological order is disrupted. Values outside it deserve closer examination.",
                    "Delta 2, Delta 4 and Delta 5 have the strongest inverse relationships here, but none passes the adjusted confirmation threshold.",
                ],
                "functions": [
                    "Blue cells show negative relationships with the following change, rose cells show positive relationships and pale cells show little observed relationship.",
                    "Each cell reports n, the number of usable comparisons. A smaller n means greater uncertainty.",
                    "A run of similar colour across neighbouring Delta orders is more informative than one isolated cell.",
                ],
                "evidence": [
                    "The green bars show how many forward comparisons remain at each Delta order. The count falls from 88 at Delta 1 to 16 at Delta 10.",
                    "The purple line shows adjusted evidence as minus log10(q). The dashed line marks the q equals 0.05 threshold.",
                    "No order crosses that threshold, so the present patterns remain research findings rather than a validated forecasting rule.",
                ],
                "advanced": [
                    "The full Delta signature combines Delta 1 to Delta 5 with persistence, sign change and agreement across levels.",
                    "The earlier signature is the predictor. Improvement in the following week is the target behaviour.",
                    "Held-out-function balanced accuracy was 0.624. Expanding-week balanced accuracy was lower at 0.563, showing that chronological transfer remains difficult.",
                    "The permutation result was 0.0297, but chronological probability calibration did not beat the baseline. Prospective validation is still required.",
                    "A separate higher-order test found that Delta 9 oscillated in 15 of 16 eligible cases. Positive Delta 3 followed in 6 of those 15, with exact p equal to 0.438, so Delta 9 oscillation did not predict positive Delta 3 in this record.",
                ],
                "flicker": [
                    "Each of the 56 windows contains the six observations immediately before a target week. The later event never enters the flicker calculation.",
                    "The targets comprise 29 improvements, 6 large function-adjusted changes and 11 new best outputs.",
                    "Longer peak spacing was the strongest candidate before new best outputs: 4.00 compared with 2.02 in other windows.",
                    "Its exploratory p value was 0.034, but the adjusted value was 0.305. The characteristic is therefore a research pointer, not confirmed evidence.",
                    "Weekly sampling is too sparse for a conventional frequency spectrum, so sign-change rate and peak spacing describe temporal frequency.",
                ],
                "atlas": [
                    "Every event is compared with the nearest non-event target week from the same function.",
                    "The smallest paired p value was 0.094 for temporal dispersion before six large events. Its adjusted value was 0.845.",
                    "The direction of the peak-spacing result was not stable when the large-event threshold changed.",
                    "The full fingerprint reached held-out-function balanced accuracy of 0.433, compared with the 0.500 prevalence baseline, and its Brier score was higher.",
                    "These results identify the present transfer boundary and guide the design of longer prospective sequences.",
                ],
                "model": [
                    "First-order Delta is the direct change between consecutive outputs. Higher orders are changes in the preceding Delta order, not changes between correspondingly numbered weeks.",
                    "Delta order k requires k plus 1 observations. With thirteen weeks, each function contains 12 first-order values and 3 tenth-order values.",
                    "The Signature of Change combines scaled Delta levels with oscillation, energy, temporal dispersion, persistence and cross-order coherence.",
                    "The event-locked fingerprint uses only observations before a known target week. A prospective model must use information available before a genuinely later outcome.",
                    "The present evidence supports detailed mathematical description but does not confirm reliable advance prediction.",
                ],
            }.get(view, [
                "Read the graph with the available sample size in view.",
                "Look for agreement across related Delta levels.",
                "Use later observations to test any predictive interpretation.",
            ])
        ui.modal_show(explanation_dialog(
            title,
            summary,
            points,
        ))

    @reactive.effect
    @reactive.event(input.explain_delta_level)
    def _explain_delta_level():
        index = int(input.delta_explain_level()) - 1
        level, definition, meaning = DELTA_MEANINGS[index]
        cases = int(PDHIS_ORDERS.loc[PDHIS_ORDERS.order == index + 1, "forward_cases"].iloc[0])
        ui.modal_show(explanation_dialog(
            f"{level}: what this Delta level means",
            meaning,
            [f"Recursive definition: {definition}.", f"Available forward comparisons in this record: {cases}.", "Interpret it with the preceding Delta levels; it does not amplify or create change that is not present in the observed sequence."],
        ))

    @reactive.effect
    @reactive.event(input.explain_bbr)
    def _explain_bbr():
        ui.modal_show(explanation_dialog(
            "BBR: Black Box Resolution",
            "BBR is the post-challenge method for testing what structure may be supported by the recorded inputs and outputs.",
            ["It compares competing explanations rather than assuming one equation.", "It tests explanations chronologically and rejects those that fail.", "It may support a local explanation without claiming the original hidden equation or a global optimum."],
        ))

    @reactive.effect
    @reactive.event(input.explain_repository)
    def _explain_repository():
        ui.modal_show(explanation_dialog(
            "How to use the repository",
            "The live Visual Book is for reading and interaction. The GitHub repository is the auditable record behind it.",
            ["Data folders preserve the 279 observations and weekly submissions.", "Analysis files preserve calculations, figures and notebooks.", "The Visual Book source shows how the live Shiny application is produced; ordinary readers do not need to run it."],
        ))

    @reactive.effect
    @reactive.event(input.previous_week)
    def _previous_week():
        ui.update_slider("week", value=max(1, int(input.week()) - 1))

    @reactive.effect
    @reactive.event(input.next_week)
    def _next_week():
        ui.update_slider("week", value=min(13, int(input.week()) + 1))

    @reactive.effect
    @reactive.event(input.previous_function)
    def _previous_function():
        ui.update_select("function", selected=str(max(1, int(input.function()) - 1)))

    @reactive.effect
    @reactive.event(input.next_function)
    def _next_function():
        ui.update_select("function", selected=str(min(8, int(input.function()) + 1)))

    @reactive.calc
    def selected_week() -> pd.DataFrame:
        return EVIDENCE[EVIDENCE.week == int(input.week())].sort_values("function")

    @render.ui
    def week_chapter():
        week = int(input.week())
        stage, text = WEEK_CONTEXT[week]
        frame = selected_week()
        prior = EVIDENCE[EVIDENCE.week == week - 1].set_index("function") if week > 1 else None
        cards = []
        for row in frame.itertuples():
            delta = None if prior is None else float(row.output - prior.loc[row.function, "output"])
            change = "Opening result" if delta is None else f"{delta:+.3g} from Week {week - 1}"
            cards.append(stat_box(f"F{row.function}", format_number(row.output), change, PASTELS[row.function - 1]))
        return ui.TagList(
            ui.div(ui.span(f"CHAPTER {week:02d}"), ui.h2(stage), ui.p(text), class_="chapter-banner reveal"),
            ui.div(*cards, class_="stat-grid compact"),
        )

    @render_widget
    def week_rank_plot():
        input.open_week_graph()
        week = int(input.week())
        frame = selected_week().copy()
        if input.week_cumulative():
            frame = EVIDENCE[EVIDENCE.week <= week].loc[
                EVIDENCE[EVIDENCE.week <= week].groupby("function").output.idxmax()
            ].sort_values("function")
            label = "Best output available by this week"
        else:
            label = "Returned output in this week"
        frame["Function"] = frame.function.map(lambda x: f"F{x}")
        fig = px.bar(frame, x="Function", y="output", color="Function", color_discrete_sequence=PASTELS,
                     custom_data=["function", "week", "output"])
        fig.update_traces(hovertemplate="Function %{customdata[0]}<br>Week %{customdata[1]}<br>Output %{customdata[2]:.8g}<extra></extra>")
        return plot_layout(fig, label)

    @render_widget
    def week_movement_plot():
        input.open_week_graph()
        week = int(input.week())
        if week == 1:
            frame = pd.DataFrame({"Function": [f"F{i}" for i in DIMENSIONS], "Movement": np.zeros(8)})
        else:
            rows = []
            for function, dimensions in DIMENSIONS.items():
                columns = [f"x{i}" for i in range(1, dimensions + 1)]
                current = EVIDENCE[(EVIDENCE.function == function) & (EVIDENCE.week == week)].iloc[0]
                prior = EVIDENCE[(EVIDENCE.function == function) & (EVIDENCE.week == week - 1)].iloc[0]
                rows.append((f"F{function}", float(np.linalg.norm(current[columns].to_numpy(float) - prior[columns].to_numpy(float)))))
            frame = pd.DataFrame(rows, columns=["Function", "Movement"])
        fig = px.bar(frame, x="Function", y="Movement", color="Function", color_discrete_sequence=PASTELS)
        fig.update_traces(hovertemplate="%{x}<br>Euclidean movement %{y:.6f}<extra></extra>")
        return plot_layout(fig, "Coordinate movement from the previous week")

    @reactive.calc
    def function_frame() -> pd.DataFrame:
        return EVIDENCE[EVIDENCE.function == int(input.function())].sort_values("week").copy()

    @render.ui
    def function_summary():
        function = int(input.function())
        frame = function_frame()
        best = frame.loc[frame.output.idxmax()]
        return ui.div(
            stat_box("Dimensions", str(DIMENSIONS[function]), "Input coordinates", PASTELS[function - 1]),
            stat_box("Best output", format_number(best.output), f"Week {int(best.week)}", PASTELS[(function + 1) % 8]),
            stat_box("Final output", format_number(frame.iloc[-1].output), "Week 13", PASTELS[(function + 3) % 8]),
            stat_box("Unique queries", str(frame[[f'x{i}' for i in range(1, DIMENSIONS[function] + 1)]].drop_duplicates().shape[0]), "Across thirteen rounds", PASTELS[(function + 5) % 8]),
            ui.div("Guess versus reality: no prospective numerical estimate is stored in the canonical weekly record. Actual portal outputs are shown without reconstructing a guess after the event.", class_="evidence-status"),
            class_="stat-grid compact",
        )

    @render_widget
    def function_trajectory():
        input.open_function_graph()
        function = int(input.function())
        frame = function_frame()
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=frame.week, y=frame.output, mode="lines+markers", name="Weekly output",
                                 line=dict(color=PASTELS[function - 1], width=3), marker=dict(size=9)))
        frame["change"] = frame.output.diff()
        fig.add_trace(go.Bar(x=frame.week, y=frame.change, name="Week change / slope",
                             marker_color="rgba(141,169,219,.42)", yaxis="y2"))
        if input.show_best():
            fig.add_trace(go.Scatter(x=frame.week, y=frame.output.cummax(), mode="lines", name="Cumulative best",
                                     line=dict(color="#d2a64a", width=3, dash="dot")))
        best = frame.loc[frame.output.idxmax()]
        fig.add_annotation(x=best.week, y=best.output, text=f"Maximum<br>{format_number(best.output)}", showarrow=True,
                           arrowcolor="#263f5a", bgcolor="#fff7e8", bordercolor="#e7c77e")
        fig.update_xaxes(dtick=1, title="Week")
        fig.update_yaxes(title="Returned output")
        fig.update_layout(
            yaxis2=dict(title="Week change", overlaying="y", side="right", showgrid=False, zeroline=True,
                        zerolinecolor="rgba(38,63,90,.25)"),
            barmode="overlay",
        )
        return plot_layout(fig, f"F{function} output trajectory")

    @render_widget
    def coordinate_trajectory():
        input.open_function_graph()
        function = int(input.function())
        columns = [f"x{i}" for i in range(1, DIMENSIONS[function] + 1)]
        if input.show_starter():
            frame = COMPLETE[(COMPLETE.function == function) & (COMPLETE.source == "starter")].copy()
            frame["sequence_label"] = frame.sequence
            title = f"F{function} starter-coordinate distribution"
            x_name = "sequence_label"
        else:
            frame = function_frame()
            title = f"F{function} weekly coordinate trajectories"
            x_name = "week"
        fig = go.Figure()
        for index, column in enumerate(columns):
            fig.add_trace(go.Scatter(x=frame[x_name], y=frame[column], mode="lines+markers" if not input.show_starter() else "markers",
                                     name=column, line=dict(width=2), marker=dict(size=7, color=PASTELS[index % len(PASTELS)])))
        fig.update_yaxes(range=[-0.03, 1.03], title="Coordinate value")
        fig.update_xaxes(title="Week" if not input.show_starter() else "Starter sequence")
        return plot_layout(fig, title)

    @render.data_frame
    def function_table():
        function = int(input.function())
        columns = ["week", *[f"x{i}" for i in range(1, DIMENSIONS[function] + 1)], "output"]
        frame = function_frame()[columns].copy()
        frame["week_change"] = frame.output.diff()
        frame["rate_of_change"] = frame.week_change
        frame["retained_best"] = frame.output.cummax()
        return render.DataGrid(frame, filters=False, selection_mode="rows", height="42vh")

    def _build_atlas_plot(view: str):
        frame = EVIDENCE.copy()
        frame["Function"] = frame.function.map(lambda value: f"F{value}")
        frame["Relative progress"] = frame.groupby("function").output.transform(
            lambda values: (values - values.min()) / (values.max() - values.min() if values.max() != values.min() else 1)
        )
        measure = "Relative progress" if input.atlas_measure() == "relative" else "output"
        if view == "heatmap":
            pivot = frame.pivot(index="Function", columns="week", values=measure).reindex([f"F{i}" for i in DIMENSIONS])
            fig = px.imshow(pivot, aspect="auto", color_continuous_scale=["#f6eef8", "#d9edf2", "#9bcfc5", "#f2b880"],
                            labels=dict(x="Week", y="Function", color=measure))
            return plot_layout(fig, "Function by week evidence map")
        if view == "winners":
            winners = winning_rows().copy()
            winners["Function"] = winners.function.map(lambda value: f"F{value}")
            fig = px.scatter(winners, x="week", y="Function", size=np.repeat(18, len(winners)), color="Function",
                             color_discrete_sequence=PASTELS, custom_data=["output"])
            fig.update_traces(marker=dict(size=22, line=dict(color="white", width=2)), hovertemplate="%{y}<br>Winning week %{x}<br>Output %{customdata[0]:.8g}<extra></extra>")
            fig.update_xaxes(dtick=1, title="Winning week")
            return plot_layout(fig, "Where the participant-query maxima occurred")
        fig = px.line(frame, x="week", y=measure, color="Function", markers=True, color_discrete_sequence=PASTELS,
                      custom_data=["output"])
        fig.update_traces(hovertemplate="%{fullData.name}<br>Week %{x}<br>Displayed %{y:.5g}<br>Original output %{customdata[0]:.8g}<extra></extra>")
        fig.update_xaxes(dtick=1, title="Week")
        return plot_layout(fig, "Weekly trajectories across all eight functions")

    @render_widget
    def atlas_weekly_plot():
        input.open_atlas_graph()
        return _build_atlas_plot("weekly")

    @render_widget
    def atlas_heatmap_plot():
        input.open_atlas_graph()
        return _build_atlas_plot("heatmap")

    @render_widget
    def atlas_winners_plot():
        input.open_atlas_graph()
        return _build_atlas_plot("winners")

    @render.text
    def pdhis_chart_title():
        return {
            "overview": "Delta of BBO",
            "meanings": "What each level of Delta means",
            "hierarchy": "What each level of the Delta hierarchy means",
            "trajectory": "Observed Delta trajectory by function and level",
            "orders": "Does a Delta order predict the next change?",
            "functions": "Function-specific Delta relationships",
            "evidence": "Predictive evidence decreases at higher orders",
            "advanced": "Can the Delta signature classify next-week improvement?",
            "flicker": "What characterised the flicker before a known event?",
            "atlas": "Does the flicker fingerprint survive stronger controls?",
            "model": "How is PDHIS defined mathematically?",
        }[input.pdhis_view()]

    @render.text
    def pdhis_interpretation():
        return {
            "overview": "PDHIS applies the Delta hierarchy to the completed BBO record while preserving the official optimisation results unchanged.",
            "meanings": "Each level measures recursively nested change already present in the observed sequence. PDHIS then tests the timing, persistence and directional coherence of the Delta series for an early indication of vector, plateau, reversal, oscillation or irregular fluctuation. Predictive value and subsequent trajectory must be established chronologically.",
            "hierarchy": "Delta n is calculated from successive values of Delta n minus 1. A higher level cannot occur independently before its preceding level, but it may expose repeated oscillation, plateau, improvement or deterioration. Delta 10 is the current practical cap, while Delta n remains extendable when the preceding level changes materially and sufficient evidence remains. Coherent propagation may support genuine vector-directed change, while unstable or directionally inconsistent patterns may indicate chaotic noise. This hypothesis requires prospective validation.",
            "trajectory": "The selected curve is calculated recursively from the range-normalised weekly outputs of one function. Look for the Signature of Change in its direction, persistence, reversals and agreement with lower Delta levels. A single high point carries less meaning on its own. Any predictive interpretation must use only information available before the later outcome.",
            "orders": "Across ten levels of Delta freedom, Delta 2, Delta 4 and Delta 5 show the strongest inverse associations with later change. These relationships need further chronological testing before they can support forecasting.",
            "functions": "F2 has the clearest reversal signature across Delta 1 to Delta 4. F5 differs, with a positive Delta 1 relationship. Function-level samples remain small.",
            "evidence": "Usable forward comparisons fall from 88 at Delta 1 to 16 at Delta 10. No order reaches an adjusted q value below 0.05.",
            "advanced": "The earlier Delta signature is the predictor and later behaviour is the target. The full regularised signature performed better than the simple prevalence baseline when one function was held out. Chronological accuracy was weaker. The higher-order test identified Delta 9 oscillation as too common to distinguish positive Delta 3 in this short record, directing attention towards more selective signatures.",
            "flicker": "The event-locked study looks backwards from known outcomes and characterises the preceding flicker. Peak spacing was the strongest candidate before new best outputs, but it did not remain significant after adjustment. The result defines a candidate temporal fingerprint for later prospective testing.",
            "atlas": "Same-function matching, threshold sensitivity and held-out-function testing identified the present stability and transfer boundary. This positive boundary finding shows which characteristics require refinement and why longer independent sequences are needed.",
            "model": "PDHIS defines a reproducible mathematical state from recursive Delta orders and temporal characteristics. It extracts retrospective behaviour from an unknown process while keeping description, association and prospective prediction as separate levels of evidence.",
        }[input.pdhis_view()]

    def _build_pdhis_plot(view: str):
        metrics = PDHIS_ORDERS.copy()
        if view == "overview":
            return go.Figure()
        if view == "meanings":
            levels = [f"Δ{i}" for i in range(1, 11)] + ["Δn"]
            definitions = [
                "y(t) - y(t-1)",
                "Δ1(t) - Δ1(t-1)",
                "Δ2(t) - Δ2(t-1)",
                "Δ3(t) - Δ3(t-1)",
                "Δ4(t) - Δ4(t-1)",
                "Δ5(t) - Δ5(t-1)",
                "Δ6(t) - Δ6(t-1)",
                "Δ7(t) - Δ7(t-1)",
                "Δ8(t) - Δ8(t-1)",
                "Δ9(t) - Δ9(t-1)",
                "Δ(n-1)(t) - Δ(n-1)(t-1)",
            ]
            meanings = [
                "Direct observed change: direction and magnitude.",
                "Change of change: acceleration, curvature, emerging plateau or reversal.",
                "Change in second-order behaviour: whether acceleration, plateau or reversal is itself changing.",
                "Evolution of the third-order pattern: persistence, reversal or developing oscillation.",
                "Medium-order transition in repeated change; tests whether a pattern propagates.",
                "Deeper recursive change; interpret through coherence with lower levels.",
                "Higher-order propagation or instability already present in the change sequence.",
                "Deep repeated change; exploratory as chronological evidence narrows.",
                "Penultimate practical level here; requires strong cross-level consistency.",
                "Current practical cap for the thirteen-week record; hypothesis-generating.",
                "Extend only when the preceding Delta changes materially and sufficient evidence remains.",
            ]
            comparisons = metrics.forward_cases.astype(int).astype(str).tolist() + ["Depends on record length"]
            fig = go.Figure(go.Table(
                columnwidth=[42, 115, 360, 82],
                header=dict(
                    values=["<b>Level</b>", "<b>Recursive definition</b>", "<b>Practical meaning</b>", "<b>Forward cases</b>"],
                    fill_color="#dcebea", align=["center", "left", "left", "center"],
                    font=dict(size=11, color="#263f5a"), height=27,
                ),
                cells=dict(
                    values=[levels, definitions, meanings, comparisons],
                    fill_color=[["#f7fbfa", "#eef5f8"] * 6],
                    align=["center", "left", "left", "center"],
                    font=dict(size=10, color="#425b70"), height=25,
                ),
            ))
            fig.update_layout(margin=dict(l=8, r=8, t=8, b=8), paper_bgcolor="rgba(0,0,0,0)")
            return fig
        if view == "trajectory":
            function = int(input.pdhis_function())
            order = int(input.pdhis_order())
            frame = EVIDENCE[EVIDENCE.function == function].sort_values("week").copy()
            span = frame.output.max() - frame.output.min()
            values = ((frame.output - frame.output.min()) / (span if span else 1.0)).to_numpy(dtype=float)
            weeks = frame.week.to_numpy(dtype=int)
            for _ in range(order):
                values = np.diff(values)
                weeks = weeks[1:]
            fig = go.Figure()
            fig.add_hline(y=0, line=dict(color="#9aaeb8", width=1, dash="dot"))
            fig.add_trace(go.Scatter(
                x=weeks, y=values, mode="lines+markers", name=f"Delta {order}",
                line=dict(color=PASTELS[(function - 1) % len(PASTELS)], width=3),
                marker=dict(size=9, line=dict(color="white", width=1.5)),
                hovertemplate=f"F{function}, Delta {order}<br>Week %{{x}}<br>Value %{{y:.6g}}<extra></extra>",
            ))
            fig.update_xaxes(dtick=1, title="Week at which the Delta value becomes available")
            fig.update_yaxes(title=f"Delta {order} of range-normalised output")
            return plot_layout(fig, f"F{function} observed Delta {order} series")
        if view == "hierarchy":
            meanings = [
                "Direct change: direction and magnitude",
                "Change of change: acceleration, curvature and emerging plateau",
                "Change of Delta 2: alteration in acceleration or oscillatory development",
                "Fourth-order transition in the recent change pattern",
                "Fifth-order transition and possible repeated reversal structure",
                "Higher-order interaction pattern, interpreted cautiously",
                "Higher-order interaction pattern, interpreted cautiously",
                "Higher-order interaction pattern, interpreted cautiously",
                "Higher-order interaction pattern, interpreted cautiously",
                "Current practical cap for the thirteen-week BBO record",
            ]
            labels = ["PDHIS"] + [f"Δ{i}" for i in range(1, 11)]
            parents = [""] + ["PDHIS"] + [f"Δ{i}" for i in range(1, 10)]
            evidence = [104] + metrics.forward_cases.astype(int).tolist()
            hover = ["Recursive Delta hierarchy"] + [
                f"{meanings[i - 1]}<br>Forward comparisons: {int(metrics.loc[metrics.order == i, 'forward_cases'].iloc[0])}"
                for i in range(1, 11)
            ]
            fig = go.Figure(go.Sunburst(
                labels=labels, parents=parents, values=[1] * len(labels), branchvalues="remainder",
                customdata=np.column_stack([hover, evidence]),
                hovertemplate="%{label}<br>%{customdata[0]}<extra></extra>",
                insidetextorientation="radial",
                marker=dict(colors=["#f8f7f2", "#dff3ed", "#e3f0f8", "#eee7f7", "#fff0df", "#f8e4ea", "#d8ece8", "#dce8f3", "#e7dcf1", "#f7e6d2", "#f1dbe2"]),
            ))
            fig.add_annotation(
                x=.5, y=.5, text="Δⁿ", showarrow=False,
                font=dict(family="Georgia, serif", size=24, color="#263f5a"),
            )
            return plot_layout(fig, "The Lotus hierarchy from direct change to Delta n")

        if view == "functions":
            frame = PDHIS_FUNCTIONS[PDHIS_FUNCTIONS.order <= 4].copy()
            matrix = frame.pivot(index="function", columns="order", values="spearman_next_change")
            counts = frame.pivot(index="function", columns="order", values="n")
            text = np.asarray([
                [f"{matrix.loc[f, o]:.2f}<br>n={int(counts.loc[f, o])}" for o in matrix.columns]
                for f in matrix.index
            ])
            fig = go.Figure(go.Heatmap(
                z=matrix.to_numpy(), x=[f"Δ{o}" for o in matrix.columns],
                y=[f"F{f}" for f in matrix.index], zmin=-1, zmax=1, zmid=0,
                colorscale=[[0, "#557f99"], [.5, "#f8f7f2"], [1, "#d77b91"]],
                text=text, texttemplate="%{text}",
                colorbar=dict(title="ρ"),
                hovertemplate="%{y}<br>%{x}<br>Correlation %{z:.3f}<extra></extra>",
            ))
            return plot_layout(fig, "Delta association with the following weekly change")

        if view == "evidence":
            fig = go.Figure()
            fig.add_trace(go.Bar(
                x=metrics.order, y=metrics.forward_cases, name="Forward comparisons",
                marker_color="#8fc5bd", text=metrics.forward_cases, textposition="outside",
                hovertemplate="Delta %{x}<br>%{y} comparisons<extra></extra>",
            ))
            fig.add_trace(go.Scatter(
                x=metrics.order, y=-np.log10(metrics.fdr_q), name="Adjusted evidence",
                mode="lines+markers", yaxis="y2", line=dict(color="#8f76b4", width=3),
                hovertemplate="Delta %{x}<br>-log10(q) %{y:.3f}<extra></extra>",
            ))
            threshold = -np.log10(.05)
            fig.add_shape(
                type="line", x0=.5, x1=10.5, y0=threshold, y1=threshold,
                xref="x", yref="y2", line=dict(color="#d65a6f", dash="dash"),
            )
            fig.add_annotation(
                x=10, y=threshold, xref="x", yref="y2", text="q = 0.05",
                showarrow=False, xanchor="right", yshift=9, font=dict(color="#b54c61"),
            )
            fig.update_xaxes(dtick=1, title="Delta order")
            fig.update_yaxes(title="Forward comparisons")
            fig.update_layout(yaxis2=dict(title="Adjusted evidence, -log10(q)", overlaying="y", side="right", showgrid=False))
            return plot_layout(fig, "Evidence count and false-discovery correction")

        if view == "advanced":
            frame = PDHIS_ADVANCED_METRICS.copy()
            frame = frame[frame.model == "Delta signature"].copy()
            frame["Validation"] = frame.validation.map({
                "Leave one function out": "Held-out function",
                "Expanding week": "Expanding week",
            })
            frame["Prediction"] = frame.prediction.map({
                "Regularised logistic": "Delta signature",
                "Prevalence baseline": "Baseline",
            })
            fig = px.bar(
                frame, x="Validation", y="balanced_accuracy", color="Prediction", barmode="group",
                color_discrete_map={"Delta signature": "#4f9d96", "Baseline": "#cbd5e1"},
                custom_data=["roc_auc", "brier_score", "n"],
            )
            fig.update_traces(
                hovertemplate="%{x}<br>%{fullData.name}<br>Balanced accuracy %{y:.3f}<br>ROC AUC %{customdata[0]:.3f}<br>Brier score %{customdata[1]:.3f}<br>Cases %{customdata[2]}<extra></extra>"
            )
            fig.add_hline(y=.5, line=dict(color="#d4a72c", dash="dash"), annotation_text="Chance-balanced reference")
            fig.update_yaxes(title="Balanced accuracy", range=[0, .75])
            return plot_layout(fig, "Out-of-sample next-week improvement classification")

        if view == "flicker":
            frame = PDHIS_FLICKER_ASSOCIATIONS.copy()
            target_order = ["positive_event", "large_event", "new_best_event"]
            feature_order = list(dict.fromkeys(frame.feature_label))
            pivot = frame.pivot(index="feature_label", columns="target", values="standardised_difference").reindex(index=feature_order, columns=target_order)
            hover = frame.pivot(index="feature_label", columns="target", values="holm_p").reindex(index=feature_order, columns=target_order)
            fig = go.Figure(go.Heatmap(
                z=pivot.to_numpy(), x=["Any improvement", "Large change", "New best"], y=feature_order,
                colorscale="RdBu", zmid=0, zmin=-1.25, zmax=1.25,
                customdata=hover.to_numpy(),
                hovertemplate="%{y}<br>%{x}<br>Standardised difference %{z:.3f}<br>Adjusted p %{customdata:.3f}<extra></extra>",
                colorbar=dict(title="Event minus<br>non-event"),
            ))
            fig.update_yaxes(autorange="reversed")
            return plot_layout(fig, "Pre-event temporal flicker fingerprint")

        if view == "atlas":
            frame = PDHIS_MATCHED_RESULTS.copy()
            target_order = ["positive_event", "large_event", "new_best_event"]
            feature_order = list(dict.fromkeys(frame.feature_label))
            pivot = frame.pivot(index="feature_label", columns="target", values="paired_standardised_difference").reindex(index=feature_order, columns=target_order)
            adjusted = frame.pivot(index="feature_label", columns="target", values="holm_p").reindex(index=feature_order, columns=target_order)
            fig = go.Figure(go.Heatmap(
                z=pivot.to_numpy(), x=["Any improvement", "Large change", "New best"], y=feature_order,
                colorscale="RdBu", zmid=0, zmin=-1.25, zmax=1.25,
                customdata=adjusted.to_numpy(),
                hovertemplate="%{y}<br>%{x}<br>Standardised paired difference %{z:.3f}<br>Adjusted p %{customdata:.3f}<extra></extra>",
                colorbar=dict(title="Event minus<br>matched"),
            ))
            fig.update_yaxes(autorange="reversed")
            return plot_layout(fig, "Same-function matched event comparisons")

        if view == "model":
            labels = ["Observed output", "Delta 1", "Delta 2 to 5", "Delta 6 to 10", "Oscillation", "Energy and dispersion", "Persistence and coherence", "Signature of Change", "Known event", "Later target"]
            sources = [0, 1, 2, 3, 1, 2, 3, 4, 5, 6, 7, 7]
            targets = [1, 2, 3, 7, 4, 5, 6, 7, 7, 7, 8, 9]
            values = [5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 2, 2]
            fig = go.Figure(go.Sankey(
                node=dict(
                    label=labels, pad=18, thickness=18,
                    color=["#8da9db", "#64b6ac", "#64b6ac", "#64b6ac", "#f2b880", "#f2b880", "#f2b880", "#b497d6", "#e58aa5", "#e58aa5"],
                ),
                link=dict(source=sources, target=targets, value=values, color="rgba(100,150,170,.25)"),
            ))
            return plot_layout(fig, "From observed output to the PDHIS Signature of Change")

        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=metrics.order, y=metrics.null_rho_high, mode="lines", line=dict(width=0),
            showlegend=False, hoverinfo="skip",
        ))
        fig.add_trace(go.Scatter(
            x=metrics.order, y=metrics.null_rho_low, mode="lines", line=dict(width=0),
            fill="tonexty", fillcolor="rgba(212,167,44,.18)", name="95% shuffled range",
            hoverinfo="skip",
        ))
        fig.add_trace(go.Scatter(
            x=metrics.order, y=metrics.spearman_next_change, mode="lines+markers",
            name="Next change", line=dict(color="#4f9d96", width=3),
        ))
        fig.add_trace(go.Scatter(
            x=metrics.order, y=metrics.spearman_next_output, mode="lines+markers",
            name="Next output", line=dict(color="#7c67ad", width=3),
        ))
        fig.add_hline(y=0, line_color="rgba(38,63,90,.35)")
        fig.update_xaxes(dtick=1, title="Delta order")
        fig.update_yaxes(title="Pooled Spearman correlation", range=[-.8, .7])
        return plot_layout(fig, "Chronological relationship by Delta order")

    @render_widget
    def pdhis_hierarchy_plot():
        input.open_pdhis_graph()
        return _build_pdhis_plot("hierarchy")

    @render_widget
    def pdhis_trajectory_plot():
        input.open_pdhis_graph()
        return _build_pdhis_plot("trajectory")

    @render_widget
    def pdhis_orders_plot():
        input.open_pdhis_graph()
        return _build_pdhis_plot("orders")

    @render_widget
    def pdhis_functions_plot():
        input.open_pdhis_graph()
        return _build_pdhis_plot("functions")

    @render_widget
    def pdhis_evidence_plot():
        input.open_pdhis_graph()
        return _build_pdhis_plot("evidence")

    @render_widget
    def pdhis_advanced_plot():
        input.open_pdhis_graph()
        return _build_pdhis_plot("advanced")

    @render_widget
    def pdhis_flicker_plot():
        input.open_pdhis_graph()
        return _build_pdhis_plot("flicker")

    @render_widget
    def pdhis_atlas_plot():
        input.open_pdhis_graph()
        return _build_pdhis_plot("atlas")

    @render_widget
    def pdhis_model_plot():
        input.open_pdhis_graph()
        return _build_pdhis_plot("model")

    @reactive.calc
    def filtered_evidence() -> pd.DataFrame:
        start, end = input.evidence_weeks()
        frame = EVIDENCE[EVIDENCE.week.between(start, end)].copy()
        if input.evidence_function() != "all":
            frame = frame[frame.function == int(input.evidence_function())]
        return frame.sort_values(["week", "function"]).reset_index(drop=True)

    @reactive.effect
    @reactive.event(input.evidence_function, input.evidence_weeks)
    def _reset_evidence_page():
        evidence_page.set(0)

    @reactive.effect
    @reactive.event(input.evidence_page_previous)
    def _evidence_page_previous():
        evidence_page.set(max(0, evidence_page() - 1))

    @reactive.effect
    @reactive.event(input.evidence_page_next)
    def _evidence_page_next():
        last_page = max(0, (len(filtered_evidence()) - 1) // 6)
        evidence_page.set(min(last_page, evidence_page() + 1))

    @render.text
    def evidence_page_label():
        total = len(filtered_evidence())
        if total == 0:
            return "No matching rows"
        start = evidence_page() * 6 + 1
        end = min(total, start + 5)
        return f"Rows {start} to {end} of {total}"

    @render.ui
    def evidence_table():
        frame = filtered_evidence()
        start = evidence_page() * 6
        page = frame.iloc[start:start + 6]
        rows = []
        for row in page.itertuples():
            inputs = []
            for index in range(1, DIMENSIONS[int(row.function)] + 1):
                value = getattr(row, f"x{index}")
                if pd.notna(value):
                    inputs.append(f"x{index}={float(value):.4g}")
            rows.append(
                ui.tags.tr(
                    ui.tags.td(f"F{int(row.function)}"),
                    ui.tags.td(str(int(row.week))),
                    ui.tags.td(", ".join(inputs), class_="evidence-inputs"),
                    ui.tags.td(format_number(row.output)),
                )
            )
        return ui.tags.table(
            ui.tags.thead(ui.tags.tr(ui.tags.th("Function"), ui.tags.th("Week"), ui.tags.th("Submitted coordinates"), ui.tags.th("Returned output"))),
            ui.tags.tbody(*rows),
            class_="compact-evidence-table",
        )


app = App(app_ui, server, static_assets=APP_DIR / "www")


