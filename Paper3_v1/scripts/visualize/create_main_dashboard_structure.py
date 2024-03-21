# Import required libraries
from dash import dcc, html
# from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from Paper3_v1.scripts.utilities.design_choices.main_dashboard_design_choices import PANEL_BACKGROUND,DASHBOARD_BACKGROUND, DASHBOARD_DIMENSIONS
from Paper3_v1.scripts.utilities.design_choices.main_dashboard_texts import *
from Paper3_v1.scripts.utilities.design_choices.main_dashboard_dropdowns import ROH_DICT, TIMEHORIZONS, SCENARIOS, CONFIDENCE, WHICH_OPTIONS, PERFORMANCE_METRICS


def create_main_dashboard_structure(app):
    app.layout = html.Div([
        html.H1(DASHBOARD_TITLE, style={'textAlign': 'center'}),

        # New panel for General Comments
        html.Div([
            html.H2(DASHBOARD_EXPLANATION['title']),
            # *[html.P(paragraph) for paragraph in DASHBOARD_EXPLANATION['body']]
            html.P(DASHBOARD_EXPLANATION['body']
                ),
        ], style={'backgroundColor': PANEL_BACKGROUND, 'padding': DASHBOARD_DIMENSIONS['padding'],
                  'marginBottom': DASHBOARD_DIMENSIONS['margin'], 'width': '100%'}),

        # Div for the left panel (Explanation and Interaction Buttons)
        html.Div([
            # Showing Options
            html.Div([
                html.H3(OPTIONS['title']),
                html.Div(OPTIONS['general_introduction'],style={'marginBottom': '5vh'}),
                dbc.Row([
                    dbc.Col([
                        html.Label('a) Select Risk Owner - Hazard', className='mb-1')], width=6,),
                    dbc.Col([
                        html.Label('b) Timehorizon for Evaluation', className='mb-1')], width=6,)]),
                dbc.Row([
                    dbc.Col([
                        dcc.Dropdown(id='risk_owner_hazard',
                                     options=[{'label': option, 'value': ROH_DICT[option]} for option in ROH_DICT],
                                     value = ROH_DICT[list(ROH_DICT.keys())[0]]
                                     ),
                    ], style={'marginRight': '-1vw'}, width=5),

                    dbc.Col(dbc.Button("?", id="tooltip-risk_owner_hazard"), width=1),

                    dbc.Col([
                        dcc.Dropdown(id='timehorizon',
                                     options=[{'label': option, 'value': TIMEHORIZONS[option]} for option in TIMEHORIZONS],
                                     value = TIMEHORIZONS[list(TIMEHORIZONS.keys())[-1]]
                                     ),
                    ], style={'marginRight': '-1vw'}, width=5),

                    dbc.Col(dbc.Button("?", id="tooltip-timehorizon"), width=1),

                ], style={'marginBottom': '2vh'}),

                dbc.Row([
                    dbc.Col([
                        html.Label('c) Scenarios (multiple-choice)', className='mb-1')], width=10, )]),
                dbc.Row([
                    dbc.Col([
                        dcc.Checklist(id='scenarios',
                                     options=[{'label': option, 'value': SCENARIOS[option]} for option in SCENARIOS],
                                     inline=True, inputStyle={"marginRight": "1vh","marginLeft": "2vh"},
                                    value=[SCENARIOS[list(SCENARIOS.keys())[0]]]
                                      ),
                    ], style={'marginRight': '0.5vw'}, width=10),

                    dbc.Col(dbc.Button("?", id="tooltip-scenarios"), width=1),

                ], style={'marginBottom': '2vh'}),

                dbc.Row([
                    dbc.Col([
                        html.Label('d) Risk attitude', className='mb-1')], width=6, ),
                    dbc.Col([
                        html.Label('e) Highlight Pathway Alternative', className='mb-1')], width=6, )]),
                dbc.Row([
                    dbc.Col([
                        dcc.Dropdown(id='confidence',
                                     options=[{'label': option, 'value': CONFIDENCE[option]} for option in CONFIDENCE],
                                     value=CONFIDENCE[list(CONFIDENCE.keys())[0]]
                                     ),
                    ], style={'marginRight': '-1vw'}, width=5),

                    dbc.Col(dbc.Button("?", id="tooltip-confidence"), width=1),

                    dbc.Col([
                        dcc.Dropdown(id='highlight_pathway',
                                     ),
                    ], style={'marginRight': '-1vw'}, width=5),

                    dbc.Col(dbc.Button("?", id="tooltip-pathways"), width=1),

                ], style={'marginBottom': '2vh'}),

            ], style={'backgroundColor': PANEL_BACKGROUND, 'padding': DASHBOARD_DIMENSIONS['padding'], 'marginBottom': DASHBOARD_DIMENSIONS['margin'],
                      'width': '100%', 'height': DASHBOARD_DIMENSIONS['options_panel'] }),

            # Tooltips for the buttons
            dbc.Tooltip(TOOLTIP_TEXT['risk_owner_hazard'], target="tooltip-risk_owner_hazard"),
            dbc.Tooltip(TOOLTIP_TEXT['timehorizon'], target="tooltip-timehorizon"),
            dbc.Tooltip(TOOLTIP_TEXT['scenarios'], target="tooltip-scenarios"),
            dbc.Tooltip(TOOLTIP_TEXT['confidence'], target="tooltip-confidence"),
            dbc.Tooltip(TOOLTIP_TEXT['pathways'], target="tooltip-pathways"),

            # Showing Performance
            html.Div([
                html.H3(PERFORMANCE['title']),
                html.Div(PERFORMANCE['general_introduction'], style={'marginBottom': '5vh'}),
                dbc.Row([
                    dbc.Col([
                        html.Label('a) Best/worst options', className='mb-1')], width=6, ),
                    dbc.Col([
                        html.Label('b) Performance Indicator', className='mb-1')], width=6, )]),
                dbc.Row([
                    dbc.Col([
                        dcc.Dropdown(id='options',
                                     options=[{'label': option, 'value': WHICH_OPTIONS[option]} for option in
                                              WHICH_OPTIONS],
                                     value=WHICH_OPTIONS[list(WHICH_OPTIONS.keys())[0]],
                                     ),
                    ], style={'marginRight': '-1vw'}, width=5),

                    dbc.Col(dbc.Button("?", id="tooltip-which_option"), width=1),

                    dbc.Col([
                        dcc.Dropdown(id='performance_metric',
                                     options=[{'label': option, 'value': PERFORMANCE_METRICS[option]} for option in
                                              PERFORMANCE_METRICS],
                                     value=PERFORMANCE_METRICS[list(PERFORMANCE_METRICS.keys())[0]],
                                     )
                    ], style={'marginRight': '-1vw'}, width=5),

                    dbc.Col(dbc.Button("?", id="tooltip-performance_metric"), width=1),

                ], style={'marginBottom': '2vh'}),

            ], style={'backgroundColor': PANEL_BACKGROUND, 'padding': DASHBOARD_DIMENSIONS['padding'],
                      'marginBottom': DASHBOARD_DIMENSIONS['margin'],
                      'width': '100%', 'height': DASHBOARD_DIMENSIONS['performance_panel']}),

            # Tooltips for the buttons
            dbc.Tooltip(TOOLTIP_TEXT['which_option'], target="tooltip-which_option"),
            dbc.Tooltip(TOOLTIP_TEXT['performance_metric'], target="tooltip-performance_metric"),

            # Exploring Multi-risk Interactions
            html.Div([
                html.H3(MULTI_RISK['title']),
                html.Div(MULTI_RISK['general_introduction'], style={'marginBottom': '5vh'}),
                dbc.Row([
                    dbc.Col([
                        html.Label('a) Multi-sectoral interactions (multiple-choice)', className='mb-1')], width=8, ),
                    ]),
                dbc.Row([
                    dbc.Col([
                        dcc.Checklist(id='multi_sectoral_interactions',),
                    ], style={'marginRight': '-1vw'}, width=8),

                    dbc.Col(dbc.Button("?", id="tooltip-multi_sectoral_interactions"), width=1),

                    ], style={'marginBottom': '2vh'}),
                dbc.Row([
                    dbc.Col([
                        html.Label('b) Objective to explore interaction effects', className='mb-1')], width=8, ),
                ]),
                dbc.Row([
                    dbc.Col([
                        dcc.Dropdown(id='interaction_objective_of_interest', ),
                    ], style={'marginRight': '-1vw'}, width=8),

                    dbc.Col(dbc.Button("?", id="tooltip-interaction_objective_of_interest"), width=1),

                ], style={'marginBottom': '2vh'}),

            ], style={'backgroundColor': PANEL_BACKGROUND, 'padding': DASHBOARD_DIMENSIONS['padding'],
                      'marginBottom': DASHBOARD_DIMENSIONS['margin'],
                      'width': '100%', 'height': DASHBOARD_DIMENSIONS['multi_risk_panel']}),

            # Tooltips for the buttons
            dbc.Tooltip(TOOLTIP_TEXT['multi_sectoral_interactions'], target="tooltip-multi_sectoral_interactions"),
            dbc.Tooltip(TOOLTIP_TEXT['interaction_objective_of_interest'], target="tooltip-interaction_objective_of_interest"),

        ], style={'width': DASHBOARD_DIMENSIONS['left_panel_width'], 'display': 'inline-block',
                  'verticalAlign': 'top'}),

        # Div for the right panels (Figures)
        html.Div([
            # Panel for Showing Options with figure
            html.Div([
                # html.H2('Showing Options'),
                html.Img(id='options-graph', style={'width': DASHBOARD_DIMENSIONS['figure_options']}),
            ], style={'backgroundColor': PANEL_BACKGROUND, 'padding': DASHBOARD_DIMENSIONS['padding'],
                      'marginBottom': DASHBOARD_DIMENSIONS['margin'], 'height': DASHBOARD_DIMENSIONS['options_panel']}),

            # Panel for Performance with figure
            html.Div([
                # html.H2('Performance'),
                dcc.Graph(id='performance-graph', style={'height': DASHBOARD_DIMENSIONS['figure_options'], 'maxHeight': '550px'}),
            ], style={'backgroundColor': PANEL_BACKGROUND, 'padding': DASHBOARD_DIMENSIONS['padding'],
                      'marginBottom': DASHBOARD_DIMENSIONS['margin'], 'height': DASHBOARD_DIMENSIONS['performance_panel']}),

            # Panel for Multi-risk interactions with figure
            html.Div([
                # html.H2('Multi-risk interactions'),
                html.Img(id='interactions-graph', style={'height': DASHBOARD_DIMENSIONS['figure_options_mr']}),
            ], style={'backgroundColor': PANEL_BACKGROUND, 'padding': DASHBOARD_DIMENSIONS['padding'], 'height': DASHBOARD_DIMENSIONS['multi_risk_panel']})
        ], style={'width': DASHBOARD_DIMENSIONS['right_panel_width'], 'display': 'inline-block', 'verticalAlign': 'top',
                  'marginLeft': DASHBOARD_DIMENSIONS['button_vdistance']}),
    ], style={'padding': DASHBOARD_DIMENSIONS['padding_dashboard'], 'backgroundColor': DASHBOARD_BACKGROUND})




    return app



