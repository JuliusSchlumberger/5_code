

TIMEHORIZONS_OF_INTEREST = [20, 60, 100]

PERFORMANCE_METRICS_LIST = ['5%', '50%', '95%', 'average']  # 5% means that only in 5% of cases a performance is exceeded

SCENARIO_OPTIONS = [['D', 'G', 'Wp'], ['D'], ['G'], ['Wp'],['D', 'G'], ['D', 'Wp'], ['G', 'Wp']]

NORMALIZATION_BENCHMARKS = {'AgrDrought_DRM_cost': 400,
                            'UrbFlood_DRM_cost': 500,
                            'ShpDrought_DRM_cost': 3000,
                            'AgrFlood_DRM_cost': 300}


for timehorizon in TIMEHORIZONS_OF_INTEREST:
    NORMALIZATION_BENCHMARKS[timehorizon] = {}
    for performance in PERFORMANCE_METRICS_LIST:
        NORMALIZATION_BENCHMARKS[timehorizon][performance] = {}


