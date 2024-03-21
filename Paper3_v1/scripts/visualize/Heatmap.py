import plotly.express as px
import numpy as np
import plotly.graph_objects as go  # Import Plotly's graph_objects module
from Paper3_v1.scripts.utilities.design_choices.add_measure_buttons import add_measure_buttons
from Paper3_v1.scripts.utilities.design_choices.main_dashboard_design_choices import COLORSCALE_HEATMAP
from Paper3_v1.scripts.utilities.design_choices.get_table_for_plot import get_table_for_plot

def Heatmap(df, risk_owner_hazard, sector_objectives, df_interaction=None):
    df = df[df[risk_owner_hazard] != 0]

    pivot_df, pivot_text_df = get_table_for_plot(df, risk_owner_hazard)
    pivot_df = pivot_df.iloc[:, 1:]
    pivot_text_df = pivot_text_df.iloc[:, 1:]

    if df_interaction is not None:
        pivot_df_interactions, pivot_text_df_interactions = get_table_for_plot(df_interaction, risk_owner_hazard)
        pivot_df_interactions = pivot_df_interactions.iloc[:, 1:]
        pivot_text_df_interactions = pivot_text_df_interactions.iloc[:, 1:]

    y_axis_values = pivot_df.index.values
    # Creating the heatmap
    # Create a heatmap figure

    if df_interaction is None:
        fig = go.Figure(data=go.Heatmap(
            z=pivot_df.round(1).values,  # Use normalized values for color
            x=pivot_df.columns,  # Objective parameters
            y=y_axis_values.astype(str),  # Risk owner hazard
            text=pivot_text_df.round(1).values,  # Original values for display
            texttemplate="%{text} MEUR",  # Display the text from 'text' in each cell
            hoverinfo="text",  # Show only the text on hover
            colorscale=COLORSCALE_HEATMAP,  # Use the custom colorscale
            zmin=0.0,
            zmax=1.0,
            colorbar=dict(tickvals=[0.1, 0.3, 0.5, 0.7, 0.9],
                          ticktext=['Lowest', 'Low', 'Medium', 'High', 'Highest'],
                          title='Performance'))
        )
    else:
        updated_text = pivot_text_df_interactions.round(1).astype(str) + ', (old: ' + pivot_text_df.round(1).astype(str) + ')'

        fig = go.Figure(data=go.Heatmap(
            z=pivot_df_interactions.round(1).values,  # Use normalized values for color
            x=pivot_df_interactions.columns,  # Objective parameters
            y=y_axis_values.astype(str),  # Risk owner hazard
            # text=updated_text.values,  # Original values for display
            text=pivot_df_interactions.round(1).values,
            texttemplate="%{text} MEUR",  # Display the text from 'text' in each cell
            hoverinfo="text",  # Show only the text on hover
            colorscale=COLORSCALE_HEATMAP,  # Use the custom colorscale
            zmin=0.0,
            zmax=1.0,
            colorbar=dict(tickvals=[0.1, 0.3, 0.5, 0.7, 0.9],
                          ticktext=['Lowest', 'Low', 'Medium', 'High', 'Highest'],
                          title='Performance'))
        )


    # fig.update_yaxes(domain=[0, 0.9])  # Adjusting the domain can change the plotting area's height



    fig = add_measure_buttons(fig, y_axis_values, risk_owner_hazard)

    fig.update_layout(
        autosize=True,  # Allows the figure to resize based on the enclosing HTML element's size
        margin=dict(l=50, r=50, t=20, b=20)  # Adjust margins to ensure content fits well; customize as needed
    )

    fig.update_xaxes(domain=[0.15, 1])  # Adjusting the domain can change the plotting area's width
    fig.update_yaxes(domain=[0.2, 1])  # Adjusting the domain can change the plotting area's height

    # fig.add_annotation(dict(font=dict(color="black", size=14),
    #                         x=0.5,
    #                         y=1.1,
    #                         showarrow=False,
    #                         text="Objective Parameter",
    #                         textangle=0,
    #                         xref="paper",
    #                         yref="paper"))

    return fig
