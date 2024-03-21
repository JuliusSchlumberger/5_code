import pandas as pd
import gzip
from Paper3_v1.scripts.utilities.map_system_parameters import PATHWAYS_TIMING_LIST, RENAME_INPUTS_DICT


def get_pathway_changes(pathways_timing_file):
    with gzip.open(pathways_timing_file, 'rb') as f:
        csv_file = pd.read_csv(f)

    csv_file.rename(columns=RENAME_INPUTS_DICT, inplace=True)
    pathways_timing_df = csv_file[csv_file['system_parameter'].isin(PATHWAYS_TIMING_LIST)]

    pathways_timing_df.loc[:, 'Value'] = pathways_timing_df['Value'].replace(0, '0').copy()

    unique_changes = pathways_timing_df.drop_duplicates(
        subset=['system_parameter', 'climvar', 'cc_scenario', 'Value', 'pw_combi', 'realization'])
    # print(unique_changes[unique_changes['Value'].str.contains('&&')])
    # print(error)

    return unique_changes

def add_end_value(df):
    # Columns to group by, excluding 'Value'
    group_columns = ['system_parameter', 'climvar', 'cc_scenario', 'pw_combi', 'realization']

    # Create an empty DataFrame to hold the new rows
    new_rows = []

    # Step 1 & 2: Group by the specified columns and take the last row of each group
    for _, group in df.groupby(group_columns):
        longest_string = group.loc[group['Value'].str.len().idxmax()].copy()

        if longest_string['Value'] == 0:
            continue
        else:
            # last_row = group.iloc[-1].copy()  # Take the last row
            # print(last_row)

            # Step 3: Modify 'Value' and 'Year' in the copied last row
            longest_string['Value'] = longest_string['Value'] + '&99'
            longest_string['year'] = 140

        # Append the modified row to the new_rows DataFrame
        new_rows.append(longest_string)

    # Convert the list of new rows into a DataFrame
    new_rows_df = pd.DataFrame(new_rows)

    # Step 4: Append the new_rows DataFrame to the original DataFrame
    unique_changes = pd.concat([df, new_rows_df], ignore_index=True)

    return unique_changes
