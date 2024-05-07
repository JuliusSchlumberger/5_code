import pandas as pd
import numpy as np
from Paper3_v1.scripts.utilities.filter_options import PERFORMANCE_METRICS_LIST, SCENARIO_OPTIONS
from Paper3_v1.scripts.process_inputs.calculate_tipping_pint_metrics import calculate_tipping_point_metrics
from Paper3_v1.scripts.utilities.convert_into_tp_files import convert_into_tp_files
from Paper3_v1.scripts.process_inputs.remove_minority_cases import remove_minority_cases
from Paper3_v1.main_central_path_directions import PATHWYAYS_SPECIFIER
from Paper3_v1.scripts.utilities.convert_into_pathway_sequence import convert_into_pathway_sequence


def get_tipping_points(df, mapping_dict, string_output_path, target_roh, interaction=None):

    # for scenario in SCENARIO_OPTIONS:
    for scenario in [['Wp']]:
        scenario_str = '&'.join(scenario)
        filtered_df = df[df['cc_scenario'].isin(scenario)].copy()

        new_df = filtered_df.copy()
        new_df = new_df[new_df.Value != '0']
        new_df = new_df[new_df.Value != '0&99']

        new_for_tps = new_df.copy()
        new_for_sequences = new_df.copy()
        # Create a new column with the substring up until the last '&'
        new_for_tps['implementation_across_multi_risk'] = new_for_tps['Value'].str.rsplit('&', n=1).str[0]  # ensure that a tipping point to implement of new measure is same independent of which measure follows
        new_for_sequences['implementation_across_multi_risk'] = new_for_sequences['Value']  # to ensure that we get every specific pathway using a specific combination
        # new_df['implementation_across_multi_risk'] = np.where(
        #     new_df['Value'].str.endswith('99'),  # Condition: Value ends with '99'
        #     new_df['Value'],  # If True: Keep the whole string
        #     new_df['Value'].str.rsplit('&', n=1).str[0]  # If False: Split and take the first part
        # )

        for metric in [PERFORMANCE_METRICS_LIST[1]]:
            system_parameter = f'pathways_list_{PATHWYAYS_SPECIFIER[target_roh]}'

            # Sequences
            # Adding a new column 'ampersand_count' that counts the occurrences of '&' in the 'Value' column
            df = new_for_sequences.copy()
            df['ampersand_count'] = df['Value'].apply(lambda x: x.count('&'))

            # Step 1: Extract ending substring from 'Value'
            df['Value_end'] = df['Value'].apply(lambda x: x.split('&')[-1])

            # Step 2: Group by necessary columns and 'Value_end'
            grouped = df.groupby(['system_parameter', 'cc_scenario', target_roh, 'ampersand_count', 'Value_end'])

            # Step 3: Count occurrences
            counts = grouped.size().reset_index(name='count')

            # Step 4: Calculate total counts for broader groups (excluding 'Value_end')
            total_counts = counts.groupby(['system_parameter', 'cc_scenario', target_roh, 'ampersand_count'])[
                'count'].transform('sum')

            # Step 5: Calculate ratio
            counts['ratio'] = counts['count'] / total_counts

            # Step 6: Merge the ratios back into the original DataFrame
            result_df = pd.merge(df, counts.drop(columns='count'),
                                 on=['system_parameter', 'cc_scenario', target_roh, 'ampersand_count', 'Value_end'],
                                 how='left')

            # Function to filter groups based on your conditions
            def filter_groups(group):
                max_ampersand_count_to_keep = None
                for ampersand_count in sorted(group['ampersand_count'].unique()):
                    sub_group = group[group['ampersand_count'] == ampersand_count]
                    rows_with_99 = sub_group[sub_group['Value'].str.endswith('&99')]

                    # Check if any row ending in '99' meets the condition
                    if not rows_with_99.empty and (rows_with_99['ratio'] > float(metric.strip('%')) / 100).any():
                        # Keep only rows ending with '99' from this ampersand_count
                        group = group[group['ampersand_count'] != ampersand_count]
                        group = pd.concat([group, rows_with_99])
                        max_ampersand_count_to_keep = ampersand_count
                        break
                    else:
                        # Remove rows ending with '99' from this ampersand_count
                        group = group[
                            (group['ampersand_count'] != ampersand_count) | ~group['Value'].str.endswith('&99')]

                if max_ampersand_count_to_keep is not None:
                    # Drop all rows with higher ampersand_count values
                    group = group[group['ampersand_count'] <= max_ampersand_count_to_keep]

                return group

            # Apply the function to each combination of system_parameter, cc_scenario, flood_agr
            filtered_df = result_df.groupby(['system_parameter', 'cc_scenario', target_roh]).apply(filter_groups).reset_index(
                drop=True)

            new_for_tps = filtered_df.copy()

            # print(result_df)
            # print(error)
            metric_sequ_df = filtered_df.drop_duplicates(subset=['Value', 'system_parameter', target_roh])

            print(metric_sequ_df)

            # Function to select the row with the maximum count of '&'
            def select_max_ampersand(group):
                # Count '&' in each 'Value' and find the index of max count
                return group.loc[group['Value'].str.count('&').idxmax()]

            # Apply the function to each group
            metric_sequ_df = metric_sequ_df.groupby([target_roh, 'system_parameter']).apply(select_max_ampersand).reset_index(
                drop=True)

            subset_sequ = metric_sequ_df[metric_sequ_df.system_parameter == system_parameter]

            subset_sequences = convert_into_pathway_sequence(subset_sequ, mapping_dict, target_roh)

            if interaction == None:
                subset_sequences.to_csv(f'{string_output_path}/all_sequences_{target_roh}_{scenario_str}_{metric}.txt', sep=' ', index=False,
                                        header=False)
                # print(subset_sequences)
            else:
                subset_sequences.to_csv(f'{string_output_path}/all_sequences_{target_roh}_{scenario_str}_{metric}_{interaction}.txt', sep=' ',
                                        index=False,
                                        header=False)

            # Tipping Points

            new_for_tps['implementation_across_multi_risk'] = new_for_tps['Value'].str.rsplit('&', n=1).str[
                0]  # ensure that a tipping point to implement of new measure is same independent of which measure follows


            metric_df = calculate_tipping_point_metrics(new_for_tps, metric).reset_index()
            metric_df['performance_metric'] = metric
            metric_df['scenario_of_interest'] = scenario_str
            system_parameter = f'pathways_list_{PATHWYAYS_SPECIFIER[target_roh]}'
            subset = metric_df[metric_df.system_parameter == system_parameter]
            print(subset)
            subset_sequences = convert_into_tp_files(subset, mapping_dict)
            if interaction == None:
                subset_sequences.to_csv(
                    f'{string_output_path}/all_tp_timings_{target_roh}_{scenario_str}_{metric}.txt',
                    sep=' ', index=False, header=False)
            else:
                subset_sequences.to_csv(
                    f'{string_output_path}/all_tp_timings_{target_roh}_{scenario_str}_{metric}_{interaction}.txt',
                    sep=' ', index=False, header=False)




