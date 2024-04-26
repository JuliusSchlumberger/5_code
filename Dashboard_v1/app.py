
import dash_bootstrap_components as dbc
from dash import dcc, Input, Output, html
from components import sidebar, content, header, TermsConditions
# from callbacks import toggle_tabs
import dash
from callbacks import toggle_glossary, toggle_tabs, update_alternatives, add_legend, \
    toggle_performance_explanation, toggle_performance_figure, update_performance, \
    update_multi_sector_interactions, update_interaction_plot, submit_responses, update_survey_tab_title, generate_session_id, toggle_termsconditions, update_surveys


from dashapp import app

app.layout = dbc.Container([
        dcc.Location(id='url', refresh=False),
        dcc.Store(id='storage-alternative_pathways', storage_type='session', data={}),  # Using session storage
        dcc.Store(id='storage-pathways_performance', storage_type='session', data={}),  # Using session storage
        dcc.Store(id='storage-interactions', storage_type='session', data={}),  # Using session storage
        dcc.Store(id='storage-general', storage_type='session', data={}),  # Using session storage
        header.header,
        TermsConditions.TermConditions,
        dbc.Row([sidebar.sidebar,
                 content.content], className="mb-0", id="content", style={"display": "none", 'height': '90vh'}),
    ],
    fluid=True, style={'height': '100vh'},  # Change to 100vh to fill the screen height
)



if __name__ == '__main__':
    app.run_server(debug=True)