
def calculate_maintenance_cost(value_elements, maint_cost, row, sprink_df):
    cost_sum = 0
    # value_elements = row['Value'].split('&')
    # Iterate over each element in value_elements
    for elem in value_elements:
        # Add the corresponding elements from the maint_cost matrix
        cost_sum += maint_cost[elem][elem]

        # Additional conditions for elem being 3 or 4
        if elem == 3 or elem == 4:
            # Define the system_parameter based on the value of elem
            system_param = 'sprink_riv' if elem == 3 else 'sprink_gw'

            # Extract the unique combination of columns
            combination = (
                row['year'], row['climvar'], row['cc_scenario'], row['pw_combi'], row['realization'], row['stage'])

            # Find the respective value in sprink_df
            sprink_value = sprink_df[(sprink_df['year'] == combination[0]) &
                                     (sprink_df['climvar'] == combination[1]) &
                                     (sprink_df['cc_scenario'] == combination[2]) &
                                     (sprink_df['pw_combi'] == combination[3]) &
                                     (sprink_df['realization'] == combination[4]) &
                                     (sprink_df['stage'] == combination[5]) &
                                     (sprink_df['system_parameter'] == system_param)]['Value'].values[0]
            # print(sprink_value)

            # Perform the calculation and add to cost_sum
            cost_sum += (float(sprink_value) * 1.03 / 10) / 1000000 # convert from EUR to MEUR
    return cost_sum