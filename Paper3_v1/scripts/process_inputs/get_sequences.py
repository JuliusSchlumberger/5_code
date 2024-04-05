import pandas as pd
from Paper3_v1.scripts.utilities.get_longest_string import get_longest_string
from Paper3_v1.scripts.utilities.convert_into_pathway_sequence import convert_into_pathway_sequence
from Paper3_v1.scripts.process_inputs.get_identifiers import get_identifiers
from Paper3_v1.main_central_path_directions import PATHWYAYS_SPECIFIER


def get_sequences(df):
    mapping_dict = get_identifiers(df)
    return mapping_dict