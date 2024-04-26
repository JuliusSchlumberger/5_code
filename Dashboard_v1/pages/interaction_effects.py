import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/interaction_effects')



visualization = dbc.Col([
    dbc.Row(dcc.Graph(id='interactions-graph', responsive=True), style={'flexGrow': 1}),
    dbc.Row(html.Img(id='alternatives-image', src=''), style={'height': '20%', 'justifyContent': 'center'}),
], style={'display': 'flex', 'flexDirection': 'column', 'height': '80vh', 'align':'top'}, width=8)


# Define the tabs
tabs = dbc.Tabs(
    [
        dbc.Tab(label="Explanation", tab_id="tab-explanation-interaction_effects"),
        dbc.Tab(label="Survey \u26A0", tab_id="tab-survey-interaction_effects",  id="survey-tab-interaction_effects")
    ],
    id="tabs-interaction_effects",
    active_tab="tab-explanation-interaction_effects",
)


# Define the tab content
tab_content = html.Div(id="tab-content-interaction_effects", style={'margin-top': '1vh'})


layout = dbc.Row(
    [dbc.Col([
        tabs,
        tab_content], width=4, style={'height': '90vh'}),
     visualization],
    style={'height': '90vh'}
)
