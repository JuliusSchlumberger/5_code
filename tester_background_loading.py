

from dash import Dash, html, dcc, Input, Output, State, dash
import json
from celery.result import AsyncResult
from tester_celery_app import load_file, celery_app  # Import the Celery app and the task

app = Dash(__name__)

app.layout = html.Div([
    html.Button("Load Data", id="load-data-btn", n_clicks=0),
    html.Div(id="data-status"),
    dcc.Interval(id="poll-interval", interval=2000, n_intervals=0, disabled=True)
])

@app.callback(
    Output("poll-interval", "disabled"),
    Input("load-data-btn", "n_clicks"),
    prevent_initial_call=True
)
def trigger_data_loading(n_clicks):
    if n_clicks > 0:
        # Assuming 'file1.csv' is the file you want to load. Adjust as necessary.
        load_file.delay(f'Paper3_v1/data/pathways_timehorizon/counts/objectives_for_count_combinations_flood_agr_flood_urb.csv')
        return False  # Enable the interval component
    return dash.no_update

@app.callback(
    Output("data-status", "children"),
    Input("poll-interval", "n_intervals"),
    State("poll-interval", "disabled"),
    prevent_initial_call=True
)
def poll_data_status(n, disabled):
    if disabled:
        return dash.no_update
    # Assuming we're only dealing with one task for simplicity
    task = AsyncResult(load_file.AsyncResult.id, app=celery_app)
    if task.state == 'SUCCESS':
        return f"Data loaded: {task.result}"
    return "Loading data..."

if __name__ == "__main__":
    app.run_server(debug=True)
