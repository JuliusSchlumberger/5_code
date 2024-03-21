import pandas as pd
from Paper3_v1.scripts.utilities.map_system_parameters import OBJECTIVE_PARAMETER_DICT


def get_objective_values(system_parameter_file):
    '''
    With this function we ensure that all objectives should be minimized. Experienced damages, crop loss, costs.
    :param system_parameter_file:
    :param objective_file:
    :return:
    '''
    df = pd.read_csv(system_parameter_file)
    # df = df.drop(['Unnamed: 0.1', 'Unnamed: 0'], axis=1)

    # Change from remaining crop revenue to crop loss
    df.loc[df.system_parameter == 'revenue_agr', 'Value'] = 9.7 - df['Value']

    objective_df = df[df.system_parameter.isin(OBJECTIVE_PARAMETER_DICT.keys())].copy()

    # Iterate through each row and replace values based on the dictionary
    for index, row in objective_df.iterrows():
        objective_df.loc[index] = row.replace(OBJECTIVE_PARAMETER_DICT)

    objective_df.rename(columns={'system_parameter': 'objective_parameter'}, inplace=True)

    return objective_df

def get_objective_values_old(system_parameter_file, benchmark_file, objective_file):
    '''
    Old Version. We derived crop loss reduction and damage reduction as objective indicators.
    :param system_parameter_file:
    :param benchmark_file:
    :param objective_file:
    :return:
    '''
    benchmark_df = pd.read_csv(benchmark_file)
    benchmark_df = benchmark_df.drop(['Unnamed: 0.1', 'Unnamed: 0'], axis=1)
    df = pd.read_csv(system_parameter_file)
    df = df.drop(['Unnamed: 0.1', 'Unnamed: 0'], axis=1)

    print(df.nunique())
    print(benchmark_df.nunique())
    # print(error)

    # Merge the two DataFrames on the specified columns
    merged_df = pd.merge(benchmark_df, df, on=['system_parameter', 'cc_scenario', 'climvar', 'year', 'realization'],
                         suffixes=('_benchmark', '_normal'))

    # Calculate the difference in 'Value' between benchmark and normal
    merged_df['Value_difference'] = merged_df['Value_benchmark'] - merged_df['Value_normal']
    test = merged_df[merged_df.system_parameter == 'DamAgr_f_tot']


    merged_df.rename(columns={'pw_combi_normal': 'pw_combi'}, inplace=True)

    # Group by the specified columns and aggregate the differences
    objective_df = merged_df.groupby(['system_parameter', 'pw_combi', 'cc_scenario', 'climvar', 'year'])[
        'Value_difference'].sum().reset_index()

    objective_df = objective_df[objective_df.system_parameter.isin(OBJECTIVE_PARAMETER_DICT.keys())]

    # Iterate through each row and replace values based on the dictionary
    for index, row in objective_df.iterrows():
        objective_df.loc[index] = row.replace(OBJECTIVE_PARAMETER_DICT)

    objective_df.rename(columns={'system_parameter': 'objective_parameter'}, inplace=True)

    objective_df.to_csv(objective_file)
