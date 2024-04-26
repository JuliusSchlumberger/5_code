import dash
from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
import plotly.io as pio
import plotly.graph_objects as go  # Import Plotly's graph_objects module
import base64
from dashapp import app

@app.callback(
    [Output('alternatives-image', 'src')],
    Input('risk_owner_hazard', 'value'))
def update_legends(risk_owner_hazard):
    # Define the path to the image
    file_path = f'assets/legends/{risk_owner_hazard}_full_legend.png'
    # Encode the image to base64 string using with statement
    with open(file_path, 'rb') as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode('ascii')

    # Return the data URI for the image
    return f'data:image/png;base64,{encoded_image}'