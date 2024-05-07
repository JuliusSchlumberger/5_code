from Paper3_v1.scripts.utilities.calculate_performance_indicators import calculate_performance_metrics
from Paper3_v1.scripts.utilities.merge_sector_pathway_into_pw_combi import merge_sector_pathway_into_pw_combi
from Paper3_v1.scripts.utilities.filter_options import PERFORMANCE_METRICS_LIST, SCENARIO_OPTIONS
from Paper3_v1.scripts.utilities.calculate_performance_indicators import calculate_performance_metrics
from Paper3_v1.scripts.utilities.generate_interaction_combinations import generate_combinations
from Paper3_v1.scripts.utilities.design_choices.main_dashboard_dropdowns import ROH_DICT_INV
from Paper3_v1.scripts.utilities.calculate_performance_indicators import custom_agg
from Paper3_v1.scripts.process_inputs.get_performance_no_interactions import get_performance_no_interactions
from Paper3_v1.scripts.utilities.get_longest_string import get_longest_string
from Paper3_v1.scripts.utilities.convert_into_pathway_sequence import convert_into_pathway_sequence
from Paper3_v1.scripts.process_inputs.get_identifiers import get_identifiers
from Paper3_v1.scripts.utilities.convert_into_tp_files import convert_into_tp_files
from Paper3_v1.scripts.process_inputs.calculate_tipping_pint_metrics import calculate_tipping_point_metrics
from Paper3_v1.main_central_path_directions import PATHWYAYS_SPECIFIER
from Paper3_v1.scripts.process_inputs.get_sequences import get_sequences
from Paper3_v1.scripts.process_inputs.get_tipping_points import get_tipping_points


import pandas as pd
import numpy as np


def get_performance_across_interactions(df, rohs, outputfile_path):

    df[rohs] = df.pw_combi.str.split('_', expand=True)
    # print(df[df.flood_urb != '00'])
    # print(error)
    mapping_dict = get_sequences(df)
    print(mapping_dict)
    # No Interactions
    for target_roh in rohs:
        df_subset = df.copy()

        relevant_roh = [target_roh]
        not_relevant_roh = [specific_roh for specific_roh in rohs if specific_roh != target_roh]
        # Remove all combinations which are not relevant
        for specific_roh in not_relevant_roh:
            df_subset = df_subset[
                df_subset[specific_roh] == '00']  # those combinations where no measure implemented for not relevant_roh
        for specific_roh in relevant_roh:
            df_subset = df_subset[
                df_subset[specific_roh] != '00']  # those combinations where measures implemented for relevant_roh

        # Group by and aggregate with custom logic
        df_subset.index.names = ['new_index_name' if x == target_roh else x for x in df_subset.index.names]
        # print(df_subset)
        # mapping_dict = get_sequences(df_subset, outputfile_path, target_roh)
        get_tipping_points(df_subset, mapping_dict, outputfile_path, target_roh)

        # With interactions
        all_interactions = [interact for interact in ROH_DICT_INV.keys() if interact != target_roh]
        # all_combis = [all_interactions[:i] for i in range(len(all_interactions)+1)]
        all_combis = [all_interactions[:i] for i in range(len(all_interactions) + 1)]
        all_combis = [target_roh + '&' + '&'.join(interaction_set) for interaction_set in all_combis]

        # interaction_combinations = generate_combinations(rohs, target_roh)

        for interaction in all_combis[1:]:
            df_subset_i = df.copy()
            relevant_roh = interaction.split('&')
            not_relevant_roh = [specific_roh for specific_roh in rohs if specific_roh not in relevant_roh]

            # Remove all combinations which are not relevant
            for specific_roh in not_relevant_roh:
                df_subset_i = df_subset_i[
                    df_subset_i[specific_roh] == '00']  # those combinations where no measure implemented for not relevant_roh
            # print(df_subset_i)
            for specific_roh in relevant_roh:
                df_subset_i = df_subset_i[
                    df_subset_i[specific_roh] != '00']  # those combinations where measures implemented for relevant_roh
            # Group by and aggregate with custom logic

            df_subset_i.index.names = ['new_index_name' if x == target_roh else x for x in df_subset_i.index.names]

            # mapping_dict = get_sequences(df_subset_i, outputfile_path, target_roh, interaction)

            get_tipping_points(df_subset_i, mapping_dict, outputfile_path, target_roh, interaction)
