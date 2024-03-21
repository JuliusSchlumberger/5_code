import numpy as np

from Paper3_v1.scripts.visualize.create_main_dashboard_structure import create_main_dashboard_structure
import dash
from dash import Input, Output, State,callback_context

from flask_caching import Cache
import dash_bootstrap_components as dbc
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go  # Import Plotly's graph_objects module
from Paper3_v1.scripts.utilities.design_choices.main_dashboard_dropdowns import PATHWAYS_TO_HIGHLIGHT, ROH_DICT, SECTOR_OBJECTIVES_BUTTONS

from Paper3_v1.main_central_path_directions import ROH_LIST
from Paper3_v1.scripts.utilities.map_system_parameters import SECTOR_OBJECTIVES
from Paper3_v1.scripts.visualize.Parallel_Coordinates_Plot import Parallel_Coordinates_Plot
from Paper3_v1.scripts.visualize.Stacked_Bar_Plot import Stacked_Bar_Plot
from Paper3_v1.scripts.visualize.Heatmap import Heatmap
from Paper3_v1.scripts.visualize.Interaction_Heatmap import Interaction_Heatmap
from Paper3_v1.scripts.utilities.design_choices.filter_dataframe_for_visualization import filter_dataframe_for_visualization
from Paper3_v1.main_central_path_directions import DIRECTORY_INTERACTIONS, DIRECTORY_OBJECTIVES_FOR_COUNT, DIRECTORY_PATH_PERFORMANCE, COLUMN_TYPES, DIRECTORY_PATHWAYS_GENERATOR, PATHWYAYS_SPECIFIER
from Paper3_v1.scripts.visualize.update_pcp_counter import update_pcp_counter
from Paper3_v1.scripts.visualize.PathwaysMaps import PathwaysMaps

import re

# Permanently changes the pandas settings
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)



# Load all relevant files
performance_df_dict = {
    ROH_LIST[0]: pd.read_csv(f'{DIRECTORY_INTERACTIONS}/performance_{ROH_LIST[0]}_no_interactions.csv'),
    ROH_LIST[1]: pd.read_csv(f'{DIRECTORY_INTERACTIONS}/performance_{ROH_LIST[1]}_no_interactions.csv'),
    ROH_LIST[2]: pd.read_csv(f'{DIRECTORY_INTERACTIONS}/performance_{ROH_LIST[2]}_no_interactions.csv'),
    ROH_LIST[3]: pd.read_csv(f'{DIRECTORY_INTERACTIONS}/performance_{ROH_LIST[3]}_no_interactions.csv')}

