import pandas as pd
import re


def convert_into_pathway_sequence_old(subset, mapping_dict):
    output_dict = {
        'from_measure': [],
        'to_measure': []
    }
    from_measure = []
    to_measure = []

    for index, row in subset.iterrows():
        sequence = row['Value']
        measure_integers = re.findall(r'\d+', sequence)
        # print('measure_integers', measure_integers)
        match_old = ''
        num_old = ''
        for match in re.finditer(r'(\d+)', sequence):
            if int(match.group()) == 0 or int(match.group()) == 99: # Starting and end measure
                continue
            else:
                num = int(match.group())
                # Get the index of the start of the number
                index = match.start()
                # Extract the substring before the number
                prefix = sequence[:index]

                if num_old == '':
                    replacement_left = 'current'
                else:
                    # Get prefix from left
                    index_old = match_old.start()
                    prefix_old = sequence[:index_old]
                    replacement_left = mapping_dict[str(num_old)][prefix_old]
                replacement_right = mapping_dict[str(num)][prefix]

                from_measure.append(replacement_left)
                to_measure.append(replacement_right)

                # Update for next one
                num_old = num
                match_old = match

    output_dict['from_measure'] = from_measure
    output_dict['to_measure'] = to_measure

    df_output = pd.DataFrame(output_dict)
    df_output = df_output.drop_duplicates()

    return df_output



def convert_into_pathway_sequence(subset, mapping_dict, roh):
    output_dict = {
        'from_measure': [],
        'to_measure': [],
        'pathway': [],
        'check_sequ': []
    }
    from_measure = []
    to_measure = []

    for index, row in subset.iterrows():
        sequence = row['Value']
        pathway =  str(int(row[roh]))

        parts = sequence.split('&')

        # Step 1: Count the & characters
        ampersand_count = sequence.count('&')
        for no_pathway_change in range(1,ampersand_count):
            left_part = parts[no_pathway_change - 1]  # The part immediately before the nth &
            right_part = parts[no_pathway_change]  # The part immediately after the nth &\
            if right_part == '99':
                pass

            else:
                # identifier left
                identifier_left = '&'.join(str(num) for num in parts[:no_pathway_change - 1]) + '&'
                if identifier_left + right_part in output_dict['check_sequ'] and any(
                        pathway in string for string in output_dict['pathway']):  # same sequence already processed
                    pass
                elif identifier_left + right_part in output_dict['check_sequ'] and not any(pathway in string for string in output_dict[
                    'pathway']):  # sequence processed, but for different pathway
                    index_pathway = output_dict['check_sequ'].index(identifier_left + right_part)
                    output_dict['pathway'][index_pathway] += ';' + pathway
                    pass
                else:
                    if parts[no_pathway_change+1] == '99':
                        identifier_right = '&'.join(str(num) for num in parts[:no_pathway_change]) + '&99'
                    else:
                        identifier_right = '&'.join(str(num) for num in parts[:no_pathway_change]) + '&'

                    if left_part == '0':
                        replacement_left = 'current'
                    else:
                        replacement_left = mapping_dict[left_part][identifier_left]
                    # print(mapping_dict)
                    # print(ampersand_count, sequence, right_part, left_part,parts[no_pathway_change], identifier_left)
                    replacement_right = mapping_dict[right_part][identifier_right]

                    output_dict['from_measure'].append(replacement_left)
                    output_dict['to_measure'].append(replacement_right)
                    output_dict['check_sequ'].append(identifier_left + right_part)
                    output_dict['pathway'].append(pathway)
    # output_dict['from_measure'] = from_measure
    # output_dict['to_measure'] = to_measure

    df_output = pd.DataFrame(output_dict)
    df_output = df_output.drop_duplicates()
    df_output = df_output.drop(columns='check_sequ')

    return df_output


