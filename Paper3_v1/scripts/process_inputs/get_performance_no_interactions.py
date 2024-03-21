import pandas as pd

def get_performance_no_interactions(df, target_roh,rohs, outputfile_path):
    not_relevant_rohs = rohs.copy()
    not_relevant_rohs.remove(target_roh)

    subset_df = df.copy()

    for roh in not_relevant_rohs:
        subset_df = subset_df[subset_df[roh] == '00']   # get pathway combinations without any other pathways implemetned

    subset_df.to_csv(f'{outputfile_path}/performance_{target_roh}_no_interactions.csv', index=False)
