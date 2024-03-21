from Paper3_v1.main_performance import create_benchmark_case
from Paper3_v1.main_central_path_directions import FILE_PATH_BENCHMARK_IN, FILE_PATH_BENCHMARK_OUT
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


benchmark_file_path_in = 'Paper3_v1/data/raw/portfolio_00_00_00_00.csv.gz'
benchmark_file_path_out = FILE_PATH_BENCHMARK_OUT

create_benchmark_case(benchmark_file_path_in, benchmark_file_path_out)