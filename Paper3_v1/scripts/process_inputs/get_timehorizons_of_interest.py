import pandas as pd

from Paper3_v1.scripts.utilities.filter_options import TIMEHORIZONS_OF_INTEREST


def get_timehorizons(objective_df):
    # Pre-allocate a list to hold the DataFrames for each time horizon
    dfs = []

    for timehorizon in TIMEHORIZONS_OF_INTEREST:
        # Filter the DataFrame without copying it for each time horizon
        filtered_df = objective_df[objective_df.year <= timehorizon]

        # Group by and sum the values as before
        timehorizon_objective_df = (
            filtered_df.groupby(['climvar', 'cc_scenario', 'pw_combi', 'objective_parameter'])['Value']
                .sum().reset_index()
        )

        # Assign the current time horizon to the filtered DataFrame
        timehorizon_objective_df['year'] = timehorizon

        # Append the resulting DataFrame to the list
        dfs.append(timehorizon_objective_df)

    # Concatenate all DataFrames in the list once, outside of the loop
    all_timehorizons = pd.concat(dfs, ignore_index=True)

    return all_timehorizons



def get_timehorizons_old(objective_df):

    all_timehorizons = pd.DataFrame()

    for timehorizon in TIMEHORIZONS_OF_INTEREST:
        df_copy = objective_df.copy()
        df_copy = df_copy[df_copy.year <= timehorizon]
        timehorizon_objective_df = \
        df_copy.groupby(['climvar', 'cc_scenario', 'pw_combi', 'objective_parameter'])[
            'Value'].sum().reset_index()
        timehorizon_objective_df['year'] = timehorizon
        all_timehorizons = pd.concat([all_timehorizons, timehorizon_objective_df], ignore_index=True)

    return all_timehorizons
    # print(all_timehorizons.nunique())