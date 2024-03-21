from Paper3_v1.main_performance import get_objective_performance_for_timehorizons
from Paper3_v1.main_central_path_directions import LIST_ALL_MODEL_OUTPUTS, FILE_PATH_BENCHMARK_OUT, DIRECTORY_PATH_PERFORMANCE,DIRECTORY_SYSTEM_PARAMETERS
import sys
import numpy as np
import os
import glob

# Specify the directory path
directory_path = 'data/raw'

# Construct the pattern to match all .gz files in the directory
pattern = os.path.join(directory_path, '*.gz')

# Use glob.glob to get a list of .gz files
gz_files = glob.glob(pattern)
list_all_pathways = gz_files
specifier = 0
set_of_model_outputs_files = list_all_pathways

benchmark_file_path = FILE_PATH_BENCHMARK_OUT
directory_path = DIRECTORY_PATH_PERFORMANCE
system_parameter_directory = DIRECTORY_SYSTEM_PARAMETERS

get_objective_performance_for_timehorizons(set_of_model_outputs_files,system_parameter_directory, benchmark_file_path,directory_path)