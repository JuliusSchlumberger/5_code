import dash
from dash import dcc, html
import dash_bootstrap_components as dbc


introduction = html.Div([
    html.P(
        "This dashboard is designed to test how different visualizations can be used to for the evaluation of Disaster Risk Management pathways in a multi-risk setting."
        "The dashboard is set in a synthetic case study. In the case study "
        "three sectoral risk owners (farmer, shipping company and a municipality) want to identify pathways to adapt to increasing risk of floods and droughts due to climate change. "
        "One of the main question is what are the most appropriate pathways for these sectoral risk owners, considering "
        "the interactions between pathways of different sectoral risk owners. "
        "The objective is to identify combination of pathways that serve all sectoral risk owners and minimize tradeoffs. "),
    html.P([
               "This dashboard is designed to support a sectoral risk owners in the evaluation of their pathway options. Key insights include:",
               html.Br(),
               "1. Identify what alternative pathway options are on the table.",
               html.Br(),
               "2. Assess the performance of different pathways across various scenarios and time horizons.",
               html.Br(),
               "3. Understand the influence of other risk owners' pathways on one's own."]),
    html.P(
        "As a user, you will take the role of a sectoral risk owner and use the visualizations to extract some information relevant for evaluating pathways. "
        "You can specify time horizons, climate scenarios, performance indicators of interest, and select what interactions with pathways from other risk owners should be explored."),
], style={'height': '80vh', 'overflow-y': 'auto'})

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




general_introduction_alternatives= [
        "In the first section of the dashboard you learn about your pathways options as sectoral risk owner to deal with a specific hazard. ",
        html.Br(),
        html.B('(1)'), " Explore what measures are part of the different pathways options.",
        html.Br(),
        html.B('(2)'), " Explore how the sequences of measures are implemented in the selected time horizon and under different climate scenarios.",
        html.Br(),
        html.Br(),
         "Select your role as sectoral risk owner and respective parameters for the evaluation."
    ]

ROH_DICT = {
    'farmer - flood': 'flood_agr',
    'farmer - drought': 'drought_agr',
    'ship company - drought': 'drought_shp',
    'municipality - flood': 'flood_urb'
}

alternative_pathways = html.Div([
    # html.H4('Explanation', style={'marginBottom': '1%'}),
    html.P(html.I('Make choices regarding the visualization and get some additional information here.')),

    html.Div(general_introduction_alternatives, style={'marginBottom': '1%'}),
    dbc.Row([
        dbc.Col(html.Label('a) Select Risk Owner - Hazard', className='mb-1'), width=5),
        dbc.Col(dcc.Dropdown(
            id='risk_owner_hazard',
            options=[{'label': option, 'value': ROH_DICT[option]} for option in ROH_DICT],
        ), width=6),
    ], style={'alignItems': 'start'}),
], style={'height': '80vh', 'overflow-y': 'auto'})



general_introduction_performance= [
        "In the second section of the dashboard, you can explore the performance of the pathways in the selected time horizon and under different climate scenarios:",
        html.Br(),
        html.B('(1)'), " Explore the performance of different pathways options across the performance criteria.",
        html.Br(),
        html.B('(2)'), " Explore how the performance evaluation changes for differernt performance indicators. ",
    ]


WHICH_OPTIONS = {
    'Parallel Coordinates Plot': 'PCP',
    'Stacked Bar': 'StackedBar',
    'Heatmap': 'Heatmap'
}

TIMEHORIZONS = {
    'next 20 years': 20,
    'next 60 years': 60,
    'next 100 years': 100
}


SCENARIOS = {
    'historic': 'D',
    '1.5 Deg': 'G',
    '4 Deg': 'Wp'
}

PERFORMANCE_METRICS = {
    '5% confidence interval': '5%',
    '50% confidence interval': '50%',
    '95% confidence interval': '95%',
    'expected performance': 'average'
}


