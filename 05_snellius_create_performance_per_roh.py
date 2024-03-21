from Paper3_v1.main_performance import get_performance_per_sector
from Paper3_v1.main_central_path_directions import DIRECTORY_TIMEHORIZON_PER_ROH,DIRECTORY_PATH_PERFORMANCE, ROH_LIST, FILE_PATH_BENCHMARK_OUT
import sys

input_directory = DIRECTORY_TIMEHORIZON_PER_ROH
performance_directory_path = DIRECTORY_PATH_PERFORMANCE
rohs = ROH_LIST
benchmark_file_path = FILE_PATH_BENCHMARK_OUT

risk_owner_hazard_of_interest=sys.argv[1]


get_performance_per_sector(input_directory, risk_owner_hazard_of_interest, benchmark_file_path, performance_directory_path)