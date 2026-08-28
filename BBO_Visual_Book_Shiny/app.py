from __future__ import annotations

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


def load_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    complete = pd.read_csv(DATA_FILE)
    assessed = complete[complete.source.str.startswith("week_")].copy()
    assessed["week"] = assessed.source.str.removeprefix("week_").astype(int)
    assessed = assessed.sort_values(["function", "week"]).reset_index(drop=True)
    if len(complete) != 279 or len(assessed) != 104:
        raise ValueError("The canonical evidence file does not contain the expected 279 observations and 104 weekly queries.")
    return complete, assessed


COMPLETE, EVIDENCE = load_data()


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


def plot_layout(fig: go.Figure, title: str = "") -> go.Figure:
    fig.update_layout(
        title=dict(text=title, x=0.02, xanchor="left", font=dict(size=20, color="#263f5a")),
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(255,255,255,0.68)",
        font=dict(family="Inter, Arial, sans-serif", color="#425b70"),
        margin=dict(l=45, r=25, t=65, b=45),
        hoverlabel=dict(bgcolor="white", font_size=13),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    )
    fig.update_xaxes(gridcolor="rgba(95,125,145,0.12)", zeroline=False)
    fig.update_yaxes(gridcolor="rgba(95,125,145,0.12)", zeroline=False)
    return fig


app_ui = ui.page_navbar(
    ui.nav_panel(
        "Cover",
        ui.div(
            ui.tags.section(
                ui.div("IMPERIAL COLLEGE LONDON  |  BLACK BOX OPTIMISATION", class_="hero-kicker"),
                ui.h1("Thirteen weeks. Eight hidden functions."),
                ui.p("A visual book of 104 decisions, their returned results and the analytical methods used to decide what came next."),
                ui.div(
                    ui.span("279 recorded observations"), ui.span("104 participant queries"),
                    ui.span("2 to 8 dimensions"), ui.span("13 rounds"), class_="hero-tags",
                ),
                class_="hero reveal",
            ),
            ui.div(
                stat_box("Functions", "8", "Each maximised independently", PASTELS[0]),
                stat_box("Weekly queries", "104", "One per function per round", PASTELS[1]),
                stat_box("Starter evidence", "175", "Course-supplied observations", PASTELS[2]),
                stat_box("Final dataset", "279", "Audited canonical rows", PASTELS[3]),
                class_="stat-grid",
            ),
            ui.div(
                ui.div(ui.span("01"), ui.strong("Read by Week"), ui.p("Follow the decisions chronologically from opening exploration to final evaluation.")),
                ui.div(ui.span("02"), ui.strong("Read by Function"), ui.p("Trace each hidden function across all thirteen submitted coordinates and outputs.")),
                ui.div(ui.span("03"), ui.strong("Explore the Evidence"), ui.p("Use interactive scientific figures without altering the official record.")),
                class_="route-grid reveal",
            ),
            class_="book-page",
        ),
    ),
    ui.nav_panel(
        "Read by Week",
        ui.div(
            book_heading("BOOK I  |  CHRONOLOGICAL READING", "The thirteen-round story", "Move through the campaign one round at a time. Each chapter combines the submitted evidence with the documented purpose of that stage."),
            ui.layout_sidebar(
                ui.sidebar(
                    ui.input_slider("week", "Choose a chapter", 1, 13, 1, step=1, ticks=True, animate={"interval": 1400, "loop": False}),
                    ui.input_switch("week_cumulative", "Show cumulative best", True),
                    ui.p("Use the play control to animate the complete thirteen-week sequence.", class_="control-note"),
                    title="Chapter controls", open="desktop",
                ),
                ui.output_ui("week_chapter"),
                output_widget("week_rank_plot", height="430px"),
                output_widget("week_movement_plot", height="430px"),
                class_="book-layout",
            ),
            class_="book-page",
        ),
    ),
    ui.nav_panel(
        "Read by Function",
        ui.div(
            book_heading("BOOK II  |  FUNCTION READING", "Eight distinct optimisation stories", "Select a function to examine its trajectory, winning week, coordinate movement and complete evidence record."),
            ui.layout_sidebar(
                ui.sidebar(
                    ui.input_select("function", "Hidden function", {str(i): f"F{i}  |  {DIMENSIONS[i]} dimensions" for i in DIMENSIONS}, selected="1"),
                    ui.input_switch("show_best", "Show cumulative best", True),
                    ui.input_switch("show_starter", "Include starter points in input view", False),
                    title="Function controls", open="desktop",
                ),
                ui.div(ui.output_ui("function_summary"), class_="summary-slot"),
                output_widget("function_trajectory", height="470px"),
                output_widget("coordinate_trajectory", height="470px"),
                ui.card(ui.card_header("Complete weekly evidence"), ui.output_data_frame("function_table"), class_="evidence-card"),
                class_="book-layout",
            ),
            class_="book-page",
        ),
    ),
    ui.nav_panel(
        "Scientific Atlas",
        ui.div(
            book_heading("BOOK III  |  SCIENTIFIC ATLAS", "Compare the complete optimisation landscape", "The atlas scales unlike outputs for fair visual comparison while retaining the original values in hover labels and tables."),
            ui.div(
                ui.input_select("atlas_measure", "Comparison measure", {"relative": "Within-function relative progress", "raw": "Original returned output"}, selected="relative"),
                ui.input_select("atlas_view", "Atlas view", {"weekly": "Weekly trajectories", "heatmap": "Function by week heat map", "winners": "Winning week and result"}, selected="weekly"),
                class_="inline-controls",
            ),
            output_widget("atlas_plot", height="590px"),
            ui.div(
                stat_box("First winning week", str(int(winning_rows().week.min())), "Earliest retained maximum", PASTELS[4]),
                stat_box("Last winning week", str(int(winning_rows().week.max())), "Latest retained maximum", PASTELS[5]),
                stat_box("Functions peaking in Week 13", str(int((winning_rows().week == 13).sum())), "Final-round maxima", PASTELS[6]),
                stat_box("Observed dimensions", "2 to 8", "Heterogeneous search spaces", PASTELS[7]),
                class_="stat-grid compact",
            ),
            class_="book-page",
        ),
    ),
    ui.nav_panel(
        "Strategy Loop",
        ui.div(
            book_heading("BOOK IV  |  DECISION SYSTEM", "How the strategy changed with evidence", "Exploration and exploitation were parallel choices. The broader loop extended each result into the next optimisation decision."),
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
            ui.div(
                ui.card(ui.card_header("Exploration"), ui.p("Broader movement purchased information about untested regions but risked leaving a strong local area."), class_="pastel-card mint"),
                ui.card(ui.card_header("Exploitation"), ui.p("Smaller movement refined supported regions but could miss a separate and better optimum."), class_="pastel-card blue"),
                ui.card(ui.card_header("Confirmation"), ui.p("Repeated coordinates tested stability, although every repeat consumed a scarce weekly evaluation."), class_="pastel-card lavender"),
                class_="three-column",
            ),
            ui.div(
                ui.h2("The stopping rule"),
                ui.p("The official challenge ended after thirteen queries per function. This finite budget meant that uncertainty could not be removed completely. A promising region sometimes remained only partly tested, so final decisions had to balance the observed score, repeatability and the value of one last alternative query."),
                class_="reading-panel reveal",
            ),
            class_="book-page",
        ),
    ),
    ui.nav_panel(
        "Evidence",
        ui.div(
            book_heading("APPENDIX  |  VERIFIED EVIDENCE", "The complete participant-query record", "Filter all 104 weekly evaluations. The table is generated directly from the canonical 279-observation dataset."),
            ui.div(
                ui.input_select("evidence_function", "Function", {"all": "All functions", **{str(i): f"F{i}" for i in DIMENSIONS}}, selected="all"),
                ui.input_slider("evidence_weeks", "Week range", 1, 13, [1, 13], step=1),
                class_="inline-controls",
            ),
            ui.card(ui.output_data_frame("evidence_table"), class_="evidence-card"),
            class_="book-page",
        ),
    ),
    title=ui.div(ui.span("◈", class_="brand-mark"), ui.span("Imperial BBO Visual Book")),
    id="main_navigation", selected="Cover",
    navbar_options=ui.navbar_options(position="sticky-top", underline=False, collapsible=True),
    header=ui.tags.head(
        ui.tags.meta(name="description", content="Interactive visual book and scientific dashboard for the Imperial BBO capstone."),
        ui.include_css(APP_DIR / "www" / "styles.css"),
    ),
    footer=ui.div("Official Week 1 to Week 13 evidence  |  279 observations  |  Reproducible Python application", class_="book-footer"),
    window_title="Imperial BBO Visual Book",
)