pathways_performance = html.Div(
    [
        html.Div([
            # html.H3('2. Pathways Performance Analysis', style={'marginBottom': '1%'}),
            html.P(html.I('Make choices regarding the visualization and get some additional information here.')),
            html.Div(general_introduction_performance, style={'marginBottom': '1%'}),

            # Use two columns inside a single row for each label-control pair for compact arrangement.
            dbc.Row([
                dbc.Col(html.Label('a) dev: Plot Alternatives', className='mb-1'), width=5),
                dbc.Col(dcc.Dropdown(
                    id='options',
                    options=[{'label': option, 'value': WHICH_OPTIONS[option]} for option in WHICH_OPTIONS],
                ), width=6),
            ], style={'marginBottom': '2vh', 'alignItems': 'start'}),

            dbc.Row([
                dbc.Col(html.Label('b) Timehorizon for Evaluation', className='mb-1'), width=5),
                dbc.Col(dcc.Dropdown(
                    id='timehorizon',
                    options=[{'label': option, 'value': TIMEHORIZONS[option]} for option in TIMEHORIZONS],
                ), width=6),
            # ], style={'marginBottom': '2vh', 'alignItems': 'start'}),
            ], style={'marginBottom': '2vh', 'alignItems': 'start'}),

            dbc.Row([
                dbc.Col(html.Label('c) Climate Scenarios', className='mb-1'), width=5),
                dbc.Col(dcc.Checklist(
                    id='scenarios',
                    options=[{'label': option, 'value': SCENARIOS[option]} for option in SCENARIOS],
                    inline=True, inputStyle={"marginRight": "1vh", "marginLeft": "1vh"},
                ), width=6),
            ], style={'marginBottom': '2vh', 'alignItems': 'start'}),

            dbc.Row([
                dbc.Col(html.Label('d) Performance Indicator', className='mb-1'), width=6),
                dbc.Col(dcc.Dropdown(
                    id='performance_metric',
                    options=[{'label': option, 'value': PERFORMANCE_METRICS[option]} for option in PERFORMANCE_METRICS],
                ), width=5),
            ], style={'marginBottom': '2vh', 'alignItems': 'start'}),

            # Modal buttons span almost the entire row
            dbc.Row([
                dbc.Col(dbc.Button("Show Explanation Performance Analysis", id="open-modal-performance_analysis", className="me-2", n_clicks=0), width={"size": 11, "offset": 0}),
                dbc.Modal([
                    dbc.ModalHeader(dbc.ModalTitle("Performance Analysis Explanation")),
                    dbc.ModalBody(id="modal-body-performance_analysis"),  # Content will be set dynamically
                    dbc.ModalFooter(
                        dbc.Button("Close", id="close-modal-performance_analysis", className="ms-auto", n_clicks=0)
                    ),
                ], id="performance_analysis-modal", is_open=False),
            ], style={'marginBottom': '2vh', 'alignItems': 'start'}),

            dbc.Row([
                dbc.Col(dbc.Button("Show Explanation Performance Figure", id="open-modal-performance_figure", className="me-2", n_clicks=0), width={"size": 11, "offset": 0}),
                dbc.Modal([
                        dbc.ModalHeader(dbc.ModalTitle("Figure Explanation")),
                        dbc.ModalBody(id="modal-body-performance_figure"),  # Content will be set dynamically
                        dbc.ModalFooter(
                            dbc.Button("Close", id="close-modal-performance_figure", className="ms-auto", n_clicks=0)
                        ),
                    ], id="performance_figure-modal", is_open=False),
            ], style={'marginBottom': '2vh', 'alignItems': 'start'}),
        ], style={'height': '80vh', 'overflow-y': 'auto'}),
    ]
)


general_introduction= [
         "In the third section, you can explore how your pathways options and performance are affected by other sectoral risk owner pathways:", html.Br(),
        html.B("(1)"), " Observe changes in the pathways options when considering interaction effects.", html.Br(),
        html.B("(2)"), " Observe changes in the performance when considering interaction effects."
    ]

ROH_DICT = {
    'farmer - flood': 'flood_agr',
    'farmer - drought': 'drought_agr',
    'ship company - drought': 'drought_shp',
    'municipality - flood': 'flood_urb'
}

INTERACTION_VIZ = {
    # 'Pathways Options': 'image',
    'Pathways Performance': 'graph'
}

interaction_effects = html.Div(
    [
        # html.H3('3. Multi-Risk Interaction Insights', style={'marginBottom': '1%'}),
        html.P(html.I('Make choices regarding the visualization and get some additional information here.')),

        html.Div(general_introduction, style={'marginBottom': '2%'}),
        dbc.Row([
            dbc.Col([
                html.Label('a) Multi-sectoral interactions (multiple-choice)', className='mb-1'),
                dcc.Checklist(id='multi_sectoral_interactions', style={'marginRight': '0'}),
            ], width=6, style={'marginBottom': '1%', 'alignItems': 'start'}),
        ], style={'marginBottom': '1%', 'alignItems': 'start'}),
        dbc.Row([
            dbc.Col([
                html.Label('b) Explore interaction effects on...', className='mb-1')
            ], width=8),
            dbc.Col([
                dcc.Dropdown(id='interaction_plot_options',
                             options=[{'label': option, 'value': INTERACTION_VIZ[option]} for option in INTERACTION_VIZ],
                             style={'width': '100%', 'alignItems': 'start'}),
            ]),
        ], style={'marginBottom': '1%', 'alignItems': 'start'}),
    ],
    style={'height': '80vh', 'overflow-y': 'auto'},
)