# objectives_for_count_dict = {
#     ROH_LIST[0]: pd.read_csv(f'{DIRECTORY_OBJECTIVES_FOR_COUNT}/objectives_for_count_no_interactions_{ROH_LIST[0]}.csv'),
#     ROH_LIST[1]: pd.read_csv(f'{DIRECTORY_OBJECTIVES_FOR_COUNT}/objectives_for_count_no_interactions_{ROH_LIST[1]}.csv'),
#     ROH_LIST[2]: pd.read_csv(f'{DIRECTORY_OBJECTIVES_FOR_COUNT}/objectives_for_count_no_interactions_{ROH_LIST[2]}.csv'),
#     ROH_LIST[3]: pd.read_csv(f'{DIRECTORY_OBJECTIVES_FOR_COUNT}/objectives_for_count_no_interactions_{ROH_LIST[3]}.csv'),
#     'flood_agr_flood_urb': pd.read_csv(f'{DIRECTORY_OBJECTIVES_FOR_COUNT}/objectives_for_count_combinations_flood_agr_flood_urb.csv'),
#     'drought_shp_flood_urb': pd.read_csv(f'{DIRECTORY_OBJECTIVES_FOR_COUNT}/objectives_for_count_combinations_drought_shp_flood_urb.csv'),
#     'drought_shp_flood_agr_flood_urb': pd.read_csv(f'{DIRECTORY_OBJECTIVES_FOR_COUNT}/objectives_for_count_combinations_drought_shp_flood_agr_flood_urb.csv'),
#     'drought_shp_flood_agr': pd.read_csv(f'{DIRECTORY_OBJECTIVES_FOR_COUNT}/objectives_for_count_combinations_drought_shp_flood_agr.csv'),
#     'drought_agr_flood_urb': pd.read_csv(f'{DIRECTORY_OBJECTIVES_FOR_COUNT}/objectives_for_count_combinations_drought_agr_flood_urb.csv'),
#     'drought_agr_flood_agr_flood_urb': pd.read_csv(f'{DIRECTORY_OBJECTIVES_FOR_COUNT}/objectives_for_count_combinations_drought_agr_flood_agr_flood_urb.csv'),
#     'drought_agr_flood_agr': pd.read_csv(f'{DIRECTORY_OBJECTIVES_FOR_COUNT}/objectives_for_count_combinations_drought_agr_flood_agr.csv'),
#     'drought_agr_drought_shp_flood_urb': pd.read_csv(f'{DIRECTORY_OBJECTIVES_FOR_COUNT}/objectives_for_count_combinations_drought_agr_drought_shp_flood_urb.csv'),
#     'drought_agr_drought_shp_flood_agr_flood_urb': pd.read_csv(f'{DIRECTORY_OBJECTIVES_FOR_COUNT}/objectives_for_count_combinations_drought_agr_drought_shp_flood_agr_flood_urb.csv'),
#     'drought_agr_drought_shp_flood_agr': pd.read_csv(f'{DIRECTORY_OBJECTIVES_FOR_COUNT}/objectives_for_count_combinations_drought_agr_drought_shp_flood_agr.csv'),
#     'drought_agr_drought_shp': pd.read_csv(f'{DIRECTORY_OBJECTIVES_FOR_COUNT}/objectives_for_count_combinations_drought_agr_drought_shp.csv'),
# #
# }
performance_interactions_df_dict = {
    # 'flood_agr_flood_urb': pd.read_csv('data/pathways_performance/all_pathways_combinations_flood_agr_flood_urb.csv'),
    # 'drought_shp_flood_urb': pd.read_csv('data/pathways_performance/all_pathways_combinations_drought_shp_flood_urb.csv'),
    # 'drought_shp_flood_agr_flood_urb': pd.read_csv('data/pathways_performance/all_pathways_combinations_drought_shp_flood_agr_flood_urb.csv'),
    # 'drought_shp_flood_agr': pd.read_csv('data/pathways_performance/all_pathways_combinations_drought_shp_flood_agr.csv'),
    'flood_agr_flood_urb': pd.read_csv(f'{DIRECTORY_INTERACTIONS}/performance_flood_agr_combi_flood_agr&flood_urb.csv'),
    'drought_agr_flood_agr_flood_urb': pd.read_csv(f'{DIRECTORY_INTERACTIONS}/performance_flood_agr_combi_flood_agr&drought_agr&flood_urb.csv'),
    'drought_agr_flood_agr': pd.read_csv(f'{DIRECTORY_INTERACTIONS}/performance_flood_agr_combi_flood_agr&drought_agr.csv'),
    # 'drought_agr_drought_shp_flood_urb': pd.read_csv('data/pathways_performance/all_pathways_combinations_drought_agr_drought_shp_flood_urb.csv'),
    # 'drought_agr_drought_shp_flood_agr_flood_urb': pd.read_csv('data/pathways_performance/all_pathways_combinations_drought_agr_drought_shp_flood_agr_flood_urb.csv'),
    # 'drought_agr_drought_shp_flood_agr': pd.read_csv('data/pathways_performance/all_pathways_combinations_drought_agr_drought_shp_flood_agr.csv'),
    # 'drought_agr_drought_shp': pd.read_csv('data/pathways_performance/all_pathways_combinations_drought_agr_drought_shp.csv'),
           }

