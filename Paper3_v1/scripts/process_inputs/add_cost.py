import pandas as pd
import gzip
from Paper3_v1.scripts.utilities.map_system_parameters import RENAME_INPUTS_DICT
from Paper3_v1.scripts.process_inputs.calculate_maintenance_cost import calculate_maintenance_cost
from Paper3_v1.scripts.process_inputs.calculate_investment_cost import calculate_investment_cost
from Paper3_v1.main_central_path_directions import DIRECTORY_PROCESSED_DATA

invest_cost = pd.read_csv(f'{DIRECTORY_PROCESSED_DATA}/invest_costs.csv', index_col=0).values
maint_cost = pd.read_csv(f'{DIRECTORY_PROCESSED_DATA}/maint_costs.csv', index_col=0).values

def add_costs(inputfile_path):

    with gzip.open(inputfile_path, 'rb') as f:
        df = pd.read_csv(f)

    df.rename(columns=RENAME_INPUTS_DICT, inplace=True)

    # Filter rows where 'system_parameter' starts with 'pathway'
    filtered_df = df[df['system_parameter'].str.startswith('pathway')].copy()
    filtered_df['Value'] = filtered_df['Value'].replace(0, '0')

    # Filter rows where 'system_parameter' starts with sprink (for irrigation maintenance)
    sprink_df = df[df['system_parameter'].str.startswith('sprink')].copy()

    # Add a new column 'cost' with all values set to 0
    filtered_df['cost'] = 0.0

    filtered_df['cost_maint'] = 0.0
    filtered_df['cost_invest'] = 0.0

    # Remove duplicates based on grouping columns + 'Value'
    unique_df = filtered_df.drop_duplicates(
        subset=['system_parameter', 'cc_scenario', 'climvar', 'realization', 'pw_combi', 'stage', 'Value'])

    # Only look at sequences which not only contain 0 and take last measure_number to calculate the investment costs
    unique_df = unique_df[unique_df['Value'].apply(lambda x: len(x) > 1)]
    unique_df['Value_Last'] = unique_df['Value'].apply(lambda x: int(x.split('&')[-1] if x.split('&')[-1] != '' else 0))

    unique_df['cost_invest'] = unique_df['Value_Last'].apply(
        lambda x: invest_cost[x][x])

    filtered_df['cost_invest'] = filtered_df.index.map(unique_df['cost_invest']).fillna(0)

    for index, row in filtered_df.iterrows():
        # Split the 'Value' string into a list of integers
        if row['Value'] == 0:
            row['Value'] = '0'
        value_elements = row['Value'].split('&')

        value_elements = [int(elem) for elem in value_elements if elem != '']

        cost_maint = calculate_maintenance_cost(value_elements, maint_cost, row, sprink_df)

        # Add this sum to the 'cost' column of the row
        filtered_df.loc[index, 'cost_maint'] = float(cost_maint)

    # Rename 'system_parameter' elements
    filtered_df['system_parameter'] = filtered_df['system_parameter'].str.replace('pathways_list', 'cost')

    # Replace 'Value' column with values from 'cost' column
    filtered_df['Value'] = filtered_df['cost_maint'] + filtered_df['cost_invest']

    # Drop the 'cost' column
    filtered_df.drop(['cost', 'cost_maint', 'cost_invest'], axis=1, inplace=True)

    # Combine filtered_df with the original df
    combined_df = pd.concat([df, filtered_df], ignore_index=True)


    # Remove unnecessary system_parameters
    combined_df = combined_df[~combined_df['system_parameter'].str.endswith('decision_value')]
    combined_df = combined_df[~combined_df['system_parameter'].str.startswith('sprink')]

    return combined_df.round(2)




def add_costs_old(inputfile_path):

    with gzip.open(inputfile_path, 'rb') as f:
        df = pd.read_csv(f)

    df.rename(columns=RENAME_INPUTS_DICT, inplace=True)

    # Filter rows where 'system_parameter' starts with 'pathway'
    filtered_df = df[df['system_parameter'].str.startswith('pathway')].copy()
    print(filtered_df.Value.unique())

    # Filter rows where 'system_parameter' starts with sprink (for irrigation maintenance)
    sprink_df = df[df['system_parameter'].str.startswith('sprink')].copy()

    # Add a new column 'cost' with all values set to 0
    filtered_df['cost'] = 0.0

    implemented_measures = []

    for index, row in filtered_df.iterrows():
        # Split the 'Value' string into a list of integers
        if row['Value'] == 0:
            row['Value'] = '0'
        value_elements = row['Value'].split('&')
        # print(index, value_elements)
        # print(row)
        value_elements = [int(elem) for elem in value_elements if elem != '']

        # Initialize cost_sum
        cost_maint = calculate_maintenance_cost(value_elements, maint_cost, row, sprink_df)
        cost_invest, implemented_measures = calculate_investment_cost(value_elements, invest_cost, implemented_measures)

        print(index, value_elements, float(cost_maint + cost_invest))
        # Add this sum to the 'cost' column of the row
        filtered_df.loc[index, 'cost'] = float(cost_maint + cost_invest)

    # Rename 'system_parameter' elements
    filtered_df['system_parameter'] = filtered_df['system_parameter'].str.replace('pathways_list', 'cost')

    # Replace 'Value' column with values from 'cost' column
    filtered_df['Value'] = filtered_df['cost']

    # Drop the 'cost' column
    filtered_df.drop('cost', axis=1, inplace=True)

    # Combine filtered_df with the original df
    combined_df = pd.concat([df, filtered_df], ignore_index=True)


    # Remove unnecessary system_parameters
    combined_df = combined_df[~combined_df['system_parameter'].str.endswith('decision_value')]
    combined_df = combined_df[~combined_df['system_parameter'].str.startswith('sprink')]

    return combined_df.round(2)
