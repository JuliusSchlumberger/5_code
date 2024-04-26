import pandas as pd
import os
from Paper3_v1.scripts.process_inputs.get_unique_pathway_changes import get_pathway_changes, add_end_value
from Paper3_v1.scripts.utilities.create_directory import create_directory_if_not_exists
from Paper3_v1.scripts.process_inputs.replace_missing_measures import replace_missing_measures
from Paper3_v1.scripts.process_inputs.get_pathways_across_interactions import get_performance_across_interactions
from Paper3_v1.main_central_path_directions import ROH_LIST

from Paper3_v1.scripts.process_inputs.get_sequences import get_sequences
from Paper3_v1.scripts.process_inputs.get_tipping_points import get_tipping_points


# Permanently changes the pandas settings
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

def create_timing_sets(set_of_model_outputs_files,specifier, pathway_sets_directory):
    create_directory_if_not_exists(pathway_sets_directory)
    create_directory_if_not_exists(f'{pathway_sets_directory}/removed_timings')
    combined_dfs = []
    timing_removed_dfs = []
    # Do for each file in set
    for model_output in set_of_model_outputs_files:
        pathway_df = get_pathway_changes(model_output)

        cleaned_pathways, timing_removed_measures = replace_missing_measures(pathway_df)

        pathway_df_end = add_end_value(cleaned_pathways)

        combined_dfs.append(pathway_df_end)
        timing_removed_dfs.append(timing_removed_measures)

    # Merge all files in set
    combined_df = pd.concat(combined_dfs, ignore_index=True)
    combined_df.to_csv(f'{pathway_sets_directory}/pathways_unique_changes_set{specifier}.csv', index=False)

    # Merge all files in set
    timing_removed_df = pd.concat(timing_removed_dfs, ignore_index=True)
    timing_removed_df.to_csv(f'{pathway_sets_directory}/removed_timings/pathways_removed_measures_set{specifier}.csv', index=False)

def combine_all_pathways_sets(directory_path,rohs, outputfile_path,filter_conditions, removed_measures_path):
    # List to hold DataFrames
    dfs = []
    directory_paths = [directory_path, f'{directory_path}/removed_timings']
    # Iterate over all files in the directory
    for filename in os.listdir(directory_paths[0]):
        if filename.endswith('.csv'):  # Check if the file is a CSV
            file_path = os.path.join(directory_paths[0], filename)
            df = pd.read_csv(file_path)
            dfs.append(df)

    # Concatenate all DataFrames in the list
    combined_df = pd.concat(dfs, ignore_index=True)
    combined_df.to_csv(outputfile_path, index=False)

    dfs = []
    # Iterate over all files in the directory
    for filename in os.listdir(directory_paths[1]):
        if filename.endswith('.csv'):  # Check if the file is a CSV
            file_path = os.path.join(directory_paths[1], filename)
            df = pd.read_csv(file_path)
            dfs.append(df)

    # Concatenate all DataFrames in the list
    combined_df = pd.concat(dfs, ignore_index=True)

    combined_df[rohs] = combined_df.pw_combi.str.split('_', expand=True).astype(int)

    # Apply Filter
    # Here we do a simple manual filtering but of course any sort of filtering could be used.
    for risk_owner in rohs:
        combined_df = combined_df[combined_df[risk_owner].isin(filter_conditions[risk_owner])]

    # Save file
    combined_df.to_csv(removed_measures_path, index=False)

def create_sequences_tipping_points(input_file_path, output_file_path):
    df = pd.read_csv(input_file_path)
    get_performance_across_interactions(df, ROH_LIST, output_file_path)