# df_timehorizons_dict = {
#     ROH_LIST[0]: pd.read_csv(f'data/aggregated_pathways_timehorizons/interactions/performance_{ROH_LIST[0]}.csv'),
#     ROH_LIST[1]: pd.read_csv(f'data/aggregated_pathways_timehorizons/interactions/performance_{ROH_LIST[1]}.csv'),
#     ROH_LIST[2]: pd.read_csv(f'data/aggregated_pathways_timehorizons/interactions/performance_{ROH_LIST[2]}.csv'),
#     ROH_LIST[3]: pd.read_csv(f'data/aggregated_pathways_timehorizons/interactions/performance_{ROH_LIST[3]}.csv'),
#     # 'flood_agr_flood_urb': pd.read_csv('data/aggregated_pathways_timehorizons/all_pathways_combinations_flood_agr_flood_urb.csv'),
#     # 'drought_shp_flood_urb': pd.read_csv('data/aggregated_pathways_timehorizons/all_pathways_combinations_drought_shp_flood_urb.csv'),
#     # 'drought_shp_flood_agr_flood_urb': pd.read_csv('data/aggregated_pathways_timehorizons/all_pathways_combinations_drought_shp_flood_agr_flood_urb.csv'),
#     # 'drought_shp_flood_agr': pd.read_csv('data/aggregated_pathways_timehorizons/all_pathways_combinations_drought_shp_flood_agr.csv'),
#     # 'drought_agr_flood_urb': pd.read_csv('data/aggregated_pathways_timehorizons/all_pathways_combinations_drought_agr_flood_urb.csv'),
#     # 'drought_agr_flood_agr_flood_urb': pd.read_csv('data/aggregated_pathways_timehorizons/all_pathways_combinations_drought_agr_flood_agr_flood_urb.csv'),
#     # 'drought_agr_flood_agr': pd.read_csv('data/aggregated_pathways_timehorizons/all_pathways_combinations_drought_agr_flood_agr.csv'),
#     # 'drought_agr_drought_shp_flood_urb': pd.read_csv('data/aggregated_pathways_timehorizons/all_pathways_combinations_drought_agr_drought_shp_flood_urb.csv'),
#     # 'drought_agr_drought_shp_flood_agr_flood_urb': pd.read_csv('data/aggregated_pathways_timehorizons/all_pathways_combinations_drought_agr_drought_shp_flood_agr_flood_urb.csv'),
#     # 'drought_agr_drought_shp_flood_agr': pd.read_csv('data/aggregated_pathways_timehorizons/all_pathways_combinations_drought_agr_drought_shp_flood_agr.csv'),
#     # 'drought_agr_drought_shp': pd.read_csv('data/aggregated_pathways_timehorizons/all_pathways_combinations_drought_agr_drought_shp.csv'),
#            }
# print(no_interaction_performance_dict)

sequence_txt_dict = {'flood_agr': f'{DIRECTORY_PATHWAYS_GENERATOR}/all_sequences_pathways_list_f_a.txt',
                     'drought_agr': f'{DIRECTORY_PATHWAYS_GENERATOR}/all_sequences_pathways_list_d_a.txt',
                     'flood_urb': f'{DIRECTORY_PATHWAYS_GENERATOR}/all_sequences_pathways_list_f_u.txt',
                     'drought_shp': f'{DIRECTORY_PATHWAYS_GENERATOR}/all_sequences_pathways_list_d_s.txt',}

current_selections = {}
interaction_sequences_dict = {}
interaction_timings_dict = {}

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


list_columns = ['climvar', 'pw_combi','objective_parameter','Value','year','scenario_of_interest']
column_types = {column_name: 'float32' if column_name in ['Value', 'year'] else 'category' for column_name in list_columns}

app = create_main_dashboard_structure(app)

