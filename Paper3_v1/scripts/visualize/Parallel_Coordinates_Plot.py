import plotly.express as px
import re
from plotly.subplots import make_subplots
from Paper3_v1.scripts.utilities.map_system_parameters import AXIS_LABELS
from Paper3_v1.scripts.utilities.design_choices.main_dashboard_design_choices import COLORSCALE_PCP,COLORSCALE
from Paper3_v1.scripts.utilities.design_choices.main_dashboard_dropdowns import ROH_DICT_INV, RANGE
import plotly.graph_objects as go
import pandas as pd
import numpy as np


from Paper3_v1.scripts.utilities.design_choices.add_measure_buttons import add_measure_buttons

def Parallel_Coordinates_Plot(df, risk_owner_hazard, figure_title, df_interaction=None):
    df = df[df[risk_owner_hazard] != 0]

    if df_interaction is None:
        pivot_df = df.pivot_table(
            index=[risk_owner_hazard,'performance_metric'],
            columns='objective_parameter',
            values='Value',
            aggfunc='sum'  # or 'mean', 'max', etc., depending on the required aggregation
        )
        reset_pivot = pivot_df.reset_index()
        # reset_pivot['Color'] = 0
        reset_pivot['performance_metric'] = reset_pivot['performance_metric'].map({'95%': 1, '50%': .5, '5%': 0, 'average': .6})
        reset_pivot['Color'] = reset_pivot['performance_metric'].copy()

    else:
        df_interaction = df_interaction[df_interaction[risk_owner_hazard] != 0]

        pivot_df1 = df.pivot_table(
            index=[risk_owner_hazard,'performance_metric'],
            columns='objective_parameter',
            values='Value',
            aggfunc='sum'  # or 'mean', 'max', etc., depending on the required aggregation
        )
        reset_pivot1 = pivot_df1.reset_index()

        reset_pivot1['performance_metric'] = reset_pivot1['performance_metric'].map(
            {'95%': 1, '50%': .5, '5%': 0, 'average': .6})
        # reset_pivot1['Color'] = reset_pivot1['performance_metric']
        reset_pivot1['Color'] = 0.8

        pivot_df2 = df_interaction.pivot_table(
            index=[risk_owner_hazard,'performance_metric'],
            columns='objective_parameter',
            values='Value',
            aggfunc='sum'  # or 'mean', 'max', etc., depending on the required aggregation
        )
        reset_pivot2 = pivot_df2.reset_index()
        reset_pivot2['Color'] = 1
        reset_pivot2['performance_metric'] = reset_pivot2['performance_metric'].map(
            {'95%': 1, '50%': .5, '5%': 0, 'average': .6})
        reset_pivot2['Color'] = reset_pivot2['performance_metric'].copy()


        reset_pivot = pd.concat([reset_pivot1, reset_pivot2], ignore_index=True)

    new_order = [risk_owner_hazard, *df['objective_parameter'].unique(), 'performance_metric', 'Color']
    reset_pivot = reset_pivot[new_order]

    # Rename axis
    reset_pivot = reset_pivot.rename(columns=AXIS_LABELS)
    reset_pivot = reset_pivot.rename(columns=ROH_DICT_INV)
    # reset_pivot = reset_pivot.rename(columns={'performance_metric':'performance_metric'})


    dimensions = [
        dict(range=RANGE[col],
            label=col, values=reset_pivot[col],)
        for col in reset_pivot.columns if col != 'Color'
    ]

    fig = go.Figure(data=
        go.Parcoords(
            line=dict(
                color=reset_pivot['Color'],
                colorscale=COLORSCALE_PCP,
            ),
            dimensions=dimensions,
            unselected=dict(line=dict(color='grey', opacity=0.2))
        )
    )

    # Add figure title
    fig.update_layout(title={'text': figure_title,'y':.98, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})

    # Adjust axis labels
    # Use np.vectorize to apply the replacement
    replace_function = np.vectorize(lambda x: { 0: '5% confident', .5: '50% confident', .6: 'robustness indicator', 1: '95% confident'}.get(x, x))

    for dimension in fig.data[0]['dimensions']:
        if dimension['label'] == ROH_DICT_INV[risk_owner_hazard]:
            dimension['tickvals'] = reset_pivot[ROH_DICT_INV[risk_owner_hazard]].unique()
            # inverted_dict = {value: key for key, value in cc_scenarios_int.items()}
            dimension['ticktext'] = [str(x) for x in reset_pivot[ROH_DICT_INV[risk_owner_hazard]].unique()]
        if dimension['label'] == 'performance_metric':    # Performance_metric
            dimension['tickvals'] = reset_pivot['performance_metric'].unique()
            # inverted_dict = {value: key for key, value in cc_scenarios_int.items()}
            dimension['ticktext'] = [str(x) for x in replace_function(reset_pivot['performance_metric'].unique())]


    # fig.update_xaxes(domain=[0.15, 1])  # Adjusting the domain can change the plotting area's width
    # fig.update_yaxes(domain=[0.2, 1])  # Adjusting the domain can change the plotting area's height

    # Add a shape for visual emphasis on the first axis
    fig.add_shape(
        type="rect",  # Add a rectangle shape
        x0=-.07, x1=0.07,  # Span a small range around the first axis
        y0=-.1, y1=1.17,
        xref="paper", yref="paper",  # Reference the entire figure's dimensions
        fillcolor="lightgrey",  # Choose a subtle fill color
        opacity=0.5,  # Make the fill semi-transparent
        layer="below",  # Ensure the shape is below the data lines
        line_width=0,
    )

    # Add a shape for visual emphasis on the other axis
    fig.add_shape(
        type="rect",  # Add a rectangle shape
        x0=0.08, x1=.91,  # Span a small range around the first axis
        y0=-.1, y1=1.17,
        xref="paper", yref="paper",  # Reference the entire figure's dimensions
        fillcolor="lightgrey",  # Choose a subtle fill color
        opacity=0.5,  # Make the fill semi-transparent
        layer="below",  # Ensure the shape is below the data lines
        line_width=0,
    )

    # Add a shape for visual emphasis on the other axis
    fig.add_shape(
        type="rect",  # Add a rectangle shape
        x0=0.92, x1=1.07,  # Span a small range around the first axis
        y0=-.1, y1=1.17,
        xref="paper", yref="paper",  # Reference the entire figure's dimensions
        fillcolor="lightgrey",  # Choose a subtle fill color
        opacity=0.5,  # Make the fill semi-transparent
        layer="below",  # Ensure the shape is below the data lines
        line_width=0,
    )

    # # Add a shape for visual emphasis on the other axis
    # fig.add_shape(
    #     type="rect",  # Add a rectangle shape
    #     x0=0.81, x1=1,  # Span a small range around the first axis
    #     y0=-.1, y1=1.17,
    #     xref="paper", yref="paper",  # Reference the entire figure's dimensions
    #     fillcolor="lightgrey",  # Choose a subtle fill color
    #     opacity=0.5,  # Make the fill semi-transparent
    #     layer="below",  # Ensure the shape is below the data lines
    #     line_width=0,
    # )

    # Add an annotation for the first axis if needed to label it as 'Strategy Options'
    fig.add_annotation(
        x=0,  # Position at the start
        y=1.1,  # Slightly above the plot
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
        x=0.08 + (.91 - 0.08) / 2,  # Position at the start
        y=1.1,  # Slightly above the plot
        text="<b>Performance Criteria</b>",  # Custom text
        showarrow=False,  # No arrow needed
        xref="paper",
        yref="paper",
        font=dict(size=12, color="black"),  # Make the font bold
        xanchor="center",
        yanchor="bottom",
    )

    # Add an annotation for the first axis if needed to label it as 'Objective performance'
    fig.add_annotation(
        x=0.92 + (1.07 - 0.92) / 2,  # Position at the start
        y=1.1,  # Slightly above the plot
        text="<b>Performance Indicator</b>",  # Custom text
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
    fig.update_layout(
        # autosize=True,  # Allows the figure to resize based on the enclosing HTML element's size
        # margin=dict(l=50, r=50, t=50, b=20)  # Adjust margins to ensure content fits well; customize as needed
    )

    return fig