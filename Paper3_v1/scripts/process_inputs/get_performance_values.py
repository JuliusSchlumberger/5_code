import pandas as pd
from Paper3_v1.scripts.utilities.filter_options import PERFORMANCE_METRICS_LIST, SCENARIO_OPTIONS
from Paper3_v1.scripts.utilities.calculate_performance_indicators import calculate_performance_metrics


def get_performance_values(timehorizon_df):

    result_dfs = []
    for scenario in SCENARIO_OPTIONS:

        scenario_str = '&'.join(scenario)
        filtered_df = timehorizon_df[timehorizon_df['cc_scenario'].isin(scenario)]

        for metric in PERFORMANCE_METRICS_LIST:
            metric_df = calculate_performance_metrics(filtered_df,['year', 'objective_parameter', 'pw_combi'], metric, 'Value').reset_index()

            metric_df['performance_metric'] = metric
            metric_df['scenario_of_interest'] = scenario_str
            result_dfs.append(metric_df)

    final_df = pd.concat(result_dfs, ignore_index=True)

    return final_df