@app.callback(
    Output('highlight_pathway', 'options'),
    Input('risk_owner_hazard', 'value'))
def set_pathways_options(selected_risk_hazard):
    if selected_risk_hazard is None or selected_risk_hazard not in PATHWAYS_TO_HIGHLIGHT:
        # Return empty list or default options if selected_risk_hazard is None or not found
        return []
    return [{'label': i, 'value': i} for i in PATHWAYS_TO_HIGHLIGHT[selected_risk_hazard]]

@app.callback(
    Output('multi_sectoral_interactions', 'options'),
    Input('risk_owner_hazard', 'value'))
def set_multi_sector_interaction_options(selected_risk_hazard):
    if selected_risk_hazard is None:
        # Return empty list or default options if selected_risk_hazard is None or not found
        return []
    # Filter out selected_risk_hazard from the ROH list
    filtered_options = [i for i in ROH_DICT if ROH_DICT[i] != selected_risk_hazard]
    # print(selected_risk_hazard)
    return [{'label': i, 'value': ROH_DICT[i]} for i in filtered_options]

@app.callback(
    Output('interaction_objective_of_interest', 'options'),
    Input('risk_owner_hazard', 'value'))
def set_multi_sector_objective_option(selected_risk_hazard):
    if selected_risk_hazard is None:
        # Return empty list or default options if selected_risk_hazard is None or not found
        return []
    # Filter out selected_risk_hazard from the SECTOR_OBJECTIVES_BUTTONS list
    return [{'label': i, 'value': i} for i in SECTOR_OBJECTIVES_BUTTONS[selected_risk_hazard]]


@app.callback(
    Output('options-graph', 'src'),
    [Input('risk_owner_hazard', 'value'),
     Input('timehorizon', 'value'),
     Input('scenarios', 'value'),
     Input('performance_metric', 'value'),
     Input('multi_sectoral_interactions', 'value'),
     ]
)
def update_options_graph(risk_owner_hazard, timehorizon, scenarios, performance_metric, interactions_of_interest):
    if any(input_value is None for input_value in
           [risk_owner_hazard, timehorizon, scenarios, performance_metric]):
        return f''

    scenarios_str = '&'.join(scenarios)
    print(scenarios_str)
    # Load files
    sequence_txt = f'{DIRECTORY_PATHWAYS_GENERATOR}/all_sequences_{risk_owner_hazard}_{scenarios_str}_{performance_metric}.txt'
    print(sequence_txt)
    tipping_points_txt = f'{DIRECTORY_PATHWAYS_GENERATOR}/all_tp_timings_{risk_owner_hazard}_{scenarios_str}_{performance_metric}.txt'
    sequence_txt_new = None
    tipping_points_txt_new = None

    if interactions_of_interest is not None:
        interactions_str = '&'.join(interaction for interaction in interactions_of_interest)
        sequence_txt_new = f'{DIRECTORY_PATHWAYS_GENERATOR}/all_sequences_{risk_owner_hazard}_{performance_metric}_{interactions_str}.txt'
        tipping_points_txt_new = f'{DIRECTORY_PATHWAYS_GENERATOR}/all_tp_timings_{risk_owner_hazard}_{scenarios_str}_{performance_metric}_{interactions_str}.txt'


        for interaction in interactions_of_interest:
            all_rohs_of_interest = interactions_of_interest + [risk_owner_hazard]
            other_interact = [roh for roh in ROH_LIST if roh in all_rohs_of_interest]
            other_interact_str = '&'.join(other_interact)

            # interaction_sequences_dict[interaction] = {
            #     f'{DIRECTORY_PATHWAYS_GENERATOR}/all_sequences_{interaction}_{scenarios_str}_{performance_metric}_{other_interact_str}.txt'
            # }
            # interaction_timings_dict[interaction] = {
            #     f'{DIRECTORY_PATHWAYS_GENERATOR}/all_tp_timings_{interaction}_{scenarios_str}_{performance_metric}_{other_interact_str}.txt'
            # }

    return PathwaysMaps(sequence_txt, tipping_points_txt,sequence_txt_new, tipping_points_txt_new, interactions_of_interest,
                 interaction_sequences_dict, interaction_timings_dict)


