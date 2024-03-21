import numpy as np
import sys
from Paper3_v1.main_central_path_directions import LIST_ALL_MODEL_OUTPUTS, DIRECTORY_PATH_PATHWAY_SETS
from Paper3_v1.main_timings import create_timing_sets
import glob
import os

# Specify the directory path
directory_path = 'data/raw'

# Construct the pattern to match all .gz files in the directory
pattern = os.path.join(directory_path, '*.gz')

# Use glob.glob to get a list of .gz files
gz_files = glob.glob(pattern)
#
# print(gz_files)
# print(error)


list_all_pathways = gz_files
set_of_model_outputs_files = list_all_pathways
pathway_sets_directory = DIRECTORY_PATH_PATHWAY_SETS

create_timing_sets(set_of_model_outputs_files,specifier=0, pathway_sets_directory=pathway_sets_directory)