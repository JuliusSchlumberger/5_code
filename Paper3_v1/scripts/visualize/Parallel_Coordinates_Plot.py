import plotly.express as px
import re
from plotly.subplots import make_subplots
from Paper3_v1.scripts.utilities.map_system_parameters import AXIS_LABELS
from Paper3_v1.scripts.utilities.design_choices.main_dashboard_design_choices import COLORSCALE_PCP,COLORSCALE
from Paper3_v1.scripts.utilities.design_choices.main_dashboard_dropdowns import ROH_DICT_INV, RANGE
import plotly.graph_objects as go
import pandas as pd


from Paper3_v1.scripts.utilities.design_choices.add_measure_buttons import add_measure_buttons

def Parallel_Coordinates_Plot(df, risk_owner_hazard, df_interaction=None):
    df = df[df[risk_owner_hazard] != 0]

    # Create a subplot layout with 1 row and 2 columns
    fig = make_subplots(
        rows=1, cols=2,
        column_widths=[0.6, 0.4],  # Left plot takes 60% of the width
        specs=[[{"type": "parcoords"}, {"type": "table"}]]  # Specify types for subplots
    )

    if df_interaction is None:
        pivot_df = df.pivot_table(
            index=risk_owner_hazard,
            columns='objective_parameter',
            values='Value',
            aggfunc='sum'  # or 'mean', 'max', etc., depending on the required aggregation
        )
        reset_pivot = pivot_df.reset_index()
        reset_pivot['Color'] = 0

    else:
        df_interaction = df_interaction[df_interaction[risk_owner_hazard] != 0]


        pivot_df1 = df.pivot_table(
            index=risk_owner_hazard,
            columns='objective_parameter',
            values='Value',
            aggfunc='sum'  # or 'mean', 'max', etc., depending on the required aggregation
        )
        reset_pivot1 = pivot_df1.reset_index()
        reset_pivot1['Color'] = 0

        pivot_df2 = df_interaction.pivot_table(
            index=risk_owner_hazard,
            columns='objective_parameter',
            values='Value',
            aggfunc='sum'  # or 'mean', 'max', etc., depending on the required aggregation
        )
        reset_pivot2 = pivot_df2.reset_index()
        reset_pivot2['Color'] = 1


        reset_pivot = pd.concat([reset_pivot1, reset_pivot2], ignore_index=True)

    reset_pivot = reset_pivot.rename(columns=AXIS_LABELS)
    reset_pivot = reset_pivot.rename(columns=ROH_DICT_INV)

    dimensions = [
        dict(range=RANGE[col],
            label=col, values=reset_pivot[col])
        for col in reset_pivot.columns if col != 'Color'
    ]

    fig.add_trace(
        go.Parcoords(
            line=dict(
                color=reset_pivot['Color'],
                colorscale=COLORSCALE_PCP,
            ),
            dimensions=dimensions,
        ),
        row=1, col=1
    )


    for dimension in fig.data[0]['dimensions']:
        if dimension['label'] == ROH_DICT_INV[risk_owner_hazard]:
            dimension['tickvals'] = reset_pivot[ROH_DICT_INV[risk_owner_hazard]].unique()
            # inverted_dict = {value: key for key, value in cc_scenarios_int.items()}
            dimension['ticktext'] = [str(x) for x in reset_pivot[ROH_DICT_INV[risk_owner_hazard]].unique()]


    # fig.update_xaxes(domain=[0.15, 1])  # Adjusting the domain can change the plotting area's width
    # fig.update_yaxes(domain=[0.2, 1])  # Adjusting the domain can change the plotting area's height

    # Add a shape for visual emphasis on the first axis
    fig.add_shape(
        type="rect",  # Add a rectangle shape
        x0=-0.07, x1=0.07,  # Span a small range around the first axis
        y0=-.1, y1=1.25,
        xref="paper", yref="paper",  # Reference the entire figure's dimensions
        fillcolor="lightgrey",  # Choose a subtle fill color
        opacity=0.5,  # Make the fill semi-transparent
        layer="below",  # Ensure the shape is below the data lines
        line_width=0,
    )

    # Add a shape for visual emphasis on the other axis
    fig.add_shape(
        type="rect",  # Add a rectangle shape
        x0=0.08, x1=0.6,  # Span a small range around the first axis
        y0=-.1, y1=1.25,
        xref="paper", yref="paper",  # Reference the entire figure's dimensions
        fillcolor="lightgrey",  # Choose a subtle fill color
        opacity=0.5,  # Make the fill semi-transparent
        layer="below",  # Ensure the shape is below the data lines
        line_width=0,
    )

    # Add an annotation for the first axis if needed to label it as 'Strategy Options'
    fig.add_annotation(
        x=0,  # Position at the start
        y=1.15,  # Slightly above the plot
        text="<b>Pathway Options</b>",  # Custom text
        showarrow=False,  # No arrow needed
        xref="paper",
        yref="paper",
        font=dict(size=12, color="black"),  # Make the font bold
        xanchor="center",
        yanchor="bottom",
    )

    # Add an annotation for the first axis if needed to label it as 'Objective performance'
    fig.add_annotation(
        x=0.08 + (.6 - 0.08) / 2,  # Position at the start
        y=1.15,  # Slightly above the plot
        text="<b>Objectives</b>",  # Custom text
        showarrow=False,  # No arrow needed
        xref="paper",
        yref="paper",
        font=dict(size=12, color="black"),  # Make the font bold
        xanchor="center",
        yanchor="bottom",
    )

    # # Add a downward arrow to indicate the direction of preference
    # fig.add_annotation(
    #     x=0.5,  # Adjust this value to position the arrow along the x-axis
    #     y=0.1,  # Adjust this value to position the arrow along the y-axis
    #     xref="paper",
    #     yref="paper",
    #     showarrow=True,
    #     arrowhead=2,  # Adjust the style of the arrowhead as needed
    #     arrowsize=1,  # Adjust the size of the arrowhead as needed
    #     arrowwidth=2,  # Adjust the width of the arrow as needed
    #     arrowcolor="black",  # Adjust the color of the arrow as needed
    #     ax=0,  # Horizontal offset
    #     ay=-50  # Negative value for downward arrow (adjust the length as needed)
    # )

    pathways_numbers = df[risk_owner_hazard].unique()

    table_inputs = pd.DataFrame({
        risk_owner_hazard: pathways_numbers,
        'no_interaction': [100] * len(pathways_numbers),
        'interaction': [100] * len(pathways_numbers),
    })
    table_inputs = table_inputs.sort_values(by=risk_owner_hazard, ascending=True)

    annotation_text = "X% of realisations for each pathway<br>satisfy selected objective ranges..."

    fig.add_annotation(
        x=0.95,  # Centered horizontally
        y=1.15,  # Positioned above the table
        xref="paper",
        yref="paper",
        text=annotation_text,
        showarrow=False,
        font=dict(size=14, color="black"),
        align="center"
    )

    # Normalize function (assuming values are in 0 to 100 range)
    def normalize_to_color(value, scale):
        # Convert percentage to a 0-1 scale
        normalized_value = value / 100
        # Determine the index in the colorscale
        index = min(int(normalized_value / 0.2), len(scale) - 1)
        return scale[index]

    # Apply the color mapping to a column (e.g., 'no_interaction')
    colors_no_interaction = table_inputs['no_interaction'].apply(lambda x: normalize_to_color(x, COLORSCALE)).tolist()

    # Placeholder: Repeat the process for 'interaction' column or any other column as needed
    colors_interaction = table_inputs['interaction'].apply(lambda x: normalize_to_color(x, COLORSCALE)).tolist()


    fig.add_trace(
        go.Table(
            header=dict(values=[f'{ROH_DICT_INV[risk_owner_hazard]} pathway options', 'Ratio (%) [no interactions]',
                                'Ratio (%) [with interactions]']),
            cells=dict(
                values=[table_inputs[risk_owner_hazard],
                        table_inputs['no_interaction'].apply(lambda x: f'{x:.2f}%'),
                        table_inputs['interaction'].apply(lambda x: f'{x:.2f}%')],
            fill_color=[['white'] * len(table_inputs), colors_no_interaction, colors_interaction],),

            domain=dict(y=[0, 1])  # Adjust the domain as needed
        ),
        row=1, col=2
    )
    return fig