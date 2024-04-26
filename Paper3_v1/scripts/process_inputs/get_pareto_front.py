

def get_pareto_front(performance_df):
    process_df = performance_df.copy()

    # Pivoting the table
    wide_df = process_df.pivot(index='Value', columns='Objective', values='Value').reset_index()
