import dash
from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
import plotly.io as pio
import plotly.graph_objects as go  # Import Plotly's graph_objects module
import json
from dashapp import app
from datetime import datetime
import uuid

def generate_session_id():
    # Current time with microseconds to ensure uniqueness as much as possible
    current_time = datetime.now().strftime("%Y%m%d%H%M%S%f")
    # Generate a random UUID
    unique_id = str(uuid.uuid4())
    # Combine them
    session_id = f"{current_time}"
    return session_id

@app.callback(
    Output('storage-general', 'data'),
    Input('storage-general', 'data'),
    prevent_initial_call=False
)
def create_session_id(storage):
    print(storage)
    if not storage:
        print('test', generate_session_id())
        return {'existing_id': generate_session_id()}
    return storage