@app.callback(
    Output('performance-graph', 'figure'),
    [Input('risk_owner_hazard', 'value'),
     Input('timehorizon', 'value'),
     Input('scenarios', 'value'),
     Input('performance_metric', 'value'),
     Input('multi_sectoral_interactions', 'value'),
    Input('performance-graph', 'restyleData'),
    Input('options', 'value'),
     ],
    [State('performance-graph', 'figure')]
)
def update_performance_graph(risk_owner_hazard, timehorizon, scenarios, performance_metric, interactions_of_interest, restyle_data,plot_type, existing_figure):
    global current_selections

    # Identify the trigger
    ctx = callback_context
    triggered_id = ctx.triggered[0]['prop_id'].split('.')[0]
    print(triggered_id)
    print(interactions_of_interest)
    if interactions_of_interest == []:
        interactions_of_interest = None

    if triggered_id != 'performance-graph' and plot_type == 'PCP':
        current_selections = {}
        restyle_data = None

    # Return empty figure if not all needed inputs are specified
    if any(input_value is None for input_value in
           [risk_owner_hazard, timehorizon, scenarios, performance_metric]):
        return go.Figure()

    else:
        #  Load Data for normal figure
        performance_df_of_interest = performance_df_dict[risk_owner_hazard]
        filtered_df = filter_dataframe_for_visualization(performance_df_of_interest, risk_owner_hazard, timehorizon,
                                           scenarios,
                                           performance_metric, interactions_of_interest)

        if plot_type == 'PCP':
            objectives_for_count = pd.read_csv(
                f'{DIRECTORY_OBJECTIVES_FOR_COUNT}/objectives_for_count_no_interactions_{risk_owner_hazard}.csv',
                dtype=COLUMN_TYPES)

        if interactions_of_interest is not None:
            # Load Data to show interactions
            all_keys = interactions_of_interest + [risk_owner_hazard]
            file_identifier1 = '&'.join(sorted(all_keys))
            file_identifier2 = '_'.join(sorted(all_keys))
            performance_df_of_interest_interactions = pd.read_csv(
                f'{DIRECTORY_PATH_PERFORMANCE}/interactions/performance_{risk_owner_hazard}_combi_{file_identifier1}.csv')

            filtered_df_interactions = filter_dataframe_for_visualization(performance_df_of_interest_interactions, risk_owner_hazard, timehorizon, scenarios,
                                                             performance_metric, interactions_of_interest)

            if plot_type == 'PCP':
                objectives_with_interactions = pd.read_csv(
                    f'{DIRECTORY_OBJECTIVES_FOR_COUNT}/objectives_for_count_combinations_{file_identifier2}.csv',
                    dtype=COLUMN_TYPES)


        if plot_type == 'PCP' and not restyle_data:

            if interactions_of_interest is None:
                return Parallel_Coordinates_Plot(df=filtered_df, risk_owner_hazard=risk_owner_hazard)
            else:
                return Parallel_Coordinates_Plot(df=filtered_df, risk_owner_hazard=risk_owner_hazard,
                                                            df_interaction=filtered_df_interactions)

        if plot_type == 'PCP' and restyle_data:
            # Adjusted access to 'data' attribute for dictionary
            if 'data' in existing_figure:
                dimensions = existing_figure['data'][0]['dimensions']
            else:
                # Handle cases where 'data' might not be present in the figure dictionary
                return go.Figure()

            existing_figure = update_pcp_counter(objectives_for_count, restyle_data, dimensions, current_selections,
                                                                     scenarios, interactions_of_interest,
                                                                     risk_owner_hazard, timehorizon,
                                                                     existing_figure, column=1)

            if interactions_of_interest is not None:
                existing_figure = update_pcp_counter(objectives_for_count, restyle_data, dimensions, current_selections,
                                                     scenarios, interactions_of_interest,
                                                     risk_owner_hazard, timehorizon,
                                                     existing_figure, column=1)

                existing_figure = update_pcp_counter(objectives_with_interactions, restyle_data, dimensions, current_selections,
                                                     scenarios, interactions_of_interest,
                                                     risk_owner_hazard, timehorizon,
                                                     existing_figure, column=2)

            return existing_figure

        # Stacked Bar
        elif plot_type == 'StackedBar':

            if interactions_of_interest is None:
                return Stacked_Bar_Plot(df=filtered_df, risk_owner_hazard=risk_owner_hazard,
                                    sector_objectives=SECTOR_OBJECTIVES[risk_owner_hazard])
            else:
                print('Test to see when error occurs')
                return Stacked_Bar_Plot(df=filtered_df, risk_owner_hazard=risk_owner_hazard,
                                        sector_objectives=SECTOR_OBJECTIVES[risk_owner_hazard],
                                        df_interaction=filtered_df_interactions)

        # Heatmap
        elif plot_type == 'Heatmap':
            if interactions_of_interest is None:
                return Heatmap(df=filtered_df, risk_owner_hazard=risk_owner_hazard,
                                   sector_objectives=SECTOR_OBJECTIVES[risk_owner_hazard])
            else:
                return Heatmap(df=filtered_df, risk_owner_hazard=risk_owner_hazard,
                               sector_objectives=SECTOR_OBJECTIVES[risk_owner_hazard], df_interaction=filtered_df_interactions)
        else:
            return go.Figure()

