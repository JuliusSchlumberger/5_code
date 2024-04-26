import dash
from dash import html, dcc, callback, Input, Output, State, callback_context
import dash_bootstrap_components as dbc
import plotly.io as pio
import plotly.graph_objects as go  # Import Plotly's graph_objects module

from dashapp import app

DASHBOARD_EXPLANATION = {
    'detailed_explanation_CI': ["The performance of pathways is tested in a wide range of computational experiments. "
                           "Instead of showing the results for all experiments, you can choose between different "
                           "performance indicators, that aggregate the results of each performance criterion into fewer values.",
                            "You selected 'Confidence Intervals' as an performance indicator. Accordingly, "
                           "you can explore the certainty of results within the set of experiments.",
                            html.Br(),html.Br(),
                            "For example: If you want to be 95% certain about the achieved performance, 95% of all " 
                            "experiments are considered and the worst performance across these experiments is shown. " 
                            "It corresponds to the most conservative performance indication of the pathway. " 
                            "Likewise, being 5% certain about the achieved performance, corresponds to an optimistic" 
                            " perspective, where only the best 5% of the experiments are considered and the worst " 
                            "performance across these scenarios is shown."],
'detailed_explanation_otherPerformance': ["The performance of pathways is tested in a wide range of computational experiments. "
                           "Instead of showing the results for all experiments, you can choose between different "
                           "performance indicators, that aggregate the results of each performance criterion into fewer values.",
                          "You selected 'Robustness Indicator' and an performance indicator. Here, "
                          "we compute robustness across the realizations in terms of the mean results "
                          "and the standard deviation across the computational experiments. As such, "
                          "you don't get insights into the factual performance. Instead the values shown"
                          "are indications which pathways have a preferred expected performance and a low variability."],
}



@app.callback(
    [Output("performance_analysis-modal", "is_open"), Output("modal-body-performance_analysis", "children")],
    [Input("open-modal-performance_analysis", "n_clicks"), Input('performance_metric', 'value'),
     Input("close-modal-performance_analysis", "n_clicks")],
    [State("performance_analysis-modal", "is_open")],
)
def toggle_modal_and_set_content_performance_analysis(open_clicks, performance_metric, close_clicks, is_open):
    triggered_id = callback_context.triggered[0]['prop_id'].split('.')[0]

    # Handle Modal Opening
    if triggered_id == "open-modal-performance_analysis" and open_clicks:
        if performance_metric:
            if performance_metric.endswith('%'):
                text = DASHBOARD_EXPLANATION['detailed_explanation_CI']
            else:
                text = DASHBOARD_EXPLANATION['detailed_explanation_otherPerformance']
            return True, text  # Explicitly open the modal with the content
        else:
            return False, "Select a Performance Indicator."  # Keep the modal closed if no plot type is selected

    # Handle Modal Closing
    elif triggered_id == "close-modal-performance_analysis" and close_clicks:
        return False, dash.no_update  # Explicitly close the modal without changing the content

    return is_open, dash.no_update  # Default: Do not change the modal state or content