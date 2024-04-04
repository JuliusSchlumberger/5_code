import numpy as np

from Paper3_v1.scripts.visualize.create_main_dashboard_structure import create_main_dashboard_structure
import dash
from dash import Input, Output, State,callback_context, dcc, html

from flask_caching import Cache
import dash_bootstrap_components as dbc
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go  # Import Plotly's graph_objects module
from Paper3_v1.scripts.utilities.design_choices.main_dashboard_dropdowns import PATHWAYS_TO_HIGHLIGHT, ROH_DICT,ROH_DICT_INV, SECTOR_OBJECTIVES_BUTTONS
from Paper3_v1.scripts.utilities.design_choices.main_dashboard_texts import PERFORMANCE
import base64
from io import BytesIO

from Paper3_v1.main_central_path_directions import ROH_LIST, PATHWAYS_GENERATOR_FIGURES, LEGENDS_LOCATION
from Paper3_v1.scripts.utilities.map_system_parameters import SECTOR_OBJECTIVES
from Paper3_v1.scripts.visualize.Parallel_Coordinates_Plot import Parallel_Coordinates_Plot
from Paper3_v1.scripts.visualize.Stacked_Bar_Plot import Stacked_Bar_Plot
from Paper3_v1.scripts.visualize.Heatmap import Heatmap
from Paper3_v1.scripts.visualize.Interaction_Heatmap import Interaction_Heatmap
from Paper3_v1.scripts.utilities.filter_options import PERFORMANCE_METRICS_LIST
from Paper3_v1.scripts.utilities.design_choices.filter_dataframe_for_visualization import filter_dataframe_for_visualization
from Paper3_v1.main_central_path_directions import DIRECTORY_INTERACTIONS, DIRECTORY_OBJECTIVES_FOR_COUNT, DIRECTORY_PATH_PERFORMANCE, COLUMN_TYPES, DIRECTORY_PATHWAYS_GENERATOR, PATHWYAYS_SPECIFIER
from Paper3_v1.scripts.visualize.update_pcp_counter import update_pcp_counter
# from Paper3_v1.scripts.visualize.PathwaysMaps import PathwaysMaps

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
    Output('performance_explanation', 'children'),
    Input('performance_metric', 'value'))
def update_explanation_text(performance_metric):
    if performance_metric is None:
        return [html.P(PERFORMANCE['nothing_selected'])]
    else:
        if performance_metric.endswith('%'):
            return [html.P(PERFORMANCE['general_explanation']), html.P(PERFORMANCE['detailed_explanation_CI'])]
        else:
            return [html.P(PERFORMANCE['general_explanation']), html.P(PERFORMANCE['detailed_explanation_otherPerformance'])]


@app.callback(
    [Output('performance_legend-image', 'src'),
    Output('pathways_legend-image', 'src')],
    Input('risk_owner_hazard', 'value'))
def update_legends(risk_owner_hazard):
    # Define the path to the image
    file_path = f'{LEGENDS_LOCATION}/{risk_owner_hazard}_full_legend.png'
    # Encode the image to base64 string using with statement
    with open(file_path, 'rb') as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode('ascii')

    # Return the data URI for the image
    return f'data:image/png;base64,{encoded_image}', f'data:image/png;base64,{encoded_image}'

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
    Output('options-graph', 'src'),
    [Input('risk_owner_hazard', 'value'),
     Input('timehorizon', 'value'),
     Input('scenarios', 'value'),
     Input('performance_metric', 'value'),
     ]
)
def update_options_graph(risk_owner_hazard, timehorizon, scenarios, performance_metric):
    if any(input_value is None for input_value in
           [risk_owner_hazard, timehorizon, scenarios, performance_metric]):
        return f''

    scenarios_str = '&'.join(scenarios)

    figure_identifier = f'{risk_owner_hazard}_{scenarios_str}_{performance_metric}.png'

    # Encode the image to base64 string
    encoded_image = base64.b64encode(open(f'{PATHWAYS_GENERATOR_FIGURES}/{figure_identifier}', 'rb').read()).decode('ascii')

    # return 'data:image/png;base64,{}'.format(encoded_image)
    return f'data:image/png;base64,{encoded_image}'



