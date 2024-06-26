from Paper3_v1.main_timings import combine_all_pathways_sets
from Paper3_v1.main_central_path_directions import DIRECTORY_PATH_PATHWAY_SETS, FILE_PATH_ALL_PATHWAYS_CHANGES, FILE_PATH_ALL_REMOVED_MEASURES, FILTER_CONDITIONS, ROH_LIST


directory_path = DIRECTORY_PATH_PATHWAY_SETS
outputfile_path = FILE_PATH_ALL_PATHWAYS_CHANGES
removed_measures_path = FILE_PATH_ALL_REMOVED_MEASURES
filter_conditions = FILTER_CONDITIONS
rohs = ROH_LIST


combine_all_pathways_sets(directory_path,rohs, outputfile_path,filter_conditions, removed_measures_path)