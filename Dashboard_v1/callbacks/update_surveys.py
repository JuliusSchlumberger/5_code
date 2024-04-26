import dash
from dash import html, dcc, callback, Input, Output, State, callback_context
import dash_bootstrap_components as dbc
import plotly.io as pio
import plotly.graph_objects as go  # Import Plotly's graph_objects module

from dashapp import app

import dash
from dash import dcc, html, Input, Output, State, callback_context
import plotly.graph_objects as go
import plotly.io as pio


# Callback to control the visibility of the text input based on selection
@app.callback(
    Output('gender-container', 'children'),
    Input('gender-radio', 'value')
)
def update_gender_input(selected_value):
    if selected_value == 'Prefer to self-describe':
        return dcc.Input(
            id='custom-gender-input',
            type='text',
            placeholder='Please describe...'
        )
    return None  # No input field if other options are selected

# Callback to control the visibility of the text input based on selection
@app.callback(
    Output('impairment-container', 'children'),
    Input('impairment-radio', 'value')
)
def update_impairment_input(selected_value):
    if selected_value == 'Yes':
        return dcc.Input(
            id='custom-impairment-input',
            type='text',
            placeholder='Please describe...'
        )
    return None  # No input field if other options are selected
