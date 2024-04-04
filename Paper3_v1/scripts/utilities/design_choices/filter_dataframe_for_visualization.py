from Paper3_v1.scripts.visualize.create_main_dashboard_structure import create_main_dashboard_structure
import dash
from dash import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go  # Import Plotly's graph_objects module
from Paper3_v1.scripts.utilities.design_choices.main_dashboard_dropdowns import PATHWAYS_TO_HIGHLIGHT, ROH_DICT, PERFORMANCE_METRICS

from Paper3_v1.main_central_path_directions import DIRECTORY_AGGREGATED_PERFORMANCE, ROH_LIST
from Paper3_v1.scripts.utilities.map_system_parameters import SECTOR_OBJECTIVES


def filter_dataframe_for_visualization(df, risk_owner_hazard, timehorizon, scenarios, performance_metric):

    # Filter the dataframe based on selections
    selected_scenarios = '&'.join(scenarios)

    # if interactions_of_interest is None:
    #     relevant_df = df_dict[risk_owner_hazard]
    #     active_for_interactions = [risk_owner_hazard]
    # else:
    #     active_for_interactions = [risk_owner_hazard] + interactions_of_interest
    #     key = '_'.join(sorted(active_for_interactions))
    #     relevant_df = df_dict[key]

    filtered_df = df[
        (df['year'].isin([timehorizon])) &  # Assuming timehorizon is a single selection, not a list
        (df['scenario_of_interest'] == selected_scenarios) &
        (df['performance_metric'].isin(performance_metric)) &
        (df.objective_parameter.isin(SECTOR_OBJECTIVES[risk_owner_hazard]))
        ].copy()

    filtered_df[ROH_LIST] = filtered_df.pw_combi.str.split('_', expand=True)

    # Split 'pw_combi' column and expand into separate columns
    filtered_df.loc[:,ROH_LIST] = filtered_df[ROH_LIST].astype(int)

    # Identify columns in B not in A
    columns_to_drop = [column for column in ROH_LIST if column != risk_owner_hazard]

    # Drop these columns from the DataFrame
    filtered_df = filtered_df.drop(columns=columns_to_drop, errors='ignore')

    return filtered_df
