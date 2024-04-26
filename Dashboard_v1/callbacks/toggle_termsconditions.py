import dash
from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
from dashapp import app



# Callback to toggle the enable state of the 'Agree' button based on the checkbox
@app.callback(
    Output("close-termsconditions", "disabled"),
    Input("terms-check", "value")
)
def toggle_agree_button(checkbox_value):
    return len(checkbox_value) == 0  # Button is disabled if checkbox is not checked

# Callback to handle closing the modal and showing content
@app.callback(
    Output("termsconditions", "is_open"),
    Output("content", "style"),
    Input("close-termsconditions", "n_clicks"),
    Input("close-termsconditions", "disabled"),
    prevent_initial_call=True
)
def toggle_initial_agreement(n, close_disabled):
    if n > 0 and close_disabled == False:   # submit activated
        print('did accept')
        return False, {'height': '90vh'}   # Hide modal and show content
    return True, {"display": "none", }  # Default state