@app.callback(
    Output('performance-graph', 'figure'),
    [Input('risk_owner_hazard', 'value'),
     Input('timehorizon', 'value'),
     Input('scenarios', 'value'),
     Input('performance_metric', 'value'),
    Input('options', 'value'),
     ],
)
def update_performance_graph(risk_owner_hazard, timehorizon, scenarios, performance_metric, plot_type):
    global current_selections

    # Return empty figure if not all needed inputs are specified
    if any(input_value is None for input_value in
           [risk_owner_hazard, timehorizon, scenarios, performance_metric]):
        return go.Figure()

    else:
        scenarios_title = ', '.join(scenarios)

        figure_title = f'{plot_type} to explore pathways performance after the next {timehorizon} years for {scenarios_title} climate scenarios'
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
            return Parallel_Coordinates_Plot(df=filtered_df, risk_owner_hazard=risk_owner_hazard, figure_title=figure_title)
        elif plot_type == 'StackedBar':
            return Stacked_Bar_Plot(df=filtered_df, risk_owner_hazard=risk_owner_hazard,
                                    sector_objectives=SECTOR_OBJECTIVES[risk_owner_hazard], figure_title=figure_title)
        elif plot_type == 'Heatmap':
            return Heatmap(df=filtered_df, risk_owner_hazard=risk_owner_hazard,
                                   sector_objectives=SECTOR_OBJECTIVES[risk_owner_hazard], figure_title=figure_title)
        else:
            return go.Figure()

