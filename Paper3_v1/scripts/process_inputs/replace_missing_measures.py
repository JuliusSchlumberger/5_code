import pandas as pd




def replace_missing_measures(df):
    # Prepare to collect indices for removal and modification
    to_remove_indices = []

    # Grouping by the specified columns
    groups = df.groupby(['pw_combi', 'cc_scenario', 'climvar', 'system_parameter'])

    for name, group in groups:
        # Identify rows that meet the condition
        condition_mask = group['Value'].str.contains('&&') | group['Value'].str.endswith('&')
        valid_rows = group[condition_mask]

        if not valid_rows.empty:
            # Find the row with the minimum Year
            min_year_idx = valid_rows['year'].idxmin()
            to_remove_indices.append(min_year_idx)

            for idx, row in valid_rows.iterrows():
                if row['system_parameter'] == 'pathways_list_d_a':
                    replaced_measure = '1'
                elif row['system_parameter'] == 'pathways_list_f_a':
                    replaced_measure = '10'

                if '&&' in row['Value']:
                    df.at[idx, 'Value'] = row['Value'].replace('&&', f'&{replaced_measure}&')
                if row['Value'].endswith('&'):
                    df.at[idx, 'Value'] = f"{row['Value'].rstrip('&')}&{replaced_measure}"

    # Remove rows
    removed_rows = df.loc[to_remove_indices]
    df = df.drop(to_remove_indices)

    return df, removed_rows


def replace_missing_measures_old_v3(df):

    # Step 1: Find special rows meeting conditions and having the lowest 'Year' for each unique combination
    special_rows = df[df['Value'].str.contains('&&') | df['Value'].str.endswith('&')]
    grouped = special_rows.groupby(['pw_combi', 'cc_scenario', 'climvar', 'system_parameter'])
    min_year_rows = grouped.apply(lambda x: x[x['year'] == x['year'].min()])

    # Step 2 & 3: Modify the 'Value' column
    replacement_strings_dict = {}

    # Iterate over each row of the DataFrame using iterrows()
    for index, row in df.iterrows():
        key_in_dict = False
        # Check the condition on 'system_parameter' and apply the corresponding replacement
        if row['system_parameter'] == 'pathways_list_d_a':
            replaced_measure = '1'
        elif row['system_parameter'] == 'pathways_list_f_a':
            replaced_measure = '10'

        if row['system_parameter'] in ['pathways_list_d_a','pathways_list_f_a']:

            # Check if the current key is a substring of row['Value']
            for key in replacement_strings_dict.keys():
                # print('key in dict', index, key)
                key_in_dict = False

                # Check if part of string has been stored
                if key in row['Value']:
                    # Replace occurrences of the key with its corresponding value in row['Value']
                    # print('&&', row['Value'], row['Value'].replace(key, replacement_strings_dict[key]))
                    row['Value'] = row['Value'].replace(key, replacement_strings_dict[key])
                    # print(row['Value'])
                    key_in_dict = True
                    break  # A match was found, no need to keep looking

            # If no part of the string was previously stored, add it to the dict and drop row which is not relevant for plotting pathways
            if not key_in_dict:
                original_value = row['Value']
                if '&&' in row['Value']:
                    # Modify row['Value'] as needed before adding to dict
                    modified_value = row['Value'].replace('&&', f'&{replaced_measure}&')
                elif row['Value'].endswith('&') and '&&' not in row['Value']: # if measure last measure is removed
                    modified_value = row['Value'] + replaced_measure
                else:
                    break
                replacement_strings_dict[original_value] = modified_value
                row['Value'] = '999999999'

            # Update the DataFrame with the modified value
            df.at[index, 'Value'] = row['Value']
        else:
            pass

    df = df[df.Value != '999999999']

    return df, min_year_rows


