from Paper3_v1.scripts.utilities.string_analysis_pathway_sequences import process_string

def get_identifiers(df):

    # Dictionary to hold the results
    result_dict = {}
    counter_dict = {}
    # Process each string in the dataframe
    only_pathways_sequences = df[['Value']].drop_duplicates()
    only_pathways_sequences['Value'].apply(lambda s: process_string(s, result_dict, counter_dict))

    return result_dict