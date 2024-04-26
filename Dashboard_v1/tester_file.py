import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

def multi_likkert_scale(question, question_id, input_list, multi_comments):
    sliders = []

    for comment in multi_comments:
        # Ensure unique and clear IDs and use better HTML formatting
        slider = html.Div([
            html.I(comment),  # Italicize comment
            html.Br(),  # Line break after comment
            dcc.Slider(
                id=f'{question_id}_{comment.replace(" ", "_")}',  # Replace spaces with underscores for better ID handling
                min=1,  # Start of the scale
                max=5,  # End of the scale
                step=1,  # Step size
                marks={i: label for i, label in enumerate(input_list, start=1)},
                value=3,  # Default value in the middle of the scale
            ),
            html.Br(),  # Line break after slider
        ])

        sliders.append(slider)

    # Avoid using * for unpacking in some contexts it may lead to issues
    return html.Div([
        html.B(html.Label([
            html.Span(question),
            html.Span('  \u273D', style={'color': 'red'})  # This adds a red dagger symbol. Ensure it's intentional and displays correctly.
        ], style={'marginBottom': '1%'})),
        html.Br(),
        html.Div(sliders, style={'marginBottom': '2%'}),  # Encapsulate sliders in a Div
    ])

# Example usage:
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
    [
        multi_likkert_scale(
            "How often do you use visualizations to make choices?",
            "viz_usage",
            ["Never", "Rarely", "Sometimes", "Often", "Always"],
            ["Comment A", "Comment B", "Comment C"]
        )
    ],
    fluid=True
)

if __name__ == "__main__":
    app.run_server(debug=True)
