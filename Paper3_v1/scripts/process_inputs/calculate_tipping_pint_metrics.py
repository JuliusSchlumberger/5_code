import pandas as pd


def calculate_tipping_point_metrics(df, metric):
    # Perform the groupby and calculate quantiles for 'year' while taking the first 'Value' from each group
    if metric in ['5%', '50%', '95%', 'average']:
        # Convert 'metric' to its decimal quantile equivalent if it's not 'average'
        quantile = 0.50 if metric == 'average' else float(metric.strip('%')) / 100

        # Group by the specified columns and aggregate
        agg_dict = {
            'year': lambda x: x.quantile(quantile),
            'Value': 'first'  # Adjust this aggregation as needed
        }
        result_df = df.groupby(['implementation_across_multi_risk', 'system_parameter']).agg(agg_dict)

        # Renaming year column to reflect the metric calculation
        # result_df = result_df.rename(columns={'year': f'year_{metric}'})

        return result_df
    else:
        raise ValueError("Unsupported metric specified")




def calculate_tipping_point_metrics_oldv2(df, metric):
    if metric == '5%':
        return df.groupby(['implementation_across_multi_risk', 'system_parameter'])['year'].quantile(0.05)
    elif metric == '50%':
        return df.groupby(['implementation_across_multi_risk', 'system_parameter'])['year'].quantile(0.50)
    elif metric == '95%':
        return df.groupby(['implementation_across_multi_risk', 'system_parameter'])['year'].quantile(0.95)
    elif metric == 'average':
        return df.groupby(['implementation_across_multi_risk', 'system_parameter'])['year'].quantile(0.50)


def calculate_tipping_point_metrics_old(df, metric):
    if metric == '5%':
        return df.groupby(['Value','implementation_across_multi_risk', 'system_parameter'])['year'].quantile(0.05)
    elif metric == '50%':
        return df.groupby(['Value','implementation_across_multi_risk', 'system_parameter'])['year'].quantile(0.50)
    elif metric == '95%':
        return df.groupby(['Value','implementation_across_multi_risk', 'system_parameter'])['year'].quantile(0.95)
    elif metric == 'average':
        return df.groupby(['Value','implementation_across_multi_risk', 'system_parameter'])['year'].quantile(0.50)
