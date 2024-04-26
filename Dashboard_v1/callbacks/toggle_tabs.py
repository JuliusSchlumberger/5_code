import dash
from dash import html, dcc, callback, Input, Output, State, callback_context
import dash_bootstrap_components as dbc
import plotly.io as pio
import plotly.graph_objects as go  # Import Plotly's graph_objects module
import components.explanations as explanations
import components.survey as survey

from dashapp import app


@app.callback(
    Output("tab-content-introduction", "children"),
    Input("tabs-introduction", "active_tab")
)
def render_tab_content_introduction(active_tab):
    if active_tab == "tab-explanation-introduction":
        return explanations.introduction  # Your explanation content
    elif active_tab == "tab-survey-introduction":
        return survey.introduction  # Your survey content
    return "No content available."


@app.callback(
    Output("tab-content-alternative_pathways", "children"),
    Input("tabs-alternative_pathways", "active_tab")
)
def render_tab_content_alternative_pathways(active_tab):
    if active_tab == "tab-explanation-alternative_pathways":
        return explanations.alternative_pathways  # Your explanation content
    elif active_tab == "tab-survey-alternative_pathways":
        return survey.alternative_pathways  # Your survey content
    return "No content available."


@app.callback(
    Output("tab-content-pathways_performance", "children"),
    Input("tabs-pathways_performance", "active_tab")
)
def render_tab_content_alternative_pathways(active_tab):
    if active_tab == "tab-explanation-pathways_performance":
        return explanations.pathways_performance  # Your explanation content
    elif active_tab == "tab-survey-pathways_performance":
        return survey.performance_pathways  # Your survey content
    return "No content available."

@app.callback(
    Output("tab-content-interaction_effects", "children"),
    Input("tabs-interaction_effects", "active_tab")
)
def render_tab_content_interaction_effects(active_tab):
    if active_tab == "tab-explanation-interaction_effects":
        return explanations.interaction_effects  # Your explanation content
    elif active_tab == "tab-survey-interaction_effects":
        return survey.interaction_effects  # Your survey content
    return "No content available."