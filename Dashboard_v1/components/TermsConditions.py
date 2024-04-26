import dash
from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc


# Define the modal which acts as a pop-up for terms and conditions
TermConditions = dbc.Modal(
    [
        dbc.ModalHeader(dbc.ModalTitle("Terms and Conditions"), close_button=False),
        dbc.ModalBody([

            html.P([
               "By participating in this short 15-minute survey, you'll help us better design these visual aids. The survey has three parts:",
               html.Br(),
               "1. A few questions about you and your experiences with visualizations.",
               html.Br(),
               "2. Tasks you'll complete using different visual aids.",
               html.Br(),
               "3. Your feedback on these visual aids."]),

            html.P(
                "Your input will be invaluable in shaping how we understand and tackle these interconnected risks in "
                "the future."),
            html.P(
                ["If you want to learn more about the context of this research, undertaken under the HORIZON 2020 ",
                 html.A("MYRIAD-EU project ", href="https://www.myriadproject.eu/", target="_blank"),
                 "please have a look at the ",
                html.A("participation information sheet.", href="https://www.myriadproject.eu/", target="_blank"),
                 ]),

            html.P([
                html.B("In giving my consent to participate in this study, I confirm that:"),
                html.Ul([
                    html.Li(["I have read and understood the ",
                            html.A("participation information sheet.", href="https://www.myriadproject.eu/", target="_blank")]),
                    html.Li("I understand that I can ask questions, using the email address above, about this research "
                            "before participating."),
                    html.Li("I understand that I am under no obligation to take part in the study, have the right to "
                            "stop my participation at any point for any reason, or decide not to answer a particular "
                            "question, and will not be required to explain my reasons for any of these actions."),
                    html.Li(["I agree to any personal information I choose to provide being processed in accordance with "
                            "the ",
                            html.A("General Data Protection Regulations.", href="https://gdpr-info.eu/", target="_blank")]),
                    html.Li("I understand that anonymised data may be used in research outputs (e.g., publications, reports, web pages).")]),
                html.B("If you are worried about this research, or if you are concerned about how it is being conducted, "
                       "you can contact  bethcie.beta@vu.nl. Before taking part in this survey, please review the "
                       "statements above. If you wish to participate, please tick the box to confirm your consent."),
            ]),
            dbc.Checklist(
                options=[
                    {"label": " I agree to the terms and conditions", "value": 1}
                ],
                value=[],
                id="terms-check",
                switch=True,
            ),
        ]
        ),
        dbc.ModalFooter(
            dbc.Button(
                "Agree",
                id="close-termsconditions",
                className="ms-auto",
                n_clicks=0,
                disabled=True  # Initially disabled
            )
        ),
    ],
    className="modal-xl",
    id="termsconditions",
    is_open=True,  # Start with the modal open
    backdrop="static",  # Prevent closing by clicking outside the modal
    keyboard=False  # Prevent closing by pressing escape key

)
