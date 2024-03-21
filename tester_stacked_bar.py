import plotly.graph_objects as go
import pandas as pd



# Assuming 'df' is your DataFrame
df = pd.DataFrame({
    'pathway_number': [1, 2, 3],
    'a_old': [100, 200, 300],
    'b_old': [150, 250, 350],
    'c_old': [200, 300, 400],
    'a_change': [20, -30, 40],
    'b_change': [-10, 50, -60],
    'c_change': [30, -20, 10]
})

# Sort the DataFrame based on 'pathway_number' for consistent plotting
df = df.sort_values('pathway_number')

# Initialize the figure
fig = go.Figure()

# Function to add traces for old values
def add_old_value_traces(variable):
    fig.add_trace(go.Bar(
        name=f'{variable}_old',
        x=df['pathway_number'],
        y=df[f'{variable}_old'],
        base=0,
        offsetgroup=variable,
    ))

# Function to add traces for change values
def add_change_traces(variable):
    fig.add_trace(go.Bar(
        name=f'{variable}_change',
        x=df['pathway_number'],
        y=df[f'{variable}_change'],
        base=df[f'{variable}_old'],
        offsetgroup=variable,
    ))

# Add traces for a, b, c
for var in ['a', 'b', 'c']:
    add_old_value_traces(var)
    add_change_traces(var)

# Customize layout
fig.update_layout(
    title='Stacked Bar Chart of Old Values and Changes',
    xaxis_title='Pathway Number',
    yaxis_title='Value',
    barmode='relative',  # This stacks the bars on top of each other
)

# Show the figure
fig.show()
