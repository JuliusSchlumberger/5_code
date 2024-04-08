import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import plotly.graph_objects as go
import plotly.express as px
import base64
from Paper3_v1.scripts.utilities.map_system_parameters import MEASURE_DICT, MEASURE_EXPL

# Permanently changes the pandas settings
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Function to get and display the image
def getImage(path, zoom=0.025):
    return OffsetImage(plt.imread(path), zoom=zoom)

def image_to_base64(path):
    with open(path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')



def decision_tree(input_file, sector, button_path):
    # Convert sequences to DataFrame
    df = pd.read_csv(input_file, names=['Measure 1', 'Measure 2', 'Measure 3', 'Measure 4'], skiprows=1)

    # Function to assign group numbers based on unique combinations
    def assign_group_numbers(df, depth):
        """Assigns group numbers based on unique combinations of measures up to a specified depth."""
        combo_col_name = f'Group up to Measure {depth}'
        # Combine measures up to the specified depth to create a unique identifier for each combination
        df[combo_col_name] = df.iloc[:, :depth].apply(lambda row: '_'.join(row), axis=1)
        # Assign group numbers based on these unique combinations
        unique_combos = {combo: idx for idx, combo in enumerate(df[combo_col_name].unique(), 1)}
        df[combo_col_name] = df[combo_col_name].map(unique_combos)

        # Sort the DataFrame by the group columns in ascending order, prioritizing 'Group up to Measure 1'
        df = df.sort_values(
            by=[f'Group up to Measure {d}' for d in range(1,depth+1)])

        return df

    # Assign group numbers for each depth
    for depth in range(1, 5):
        df = assign_group_numbers(df, depth)


    df_sorted = df.copy()
    # Initialize the Position_measure_4 column with the values from 'Group up to Measure 4'
    df_sorted['Position_measure_4'] = df_sorted['Group up to Measure 4']

    # Function to calculate position measures based on the logic described
    def calculate_position_measure(df, current_measure, reference_measure):
        # Calculate the unique counts for the reference measure to determine uniqueness
        unique_counts = df.groupby(reference_measure)[reference_measure].transform('count')
        # If unique (count == 1), keep the current position measure value
        # Otherwise, calculate the average of the current position measure for rows with the same reference measure value
        df[f'Position_measure_{current_measure}'] = df.groupby(reference_measure)[f'Position_measure_{current_measure+1}'].transform(lambda x: (x.min() + x.max()) / 2) \
            .where(unique_counts > 1, df[f'Position_measure_{current_measure+1}'])
        return df

    # Calculate Position_measure_3
    df_sorted = calculate_position_measure(df_sorted, 3, 'Group up to Measure 3')

    # Calculate Position_measure_2
    df_sorted = calculate_position_measure(df_sorted, 2, 'Group up to Measure 2')

    # Calculate Position_measure_1 similarly, but since it's the first measure, it refers to itself for uniqueness
    df_sorted = calculate_position_measure(df_sorted, 1, 'Group up to Measure 1')

    df_sorted['Position_measure_0'] = (df_sorted['Position_measure_1'].min() + df_sorted['Position_measure_1'].max()) / 2
    df_sorted[f'Group up to Measure 0'] = 1

    # df_sorted[['Group up to Measure 1', 'Group up to Measure 2', 'Group up to Measure 3', 'Group up to Measure 4',
    #            'Position_measure_1', 'Position_measure_2', 'Position_measure_3', 'Position_measure_4']]

    # Preparing data for the scatter plot
    x_positions = []
    y_positions = []
    image_paths = []
    measure_names = []
    measure_expl = []

    # Iterating over the Position_measure columns to collect x and y positions for the scatter plot
    for i in range(5):
        column_name = f'Position_measure_{i}'
        x_positions.extend([i] * len(df_sorted))  # X position based on the measure number
        y_positions.extend(df_sorted[column_name])  # Y position from the column values
        if i == 0:
            image_paths.extend([f'{button_path}/no_measure.png' for _ in df_sorted.index])
            measure_names.extend([f'Starting Point/No Measure' for _ in df_sorted.index])
            measure_expl.extend([f'' for _ in df_sorted.index])
        else:
            column_name = f'Measure {i}'
            image_paths.extend(f'{button_path}/{x}.png' for x in df_sorted[column_name])
            measure_names.extend([MEASURE_DICT[x] for x in df_sorted[column_name]])
            measure_expl.extend([MEASURE_EXPL[x] for x in df_sorted[column_name]])

    # Creating a DataFrame with the correct structure
    df_test = pd.DataFrame({
        'X_Positions': x_positions,
        'Y_Positions': y_positions,
        'Image_Paths': image_paths,
        'Measure_Names': measure_names,
        'Measure_Explanation': measure_expl
    })
    df_test = df_test.drop_duplicates()
    fig = go.Figure()
    # Creating the scatter plot with Plotly
    fig.add_trace(go.Scatter(x=df_test['X_Positions'], y=df_test['Y_Positions'],
                     text=df_test['Measure_Names'],
                     mode='markers',  # Only markers, no lines
                     # This can be useful if you want simple hover text, but we'll use hovertemplate instead
                     hovertemplate=
                     "<b>Measure Name: %{text}</b><br>" +
                     "<b>Explanation:</b><br>%{customdata}<br>" +
                     "<extra></extra>",  # Use <extra></extra> to hide the trace name in the hover
                     customdata=df_test['Measure_Explanation'],  # Using custom data for the explanation
                  ))

    # Adding vertical lines based on the logic described
    for i in range(4):  # Only up to measure 3 since we look ahead by one
        current_column = f'Group up to Measure {i}'
        next_column = f'Group up to Measure {i + 1}'
        unique_groups = df_sorted[current_column].unique()

        for group in unique_groups:
            group_rows = df_sorted[df_sorted[current_column] == group]
            next_measure_groups = group_rows[next_column].unique()

            if len(next_measure_groups) > 1:
                min_pos = group_rows[f'Position_measure_{i + 1}'].min()
                max_pos = group_rows[f'Position_measure_{i + 1}'].max()
                fig.add_shape(type='line',
                              x0=i + 0.5, y0=min_pos,
                              x1=i + 0.5, y1=max_pos,
                              line=dict(color='green', width=2)
                              )

    # Adding horizontal lines for both identical and different y-values between measures
    drawn_lines = set()  # Initialize a set to keep track of drawn lines
    only_necessary = df_sorted.drop_duplicates(subset=[f'Position_measure_{k}' for k in range(4)])
    print(only_necessary)
    for index, row in only_necessary.iterrows():
        for i in range(4):  # Up to measure 3 to look ahead to measure 4
            current_pos = row[f'Position_measure_{i}']
            next_pos = row[f'Position_measure_{i + 1}']

            line_part0 = (i, current_pos, i+1, current_pos)
            # Define line coordinates for horizontal line part 1
            line_part1 = (i, current_pos, i + 0.5, current_pos)
            # Define line coordinates for horizontal line part 2
            line_part2 = (i + 0.5, next_pos, i + 1, next_pos)

            if current_pos == next_pos:
                if line_part0 not in drawn_lines:
                    fig.add_shape(type='line', x0=line_part0[0], y0=line_part0[1], x1=line_part0[2], y1=line_part0[3],
                                  line=dict(color='green', width=2), layer='below')
                    drawn_lines.add(line_part0)  # Mark this line as drawn
            # Draw the first part of the horizontal line if it hasn't been drawn
            else:
                if line_part1 not in drawn_lines:
                    fig.add_shape(type='line', x0=line_part1[0], y0=line_part1[1], x1=line_part1[2], y1=line_part1[3],
                                  line=dict(color='green', width=2), layer='below')
                    drawn_lines.add(line_part1)  # Mark this line as drawn

                # Draw the second part of the horizontal line if it hasn't been drawn
                if line_part2 not in drawn_lines:
                    fig.add_shape(type='line', x0=line_part2[0], y0=line_part2[1], x1=line_part2[2], y1=line_part2[3],
                                  line=dict(color='green', width=2), layer='below')
                    drawn_lines.add(line_part2)  # Mark this line as drawn
    for i, row in df_test.iterrows():
        fig.add_layout_image(
            source=row['Image_Paths'],
            # URL or path to your image
            xref="x",  # Use "paper" for positioning relative to the plot area
            yref="y",  # Use "paper" for positioning relative to the plot area
            x=row['X_Positions'],  # X-coordinate position
            y=row['Y_Positions'],  # Y-coordinate position
            sizex=.9,  # Adjust size as needed
            sizey=.9,  # Adjust size as needed
            xanchor="center",
            yanchor="middle",
            layer="above"  # Place the image below or above the data
        )

    #

    # Adjust layout for the y-axis on the right
    fig.update_layout(
        yaxis=dict(side='right', showgrid=False),
        xaxis=dict(
        tickmode = 'linear',
        tick0 = 0,
        dtick = 1,
        showgrid=False),
        title='Alternative Pathways and their Measure Sequences',
        xaxis_title="Measure Number",
        yaxis_title="Alternative Pathways"
    )

    # Optionally, adjust layout further for aesthetics
    fig.update_layout(
        showlegend=False,
        plot_bgcolor="white",
        font=dict(
            # family="Courier New, monospace",
            size=12,
            # color="RebeccaPurple"
        )
    )

    # fig.show()
    fig.write_html(f"Paper3_v1/figures/decision_tree/stage3_portfolios_{sector}.html")

sectors = ['flood_agr', 'drought_agr', 'flood_urb', 'drought_shp']
input_file = 'Paper3_v1/data/stage3_portfolios_'
# button_path = 'Paper3_v1/data/logos/colorized'
button_path = 'https://raw.githubusercontent.com/JuliusSchlumberger/5_code/master/Paper3_v1/data/logos/colorized'
for sector in sectors:
    decision_tree(f'{input_file}{sector}.txt',sector, button_path)