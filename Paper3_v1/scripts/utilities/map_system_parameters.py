

RENAME_INPUTS_DICT = {
    'output': 'system_parameter',
    'portfolio': 'pw_combi',
    'value': 'Value'
}

SYSTEM_PARAMETERS_LIST = ['DamAgr_f_tot', 'cost_f_a',
 'DamAgr_d_tot', 'cost_d_a', 'revenue_agr',
 'DamUrb_tot', 'cost_f_u',
 'DamShp_tot', 'cost_d_s']

PATHWAYS_TIMING_LIST = ['pathways_list_f_a','pathways_list_d_a', 'pathways_list_f_u','pathways_list_d_s']


OBJECTIVE_PARAMETER_DICT = {'DamAgr_f_tot':'Farmer_Structural_Damage',
                            'cost_f_a':'Farmer_Flood_Measure_Costs',
                            # 'DamAgr_d_tot':'AgrDrought_DamageReduction', # this is just damage, neglects land loss effect
                            'cost_d_a':'Farmer_Drought_Measure_Costs',
                            'revenue_agr':'Crop_Loss',
                            'DamUrb_tot':'Municipality_Structural_Damage',
                            'cost_f_u':'Municipality_Measure_Costs',
                            'DamShp_tot':'Shipping_Economic_Loss',
                            'cost_d_s':'Shipping_Measure_Costs'}

AXIS_LABELS = {}
for key, element in OBJECTIVE_PARAMETER_DICT.items():
    AXIS_LABELS[element] = element + ' [MEUR]'



BENCHMARK_CROP_REVENUE = 9.7

BENCHMARK_GROUPS = {
    'from_baseline': [
        OBJECTIVE_PARAMETER_DICT['DamAgr_f_tot'],
        OBJECTIVE_PARAMETER_DICT['revenue_agr'],
        OBJECTIVE_PARAMETER_DICT['DamUrb_tot'],
        OBJECTIVE_PARAMETER_DICT['DamShp_tot']
    ],
    'from_inputs': [
        OBJECTIVE_PARAMETER_DICT['cost_f_a'],
        OBJECTIVE_PARAMETER_DICT['cost_d_a'],
        OBJECTIVE_PARAMETER_DICT['cost_f_u'],
        OBJECTIVE_PARAMETER_DICT['cost_d_s']
    ]
}

SECTOR_OBJECTIVES = {'flood_agr': [OBJECTIVE_PARAMETER_DICT['DamAgr_f_tot'], OBJECTIVE_PARAMETER_DICT['revenue_agr'], OBJECTIVE_PARAMETER_DICT['cost_f_a'], ],
                             'drought_agr': [OBJECTIVE_PARAMETER_DICT['revenue_agr'], OBJECTIVE_PARAMETER_DICT['cost_d_a']],
                             'flood_urb': [OBJECTIVE_PARAMETER_DICT['DamUrb_tot'], OBJECTIVE_PARAMETER_DICT['cost_f_u']],
                             'drought_shp': [OBJECTIVE_PARAMETER_DICT['DamShp_tot'], OBJECTIVE_PARAMETER_DICT['cost_d_s']]}

MEASURE_NUMBERS = {
            'no_measure': 100,
            'd_resilient_crops': 1,
            'd_rain_irrigation': 2,
            'd_gw_irrigation': 3,
            'd_riv_irrigation': 4,
            'd_soilm_practice': 5,
            'd_multimodal_transport': 6,
            'd_medium_ships': 7,
            'd_small_ships': 8,
            'd_dredging': 9,
            'f_resilient_crops': 10,
            'f_ditches': 11,
            'f_local_support': 12,
            'f_dike_elevation_s': 13,
            'f_dike_elevation_l': 14,
            'f_maintenance': 15,
            'f_room_for_river': 16,
            'f_wet_proofing_houses': 17,
            'f_local_protect': 18,
            'f_awareness_campaign': 19
        }


INVERTED_MEASURE_NUMBERS = {value: key for key, value in MEASURE_NUMBERS.items()}


method_names = [
    "d_resilient_crops", "d_rain_irrigation", "d_gw_irrigation", "d_riv_irrigation",
    "d_soilm_practice", "d_multimodal_transport", "d_medium_ships", "d_small_ships",
    "d_dredging", "f_resilient_crops", "f_ditches", "f_local_support", "f_dike_elevation_s",
    "f_dike_elevation_l", "f_maintenance", "f_room_for_river", "f_wet_proofing_houses",
    "f_local_protect", "f_awareness_campaign", "no_measure"
]

names = [
    "Drought resilient crops", "Rainwater irrigation", "Groundwater irrigation", "River irrigation",
    "Soil moisture practice", "Multi-modal transport subsidies", "Fleet of medium size ships",
    "Fleet of small size ships", "River dredging", "Flood resilient crops", "Ditch system",
    "Local support conservation scheme", "Small dike elevation increase", "Large dike elevation increase",
    "Dike maintenance", "Room for the River", "Flood proof houses", "Local protection", "Awareness campaign", "no_measure"
]

# Create dictionary with method_name as keys and Name as values
MEASURE_DICT = dict(zip(method_names, names))
