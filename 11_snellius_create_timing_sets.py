import numpy as np
import sys
from Paper3_v1.main_central_path_directions import LIST_ALL_MODEL_OUTPUTS, DIRECTORY_PATH_PATHWAY_SETS
from Paper3_v1.main_timings import create_timing_sets


list_all_pathways = np.loadtxt(LIST_ALL_MODEL_OUTPUTS, dtype=str, delimiter=',')
set_of_model_outputs_files = list_all_pathways[int(sys.argv[2]):int(sys.argv[3])]
pathway_sets_directory = DIRECTORY_PATH_PATHWAY_SETS

create_timing_sets(set_of_model_outputs_files,specifier=int(sys.argv[1]), pathway_sets_directory=pathway_sets_directory)