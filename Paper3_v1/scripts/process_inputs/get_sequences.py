import pandas as pd
from Paper3_v1.scripts.utilities.get_longest_string import get_longest_string
from Paper3_v1.scripts.utilities.convert_into_pathway_sequence import convert_into_pathway_sequence
from Paper3_v1.scripts.process_inputs.get_identifiers import get_identifiers
from Paper3_v1.main_central_path_directions import PATHWYAYS_SPECIFIER


def get_sequences(df, string_output_path, target_roh, interaction=None):

    mapping_dict = get_identifiers(df)

    # system_parameter = f'pathways_list_{PATHWYAYS_SPECIFIER[target_roh]}'
    #
    # subset = df[df.system_parameter == system_parameter].copy()



    return mapping_dict