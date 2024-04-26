import dash
from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
import plotly.io as pio
import plotly.graph_objects as go  # Import Plotly's graph_objects module
import json
from dashapp import app
from datetime import datetime

# input datetime
dt = datetime(2018, 10, 22, 0, 0)

@app.callback(
    Output('interactions-container', 'children'),
    Input('submit-survey-interactions', 'n_clicks'),
    [State('age-input', 'value'),
    State('storage-general', 'data')]
)
def save_answers_interactions(n_clicks, age, session_id):
    if n_clicks > 0:
        # Unique identifier - customize this as per your requirement
        unique_id = "response_introduction"
        filename = f"responses/{unique_id}_{session_id['existing_id']}.json"

        # Data to save
        data = {
            "age": age,
        }

        # Write data to a file
        with open(filename, 'w') as file:
            json.dump(data, file)
        return f'Your response has been saved ({n_clicks}).'
    else:
        return 'Please submit your response.'

@app.callback(
    Output('alternative_pathways-container', 'children'),
    Input('submit-survey-alternative_pathways', 'n_clicks'),
    State('pathway_number-input', 'value'),
    State('f_resilient_crops-input', 'value'),
    State('long_term-input', 'value'),
    State('flexibility-level', 'value'),
    State('storage-general', 'data')
)
def save_answers_alternatives(n_clicks, pathway_number, f_resilient_crops, long_term,flexibility, session_id):
    if n_clicks > 0:
        # Unique identifier - customize this as per your requirement
        unique_id = "response_alternatives"
        filename = f"responses/{unique_id}_{session_id['existing_id']}.json"

        # Data to save
        data = {
            "pathway_number": pathway_number,
            "pathway_number": pathway_number,
            "f_resilient_crops": f_resilient_crops,
            "long_term": long_term,
            "flexibility":flexibility
        }

        # Write data to a file
        with open(filename, 'w') as file:
            json.dump(data, file)
        return f'Your response has been saved ({n_clicks}).'
    else:
        return 'Please submit your response.'

@app.callback(
    Output('pathways_performance-container', 'children'),
    Input('submit-survey-pathways_performance', 'n_clicks'),
    State('color-input', 'value'),
    State('crop_loss-input', 'value'),
    State('performance-input', 'value'),
    State('tradeoff-input', 'value'),
    State('storage-general', 'data')
)
def save_answers_performance(n_clicks, color, crop_loss, performance,tradeoff, session_id):
    if n_clicks > 0:
        # Unique identifier - customize this as per your requirement
        unique_id = "response_pathways"
        filename = f"responses/{unique_id}_{session_id['existing_id']}.json"

        # Data to save
        data = {
            "color": color,
            "crop_loss": crop_loss,
            "performance": performance,
            "tradeoff": tradeoff,
        }

        # Write data to a file
        with open(filename, 'w') as file:
            json.dump(data, file)
        return f'Your response has been saved ({n_clicks}).'
    else:
        return 'Please submit your response.'

@app.callback(
    Output('interaction_effects-container', 'children'),
    Input('submit-survey-interaction_effects', 'n_clicks'),
    State('measure_shift-input', 'value'),
    State('performance_change-input', 'value'),
    State('strong_tradeoffs-input', 'value'),
    State('strong_synergy-input', 'value'),
    State('storage-general', 'data')
)
def save_answers_interactions(n_clicks, measure_shift, performance_change, strong_tradeoffs,strong_synergy, session_id):
    if n_clicks > 0:
        # Unique identifier - customize this as per your requirement
        unique_id = "response_interactions"
        filename = f"responses/{unique_id}_{session_id['existing_id']}.json"

        # Data to save
        data = {
            "measure_shift": measure_shift,
            "performance_change": performance_change,
            "strong_tradeoffs": strong_tradeoffs,
            "strong_synergy": strong_synergy,
        }

        # Write data to a file
        with open(filename, 'w') as file:
            json.dump(data, file)
        return f'Your response has been saved ({n_clicks}).'
    else:
        return 'Please submit your response.'
