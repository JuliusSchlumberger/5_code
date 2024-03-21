import pandas as pd
from Paper3_v1.scripts.utilities.map_system_parameters import OBJECTIVE_PARAMETER_DICT
from Paper3_v1.scripts.process_inputs.get_timehorizons_of_interest import get_timehorizons
from Paper3_v1.scripts.process_inputs.get_performance_values import get_performance_values
from Paper3_v1.main_central_path_directions import DIRECTORY_PROCESSED_DATA


def create_benchmark_for_normalization(benchmark_df,benchmark_performance_file):

    benchmark_df = benchmark_df[benchmark_df.system_parameter.isin(OBJECTIVE_PARAMETER_DICT.keys())]

    # Change from remaining crop revenue to crop loss
    benchmark_df.loc[benchmark_df.system_parameter == 'revenue_agr', 'Value'] = 9.7 - benchmark_df['Value']

    # Iterate through each row and replace values based on the dictionary
    for index, row in benchmark_df.iterrows():
        benchmark_df.loc[index] = row.replace(OBJECTIVE_PARAMETER_DICT)


    benchmark_df.rename(columns={'system_parameter': 'objective_parameter'}, inplace=True)

    timehorizon_df = get_timehorizons(benchmark_df)
    performance_df = get_performance_values(timehorizon_df)

    performance_df.to_csv(benchmark_performance_file, index=False)