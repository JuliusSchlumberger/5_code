from Paper3_v1.main_performance import create_system_parameters_per_pw_combi
from Paper3_v1.main_central_path_directions import LIST_ALL_MODEL_OUTPUTS, FILE_PATH_BENCHMARK_OUT, DIRECTORY_PATH_PERFORMANCE,DIRECTORY_SYSTEM_PARAMETERS, DIRECTORY_TIMEHORIZON_PATHWAYS
import sys
import numpy as np


list_all_pathways = np.loadtxt(LIST_ALL_MODEL_OUTPUTS, dtype=str, delimiter=',')
specifier = int(sys.argv[1])
set_of_model_outputs_files = list_all_pathways[int(sys.argv[2]):int(sys.argv[3])]

benchmark_file_path = FILE_PATH_BENCHMARK_OUT
directory_path = DIRECTORY_PATH_PERFORMANCE
system_parameter_directory = DIRECTORY_SYSTEM_PARAMETERS

create_system_parameters_per_pw_combi(set_of_model_outputs_files,system_parameter_directory)