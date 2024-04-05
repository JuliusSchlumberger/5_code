from Paper3_v1.scripts.utilities.design_choices.main_dashboard_dropdowns import ROH_DICT_INV

PANEL_BACKGROUND = '#B3E5FC'
DASHBOARD_BACKGROUND = '#E1F5FE'


DASHBOARD_BACKGROUND = '#B3E5FC'
PANEL_BACKGROUND = '#E1F5FE'

DASHBOARD_DIMENSIONS = {
    'padding':  '1vw',
    'padding_dashboard':  '1vw',
    'left_panel_width': '30vw',
    'right_panel_width': '66vw',
    'margin': '1vh',
    'button_vdistance': '2vh',
    'figure_options': '64vw',
    'figure_legend': '7vw',
    'figure_options_mr': '50vh',
    'options_panel': '650px',
    'performance_panel': '750px',
    'multi_risk_panel': '500px'


}

FIGSIZES = {
    'options_figure': (12,5.5)
}


# Define a custom discrete colorscale
COLORSCALE_HEATMAP = [
    [0.0, '#fa8de0'], [0.2, '#fa8de0'],  # First segment
    [0.2, '#f2a7c2'], [0.4, '#f2a7c2'],  # Second segment
    [0.4, '#f3f3f3'], [0.6, '#f3f3f3'],  # Third segment
    [0.6, '#d7d57f'], [0.8, '#d7d57f'],  # Fourth segment
    [0.8, '#c3ea57'], [1.0, '#c3ea57']  # Fifth and last segment
]

COLORSCALE = [
    '#fa8de0',  # 0.0 to 0.2
    '#f2a7c2',  # 0.2 to 0.4
    '#f3f3f3',  # 0.4 to 0.6
    '#d7d57f',  # 0.6 to 0.8
    '#c3ea57'   # 0.8 to 1.0
]


# COLORSCALE_PCP = [[0, 'grey'],[.5, 'red'],  [1, 'red']]
COLORSCALE_PCP = [[.0, '#c3ea57' ],[.5, 'blue'],[.6, 'blue'],[.8, '#f3f3f3'], [1, '#fa8de0']]
# COLORSCALE_PCP = ['fa8de0', 'f3f3f3', 'f3f3f3', 'c3ea57']

MEASURE_COLORS = {
    list(ROH_DICT_INV.keys())[0]: ['#b3cde3', '#6497b1', '#005b96', '#03396c', '#011f4b', '#011a30'],
    list(ROH_DICT_INV.keys())[1]: ['#ffcc99', '#ffaa66', '#ff8800', '#cc6e00', '#994c00', '#663300'],
    list(ROH_DICT_INV.keys())[2]: ['#b2dfdb', '#80cbc4', '#4db6ac', '#00897b', '#00695c', '#004d40'],
    list(ROH_DICT_INV.keys())[3]: ['#cec3e6', '#9d94cc', '#6e63b3', '#4e429f', '#3b318c', '#2e2570']
}

OBJECTIVE_COLORS = {
    list(ROH_DICT_INV.keys())[0]: ['#b3cde3', '#6497b1', '#005b96', '#03396c', '#011f4b', '#011a30'],
    list(ROH_DICT_INV.keys())[1]: ['#ffcc99', '#ff8800'],
    list(ROH_DICT_INV.keys())[2]: ['#b2dfdb', '#4db6ac'],
    list(ROH_DICT_INV.keys())[3]: ['#cec3e6', '#6e63b3']
}
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
MEASURE_COLORS = {
            '100': '#f3f3f3',
            '1': '#ffcc99',
            '2': '#ffaa66',
            '3': '#ff8800',
            '4': '#cc6e00',
            '5': '#994c00',
            '6':'#cec3e6',
            '7': '#9d94cc',
            '8': '#4e429f',
            '9': '#2e2570',
            '10': '#b3cde3',
            '11': '#6497b1',
            '12': '#03396c',
            '13': '#011f4b',
            '14': '#011a30',
            '15': '#005b96',
            '16': '#b2dfdb',
            '17': '#00897b',
            '18': '#00695c',
            '19': '#004d40'
        }
