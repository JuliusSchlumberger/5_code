from dash import dcc, html
import dash_bootstrap_components as dbc


# Assume GLOSSARY_TERMS is defined somewhere, e.g.,
GLOSSARY_TERMS={
    'Disaster Risk Management': 'Strategies and practices to reduce vulnerabilities and manage the impacts of natural hazards.',
    'Pathway': 'A sequence of measures that are implemented to adjust to future changes.',
    'Multi-Risk Setting': 'A context in which multiple hazards interact and impacts to and responses by different actors influence each other.',
    'Sectoral Risk Owner': 'Individuals or entities responsible for managing risks in specific sectors, such as a shipping company, farmer, or municipality.',
    'Climate Scenarios': 'Plausible time-series of e.g. precipitation intensity or river discharge for different warming scenarios. '
                         'Multiple time-series per climate scenario to capture uncertainty and natural variability.',
    'Performance': 'Evaluated regarding a set of criteria using indicators to deal with uncertainty in and across climate scenarios.',
    'Trade-offs': 'Compromises made when choosing between two or more competing options.',
    'Interactions': 'Pathways of different sectoral risk owners can interfere with or benefit from each other, leading to changes in performance or available options.'
}

# Define the header with an additional modal for the glossary
header = dbc.Row(
    [   dbc.Col(html.H3("Dashboard For Pathways Analysis (Sectoral Risk Owner)", className="mb-2 header-background"), width=10),
        dbc.Col(dbc.Button("Help", color="primary", className="mb-2 custom-button-outline", outline=True, style={'width': '100%'}), width=1, className="text-right header-background"),
        dbc.Col(dbc.Button("Glossary", id="open-glossary", color="primary", className="mb-2 custom-button-outline", outline=True, style={'width': '100%'}), width=1, className="text-right header-background"),
         # Modal definition
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Glossary")),
                dbc.ModalBody(html.Ul([html.Li([html.B(f"{term}"), f": {definition}"]) for term, definition in GLOSSARY_TERMS.items()])),
                dbc.ModalFooter(
                    dbc.Button("Close", id="close-glossary", className="ms-auto")
                ),
            ],
            id="glossary-modal",
            is_open=False,
        ),
    ],
    align="center",
    className="mb-1 header-background",
    style={'height': '10vh', 'color':"primary"}
)

