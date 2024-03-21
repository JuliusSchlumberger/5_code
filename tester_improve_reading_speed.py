import pandas as pd
import time

# Path to your CSV file
csv_file = 'Paper3_v1/data/pathways_timehorizon/counts/objectives_for_count_combinations_drought_shp_flood_agr_flood_urb.csv'

# Read the CSV file into a DataFrame
# df = pd.read_csv(csv_file)

# Path for the HDF5 file you want to create
hdf5_file = 'Paper3_v1/data/pathways_timehorizon/counts/objectives_for_count_combinations_drought_shp_flood_agr_flood_urb.h5'

# Save the DataFrame to HDF5
# df.to_hdf(hdf5_file, key='my_dataset', mode='w', format='table', data_columns=True)

list_columns = ['climvar', 'pw_combi','objective_parameter','Value','year','scenario_of_interest']
column_types = {column_name: 'float32' if column_name in ['Value', 'year'] else 'category' for column_name in list_columns}

# Example user-provided values
flood_agr_values = ['01', '03', '05']
drought_shp_values = ['03', '06', '02']
flood_urb_values = ['05', '06', '07']

flood_agr_values = [3,4,5]
drought_shp_values = [9,8,7]
flood_urb_values = [10,11,12]


# Dynamically building the query string
flood_urb_query = " | ".join([f"flood_urb == {val}" for val in flood_urb_values])
flood_agr_query = " | ".join([f"flood_agr == {val}" for val in flood_agr_values])
drought_shp_query = " | ".join([f"flood_urb == {val}" for val in drought_shp_values])
# Assuming your full query involves multiple conditions, combine them similarly
# Here's how you might construct a complete query with multiple conditions
complete_query = flood_urb_query + '&' +  flood_agr_query + '&' + drought_shp_query  # In practice, you'd combine multiple conditions with ' & '


# Constructing a query string
query = (
    f"flood_agr in {flood_agr_values} & "
    f"drought_shp in {drought_shp_values} & "
    f"flood_urb in {flood_urb_values}"
)

query = (
    # f"flood_agr in {flood_agr_values} & "
    # f"drought_shp in {drought_shp_values} & "
    f"flood_urb in {flood_urb_values}"
)
#
# test = pd.read_hdf(hdf5_file, 'my_dataset')
# print(test[test.flood_agr.isin(flood_agr_values)],
#       # test.drought_shp.unique(),
#       # test.flood_urb.unique()
#       )
# print(test.dtypes)

# Number of iterations to measure read speed
n_iterations = 5

# Measure CSV read times
csv_read_times = []
# for _ in range(n_iterations):
#     start_time = time.time()
#     pd.read_csv(csv_file, dtype=column_types)
#     csv_read_times.append(time.time() - start_time)

# Measure HDF5 read times
hdf5_read_times = []
for _ in range(n_iterations):
    start_time = time.time()
    # Now, use this complete_query in pd.read_hdf
    df = pd.read_hdf(hdf5_file, 'my_dataset', where=complete_query)
    # df_filtered = df[(df.flood_agr.isin(flood_agr_values)) &
    #                  (df.flood_urb.isin(flood_urb_values)) &
    #                  (df.drought_shp.isin(drought_shp_values))].copy()

    # pd.read_hdf(hdf5_file, 'my_dataset', where=complete_query)
    hdf5_read_times.append(time.time() - start_time)

# Calculate average read times
avg_csv_read_time = sum(csv_read_times) / n_iterations
avg_hdf5_read_time = sum(hdf5_read_times) / n_iterations

print(f"Average CSV read time: {avg_csv_read_time} seconds")
print(f"Average HDF5 read time: {avg_hdf5_read_time} seconds")