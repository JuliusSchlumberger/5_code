import dash
from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
import plotly.io as pio
import plotly.graph_objects as go  # Import Plotly's graph_objects module

from dashapp import app



@app.callback(
    Output('interactions-graph', 'figure'),
    [Input('session-store_performance', 'data'),
    Input('session-store_alternatives', 'data'),
Input('session-store_interaction', 'data')
#     [
# State('session-store_alternatives', 'data'),
     ],
)
def update_interaction_graph(stored_data_performance, stored_data_alternatives, stored_data_interactions):
    # print(stored_data)
    # Return empty figure if not all needed inputs are specified
    if any(input_value is None for input_value in
           [stored_data_alternatives['risk_owner_hazard'], stored_data_performance['timehorizon'], stored_data_performance["scenarios"], stored_data_performance['performance_metric'], stored_data_interactions['interactions_of_interest'], stored_data_interactions['interaction_plot']]):
        return go.Figure()
    else:
        if len(stored_data_performance["scenarios"]) > 1:
            scenario_str = '&'.join(stored_data_performance["scenarios"])
        else:
            scenario_str = stored_data_performance["scenarios"][0]
        interaction_str = stored_data_alternatives['risk_owner_hazard'] + '&' + '&'.join(stored_data_interactions['interactions_of_interest'])
        file_path = f'assets/figures/{stored_data_performance["plot_type"]}/{stored_data_alternatives["risk_owner_hazard"]}/{interaction_str}/plot_{stored_data_performance["timehorizon"]}_{scenario_str}_{stored_data_performance["performance_metric"]}.json'

        with open(file_path, 'r') as f:
            fig = pio.from_json(f.read())

        return fig

