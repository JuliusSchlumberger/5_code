import numpy as np

def calculate_investment_cost(value_elements, invest_cost, implemented_measures):
    # investment_cost = 0
    #
    # # Iterate over each element in value_elements
    # for elem in value_elements:
    #     # Check if the measure is not implemented and add investment cost
    elem = value_elements[-1]
    investment_cost = invest_cost[elem][elem]
    # implemented_measures = np.append(implemented_measures, elem)
    # if elem not in implemented_measures:
    #     # Retrieve the investment cost for this element
    #     # Assuming the index in the ndarray corresponds directly to the element value
    #     investment_cost += invest_cost[elem][elem]
    #     implemented_measures = np.append(implemented_measures, elem)

    return investment_cost, implemented_measures