@app.callback(
    [Output('interactions-graph', 'figure'),
     Output('interactions-graph', 'style'),
     Output('interactions-image', 'src'),
     Output('interactions-image', 'style')],
    [Input('risk_owner_hazard', 'value'),
     Input('timehorizon', 'value'),
     Input('scenarios', 'value'),
     Input('performance_metric', 'value'),
     Input('multi_sectoral_interactions', 'value'),
    Input('interaction_plot_options', 'value'),
Input('options', 'value'),
     ],
)
def update_interaction_graph(risk_owner_hazard, timehorizon, scenarios, performance_metric, interactions_of_interest, interaction_plot, plot_type):
    # Return empty figure if not all needed inputs are specified
    if any(input_value is None for input_value in
           [risk_owner_hazard, timehorizon, scenarios, performance_metric]):
        return go.Figure(), {}, '', {'display': 'none'}  # Show graph, hide image
    elif interactions_of_interest == []:
        return go.Figure(), {}, '', {'display': 'none'}  # Show graph, hide image


    if interaction_plot == 'graph':
        # Create Performance Plot
        scenarios_title = ', '.join(scenarios)

        figure_title = f'{plot_type} to explore pathways performance after the next {timehorizon} years for {scenarios_title} climate scenarios'

        # Load Data to show interactions
        interactions_title = ', '.join([ROH_DICT_INV[interaction] for interaction in interactions_of_interest])
        figure_title += f'accounting for the presence of {interactions_title} pathways '

        # all_keys = interactions_of_interest + [risk_owner_hazard]
        file_identifier1 = risk_owner_hazard + '&' + '&'.join(interactions_of_interest)

        performance_df_of_interest = performance_df_dict[risk_owner_hazard]
        performance_df_of_interest_interactions = pd.read_csv(
            f'{DIRECTORY_PATH_PERFORMANCE}/interactions/performance_{risk_owner_hazard}_combi_{file_identifier1}.csv')

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

        filtered_df_interactions = filter_dataframe_for_visualization(performance_df_of_interest_interactions,
                                                                      risk_owner_hazard,
                                                                      timehorizon,
                                                                      scenarios,
                                                                      relevant_metrics)

        if plot_type == 'PCP':
            return Parallel_Coordinates_Plot(df=filtered_df, risk_owner_hazard=risk_owner_hazard,
                                             df_interaction=filtered_df_interactions, figure_title=figure_title), {}, '', {'display': 'none'}  # Show graph, hide image
        elif plot_type == 'StackedBar':
            return Stacked_Bar_Plot(df=filtered_df, risk_owner_hazard=risk_owner_hazard,
                                    sector_objectives=SECTOR_OBJECTIVES[risk_owner_hazard],
                                    df_interaction=filtered_df_interactions, figure_title=figure_title), {}, '', {'display': 'none'}  # Show graph, hide image
        elif plot_type == 'Heatmap':
            return Heatmap(df=filtered_df, risk_owner_hazard=risk_owner_hazard,
                           sector_objectives=SECTOR_OBJECTIVES[risk_owner_hazard],
                           df_interaction=filtered_df_interactions, figure_title=figure_title), {}, '', {'display': 'none'}  # Show graph, hide image
        else:
            return go.Figure(), {}, '', {'display': 'none'}  # Show graph, hide image
    elif interaction_plot == 'image':
        # Create Options Plot
        scenarios_str = '&'.join(scenarios)

        interactions_str = risk_owner_hazard + '&' + '&'.join(interaction for interaction in interactions_of_interest)
        figure_identifier = f'{risk_owner_hazard}_{scenarios_str}_{performance_metric}_{interactions_str}.png'

        # Encode the image to base64 string
        encoded_image = base64.b64encode(open(f'{PATHWAYS_GENERATOR_FIGURES}/{figure_identifier}', 'rb').read()).decode(
            'ascii')

        return {}, {'display': 'none'}, f'data:image/png;base64,{encoded_image}', {}  # Hide graph, show image
    else:
        # Fallback case, hide both
        return {}, {'display': 'none'}, '', {'display': 'none'}

    #
    # # Return empty figure if not all needed inputs are specified
    # if any(input_value is None for input_value in
    #        [risk_owner_hazard, timehorizon, scenarios, performance_metric, interactions_of_interest, interaction_objective_of_interest]):
    #
    #     return f''
    #
    # # Create filtered set
    # # Load relevant files
    # performance_dfs_of_interest = {}
    # baseline_df = performance_df_dict[risk_owner_hazard]
    # baseline_df = filter_dataframe_for_visualization(baseline_df, risk_owner_hazard, timehorizon,
    #                                                  scenarios,
    #                                                  [performance_metric], interactions_of_interest)
    # baseline_df = baseline_df[baseline_df.objective_parameter == interaction_objective_of_interest]
    #
    # for interaction in interactions_of_interest:
    #     print('test', interaction)
    #     file_identifier = risk_owner_hazard + '&' + interaction
    #     file_name = f'{DIRECTORY_PATH_PERFORMANCE}/interactions/interaction_map/performance_{risk_owner_hazard}_combi_{file_identifier}.csv'
    #     interaction_df = filter_dataframe_for_visualization(pd.read_csv(file_name),
    #                                                         risk_owner_hazard,
    #                                                         timehorizon,
    #                                                         scenarios,
    #                                                         [performance_metric],
    #                                                         interactions_of_interest)
    #     print(interaction_objective_of_interest)
    #     performance_dfs_of_interest[file_identifier] = interaction_df[
    #         interaction_df.objective_parameter == interaction_objective_of_interest]
    #
    # return Interaction_Heatmap(baseline_df, performance_dfs_of_interest,risk_owner_hazard)
    #
    #
    # # filtered_df = performance_df_of_interest

#
# @app.callback(
#     [Output('graph-output', 'figure'),
#      Output('graph-output', 'style'),
#      Output('image-output', 'src'),
#      Output('image-output', 'style')],
#     [Input('data-selector', 'value')]
# )
# def update_output(selected_value):
#
#


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

