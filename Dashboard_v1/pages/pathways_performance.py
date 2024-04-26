import dash
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/pathways_performance')


visualization = dbc.Col([
    dbc.Row(dcc.Graph(id='performance-graph', responsive=True), style={'flex': '1'}),
    dbc.Row(html.Img(id='alternatives-image', src='', style={'align': 'middle'}), style={'height': '20%'}),
], style={'display': 'flex', 'flexDirection': 'column', 'height': '80vh'}, width=8)


# Define the tabs
tabs = dbc.Tabs(
    [
        dbc.Tab(label="Explanation", tab_id="tab-explanation-pathways_performance"),
        dbc.Tab(label="Survey \u26A0", tab_id="tab-survey-pathways_performance",  id="survey-tab-pathways_performance")
    ],
    id="tabs-pathways_performance",
    active_tab="tab-explanation-pathways_performance",
)


# Define the tab content
tab_content = html.Div(id="tab-content-pathways_performance", style={'margin-top': '1vh'})


layout = dbc.Row(
    [dbc.Col([
        tabs,
        tab_content], width=4, style={'height': '90vh'}),
     visualization],
    style={'height': '90vh'}
)
