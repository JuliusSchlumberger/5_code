import dash
from dash import html, dcc, callback, Input, Output, State, callback_context
import dash_bootstrap_components as dbc
import plotly.io as pio
import plotly.graph_objects as go  # Import Plotly's graph_objects module

from dashapp import app


DASHBOARD_EXPLANATION = {
    'PCP': "A parallel coordinate plot is a way to visualize how each pathway performs across various criteria, "
           "represented by several parallel axes."
           "This plot can uncover relationships between performance criteria and identify clusters of similar pathways. "
           "To read it, follow a line across the axes to see how the variables' values change for a single "
           "data point. Comparing lines can help you spot similarities or differences among data points across "
           "multiple dimensions.",
    'Heatmap': 'A heatmap displays data as a matrix of colored cells, where each color represents a range of values. '
               'The varying shades from light to dark (or through a spectrum of colors) indicate the magnitude of '
               'some variable, such as temperature, frequency, or intensity. This visual representation helps identify '
               'patterns, trends, and outliers at a glance. To read a heatmap, look at the color scale to understand '
               'what each color means, then match the colors in the grid to see how the values change '
               'across two dimensions.',
    'StackedBar': 'A stacked bar chart shows the breakdown of multiple categories stacked on top of each other within'
                  ' bars, where the length of each bar represents the total amount. In this specific chart, a shorter '
                  'total length indicates better performance, allowing you to quickly compare overall performance '
                  'across different pathways options. To interpret this chart, examine the lengths of the bars to '
                  'gauge performance, and look at the segments within each bar to understand the contribution of '
                  'each category to the total.',
}



@app.callback(
    [Output("performance_figure-modal", "is_open"), Output("modal-body-performance_figure", "children")],
    [Input("open-modal-performance_figure", "n_clicks"), Input('options', 'value'),
     Input("close-modal-performance_figure", "n_clicks")],
    [State("performance_figure-modal", "is_open")],
)
def toggle_modal_and_set_content_performance_figure(open_clicks, plot_type, close_clicks, is_open):
    triggered_id = callback_context.triggered[0]['prop_id'].split('.')[0]

    # Handle Modal Opening
    if triggered_id == "open-modal-performance_figure" and open_clicks:
        if plot_type:
            text = DASHBOARD_EXPLANATION[plot_type]
            return True, text  # Explicitly open the modal with the content
        else:
            return False, "Select a Plot type."  # Keep the modal closed if no plot type is selected

    # Handle Modal Closing
    elif triggered_id == "close-modal-performance_figure" and close_clicks:
        return False, dash.no_update  # Explicitly close the modal without changing the content

    return is_open, dash.no_update  # Default: Do not change the modal state or content