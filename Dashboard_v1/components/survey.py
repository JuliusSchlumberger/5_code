import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

def single_number_question(question, question_id,type='number'):
    return html.Div([
        html.B(html.Label([html.Span(question), html.Span('  \u273D',style={'color': 'red'})], style={'marginBottom': '1%'})),
        html.Br(),
        dcc.Input(id=question_id, type=type, style={'marginBottom': '2%'}),  # Increased margin
        html.Br(),
    ], style={'marginBottom': '2%'})  # Space between this question and the next

def short_text_question(question, question_id,type='text'):
    return html.Div([
        html.B(html.Label([html.Span(question), html.Span('  \u273D',style={'color': 'red'})], style={'marginBottom': '1%'})),
        html.Br(),
        dcc.Input(id=question_id, type=type, style={'marginBottom': '2%'}),  # Increased margin
        html.Br(),
    ], style={'marginBottom': '2%'})  # Space between this question and the next

def multiple_choice(question, question_id, option_dict):
    return html.Div([
        html.B(html.Label([html.Span(question), html.Span('  \u273D',style={'color': 'red'})], style={'marginBottom': '1%'})),
        dcc.RadioItems(
            id=question_id,
            options=[{'label': key, 'value': element} for key, element in option_dict.items()],
            style={'marginBottom': '2%'}  # Adjust spacing if needed
        ),
        html.Br(),
    ], style={'marginBottom': '2%'})

def gender_question(question):
    return html.Div([
        html.B(html.Label([html.Span(question), html.Span('  \u273D', style={'color': 'red'})], style={'marginBottom': '1%'})),
        dcc.RadioItems(
            id='gender-radio',
            options=[
                {'label': 'Female', 'value': 'Female'},
                {'label': 'Non-binary', 'value': 'Non-binary'},
                {'label': 'Male', 'value': 'Male'},
                {'label': 'Prefer not to say', 'value': 'Prefer not to say'},
                {'label': 'Prefer to self-describe', 'value': 'Prefer to self-describe'},
                {'label': 'Other', 'value': 'Other'}
            ],
            labelStyle={'display': 'block'}  # Display each option in a new line
        ),
        html.Div(id='gender-container'),  # Container for the text input
        html.Br(),
    ])

def visual_impairments():
    return html.Div([
        html.B(html.Label([html.Span("Do you have any visual impairments or conditions that might influence the way you "
                              "perceive visual content?"), html.Span('  \u273D', style={'color': 'red'})], style={'marginBottom': '1%'})),
        html.Br(),
        html.I("We ask this question solely to ensure our designs are inclusive and to understand any potential "
               "challenges participants might experience. Your feedback will be used to enhance the accessibility "
               "of our visual tools."),
        html.Br(),
        dcc.RadioItems(
            id='impairment-radio',
            options=[
                {'label': 'No', 'value': 'No'},
                {'label': 'Yes', 'value': 'Yes'},
                {'label': "I don't know", 'value': 'IdontKnow'},
            ],
            labelStyle={'display': 'block'}  # Display each option in a new line
        ),
        html.Div(id='impairment-container'),  # Container for the text input
        html.Br(),
    ])

def likkert_scale(question, question_id, input_list, comment):
    return html.Div([
                    html.B(html.Label([html.Span(question), html.Span('  \u273D', style={'color': 'red'})], style={'marginBottom': '1%'})),
                    html.Br(),
                    html.I(comment), html.Br(),
                    dcc.Slider(
                        id=question_id,
                        min=1,     # Start of the scale
                        max=5,     # End of the scale
                        step=1,    # Step size
                        marks={
                            1: input_list[0],
                            2: input_list[1],
                            3: input_list[2],
                            4: input_list[3],
                            5: input_list[4]
                        },
                        value=3,   # Default value in the middle of the scale
                    ),
                    html.Br(),
                ], style={'marginBottom': '2%'})

def multi_likkert_scale(question, question_id, input_list, multi_comments):
    sliders = []

    for comment in multi_comments:
        # Ensure unique and clear IDs and use better HTML formatting
        slider = html.Div([
            html.I(comment),
            dcc.Slider(
                id=f'{question_id}_{comment.replace(" ", "_")}',
                # Replace spaces with underscores for better ID handling
                min=1,  # Start of the scale
                max=5,  # End of the scale
                step=1,  # Step size
                marks={i: label for i, label in enumerate(input_list, start=1)},
                value=3,  # Default value in the middle of the scale
            ),
            html.Br(),
        ])

        sliders.append(slider)

    return html.Div([
                    html.B(html.Label([html.Span(question), html.Span('  \u273D', style={'color': 'red'})], style={'marginBottom': '1%'})),
                    html.Br(),
                    html.Div(sliders, style={'marginBottom': '2%'}),  # Encapsulate sliders in a Div
                ], style={'marginBottom': '2%'})



def submit_answers(button_id, container_id):
    return [html.Button('Submit', id=button_id, n_clicks=0,className='btn btn-primary',  style={'marginBottom': '2%'}), html.Div(id=container_id, children=[])]


## INTRODUCTION

