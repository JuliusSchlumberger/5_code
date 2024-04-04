import pandas as pd
import numpy as np
from Paper3_v1.scripts.utilities.filter_options import PERFORMANCE_METRICS_LIST, SCENARIO_OPTIONS
from Paper3_v1.scripts.process_inputs.calculate_tipping_pint_metrics import calculate_tipping_point_metrics
from Paper3_v1.scripts.utilities.convert_into_tp_files import convert_into_tp_files
from Paper3_v1.scripts.process_inputs.remove_minority_cases import remove_minority_cases
from Paper3_v1.main_central_path_directions import PATHWYAYS_SPECIFIER
from Paper3_v1.scripts.utilities.convert_into_pathway_sequence import convert_into_pathway_sequence


def get_tipping_points(df, mapping_dict, string_output_path, target_roh, interaction=None):

    for scenario in SCENARIO_OPTIONS:

        scenario_str = '&'.join(scenario)
        filtered_df = df[df['cc_scenario'].isin(scenario)]

        new_df = filtered_df.copy()
        new_df = new_df[new_df.Value != '0']
        new_df = new_df[new_df.Value != '0&99']
        # Create a new column with the substring up until the last '&'
        new_df['implementation_across_multi_risk'] = new_df['Value'].str.rsplit('&', n=1).str[0]
        # new_df['implementation_across_multi_risk'] = new_df['Value']
        # new_df['implementation_across_multi_risk'] = np.where(
        #     new_df['Value'].str.endswith('99'),  # Condition: Value ends with '99'
        #     new_df['Value'],  # If True: Keep the whole string
        #     new_df['Value'].str.rsplit('&', n=1).str[0]  # If False: Split and take the first part
        # )
        # print(new_df[new_df.Value.str.startswith('0&10&11&')])
        # print(error)
        # print(new_df[new_df.Value.str.contains('&100')])


        for metric in [PERFORMANCE_METRICS_LIST[1]]:
            metric_df = calculate_tipping_point_metrics(new_df, metric).reset_index()
            metric_df['performance_metric'] = metric
            metric_df['scenario_of_interest'] = scenario_str

            system_parameter = f'pathways_list_{PATHWYAYS_SPECIFIER[target_roh]}'
            subset = metric_df[metric_df.system_parameter == system_parameter]

            subset_sequences = convert_into_pathway_sequence(subset, mapping_dict)
            if interaction == None:
                subset_sequences.to_csv(f'{string_output_path}/all_sequences_{target_roh}_{scenario_str}_{metric}.txt', sep=' ', index=False,
                                        header=False)
                # print(subset_sequences)
            else:
                subset_sequences.to_csv(f'{string_output_path}/all_sequences_{target_roh}_{scenario_str}_{metric}_{interaction}.txt', sep=' ',
                                        index=False,
                                        header=False)


            subset_sequences = convert_into_tp_files(subset, mapping_dict)

            if interaction == None:
                subset_sequences.to_csv(f'{string_output_path}/all_tp_timings_{target_roh}_{scenario_str}_{metric}.txt', sep=' ', index=False, header=False)
            else:
                subset_sequences.to_csv(f'{string_output_path}/all_tp_timings_{target_roh}_{scenario_str}_{metric}_{interaction}.txt',
                                        sep=' ', index=False, header=False)