def server(input: Inputs, output: Outputs, session: Session) -> None:
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
            class_="stat-grid compact",
        )

    @render_widget
    def function_trajectory():
        function = int(input.function())
        frame = function_frame()
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=frame.week, y=frame.output, mode="lines+markers", name="Weekly output",
                                 line=dict(color=PASTELS[function - 1], width=3), marker=dict(size=9)))
        if input.show_best():
            fig.add_trace(go.Scatter(x=frame.week, y=frame.output.cummax(), mode="lines", name="Cumulative best",
                                     line=dict(color="#d2a64a", width=3, dash="dot")))
        best = frame.loc[frame.output.idxmax()]
        fig.add_annotation(x=best.week, y=best.output, text=f"Maximum<br>{format_number(best.output)}", showarrow=True,
                           arrowcolor="#263f5a", bgcolor="#fff7e8", bordercolor="#e7c77e")
        fig.update_xaxes(dtick=1, title="Week")
        fig.update_yaxes(title="Returned output")
        return plot_layout(fig, f"F{function} output trajectory")

    @render_widget
    def coordinate_trajectory():
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
        return render.DataGrid(function_frame()[columns], filters=True, selection_mode="rows", height="470px")

    @render_widget
    def atlas_plot():
        frame = EVIDENCE.copy()
        frame["Function"] = frame.function.map(lambda value: f"F{value}")
        frame["Relative progress"] = frame.groupby("function").output.transform(
            lambda values: (values - values.min()) / (values.max() - values.min() if values.max() != values.min() else 1)
        )
        measure = "Relative progress" if input.atlas_measure() == "relative" else "output"
        view = input.atlas_view()
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

    @render.data_frame
    def evidence_table():
        start, end = input.evidence_weeks()
        frame = EVIDENCE[EVIDENCE.week.between(start, end)].copy()
        if input.evidence_function() != "all":
            frame = frame[frame.function == int(input.evidence_function())]
        columns = ["function", "week", *[f"x{i}" for i in range(1, 9)], "output"]
        return render.DataGrid(frame[columns].dropna(axis=1, how="all"), filters=True, selection_mode="rows", height="610px")


app = App(app_ui, server, static_assets=APP_DIR / "www")
