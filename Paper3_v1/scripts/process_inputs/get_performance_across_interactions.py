from Paper3_v1.scripts.utilities.calculate_performance_indicators import calculate_performance_metrics
from Paper3_v1.scripts.utilities.merge_sector_pathway_into_pw_combi import merge_sector_pathway_into_pw_combi
from Paper3_v1.scripts.utilities.filter_options import PERFORMANCE_METRICS_LIST, SCENARIO_OPTIONS
from Paper3_v1.scripts.utilities.calculate_performance_indicators import calculate_performance_metrics
from Paper3_v1.scripts.utilities.generate_interaction_combinations import generate_combinations
from Paper3_v1.scripts.utilities.calculate_performance_indicators import custom_agg
from Paper3_v1.scripts.process_inputs.get_performance_no_interactions import get_performance_no_interactions
import pandas as pd
import numpy as np


def get_performance_across_interactions(df, rohs, target_roh, outputfile_path):

    interaction_combinations = generate_combinations(rohs,target_roh)
    # print(df.pw_combi.unique)
    print(rohs)

    df[rohs] = df.pw_combi.str.split('_', expand=True)

    get_performance_no_interactions(df, target_roh,rohs, outputfile_path)

    for interaction in interaction_combinations:

        df_subset = df.copy()

        relevant_roh = interaction.split('&')
        not_relevant_roh = [specific_roh for specific_roh in rohs if specific_roh not in relevant_roh]

        # Remove all combinations which are not relevant
        for specific_roh in not_relevant_roh:
            df_subset = df_subset[df_subset[specific_roh] == '00']  # those combinations where no measure implemented for not relevant_roh

        for specific_roh in relevant_roh:
            df_subset = df_subset[df_subset[specific_roh] != '00']  # those combinations where measures implemented for relevant_roh

        # Group by and aggregate with custom logic
        df_subset.index.names = ['new_index_name' if x == target_roh else x for x in df_subset.index.names]
        print(df_subset)
        try:
            result_full_aggregation = df_subset.groupby(
                ['objective_parameter', 'scenario_of_interest', 'performance_metric', 'year', target_roh]).apply(
                lambda x: pd.Series({
                    'Value': custom_agg(x['Value'], x['performance_metric'].iloc[0]),
                    'normalized_values': custom_agg(x['normalized_values'], x['performance_metric'].iloc[0])
                }).round(2)
            ).reset_index()

            # Find the position of the column name in `rohs`
            position = rohs.index(target_roh)

            # Create the new column by modifying the 'default_pw_combi' pattern for each row
            result_full_aggregation['pw_combi'] = result_full_aggregation[target_roh].apply(
                lambda x: ['00' if pos != position else x for pos in range(len(rohs))])

            # Join the lists into strings for each row
            result_full_aggregation['pw_combi'] = result_full_aggregation['pw_combi'].apply(lambda x: '_'.join(x))

            result_full_aggregation.to_csv(f'{outputfile_path}/performance_{target_roh}_combi_{interaction}.csv', index=False)
            df_subset.to_csv(f'{outputfile_path}/interaction_map/performance_{target_roh}_combi_{interaction}.csv', index=False)
        except ValueError:
            pass


def get_performance_across_interactions_old(df, rohs, target_sector):
    result_dfs = []

    df[rohs] = df.pw_combi.str.split('_', expand=True)
    
    # Filtering columns that don't contain only zeros
    filtered_columns = [col for col in rohs if not all(df[col] == '00')]

    for sh in filtered_columns:
        df_subset = df[df[sh] != '00'].copy()
        # Custom aggregation function

        # Group by and aggregate with custom logic
        result = df_subset.groupby(['objective_parameter', 'scenario_of_interest', 'performance_metric', 'year', sh]).apply(
            lambda x: pd.Series({
                'Value': custom_agg(x['Value'], x['performance_metric'].iloc[0]),
                'normalized_values': custom_agg(x['normalized_values'], x['performance_metric'].iloc[0])
            })
        ).reset_index()

        # Find the position of the column name in `rohs`
        position = rohs.index(sh)

        # Create the new column by modifying the 'default_pw_combi' pattern for each row
        result['pw_combi'] = result[sh].apply(
            lambda x: ['00' if pos != position else x for pos in range(len(rohs))])

        # Join the lists into strings for each row
        result['pw_combi'] = result['pw_combi'].apply(lambda x: '_'.join(x))

        result_dfs.append(result)

    final_df = pd.concat(result_dfs, ignore_index=True)
    return final_df


def get_performance_across_interactions_old(df, rohs ):
    # Process each sector-hazard

    result_dfs = []

    df[rohs] = df.pw_combi.str.split('_', expand=True)
    for sh in rohs:
        for metric in PERFORMANCE_METRICS_LIST:
            groupby_group = ['objective_parameter', 'scenario_of_interest', 'performance_metric', 'year', sh]
            metric_df_Value = calculate_performance_metrics(df, groupby_group,
                                                      metric, 'Value').reset_index()
            metric_df_normalized = calculate_performance_metrics(df, groupby_group,
                                                            metric, 'normalized_values').reset_index()

            # Merge the DataFrames on the groupby columns, adding the normalized values to the metric_df_Value
            metric_df_Value = metric_df_Value.merge(
                metric_df_normalized[groupby_group + ['normalized_values']],
                on=groupby_group,
                how='left'
            )

            metric_df_Value['interaction_aggregation_metric'] = metric
            result_dfs.append(metric_df_Value)

    final_df = pd.concat(result_dfs, ignore_index=True)

    return final_df