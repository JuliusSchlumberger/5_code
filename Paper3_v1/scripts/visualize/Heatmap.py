import plotly.express as px
import numpy as np
import plotly.graph_objects as go  # Import Plotly's graph_objects module
from Paper3_v1.scripts.utilities.design_choices.add_measure_buttons import add_measure_buttons
from Paper3_v1.scripts.utilities.design_choices.main_dashboard_design_choices import COLORSCALE_HEATMAP
from Paper3_v1.scripts.utilities.design_choices.main_dashboard_dropdowns import ROH_DICT_INV
from Paper3_v1.scripts.utilities.design_choices.get_table_for_plot import get_table_for_plot
from plotly.subplots import make_subplots

def Heatmap(df, risk_owner_hazard, sector_objectives, figure_title, df_interaction=None):
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
                          title='Performance')),
        )
    else:
        updated_text = pivot_text_df_interactions.round(1).astype(str) + ' (old: ' + pivot_text_df.round(1).astype(str) + ')'

        fig = go.Figure(data=go.Heatmap(
            z=pivot_df_interactions.round(1).values,  # Use normalized values for color
            x=pivot_df_interactions.columns,  # Objective parameters
            y=y_axis_values.astype(str),  # Risk owner hazard
            # text=updated_text.values,  # Original values for display
            text=updated_text,
            texttemplate="%{text} MEUR",  # Display the text from 'text' in each cell
            hoverinfo="text",  # Show only the text on hover
            colorscale=COLORSCALE_HEATMAP,  # Use the custom colorscale
            zmin=0.0,
            zmax=1.0,
            colorbar=dict(tickvals=[0.1, 0.3, 0.5, 0.7, 0.9],
                          ticktext=['Lowest', 'Low', 'Medium', 'High', 'Highest'],
                          title='Performance',)), # Adjusts the colorbar length to 70% of the figure heighy
        )


    # fig.update_yaxes(domain=[0, 0.9])  # Adjusting the domain can change the plotting area's height



    fig = add_measure_buttons(fig, y_axis_values, risk_owner_hazard)

    # Add figure title
    fig.update_layout(title={'text': figure_title,'y':.98, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})

    fig.update_yaxes(title_text='')
    fig.add_annotation(
        x=-0.1,  # Adjust this value to move the label left or right
        y=0.6,  # Adjust this value to move the label up or down
        text=f'{ROH_DICT_INV[risk_owner_hazard]} pathway options',  # Your y-axis label text here
        showarrow=False,
        xref='paper',
        yref='paper',
        textangle=-90,  # Rotate text for vertical orientation
        font=dict(size=14),  # Adjust font size as needed
        align='center'
    )

    fig.update_layout(
        autosize=True,  # Allows the figure to resize based on the enclosing HTML element's size
        margin=dict(l=50, r=50, t=50, b=20),  # Adjust margins to ensure content fits well; customize as needed
        xaxis=dict(side='top')
    )

    fig.update_xaxes(domain=[0.15, 1])  # Adjusting the domain can change the plotting area's width
    fig.update_yaxes(title_text='')
    fig.add_annotation(
        x=-0.03,  # Adjust this value to move the label left or right
        y=0.5,  # Adjust this value to move the label up or down
        text=f'{ROH_DICT_INV[risk_owner_hazard]} pathway options',  # Your y-axis label text here
        showarrow=False,
        xref='paper',
        yref='paper',
        textangle=-90,  # Rotate text for vertical orientation
        font=dict(size=14),  # Adjust font size as needed
        align='center'
    )

    # fig.update_yaxes(domain=[0.2, 1])  # Adjusting the domain can change the plotting area's height
    # fig.update_layout(width=800, height=600)  # Adjust figure size


    return fig