introduction = html.Div([
    # html.H4('Survey (2/4)', style={'marginBottom': '0.2%'}),
    html.P(html.I('Please fill the following questions before submitting using the "submit" button at the end')),
    html.P([html.Span('\u273D',style={'color': 'red'}), html.Span(html.I('= required input'))]),

    html.H4("Personal information"),
    html.I("We request details on your age and gender to ensure a diverse representation in our dataset, enabling a "
           "more comprehensive understanding of how different demographic groups perceive and interact with our "
           "visualization techniques. This information will solely be used for analytical purposes to identify "
           "potential patterns or biases and will not be linked to individual responses or disclosed in any identifying "
           "manner."),
    html.Br(),
    gender_question("Which of the following best represents your gender?"),

    visual_impairments(),

    single_number_question('Please indicate your age.', 'age-input'),

    html.H4("Information about your expertise"),

    multiple_choice("What is your field of work?",
                    'work-input',
                    {"Research": "Research", 'Public Administration': 'Public Administration',
                     'Private sector': 'Public Administration', 'Other': 'Other'}),

    short_text_question("What are your areas of expertise (use key terms and separate by ';')", 'expertise_input'),

    likkert_scale("How often do you use visualizations to make choices?",
                  'use_frequency-input',
                  ['never', '', '', '', 'every day'],
                  'With this question, we want to establish your familiarity with visualizations and using them to '
                  'extract information about alternative options to inform a decision.'),

    multi_likkert_scale("What is your experience with the following visualization techniques?",
                        "viztype-intput",
                        ['never', '', '', '', 'every day'],
                        ["Bar chart", "Parallel Coordinates Plot", "Scatter Plots", "Heatmaps", "Visualization of Uncertainty"]),

    *submit_answers('submit-survey-introduction', 'introduction-container'),
    ], style={'height': '80vh', 'overflow-y': 'auto'},
) # Adjusted height to auto for flexibility

option_dict = {
    ' Ditch System': 'Ditch_System',
    ' Dike Maintenance': 'Dike_Maintenance',
    ' Flood Resilient Crops': 'Flood_Resilient_Crops'
}

## ALTERNATIVE PATHWAYS

alternative_pathways = html.Div([
    # html.H4('Survey (2/4)', style={'marginBottom': '0.2%'}),
    html.P(html.I('Please fill the following questions before submitting using the "submit" button at the end')),
    html.P([html.Span('\u273D',style={'color': 'red'}), html.Span(html.I('= required input'))]),

    single_number_question('How many pathway alternatives do you have?', 'pathway_number-input'),

    single_number_question('For the agricultural flood risk pathways: How many alternative pathways start with measure "flood resilient crops"?', 'f_resilient_crops-input'),

    short_text_question('Which measure is considered most often as the long-term measure (being implemented an the far future) for the agricultural flood risk pathways?', 'long_term-input'),

    multiple_choice('Which first implemented measure offers the most flexibility with regards to future options?', 'flexibility-level', option_dict),
    # For multiple choice questions, follow a similar pattern
    *submit_answers('submit-survey-alternative_pathways', 'alternative_pathways-container'),
    ], style={'height': '80vh', 'overflow-y': 'auto'},
) # Adjusted height to auto for flexibility

option_dict = {str(key): key for key in range(1,9)}
performance_pathways = html.Div([
    # html.H4('Survey (3/4)', style={'marginBottom': '1%'}),
    html.P(html.I('Please fill the following questions before submitting using the "submit" button at the end')),
    html.P([html.Span('\u273D',style={'color': 'red'}), html.Span(html.I('= required input'))]),

    short_text_question('What color/position shows better perfomance?',
                        'color-input'),

    single_number_question('For the agricultural flood risk pathways: How much Crop Loss do we expect with in an '
                           'optimistic case for Pathway 5 over a timerhorizon of 60 years under a high climate change scenario?',
                           'crop_loss-input'),

    multiple_choice('When accounting for all climate change scenarios, which flood - agriculture pathways rank highest '
                    'in most model experiments across at least two of the performance criteria?',
                    'performance-input', option_dict),

    multiple_choice('Which flood - agriculture pathway has the biggest trade-off between Structural Damage and '
                    'Risk Reduction Costs after 100 years in 50% of the modelling experiments?',
                    'tradeoff-input', option_dict),

    # For multiple choice questions, follow a similar pattern
    *submit_answers('submit-survey-pathways_performance', 'pathways_performance-container'),
    ], style={'height': '80vh', 'overflow-y': 'auto'})


interaction_effects = html.Div([
    # html.H4('Survey (3/4)', style={'marginBottom': '1%'}),
    html.P(html.I('Please fill the following questions before submitting using the "submit" button at the end')),
    html.P([html.Span('\u273D',style={'color': 'red'}), html.Span(html.I('= required input'))]),

    single_number_question('How many years did the implementation of measure X in pathway 1 shift when accounting for the presence of farmer – drought pathways?',
                        'measure_shift-input'),

    short_text_question('How did the performance of pathway X regarding Crop Losses change when accounting for presence of farmer – drought pathways?',
                        'performance_change-input'),

    short_text_question('Name three flood-farmer pathways that experience strong trade-off effects from farmer – drought pathways',
                        'strong_tradeoffs-input'),

    short_text_question('Which pathway experiences the strongest synergistic effect from the general presence of farmer-drought pathways?',
                        'strong_synergy-input'),


    # For multiple choice questions, follow a similar pattern
    *submit_answers('submit-survey-interaction_effects', 'interaction_effects-container'),
    ], style={'height': '80vh', 'overflow-y': 'auto'})

