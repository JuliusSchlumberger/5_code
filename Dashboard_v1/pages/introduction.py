import dash
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/')



# Define the tabs
tabs = dbc.Tabs(
    [
        dbc.Tab(label="Explanation", tab_id="tab-explanation-introduction"),
        dbc.Tab(label="Survey \u26A0", tab_id="tab-survey-introduction",  id="survey-tab-introduction")
    ],
    id="tabs-introduction",
    active_tab="tab-explanation-introduction",
)


# Define the tab content
tab_content = html.Div(id="tab-content-introduction", style={'margin-top': '1vh'})


layout = dbc.Row(
    [dbc.Col([
        tabs,
        tab_content], width=10, style={'height': '90vh'}),
    ],
    style={'height': '90vh'}
)


