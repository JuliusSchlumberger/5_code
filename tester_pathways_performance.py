from Paper3_v1.scripts.visualize.create_main_dashboard_structure import create_main_dashboard_structure
import dash
from dash import Input, Output, State,callback_context, dcc, html
import plotly.io as pio

from flask_caching import Cache
import dash_bootstrap_components as dbc
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go  # Import Plotly's graph_objects module
from Paper3_v1.scripts.utilities.design_choices.main_dashboard_dropdowns import PATHWAYS_TO_HIGHLIGHT, ROH_DICT,ROH_DICT_INV, SECTOR_OBJECTIVES_BUTTONS, TIMEHORIZONS_INV
from Paper3_v1.scripts.utilities.design_choices.main_dashboard_texts import PERFORMANCE, DASHBOARD_EXPLANATION
import base64
from io import BytesIO

from Paper3_v1.main_central_path_directions import ROH_LIST, PATHWAYS_GENERATOR_FIGURES, LEGENDS_LOCATION
from Paper3_v1.scripts.utilities.map_system_parameters import SECTOR_OBJECTIVES
from Paper3_v1.scripts.visualize.Parallel_Coordinates_Plot import Parallel_Coordinates_Plot
from Paper3_v1.scripts.visualize.Stacked_Bar_Plot import Stacked_Bar_Plot
from Paper3_v1.scripts.visualize.Heatmap import Heatmap
from Paper3_v1.scripts.visualize.Interaction_Heatmap import Interaction_Heatmap
from Paper3_v1.scripts.utilities.filter_options import PERFORMANCE_METRICS_LIST, SCENARIO_OPTIONS
from Paper3_v1.scripts.utilities.design_choices.filter_dataframe_for_visualization import filter_dataframe_for_visualization
from Paper3_v1.scripts.utilities.design_choices.main_dashboard_dropdowns import SCENARIOS_INV
from Paper3_v1.main_central_path_directions import DIRECTORY_INTERACTIONS, DIRECTORY_OBJECTIVES_FOR_COUNT, DIRECTORY_PATH_PERFORMANCE, COLUMN_TYPES, DIRECTORY_PATHWAYS_GENERATOR, PATHWYAYS_SPECIFIER
from Paper3_v1.scripts.visualize.update_pcp_counter import update_pcp_counter
import pathlib
# from Paper3_v1.scripts.visualize.PathwaysMaps import PathwaysMaps


performance_df_dict = {
    ROH_LIST[0]: pd.read_csv(f'{DIRECTORY_INTERACTIONS}/performance_{ROH_LIST[0]}_no_interactions.csv'),
    ROH_LIST[1]: pd.read_csv(f'{DIRECTORY_INTERACTIONS}/performance_{ROH_LIST[1]}_no_interactions.csv'),
    ROH_LIST[2]: pd.read_csv(f'{DIRECTORY_INTERACTIONS}/performance_{ROH_LIST[2]}_no_interactions.csv'),
    ROH_LIST[3]: pd.read_csv(f'{DIRECTORY_INTERACTIONS}/performance_{ROH_LIST[3]}_no_interactions.csv')}



def pathways_performance(scenarios, plot_type, risk_owner_hazard, performance_metric, timehorizon):
    if len(scenarios) == 1:
        scenarios_title = f'{SCENARIOS_INV[scenarios[0]]} climate scenario'
    else:
        better_names = [SCENARIOS_INV[scen] for scen in scenarios]
        scenarios_title = 'across multiple climate scenarios [' + ' & '.join(better_names) + ']'

    figure_title = f'Analyse Pathways Performance ({timehorizon} years; {scenarios_title})'
    #  Load Data for normal figure
    performance_df_of_interest = performance_df_dict[risk_owner_hazard]
    if plot_type == 'PCP':
        if performance_metric in PERFORMANCE_METRICS_LIST[:-1]:
            relevant_metrics = PERFORMANCE_METRICS_LIST[:-1]
        else:
            relevant_metrics = [performance_metric]
    else:
        relevant_metrics = [performance_metric]
    filtered_df = filter_dataframe_for_visualization(performance_df_of_interest, risk_owner_hazard,
                                                     timehorizon,
                                                     scenarios,
                                                     relevant_metrics)

    if plot_type == 'PCP':
        fig = Parallel_Coordinates_Plot(df=filtered_df, risk_owner_hazard=risk_owner_hazard, figure_title=figure_title)

        initial_dimensions = list(fig['data'][0]['dimensions'])  # Create a copy of the dimensions

        # for i, dim in enumerate(initial_dimensions):
        #     if dim['label'] == 'performance_metric':
        #         # Define your ranges mapping
        #         ranges = {'5%': 0, '50%': .5, 'average': .6, '95%': 1}
        #         target_range = ranges.get(performance_metric, 0.5)  # Default to 0.5 if not found
        #
        #         # Set the constraintrange around the target value
        #         dim["constraintrange"] = [target_range - 0.05, target_range + 0.05]
        #     elif dim['label'] == ROH_DICT_INV[risk_owner_hazard]:
        #         # Define your ranges mapping
        #         ranges = {'5%': 0, '50%': .5, 'average': .6, '95%': 1}
        #         target_range = ranges.get(performance_metric, 0.5)  # Default to 0.5 if not found
        #     else:
        #         # Remove any existing constraintrange
        #         dim.pop("constraintrange", None)

        # Ensure to update the dimensions in the correct location
        fig['data'][0]['dimensions'] = initial_dimensions

        return fig
    elif plot_type == 'StackedBar':
        return Stacked_Bar_Plot(df=filtered_df, risk_owner_hazard=risk_owner_hazard,
                                sector_objectives=SECTOR_OBJECTIVES[risk_owner_hazard], figure_title=figure_title)
    elif plot_type == 'Heatmap':
        return Heatmap(df=filtered_df, risk_owner_hazard=risk_owner_hazard,
                       sector_objectives=SECTOR_OBJECTIVES[risk_owner_hazard], figure_title=figure_title)
    else:
        return go.Figure()


for plot_type in ['StackedBar', 'PCP', 'Heatmap']:
# for plot_type in ['PCP']:
    for risk_owner_hazard in ROH_DICT_INV:
        for performance_metric in PERFORMANCE_METRICS_LIST:
            for timehorizon in TIMEHORIZONS_INV:
                for scenarios in SCENARIO_OPTIONS:
                    if len(scenarios) > 1:
                        scenario_str = '&'.join(scenarios)
                    else:
                        scenario_str = scenarios[0]
                    fig = pathways_performance(scenarios, plot_type, risk_owner_hazard, performance_metric, timehorizon)
                    fig.show()
                    print(error)
                    pathlib.Path(f'Dashboard_v1/assets/figures/{plot_type}/{risk_owner_hazard}/').mkdir(parents=True, exist_ok=True)
                    fig.write_json(f'Dashboard_v1/assets/figures/{plot_type}/{risk_owner_hazard}/plot_{timehorizon}_{scenario_str}_{performance_metric}.json')
                    # fig.write_html(
                    #     f'Dashboard_v1/assets/figures/{plot_type}/{risk_owner_hazard}/plot_{timehorizon}_{scenario_str}_{performance_metric}.html')

