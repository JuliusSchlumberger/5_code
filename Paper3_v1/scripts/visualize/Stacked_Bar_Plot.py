import plotly.express as px
import pandas as pd
from Paper3_v1.scripts.utilities.design_choices.add_measure_buttons import add_measure_buttons
from Paper3_v1.scripts.utilities.find_key_by_value_string import find_key_by_value_string
from Paper3_v1.scripts.utilities.design_choices.main_dashboard_dropdowns import ROH_DICT, ROH_DICT_INV
from Paper3_v1.scripts.utilities.design_choices.get_bar_style import get_bar_style
from Paper3_v1.scripts.utilities.design_choices.colors import SECTOR_OBJECTIVE_COLORS
from Paper3_v1.scripts.utilities.design_choices.get_table_for_plot import get_table_for_plot
from Paper3_v1.scripts.utilities.design_choices.get_change_between_old_and_new import get_change_between_old_and_new

import plotly.graph_objects as go  # Import Plotly's graph_objects module

def Stacked_Bar_Plot(df, risk_owner_hazard, sector_objectives, figure_title, df_interaction=None):
    df = df[df[risk_owner_hazard] != 0]
    
    pivot_df,pivot_text_df = get_table_for_plot(df, risk_owner_hazard)
    

    if df_interaction is not None:
        print('Interaction added')
        pivot_df, pivot_text_df = get_table_for_plot(df, risk_owner_hazard)

        df_interaction = df_interaction[df_interaction[risk_owner_hazard] != 0]

        pivot_interaction, pivot_interaction_text = get_table_for_plot(df_interaction, risk_owner_hazard)
        # print(df_interaction)
        # print(pivot_df)
        # print(pivot_interaction)
        # print(error)

        # Calculate differences and add them as new columns
        pivot_interaction, objectives_with_interactions = get_change_between_old_and_new(pivot_df,
                                                                                         pivot_interaction,
                                                                                         sector_objectives,
                                                                                         risk_owner_hazard)
        pivot_interaction_text, _ = get_change_between_old_and_new(pivot_text_df,
                                                                         pivot_interaction_text,
                                                                         sector_objectives,risk_owner_hazard, normalized=False)

        print(pivot_interaction_text)
    y_axis_values = pivot_df.index.values

    if df_interaction is None:
        plot_df = pivot_df
        text_df = pivot_text_df
        plot_objectives = sector_objectives
    elif df_interaction is not None:
        plot_df = pivot_interaction
        plot_df.index = plot_df[risk_owner_hazard]
        text_df = pivot_interaction_text
        text_df.index = text_df[risk_owner_hazard]
        plot_objectives = objectives_with_interactions


    fig = go.Figure()
    for col in plot_objectives:
        if col in sector_objectives:
            hover_texts = [f'Pathway option: {plot_df.at[i, risk_owner_hazard]}<br>{col}: {text_df.at[i, col]}'
                           for i in plot_df.index]
        elif col.endswith('tradeoff'):
            obj_key = [column for column in sector_objectives if col.startswith(column)][0]
            hover_texts = [
                f'Pathway option: {plot_df.at[i, risk_owner_hazard]}<br>change regarding {obj_key}: {text_df.at[i, col]} (trade-off)'
                for i in plot_df.index]
        else:  # Assuming the only other option is '_synergy'
            obj_key = [column for column in sector_objectives if col.startswith(column)][0]
            hover_texts = [
                f'Pathway option: {plot_df.at[i, risk_owner_hazard]}<br>change regarding {obj_key}: {text_df.at[i, col]} (synergy)'
                for i in plot_df.index]
        base_objective = [objective for objective in sector_objectives if col.startswith(objective)]
        color = SECTOR_OBJECTIVE_COLORS[risk_owner_hazard][base_objective[0]]
        pattern = dict(shape='/', bgcolor=color, fgcolor='white') if col.endswith('_tradeoff') else dict(
            shape='.', bgcolor=color, fgcolor='white') if col.endswith('_synergy') else None

        # Add  objective values
        fig.add_trace(go.Bar(
            name=col,
            x=plot_df[col],
            y=plot_df[risk_owner_hazard].astype(str),
            orientation='h',
            # text=text_df[col],  # Use text from the corresponding text_df column
            # hovertext=hover_texts,
            marker=dict(color=color, pattern=pattern)
        ))

    # Convert hover_pivot to a dictionary for easier access
    hover_data_dict = text_df.to_dict('index')

    # Update the hover template for each trace (bar segment) in the figure
    for trace in fig.data:
        new_hovertemplate = []

        for index, value in enumerate(trace.y):
            risk_owner_value = trace.y[index]
            objective_value = trace.x[index]

            # Retrieve the corresponding hover value from hover_pivot
            hover_value = hover_data_dict[int(risk_owner_value)].get(trace.name, '')

            # Customize the hover text; adjust the formatting as needed
            hover_text = f"<b>{find_key_by_value_string(ROH_DICT, risk_owner_hazard)} pathway {risk_owner_value}</b><br>{trace.name}: {int(hover_value)} MEUR (baseline (no actions taken: tbc)"
            new_hovertemplate.append(hover_text)

        # Update the hovertemplate for the trace
        trace.hovertemplate = new_hovertemplate

    # Update the Y-axis label
    # fig.update_yaxes(title_text=f'{find_key_by_value_string(ROH_DICT, risk_owner_hazard)} pathway options')
    fig.update_yaxes(title_text='')
    fig.add_annotation(
        x=-0.0,  # Adjust this value to move the label left or right
        y=0.6,  # Adjust this value to move the label up or down
        text=f'{ROH_DICT_INV[risk_owner_hazard]} pathway options',  # Your y-axis label text here
        showarrow=False,
        xref='paper',
        yref='paper',
        textangle=-90,  # Rotate text for vertical orientation
        font=dict(size=14),  # Adjust font size as needed
        align='center'
    )

    # Rotate text to be horizontal
    # fig.update_traces(textangle=0)

    # Remove the x-tick labels
    fig.update_xaxes(showticklabels=False,title_text='')

    # Update layout for stacked bar
    fig.update_layout(barmode='relative')

    fig = add_measure_buttons(fig, y_axis_values, risk_owner_hazard)
    # Add figure title
    fig.update_layout(title={'text': figure_title,'y':.98, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})

    # Add arrows and text annotations
    # Arrow pointing to the right (better than baseline)
    fig.add_annotation(
        x=0.3, y=-0.1,
        text="Better than baseline",
        showarrow=True,
        arrowhead=2,
        ax=-40,  # Adjust ax, ay for arrow length and direction
        ay=0,
        yshift=-50,  # Adjust to place the annotation below the plot
        xanchor='right'  # Anchor text to the left of the arrow
    )

    # Arrow pointing to the left (worse than baseline)
    fig.add_annotation(
        x=-0.3, y=-0.1,
        text="Worse than baseline",
        showarrow=True,
        arrowhead=2,
        ax=40,  # Adjust ax, ay for arrow length and direction
        ay=0,
        yshift=-50,  # Adjust to place the annotation below the plot
        xanchor='left'  # Anchor text to the right of the arrow
    )

    fig.update_layout(
        autosize=True,  # Allows the figure to resize based on the enclosing HTML element's size
        margin=dict(l=50, r=50, t=50, b=20)  # Adjust margins to ensure content fits well; customize as needed
    )

    fig.update_xaxes(domain=[0.15, 1])  # Adjusting the domain can change the plotting area's width
    fig.update_yaxes(domain=[0.2, 1])  # Adjusting the domain can change the plotting area's height



    return fig
