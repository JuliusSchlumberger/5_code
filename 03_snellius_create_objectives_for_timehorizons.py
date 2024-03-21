import numpy as np
import sys
from Paper3_v1.main_central_path_directions import LIST_ALL_MODEL_OUTPUTS, DIRECTORY_SYSTEM_PARAMETERS, DIRECTORY_TIMEHORIZON_PATHWAYS
from Paper3_v1.main_performance import get_objective_for_timehorizons


list_all_pathways = np.loadtxt(LIST_ALL_MODEL_OUTPUTS, dtype=str, delimiter=',')
system_parameter_directory = DIRECTORY_SYSTEM_PARAMETERS
timehorizon_directory_path = DIRECTORY_TIMEHORIZON_PATHWAYS

set_of_model_outputs_files = list_all_pathways[int(sys.argv[2]):int(sys.argv[3])]
specifier=int(sys.argv[1])

get_objective_for_timehorizons(set_of_model_outputs_files,system_parameter_directory,system_parameter_directory, timehorizon_directory_path)