@app.callback(
    Output('interactions-graph', 'src'),
    [Input('risk_owner_hazard', 'value'),
     Input('timehorizon', 'value'),
     Input('scenarios', 'value'),
     Input('performance_metric', 'value'),
     Input('multi_sectoral_interactions', 'value'),
    Input('interaction_objective_of_interest', 'value'),
     ],
)
def update_interaction_graph(risk_owner_hazard, timehorizon, scenarios, performance_metric, interactions_of_interest, interaction_objective_of_interest):
    # Return empty figure if not all needed inputs are specified
    if any(input_value is None for input_value in
           [risk_owner_hazard, timehorizon, scenarios, performance_metric, interactions_of_interest, interaction_objective_of_interest]):

        return f''

    # Create filtered set
    # Load relevant files
    performance_dfs_of_interest = {}
    baseline_df = performance_df_dict[risk_owner_hazard]
    baseline_df = filter_dataframe_for_visualization(baseline_df, risk_owner_hazard, timehorizon,
                                                     scenarios,
                                                     performance_metric, interactions_of_interest)
    baseline_df = baseline_df[baseline_df.objective_parameter == interaction_objective_of_interest]

    for interaction in interactions_of_interest:
        print('test', interaction)
        file_identifier = risk_owner_hazard + '&' + interaction
        file_name = f'{DIRECTORY_PATH_PERFORMANCE}/interactions/interaction_map/performance_{risk_owner_hazard}_combi_{file_identifier}.csv'
        interaction_df = filter_dataframe_for_visualization(pd.read_csv(file_name),
                                                            risk_owner_hazard,
                                                            timehorizon,
                                                            scenarios,
                                                            performance_metric,
                                                            interactions_of_interest)
        print(interaction_objective_of_interest)
        performance_dfs_of_interest[file_identifier] = interaction_df[
            interaction_df.objective_parameter == interaction_objective_of_interest]

    return Interaction_Heatmap(baseline_df, performance_dfs_of_interest,risk_owner_hazard)


    # filtered_df = performance_df_of_interest