def replace_missing_measures_old_v2(df):

    # Step 1: Find special rows meeting conditions and having the lowest 'Year' for each unique combination
    special_rows = df[df['Value'].str.contains('&&') | df['Value'].str.endswith('&')]
    grouped = special_rows.groupby(['pw_combi', 'cc_scenario', 'climvar', 'system_parameter'])
    min_year_rows = grouped.apply(lambda x: x[x['year'] == x['year'].min()])

    # Step 2 & 3: Modify the 'Value' column
    replacement_strings_dict = {}

    # Iterate over each row of the DataFrame using iterrows()
    for index, row in df.iterrows():
        key_in_dict = False
        # Check the condition on 'system_parameter' and apply the corresponding replacement
        if row['system_parameter'] == 'pathways_list_d_a':
            if '&&' in row['Value']:
                # Check if part of string has been stored

                for key in replacement_strings_dict.keys():
                    # print('key in dict', index, key)
                    # Check if the current key is a substring of row['Value']
                    key_in_dict = False
                    if key in row['Value']:
                        # Replace occurrences of the key with its corresponding value in row['Value']
                        # print('&&', row['Value'], row['Value'].replace(key, replacement_strings_dict[key]))
                        row['Value'] = row['Value'].replace(key, replacement_strings_dict[key])
                        # print(row['Value'])
                        key_in_dict = True
                        break  # A match was found, no need to keep looking

                # If no part of the string was previously stored, add it to the dict
                if not key_in_dict:
                    original_value = row['Value']
                    # Modify row['Value'] as needed before adding to dict
                    modified_value = row['Value'].replace('&&', '&1&') + '&100'
                    replacement_strings_dict[original_value] = modified_value
                    # print(modified_value)
                    # Update the row's 'Value' to the modified value
                    row['Value'] = modified_value
            elif row['Value'].endswith('&') and '&&' not in row['Value']: # if measure last measure is removed
                replaced_string = row['Value'] + '&'    # ensure that right string is removed when next measure is implemented
                # print('at end &', row['Value'], row['Value'] + '1&100')
                row['Value'] = row['Value'] + '1&100'
                replacement_strings_dict[replaced_string] = row['Value'] + '&'  # for future rows which add additional measures
                # print(row['Value'])
            else:
                pass
            # Update the DataFrame with the modified value

            df.at[index, 'Value'] = row['Value']

        #     # return row['Value'].replace('&&', '&1&100&') + ('1&100' if row['Value'].endswith('&') else '')
        # elif row['system_parameter'] == 'pathways_list_f_a':
        #     return row['Value'].replace('&&', '&10&100&') + ('10&100' if row['Value'].endswith('&') else '')
        # else:
        #     # Apply the default replacement if none of the specific conditions are met
        #     return row['Value'].replace('&&', '&100&') + ('100' if row['Value'].endswith('&') else '')

    # # Use apply with axis=1 to operate row-wise
    # df['Value'] = df.apply(
    #     lambda row: replace_value(row) if '&&' in row['Value'] or row['Value'].endswith('&') else row[
    #         'Value'], axis=1)
    # if len(list(replacement_strings_dict.keys())) > 0:
    #     print(replacement_strings_dict)
        # print(error)

    return df, min_year_rows

def replace_missing_measures_old_v1(df):

    # Step 1: Find special rows meeting conditions and having the lowest 'Year' for each unique combination
    special_rows = df[df['Value'].str.contains('&&') | df['Value'].str.endswith('&')]
    grouped = special_rows.groupby(['pw_combi', 'cc_scenario', 'climvar', 'system_parameter'])
    min_year_rows = grouped.apply(lambda x: x[x['year'] == x['year'].min()])

    # Step 2: Initialize a DataFrame to collect special rows 'R'
    rows_R = pd.DataFrame()

    for _, row in min_year_rows.iterrows():
        combination = (row['pw_combi'], row['cc_scenario'], row['climvar'], row['system_parameter'])
        string_to_be_replaced = row['Value']

        # Find the row with the next smaller 'Year' for the given combination
        prev_years = df[(df['pw_combi'] == combination[0]) &
                        (df['cc_scenario'] == combination[1]) &
                        (df['climvar'] == combination[2]) &
                        (df['system_parameter'] == combination[3]) &
                        (df['year'] < row['year'])]
        if not prev_years.empty:
            next_smaller_year_row = prev_years.nlargest(1, 'year')
            string_to_be_replaced_with = next_smaller_year_row['Value'].values[0]

            # Remove the year where measure has been removed from dataframe
            df = df.drop(index=next_smaller_year_row.index, inplace=False)

            # Step 3: Replace part of Value strings for the unique combination
            mask = (df['pw_combi'] == combination[0]) & (df['cc_scenario'] == combination[1]) & (
                        df['climvar'] == combination[2]) & (df['system_parameter'] == combination[3])

            df.loc[mask, 'Value'] = df.loc[mask, 'Value'].str.replace(string_to_be_replaced, string_to_be_replaced_with)

            # Step 4: Add row R to the separate DataFrame
            rows_R = pd.concat([rows_R, row.to_frame().T])

    # Reset index of rows_R if needed
    rows_R.reset_index(drop=True, inplace=True)
    return df, rows_R