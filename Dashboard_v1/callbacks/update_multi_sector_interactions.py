import dash
from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
import plotly.io as pio
import plotly.graph_objects as go  # Import Plotly's graph_objects module

from dashapp import app

ROH_DICT = {
    'farmer - flood': 'flood_agr',
    'farmer - drought': 'drought_agr',
    'ship company - drought': 'drought_shp',
    'municipality - flood': 'flood_urb'
}

@app.callback(
    Output('multi_sectoral_interactions', 'options'),
    Input('session-store_alternatives', 'data'))
def set_multi_sector_interaction_options(stored_data_interactions):
    if stored_data_interactions['risk_owner_hazard'] is None:
        # Return empty list or default options if selected_risk_hazard is None or not found
        return []
    # Filter out selected_risk_hazard from the ROH list
    filtered_options = [i for i in ROH_DICT if ROH_DICT[i] != stored_data_interactions['risk_owner_hazard']]
    # print(selected_risk_hazard)
    return [{'label': i, 'value': ROH_DICT[i]} for i in filtered_options]