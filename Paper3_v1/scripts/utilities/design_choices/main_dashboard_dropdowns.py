from Paper3_v1.scripts.utilities.map_system_parameters import SECTOR_OBJECTIVES, OBJECTIVE_PARAMETER_DICT

ROH_DICT = {
    'farmer - flood': 'flood_agr',
    'farmer - drought': 'drought_agr',
    'ship company - drought': 'drought_shp',
    'municipality - flood': 'flood_urb'
}

ROH_DICT_INV = {}
for key, element in ROH_DICT.items():
    ROH_DICT_INV[element] = key

TIMEHORIZONS = {
    'next 20 years': 20,
    'next 60 years': 60,
    'next 100 years': 100
}

SCENARIOS = {
    'current': 'D',
    '1.5 Deg warmer': 'G',
    '4 Deg warmer': 'Wp'
}

CONFIDENCE = {
    'risk averse': '95%',
    'risk neutral': '50%',
    'risk taking': '5%'
}

PATHWAYS_TO_HIGHLIGHT = {
    'flood_agr': range(1,13),
    'drought_agr': range(1,9),
    'drought_shp': range(1,12),
    'flood_urb': range(1,18)
}

WHICH_OPTIONS = {
    'best': 'best',
    'worst': 'worst'
}

WHICH_OPTIONS = {
    'PCP': 'PCP',
    'StackedBar': 'StackedBar',
    'Heatmap': 'Heatmap'
}

PERFORMANCE_METRICS = {
    '5% confidence interval': '5%',
    '50% confidence interval': '50%',
    '95% confidence interval': '95%',
    'expected performance': 'average'
}

# SECTOR_OBJECTIVES_BUTTONS = {}
# for key in SECTOR_OBJECTIVES:
#     SECTOR_OBJECTIVES_BUTTONS[key]= {}
#     for label in SECTOR_OBJECTIVES[key]:
#         SECTOR_OBJECTIVES_BUTTONS[key][label] = key_item for key_item, value in OBJECTIVE_PARAMETER_DICT.items() if label == value

SECTOR_OBJECTIVES_BUTTONS = {
    key: {label: [key_item for key_item, value in OBJECTIVE_PARAMETER_DICT.items() if label == value]
          for label in labels}
    for key, labels in SECTOR_OBJECTIVES.items()
}

RANGE = {
    'AgrFlood_Damage [MEUR]': [0,400],
    'AgrFlood_DRM_cost [MEUR]':[0,400],
    # 'DamAgr_d_tot':'AgrDrought_DamageReduction', # this is just damage, neglects land loss effect
    'AgrDrought_DRM_cost [MEUR]':[0,400],
    'Agr_CropLoss [MEUR]':[0,800],
    'UrbFlood_Damage [MEUR]':[0,1000],
    'UrbFlood_DRM_cost [MEUR]':[0,500],
    'ShpDrought_Damage [MEUR]':[0,2000],
    'ShpDrought_DRM_cost [MEUR]':[0,2000],
    list(ROH_DICT.keys())[0]:[1,14],
    list(ROH_DICT.keys())[1]:[1,14],
    list(ROH_DICT.keys())[2]:[1,14],
    list(ROH_DICT.keys())[3]:[1,14],
}