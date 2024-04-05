from Paper3_v1.scripts.process_inputs.get_normalized_performance import get_normalized_performance
from Paper3_v1.scripts.process_inputs.add_cost import add_costs
from Paper3_v1.scripts.utilities.map_system_parameters import SYSTEM_PARAMETERS_LIST
from Paper3_v1.scripts.utilities.create_directory import create_directory_if_not_exists
from Paper3_v1.scripts.process_inputs.create_benchmark_for_normalization import create_benchmark_for_normalization
from Paper3_v1.scripts.process_inputs.get_objective_values import get_objective_values
from Paper3_v1.scripts.process_inputs.get_timehorizons_of_interest import get_timehorizons
from Paper3_v1.scripts.process_inputs.get_performance_values import get_performance_values
from Paper3_v1.scripts.utilities.get_pathway_combi import get_pathway_combi
from Paper3_v1.scripts.utilities.combine_objective_per_roh import combine_objective_per_roh
from Paper3_v1.scripts.process_inputs.get_performance_across_interactions import get_performance_across_interactions
from Paper3_v1.scripts.utilities.find_substring import find_substring
from Paper3_v1.scripts.utilities.get_pathway_interaction_files import load_and_aggregate_files


import pandas as pd
import os
import glob

def create_benchmark_case(benchmark_file_path_in, benchmark_file_path_out):
    df_with_cost = add_costs(benchmark_file_path_in)

    system_performance_df = df_with_cost[df_with_cost['system_parameter'].isin(SYSTEM_PARAMETERS_LIST)]

    create_benchmark_for_normalization(system_performance_df, benchmark_file_path_out)


def create_system_parameters_per_pw_combi(set_of_model_outputs_files, system_parameter_directory):

    create_directory_if_not_exists(system_parameter_directory)

    # Creating a full path pattern to match all CSV files in the directory
    pattern = os.path.join(system_parameter_directory, '*.csv')

    # Using glob to find all paths that match the pattern
    csv_files = glob.glob(pattern)


    # Do for each file in set
    for model_output in set_of_model_outputs_files:
        pathway_combo = get_pathway_combi(model_output)

        if any(pathway_combo in string for string in csv_files):
            print(f'{pathway_combo} already created.')
        else:
            print(f'{pathway_combo} will be created.')
            df_with_cost = add_costs(model_output)
            system_parameters_df = df_with_cost[df_with_cost['system_parameter'].isin(SYSTEM_PARAMETERS_LIST)]

            system_parameters_df.to_csv(f'{system_parameter_directory}/pathways_combi_{pathway_combo}.csv', index=False)

def combine_system_parameters(directory_path, rohs, outputfile_path):
    create_directory_if_not_exists(outputfile_path)

    load_and_aggregate_files(directory_path, rohs, outputfile_path)


def get_objective_for_timehorizons(set_of_model_outputs_files,system_parameter_directory,system_parameter_directory_path, timehorizon_directory_path):

    create_directory_if_not_exists(system_parameter_directory_path)
    create_directory_if_not_exists(timehorizon_directory_path)

    # Creating a full path pattern to match all CSV files in the directory
    pattern = os.path.join(timehorizon_directory_path, '*.csv')

    # Using glob to find all paths that match the pattern
    csv_files = glob.glob(pattern)

    # Do for each file in set
    for model_output in set_of_model_outputs_files:
        pathway_combo = get_pathway_combi(model_output)

        if any(pathway_combo in string for string in csv_files):
            print(f'{pathway_combo} already created.')
        else:
            print(f'{pathway_combo} will be created.')

            objective_df = get_objective_values(f'{system_parameter_directory}/pathways_combi_{pathway_combo}.csv')

            timehorizon_df = get_timehorizons(objective_df)
            timehorizon_df.to_csv(f'{timehorizon_directory_path}/pathway_combi_{pathway_combo}.csv', index=False)

def aggregate_objective_files_per_sector(input_directory, risk_owner_hazard_of_interest, output_directory):
    create_directory_if_not_exists(output_directory)

    # Creating a full path pattern to match all CSV files in the directory
    pattern = os.path.join(input_directory, '*.csv')

    # Using glob to find all paths that match the pattern
    csv_files = glob.glob(pattern)

    risk_hazard_df = combine_objective_per_roh(risk_owner_hazard_of_interest, csv_files)
    risk_hazard_df.to_csv(f'{output_directory}/objectives_{risk_owner_hazard_of_interest}.csv', index=False)

def get_performance_per_sector(input_directory, risk_owner_hazard_of_interest, benchmark_file_path, performance_directory_path):
    create_directory_if_not_exists(performance_directory_path)

    timehorizon_df = pd.read_csv(f'{input_directory}/objectives_{risk_owner_hazard_of_interest}.csv')

    performance_df = get_performance_values(timehorizon_df)

    get_normalized_performance(performance_df, benchmark_file_path,
                               f'{performance_directory_path}/performance_{risk_owner_hazard_of_interest}_normalized.csv')


# def combine_all_performance_sets(directory_path, rohs, outputfile_path):
#     create_directory_if_not_exists(outputfile_path)
#
#     load_and_aggregate_files(directory_path, rohs, outputfile_path)

def get_pathways_performances_across_interactions(directory_path, rohs, outputfile_path):
    create_directory_if_not_exists(outputfile_path)
    create_directory_if_not_exists(f'{outputfile_path}/interaction_map')

    # Creating a full path pattern to match all CSV files in the directory
    pattern = os.path.join(directory_path, '*.csv')

    # Using glob to find all paths that match the pattern
    csv_files = glob.glob(pattern)

    for file_path in csv_files:
        # filename = file_path.split('/')[-1]

        target_sector = find_substring(file_path, rohs)

        df = pd.read_csv(file_path)

        get_performance_across_interactions(df, rohs, target_sector, outputfile_path)




