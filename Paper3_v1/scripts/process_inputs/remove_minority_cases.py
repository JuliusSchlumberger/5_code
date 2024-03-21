import pandas as pd
import re

def remove_minority_cases(df):
    full_ends = []

    df_without_ends = df[~df.Value.str.endswith('end')]

    for system_parameter in df.system_parameter.unique():
        subset = df[df.system_parameter == system_parameter]

        all_with_ends = subset[subset.Value.str.endswith('end')]

        for one_with_end in all_with_ends.Value.unique():
            # Remove '&end' only if it is at the end of the string
            start_with_pattern = re.sub('end$', '', one_with_end)

            # Calculate the percentage
            percentage = len(subset[subset.Value == one_with_end]) / len(subset[subset.Value.str.startswith(start_with_pattern)])

            # Decide to keep or remove rows based on the condition
            if percentage > 0.5:
                # If more than 50% end with '&end', keep these rows and remove others
                full_ends.append(all_with_ends[all_with_ends.Value == one_with_end])
            else:
                # all_with_ends = all_with_ends[all_with_ends.Value != one_with_end]
                pass

    if full_ends != []:
        df_without_minority_cases = pd.concat([df_without_ends,pd.concat(full_ends, ignore_index=True)], ignore_index=True)
    else:
        df_without_minority_cases = df_without_ends
    return df_without_minority_cases
