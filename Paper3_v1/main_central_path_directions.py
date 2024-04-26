from Paper3_v1.scripts.utilities.map_system_parameters import MEASURE_NUMBERS
import pandas as pd


DIRECTORY_MODEL_OUTPUTS = 'model_outputs/005000/stage_3/multihaz_multisec'
LIST_ALL_MODEL_OUTPUTS =  'model_outputs/005000/all_files_multihaz_multisec.txt'

FILE_PATH_BENCHMARK_IN = 'model_outputs/005000/stage_3/multihaz_multisec/portfolio_00_00_00_00.csv.gz'
FILE_PATH_BENCHMARK_OUT = 'Paper3_v1/data/processed/benchmark_performance.csv'
FILE_PATH_ALL_PERFORMANCE = 'Paper3_v1/data/all_pathways_performance.csv'
FILE_PATH_ALL_PATHWAYS_CHANGES = 'Paper3_v1/data/all_pathways_unique_changes.csv'
FILE_PATH_ALL_REMOVED_MEASURES = 'Paper3_v1/data/all_pathways_removed_measures.csv'
FILE_PATH_ALL_PATHWAYS_SECTORS = 'Paper3_v1/data/stage3_portfolios_'
PATHWAYS_GENERATOR_FIGURES = 'Paper3_v1/figures/Pathways_Generator'
LEGENDS_LOCATION = 'Paper3_v1/legends'
LEGENDS_LOCATION_GITHUB = 'https://raw.githubusercontent.com/JuliusSchlumberger/5_code/master/Paper3_v1/legends/colorized'


DIRECTORY_MEASURE_LOGOS_GITHUB = 'https://raw.githubusercontent.com/JuliusSchlumberger/WaasMR/master/viz'
DIRECTORY_MEASURE_LOGOS = 'data/logos/'

DIRECTORY_SYSTEM_PARAMETERS = 'Paper3_v1/data/system_parameters'
DIRECTORY_TIMEHORIZON_PATHWAYS = 'Paper3_v1/data/pathways_timehorizon'
DIRECTORY_TIMEHORIZON_PER_ROH = f'{DIRECTORY_TIMEHORIZON_PATHWAYS}/risk_owner_hazard'
DIRECTORY_OBJECTIVES_FOR_COUNT = f'{DIRECTORY_TIMEHORIZON_PATHWAYS}/counts'
DIRECTORY_PATH_PERFORMANCE = 'Paper3_v1/data/pathways_performance'
DIRECTORY_PATH_FILTERED = 'Paper3_v1/data/filtered_pathways'
DIRECTORY_INTERACTIONS = f'{DIRECTORY_PATH_PERFORMANCE}/interactions'

DIRECTORY_PATH_PATHWAY_SETS = 'Paper3_v1/data/pathway_sets'
DIRECTORY_PATHWAYS_GENERATOR = 'Paper3_v1/data/pathways_generator'

DIRECTORY_PROCESSED_DATA = 'Paper3_v1/data'
DIRECTORY_AGGREGATED_PERFORMANCE = 'Paper3_v1/data/aggregated_pathways_performance'
DIRECTORY_AGGREGATED_TIMEHORIZONS = 'Paper3_v1/data/aggregated_pathways_timehorizons'
DIRECTORY_AGGREGATED_PLOT_PERFORMANCE = 'Paper3_v1/data/aggregated_pathways_performance_plot_performance'
DIRECTORY_AGGREGATED_PLOT_TIMEHORIZONS = 'Paper3_v1/data/aggregated_pathways_timehorizons'


ROH_LIST = ['flood_agr', 'drought_agr', 'flood_urb', 'drought_shp']
LIST_COLUMNS = ['climvar', 'pw_combi','objective_parameter','Value','year','scenario_of_interest']
COLUMN_TYPES = {column_name: 'float32' if column_name in ['Value', 'year'] else 'category' for column_name in LIST_COLUMNS}
MEASURE_LOGOS = {measure: f'{DIRECTORY_MEASURE_LOGOS}/{measure}.png' for measure in MEASURE_NUMBERS.keys()}
MEASURE_LOGOS_GITHUB = {measure: f'{DIRECTORY_MEASURE_LOGOS_GITHUB}/logos/{measure}.png' for measure in MEASURE_NUMBERS.keys()}

PATHWYAYS_SPECIFIER = {'flood_agr': 'f_a',
                       'drought_agr': 'd_a',
                       'flood_urb': 'f_u',
                       'drought_shp': 'd_s'}

ALL_PATHWAYS = {'flood_agr': pd.read_csv(f'{FILE_PATH_ALL_PATHWAYS_SECTORS}flood_agr.txt',
                                          names=['1', '2', '3', '4'], dtype='str'),
                'drought_agr': pd.read_csv(f'{FILE_PATH_ALL_PATHWAYS_SECTORS}drought_agr.txt',
                                         names=['1', '2', '3', '4'], dtype='str'),
                'flood_urb': pd.read_csv(f'{FILE_PATH_ALL_PATHWAYS_SECTORS}flood_urb.txt',
                                                         names=['1', '2', '3', '4'], dtype='str'),
                'drought_shp': pd.read_csv(f'{FILE_PATH_ALL_PATHWAYS_SECTORS}drought_shp.txt',
                                                         names=['1', '2', '3', '4'], dtype='str'),
                }


FILTER_CONDITIONS = {
    ROH_LIST[0]: [0, 1, 3, 5, 7, 9, 11, 13],
    ROH_LIST[1]: [0, 1, 3, 5, 6, 7, 8, 9],
    ROH_LIST[2]: [0, 1, 3, 5, 7, 9, 11, 13],
    ROH_LIST[3]: [0, 1, 2, 4, 5, 8, 9 ],
}



