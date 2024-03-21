import pandas as pd
import numpy as np
import plotly.graph_objects as go  # Import Plotly's graph_objects module

from Paper3_v1.main_central_path_directions import MEASURE_LOGOS, ALL_PATHWAYS
from Paper3_v1.scripts.utilities.design_choices.add_logos_legend import add_logos_legend





def add_measure_buttons(fig, y_ticks, risk_owner_hazard):
    legend_items = []
    for y_tick in y_ticks:
        # Identify specific set of measures
        row = ALL_PATHWAYS[risk_owner_hazard].loc[int(y_tick)-1,:].values

        for i, measure in enumerate(row[::-1]):
            if measure not in ['no_measure', np.nan, 'nan', np.NaN, '']:
                # Get the logo filename for the current column from the dictionary
                img_path = MEASURE_LOGOS[measure]

                fig.add_layout_image(
                    dict(
                        source=img_path,
                        xref="paper",  # Use "paper" for relative positioning
                        yref="y",  # Use axis ID for aligning with specific ticks
                        x=0.12 - i * 0.027,  # Adjust this value to position the image on the x-axis
                        y=str(int(y_tick)-1),  # Align with a specific y-axis tick label
                        sizex=.8,
                        sizey=.8,
                        xanchor="center",
                        yanchor="middle"
                    )
                )

                legend_items.append({'name': measure, 'logo': img_path})

    # Use a set to track seen dictionaries (requires dicts to be hashable, Python 3.7+)
    seen = set()
    unique_dicts = []
    for d in legend_items:
        # Convert dict to a hashable form (tuple of sorted items)
        hashable_dict = tuple(sorted(d.items()))
        if hashable_dict not in seen:
            unique_dicts.append(d)
            seen.add(hashable_dict)


    fig = add_logos_legend(fig, unique_dicts)


    return fig




