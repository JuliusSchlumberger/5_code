from Paper3_v1.scripts.utilities.design_choices.main_dashboard_dropdowns import ROH_DICT_INV

PANEL_BACKGROUND = '#e0e0e0'
DASHBOARD_BACKGROUND = '#f0f0f0'

DASHBOARD_DIMENSIONS = {
    'padding':  '1vw',
    'padding_dashboard':  '1vw',
    'left_panel_width': '30vw',
    'right_panel_width': '66vw',
    'margin': '1vh',
    'button_vdistance': '2vh',
    'figure_options': '64vw',
    'figure_options_mr': '50vh',
    'options_panel': '600px',
    'performance_panel': '600px',
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


COLORSCALE_PCP = [[0, 'grey'],[.5, 'red'],  [1, 'red']]

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