# @app.callback(
#     Output('performance-graph', 'figure'),
#     [Input('risk_owner_hazard', 'value'),
#      Input('timehorizon', 'value'),
#      Input('scenarios', 'value'),
#      Input('performance_metric', 'value'),
#      Input('multi_sectoral_interactions', 'value'), ]
# )
# def update_graphs_multi_interaction(risk_owner_hazard, timehorizon, scenarios, performance_metric,
#                              interactions_of_interest):
#     '''
#     Update options and performance plots. Create interaction plot
#     :param risk_owner_hazard:
#     :param timehorizon:
#     :param scenarios:
#     :param performance_metric:
#     :param interactions_of_interest:
#     :return:
#     '''
#     if any(input_value is None for input_value in
#            [risk_owner_hazard, timehorizon, scenarios, performance_metric]):
#         performance_fig = go.Figure()
#     else:
#         filtered_normal_performance_df = filter_dataframe_for_visualization(performance_df_dict, risk_owner_hazard,
#                                                                             timehorizon,
#                                                                             scenarios,
#                                                                             performance_metric,
#                                                                             interactions_of_interest,
#                                                                             plot_type='performance_no_interactions')
#
#         filtered_interaction_performance_df = filter_dataframe_for_visualization(performance_interactions_df_dict,
#                                                                                  risk_owner_hazard,
#                                                                                  timehorizon,
#                                                                                  scenarios,
#                                                                                  performance_metric,
#                                                                                  interactions_of_interest,
#                                                                                  plot_type='performance_with_interactions')
#
#
#
#         # PCP
#         # fig = Parallel_Coordinates_Plot(df=filtered_df, risk_owner_hazard=risk_owner_hazard)
#
#         # Stacked Bar
#         # fig = Stacked_Bar_Plot(df=filtered_df, risk_owner_hazard=risk_owner_hazard,
#         #                        sector_objectives=SECTOR_OBJECTIVES[risk_owner_hazard])
#
#         # Heatmap
#         # fig = Heatmap(df=filtered_df, risk_owner_hazard=risk_owner_hazard,
#         #                        sector_objectives=SECTOR_OBJECTIVES[risk_owner_hazard])
#
#
#     # return fig


#
# @app.callback(
#     Output('performance-graph', 'figure'),
#     [Input('risk_owner_hazard', 'value'),
#      Input('performance-graph', 'restyleData'),
#      Input('multi_sectoral_interactions', 'value')],
#     [State('performance-graph', 'figure')]
# )
# def update_counter(risk_owner_hazard, restyle_data, interactions_of_interest, existing_figure):
#     # Initialize current_selections if not already done
#     if 'current_selections' not in globals():
#         global current_selections
#         current_selections = {}
#
#     # Check if there's meaningful restyle_data
#     if restyle_data and 'dimensions' in restyle_data[0]:
#         dimensions = existing_figure['data'][0]['dimensions']
#         for change_key, change_value in restyle_data[0].items():
#             match = re.match(r'dimensions\[(\d+)\].constraintrange', change_key)
#             if match:
#                 axis_index = int(match.group(1))
#                 axis_name = dimensions[axis_index]['label']
#                 current_selections[axis_name] = change_value
#
#     # Assuming df_timehorizons_dict and other necessary data preparations are done outside this function
#     # Placeholder for fetching relevant DataFrames based on risk_owner_hazard and interactions_of_interest
#     relevant_df_no_interaction, relevant_df_interaction = get_relevant_dfs(risk_owner_hazard, interactions_of_interest,
#                                                                            df_timehorizons_dict, ROH_LIST)
#
#     # Calculate ratios
#     column_no_interaction = calculate_ratios(relevant_df_no_interaction, current_selections, risk_owner_hazard)
#     column_interaction = calculate_ratios(relevant_df_interaction, current_selections, risk_owner_hazard)
#
#     # Update the table subplot
#     existing_figure['data'][1]['cells']['values'] = [relevant_df_no_interaction[risk_owner_hazard].unique(), column_no_interaction, column_interaction]
#
#     return existing_figure

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

