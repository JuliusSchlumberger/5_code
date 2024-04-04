from Paper3_v1.scripts.visualize.create_classic_pathways import create_grey_plot_colours
from Paper3_v1.scripts.utilities.design_choices.main_dashboard_dropdowns import ROH_DICT_INV
from Paper3_v1.scripts.utilities.filter_options import PERFORMANCE_METRICS_LIST, SCENARIO_OPTIONS, TIMEHORIZONS_OF_INTEREST
from Paper3_v1.scripts.visualize.create_classic_pathways import create_classic_pathways
from Paper3_v1.scripts.utilities.design_choices.create_pathways_map import create_pathways_map
from Paper3_v1.scripts.utilities.design_choices.get_tp_positions import get_tp_positions
from Paper3_v1.scripts.utilities.design_choices.pathways_calculate_vertical_distance import pathways_calculate_vertical_distance
from Paper3_v1.scripts.utilities.design_choices.shuffle_starting_measures import shuffle_order_starting_measures
from Paper3_v1.scripts.utilities.design_choices.optimize_positioning import optimize_positioning
from Paper3_v1.main_central_path_directions import DIRECTORY_PATHWAYS_GENERATOR
import matplotlib.pyplot as plt
from adaptation_pathways.plot import plot_classic_pathway_map as plot

from adaptation_pathways.graph import (
    action_level_by_first_occurrence,
    read_sequences,
    read_tipping_points,
    sequence_graph_to_pathway_map,
    sequences_to_sequence_graph,
)


optimize_positions = False


for roh_of_interest in list(ROH_DICT_INV.keys()):
    print(roh_of_interest)
    all_interactions = [interact for interact in ROH_DICT_INV.keys() if interact != roh_of_interest]
    # all_combis = [all_interactions[:i] for i in range(len(all_interactions)+1)]
    all_combis = [all_interactions[:i] for i in range(len(all_interactions))]
    all_combis = ['&'.join(interaction_set) for interaction_set in all_combis]

    for metric in PERFORMANCE_METRICS_LIST:
        print(metric)
        for scenario in SCENARIO_OPTIONS:
            print(scenario)
            scenario_str = '&'.join(scenario)
            scenarios_title = ', '.join(scenario)
            for interaction in all_combis:
                print(interaction)
                if interaction ==  "":
                    interaction_specifier = ''
                    figure_title = f'Pathways Map to explore pathways options for {scenarios_title} climate scenarios'
                else:
                    interaction_specifier = '_' + roh_of_interest + '&' + interaction
                    split_for_title = interaction.split('&')
                    interactions_title = [ROH_DICT_INV[interact] for interact in split_for_title]
                    interactions_title = ', '.join(interactions_title)
                    figure_title += f'accounting for the presence of {interactions_title} pathways '
                print(interaction_specifier)
                file_specifier = f'{roh_of_interest}_{scenario_str}_{metric}{interaction_specifier}.txt'

                sequences_txt = f'data/pathways_generator/all_sequences_{file_specifier}'
                tipping_points_txt = f'data/pathways_generator/all_tp_timings_{file_specifier}'

                # pathways_map, tipping_points, sequence_graph = create_pathways_map(sequences_txt, tipping_points_txt)
                fig1, ax = plt.subplots(layout="constrained", figsize=(12,6))

                if optimize_positions:
                    best_sequence = optimize_positioning(sequences_txt, tipping_points_txt, num_iterations=50)
                    pass
                else:
                    with open(sequences_txt, 'r') as file:
                        sequences = read_sequences(file)

                    sequence_graph = sequences_to_sequence_graph(sequences)
                    level_by_action = action_level_by_first_occurrence(sequences)

                    pathway_map = sequence_graph_to_pathway_map(sequence_graph)

                    with open(tipping_points_txt, 'r') as file:
                        tipping_points = read_tipping_points(file, pathway_map.actions(), )

                    pathway_map.assign_tipping_points(tipping_points)
                    pathway_map.set_attribute("level", level_by_action)

                    plot(ax, pathway_map)


                fig1.show()
                print(error)
                # pathways_map, tipping_points, sequence_graph = create_pathways_map(sequences_txt, tipping_points_txt)
                #
                # plt.show()
                # print(tipping_points)
                # print(ax.get_yticklabels())
                # print(sequence_graph)

                fig, axes = create_classic_pathways(ax, tipping_points, pathways_map, sequence_graph)




                plt.title(figure_title)

                fig.savefig(f'figures/Pathways_Generator/{file_specifier[:-4]}.png', dpi=300)
                plt.close()
                plt.clf()


