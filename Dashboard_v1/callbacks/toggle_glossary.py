import dash
from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
from dashapp import app

# Define callback to toggle the modal
@app.callback(
    Output("glossary-modal", "is_open"),
    [Input("open-glossary", "n_clicks"), Input("close-glossary", "n_clicks")],
    [State("glossary-modal", "is_open")],
)
def toggle_glossary(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open