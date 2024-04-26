from dash import dcc, html
import dash_bootstrap_components as dbc


sidebar = dbc.Col([
                # html.H6("Structure", className="display-4"),
                # html.Hr(),
                html.H4(
                    "Navigation",className="compact-sidebar"
                ),
                html.Hr(),
                dbc.Nav(
                    [
                        dbc.NavLink("Introduction", href="/", active="exact", id='navigation-introduction'),
                        dbc.NavLink("1. Alternative Pathways", href="/alternative_pathways", active="exact", id='navigation-alternative_pathways'),
                        dbc.NavLink("2. Pathway Performance", href="/pathways_performance", active="exact", id='navigation-pathways_performance'),
                        dbc.NavLink("3. Measure timings", href="/measure_timings", active="exact", id='navigation-measure_timings'),
                        dbc.NavLink("4. Interaction effects", href="/interaction_effects", active="exact", id='navigation-interaction_effects'),
                    ],
                    vertical=True,
                    pills=True,
                    className="compact-sidebar"
                )
            ],id='sidebar', style={'height':'90vh',"background-color": "#f8f9fa"},md=2,
)