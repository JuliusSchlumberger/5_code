import dash
from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
import plotly.io as pio
import plotly.graph_objects as go  # Import Plotly's graph_objects module
import json
from dashapp import app
from datetime import datetime

@app.callback(
    [Output("survey-tab-introduction", "label"),
    Output("navigation-introduction", "children")],
    Input("submit-survey-introduction", "n_clicks"),
    prevent_initial_call=True
)
def update_survey_introduction_tab_label(n_clicks):
    if n_clicks > 0:
        return "Survey \u2714", "\u2611 Introduction"  # Change the label to indicate submission
    return "Survey \u26A0", "Introduction"  # Default label if no submissions



@app.callback(
    [Output("survey-tab-alternative_pathways", "label"),
    Output("navigation-alternative_pathways", "children")],
    Input("submit-survey-alternative_pathways", "n_clicks"),
    prevent_initial_call=True
)
def update_survey_alternatives_tab_label(n_clicks):
    if n_clicks > 0:
        return "Survey \u2714", "\u2611 1. Alternative Pathways"  # Change the label to indicate submission
    return "Survey \u26A0", "1. Alternative Pathways"  # Default label if no submissions

@app.callback(
    [Output("survey-tab-pathways_performance", "label"),
    Output("navigation-pathways_performance", "children")],
    Input("submit-survey-pathways_performance", "n_clicks"),
    prevent_initial_call=True
)
def update_survey_performance_tab_label(n_clicks):
    if n_clicks > 0:
        return "Survey \u2714", "\u2611 2. Pathway Performance"  # Change the label to indicate submission
    return "Survey \u26A0", "2. Pathway Performance"  # Default label if no submissions

@app.callback(
    [Output("survey-tab-interaction_effects", "label"),
    Output("navigation-interaction_effects", "children")],
    Input("submit-survey-interaction_effects", "n_clicks"),
    prevent_initial_call=True
)
def update_survey_interaction_tab_label(n_clicks):
    if n_clicks > 0:
        return "Survey \u2714", "\u2611 4. Interaction effects"  # Change the label to indicate submission
    return "Survey \u26A0", "4. Interaction effects"  # Default label if no submissions
