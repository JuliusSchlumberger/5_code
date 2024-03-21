import pandas as pd
from Paper3_v1.scripts.utilities.normalize_performance import normalize_performance

def get_normalized_performance(performance_df, benchmark_df_file, normalized_df_file):

    benchmark_df = pd.read_csv(benchmark_df_file)

    # Merge the two DataFrames on the specified columns
    merged_df = pd.merge(performance_df,benchmark_df, on=['objective_parameter','scenario_of_interest', 'performance_metric', 'year'],
                         suffixes=('_normal', '_benchmark'))

    merged_df['normalized_values'] = merged_df.apply(normalize_performance,axis=1)

    # Group by the specified columns and aggregate the differences
    objective_df = merged_df.groupby(['objective_parameter', 'pw_combi_normal', 'scenario_of_interest', 'performance_metric', 'year', 'Value_normal'])[
        'normalized_values'].sum().reset_index()

    objective_df.rename(columns={'pw_combi_normal': 'pw_combi'}, inplace=True)
    objective_df.rename(columns={'Value_normal': 'Value'}, inplace=True)

    objective_df.to_csv(normalized_df_file, index=False)


