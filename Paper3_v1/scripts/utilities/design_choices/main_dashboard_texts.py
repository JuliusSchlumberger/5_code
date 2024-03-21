from dash import html
#

DASHBOARD_TITLE = 'Dashboard to Evaluate Multi-Risk Pathways (Sectoral Risk Owner Perspective)'

# DASHBOARD_EXPLANATION = {
#     'title': 'Dashboard Explanation',
#     'body': [
#         "Designed for sectoral risk owners (e.g., farmers, shipping companies, housing companies), this dashboard aids in strategizing against future hazards. Key insights include:",
#         html.Br(),
#         "1. Exploring alternative pathway strategies.",
#         html.Br(),
#         "2. Assessing strategy performance across various scenarios and time horizons.",
#         html.Br(),
#         "3. Understanding the influence of other risk owners' strategies on one's own.",
#         html.Br(), html.Br(),
#         "Specify time horizons, climate scenarios, performance indicators, and strategies from other risk owners to explore strategic options."
#     ]
# }

DASHBOARD_EXPLANATION = {
    'title': 'Dashboard Explanation',
    'body': [
        "Designed for sectoral risk owners (e.g., farmers, shipping companies, housing companies), this dashboard aids in strategizing against future hazards. Key insights include:",
        html.Br(),
        "1. Exploring alternative ",
        html.Abbr("pathway",
                  title="A sequence of actions or strategies aimed at achieving a specific goal.",
                  style={'textDecoration': 'underline', 'textDecorationStyle': 'solid', 'color': 'blue'}),
        " strategies.",
        html.Br(),
        "2. Assessing strategy performance across various scenarios and time horizons.",
        html.Br(),
        "3. Understanding the influence of other risk owners' strategies on one's own.",
        html.Br(), html.Br(),
        "Specify time horizons, climate scenarios, performance indicators, and strategies from other risk owners to explore strategic options."
    ]
}

OPTIONS = {
    'title': '1. Pathway Options Overview',
    'general_introduction': [
        "The first visualization displays alternative pathways available to the sectoral risk owner. Filter the dataset by selecting relevant time horizons and uncertainty scenarios to evaluate these alternatives."
    ]
}

PERFORMANCE = {
    'title': '2. Pathways Performance Analysis',
    'general_introduction': [
        "The second visualization highlights the performance of pathway options based on the specified time horizon and selected scenarios.",
        html.Br(),
        "Choose a performance metric to guide your analysis."
    ]
}

MULTI_RISK = {
    'title': '3. Multi-Risk Interaction Insights',
    'general_introduction': [
        "The third section delves into the interaction effects between different pathway combinations.", html.Br(),
        html.B("(1)"), " Observe changes in the options and performance plots when considering interaction effects.", html.Br(),
        html.B("(2)"), " The adjacent visualization reveals synergistic or trade-off effects of another risk owner's pathway on the performance of your pathways, focusing solely on direct interactions."
    ]
}



TOOLTIP_TEXT = {
    'risk_owner_hazard': 'Choose a risk owner and their relevant hazards to analyze potential pathways.',
    'timehorizon': 'Select the time horizon for evaluating and comparing pathway outcomes.',
    'scenarios': 'Choose one or more scenarios for analysis. Each scenario is weighted equally when assessing performance across multiple scenarios.',
    'confidence': 'Consider removing this option.',
    'pathways': 'Enables highlighting of specific pathways in the analysis, enhancing the visibility of their performance and interactions.',
    'which_option': 'Consider removing this option.',
    'performance_metric': 'Select a performance metric for evaluating outcomes. Metrics aggregate performance variations under different futures (e.g., climate or interaction scenarios) into confidence intervals. Choose from optimistic (5% CI), expected (50% CI), or pessimistic (95% CI) perceptions.',
    'multi_sectoral_interactions': 'Select other risk owners to examine their impact on your selected pathways and performance metrics.',
    'interaction_objective_of_interest': 'Pick an objective pertinent to your risk owner and hazard to investigate specific interactions affecting pathways.'
}
