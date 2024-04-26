import dash
from dash import html, dcc, callback, Input, Output, State,callback_context
import dash_bootstrap_components as dbc
import plotly.io as pio
import plotly.graph_objects as go  # Import Plotly's graph_objects module

from dashapp import app

@app.callback(
    [Output('alternatives-graph', 'figure'),
Output('storage-alternative_pathways', 'data'),
     Output('risk_owner_hazard', 'value')],
    [Input('risk_owner_hazard', 'value'),
     ],
State('storage-alternative_pathways', 'data'),
)
def update_options_graph(risk_owner_hazard, stored_data):

    print(risk_owner_hazard)

    if risk_owner_hazard is not None:   # if this is not empty
        stored_data['risk_owner_hazard'] = risk_owner_hazard
        relevant_input = risk_owner_hazard
    else:
        if any(input_value is None for input_value in
               [stored_data['risk_owner_hazard']]):
            return go.Figure(), dash.no_update, dash.no_update
        relevant_input = stored_data['risk_owner_hazard']

    print(stored_data)
    figure_identifier = f'assets/figures/decision_tree/alternative_pathways_{relevant_input}.json'

    with open(figure_identifier, 'r') as f:
        fig = pio.from_json(f.read())
    print('relevant_input', relevant_input)
    return fig, stored_data, relevant_input
