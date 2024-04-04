from Paper3_v1.scripts.utilities.map_system_parameters import OBJECTIVE_PARAMETER_DICT

TIMEHORIZONS_OF_INTEREST = [20, 60, 100]

PERFORMANCE_METRICS_LIST = ['5%', '50%', '95%', 'average']  # 5% means that only in 5% of cases a performance is exceeded

SCENARIO_OPTIONS = [['D', 'G', 'Wp'], ['D'], ['G'], ['Wp'],['D', 'G'], ['D', 'Wp'], ['G', 'Wp']]


NORMALIZATION_BENCHMARKS = {OBJECTIVE_PARAMETER_DICT['cost_d_a']: 400,
                            OBJECTIVE_PARAMETER_DICT['cost_f_u']: 500,
                            OBJECTIVE_PARAMETER_DICT['cost_d_s']: 3000,
                            OBJECTIVE_PARAMETER_DICT['cost_f_a']: 300}


for timehorizon in TIMEHORIZONS_OF_INTEREST:
    NORMALIZATION_BENCHMARKS[timehorizon] = {}
    for performance in PERFORMANCE_METRICS_LIST:
        NORMALIZATION_BENCHMARKS[timehorizon][performance] = {}


