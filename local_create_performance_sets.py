import numpy as np
import pandas as pd
import sys
from Paper3_v1.main_central_path_directions import LIST_ALL_MODEL_OUTPUTS, DIRECTORY_SYSTEM_PARAMETERS, DIRECTORY_TIMEHORIZON_PATHWAYS, DIRECTORY_TIMEHORIZON_PER_ROH
from Paper3_v1.main_performance import create_system_parameters_per_pw_combi,get_objective_for_timehorizons, aggregate_objective_files_per_sector
import glob
import os

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


# Specify the directory path
directory_path = 'Paper3_v1/data/raw'

# # Construct the pattern to match all .gz files in the directory
# pattern = os.path.join(directory_path, '*.gz')
#
# # Use glob.glob to get a list of .gz files
# gz_files = glob.glob(pattern)
# #
# # print(gz_files)
# # print(error)
#
#
# list_all_pathways = gz_files
# system_parameter_directory = DIRECTORY_SYSTEM_PARAMETERS
#
# set_of_model_outputs_files = list_all_pathways
# specifier=0
# timehorizon_directory_path = DIRECTORY_TIMEHORIZON_PATHWAYS
#
# create_system_parameters_per_pw_combi(set_of_model_outputs_files,system_parameter_directory)
#
# get_objective_for_timehorizons(set_of_model_outputs_files,system_parameter_directory,system_parameter_directory, timehorizon_directory_path)
# #
#
# risk_owner_hazard_of_interest='flood_agr'
# input_directory = DIRECTORY_TIMEHORIZON_PATHWAYS
# output_directory = DIRECTORY_TIMEHORIZON_PER_ROH
# aggregate_objective_files_per_sector(input_directory, risk_owner_hazard_of_interest, output_directory)
#
# from Paper3_v1.main_performance import get_performance_per_sector
# from Paper3_v1.main_central_path_directions import DIRECTORY_TIMEHORIZON_PER_ROH,DIRECTORY_PATH_PERFORMANCE, ROH_LIST, FILE_PATH_BENCHMARK_OUT
#
# input_directory = DIRECTORY_TIMEHORIZON_PER_ROH
# performance_directory_path = DIRECTORY_PATH_PERFORMANCE
# rohs = ROH_LIST
# benchmark_file_path = FILE_PATH_BENCHMARK_OUT
#
# risk_owner_hazard_of_interest='flood_agr'
# #
# #
# get_performance_per_sector(input_directory, risk_owner_hazard_of_interest, benchmark_file_path, performance_directory_path)


from Paper3_v1.main_performance import get_pathways_performances_across_interactions
from Paper3_v1.main_central_path_directions import DIRECTORY_PATH_PERFORMANCE, DIRECTORY_INTERACTIONS, ROH_LIST


directory_path = DIRECTORY_PATH_PERFORMANCE
outputfile_path = DIRECTORY_INTERACTIONS
rohs = ROH_LIST

get_pathways_performances_across_interactions(directory_path, rohs, outputfile_path)