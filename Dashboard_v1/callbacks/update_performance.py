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


@app.callback(
    [
        Output('performance-graph', 'figure'),
        Output('storage-pathways_performance', 'data'),
        Output('timehorizon', 'value'),
        Output('scenarios', 'value'),
        Output('performance_metric', 'value'),
        Output('options', 'value')
    ],
    [
        Input('timehorizon', 'value'),
        Input('scenarios', 'value'),
        Input('performance_metric', 'value'),
        Input('options', 'value')
    ],
    [State('storage-pathways_performance', 'data'),
     State('storage-alternative_pathways', 'data'),]
)
def update_performance_graph(timehorizon, scenarios, performance_metric, options, stored_data_performance, stored_data_alternatives):
    if all(input_value is not None for input_value in
               [timehorizon, scenarios, performance_metric, options]):   # if this is not empty
        stored_data_performance['timehorizon'] = timehorizon
        stored_data_performance['scenarios'] = scenarios
        stored_data_performance['performance_metric'] = performance_metric
        stored_data_performance['options'] = options
    else:
        if any(input_value is None for input_value in
               [stored_data_performance['timehorizon'], stored_data_performance['scenarios'],
                stored_data_performance['performance_metric'], stored_data_performance['options']]):
            return go.Figure(), dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update

    # Assume we have necessary details in stored_data_performance to generate the figure
    scenario_str = '&'.join(stored_data_performance['scenarios']) if len(stored_data_performance['scenarios'])>1 else stored_data_performance['scenarios'][0]
    file_path = f'assets/figures/{stored_data_performance["options"]}/' \
                f'{stored_data_alternatives["risk_owner_hazard"]}/' \
                f'plot_{stored_data_performance["timehorizon"]}_{scenario_str}_{stored_data_performance["performance_metric"]}.json'
    with open(file_path, 'r') as f:
        fig = pio.from_json(f.read())
    return fig, stored_data_performance, stored_data_performance['timehorizon'], stored_data_performance['scenarios'], \
           stored_data_performance['performance_metric'], stored_data_performance['options']

#
#
# @app.callback(
#     [
#         Output('performance-graph', 'figure'),
#         Output('storage-pathways_performance', 'data'),
#         Output('timehorizon', 'value'),
#         Output('scenarios', 'value'),
#         Output('performance_metric', 'value'),
#         Output('options', 'value')
#     ],
#     [
#         Input('timehorizon', 'value'),
#         Input('scenarios', 'value'),
#         Input('performance_metric', 'value'),
#         Input('options', 'value')
#     ],
#     [
#         State('storage-alternative_pathways', 'data'),
#         State('storage-pathways_performance', 'data')
#     ],
# )
# def update_performance_graph(timehorizon, scenarios, performance_metric, options, stored_data_alternatives, stored_data_performance):
#     ctx = dash.callback_context
#
#     # Initialize stored data if it's not present
#     if not stored_data_performance:
#         stored_data_performance = {}
#
#     # Update stored data from inputs if available
#     inputs = [timehorizon, scenarios, performance_metric, options]
#     keys = ['timehorizon', 'scenarios', 'performance_metric', 'options']
#     for key, input_value in zip(keys, inputs):
#         if input_value is not None:
#             stored_data_performance[key] = input_value
#         elif key not in stored_data_performance:
#             stored_data_performance[key] = None  # Use a default or previous state
#
#     # Handle missing data and early exit if necessary
#     if any(value is None for value in [stored_data_alternatives.get('risk_owner_hazard'), *inputs]):
#         return go.Figure(), stored_data_performance, timehorizon, scenarios, performance_metric, options
#
#     # Assume all needed inputs are specified correctly
#     if scenarios:
#         scenario_str = '&'.join(scenarios) if isinstance(scenarios, list) and len(scenarios) > 1 else scenarios[0]
#     else:
#         scenario_str = 'default_scenario'  # Set a default or handle empty scenario list
#
#     file_path = f'assets/figures/{stored_data_performance.get("options", "default_type")}/{stored_data_alternatives.get("risk_owner_hazard", "default_hazard")}/plot_{stored_data_performance.get("timehorizon", "default_time")}_{scenario_str}_{stored_data_performance.get("performance_metric", "default_metric")}.json'
#
#     try:
#         with open(file_path, 'r') as f:
#             fig = pio.from_json(f.read())
#     except FileNotFoundError:
#         fig = go.Figure()
#
#     return fig, stored_data_performance, timehorizon, scenarios, performance_metric, options

# @app.callback(
#     [Output('timehorizon', 'value'),
#    Output('scenarios', 'value'),
#    Output('performance_metric', 'value'),
#    Output('options', 'value')],
#     Input('url', 'pathname'),
# State('storage-pathways_performance', 'data')
# )
# def uptade_performance_entries(pathname,storage_data):
#     print('update_entrie', storage_data)
#     # Identify which input triggered the callback
#     trigger_id = callback_context.triggered[0]['prop_id'].split('.')[0]
#     if pathname == '/pathways_performance':
#         print('tester', storage_data['performance_metric'], storage_data['timehorizon'])
#
#         return 60, storage_data['scenarios'],storage_data['performance_metric'],storage_data['options']
#     else:
#         print('second_check')
#         return dash.no_update, dash.no_update, dash.no_update, dash.no_update