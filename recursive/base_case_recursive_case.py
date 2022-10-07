# def recursive_function(parameters):
#    if base_case_condition(parameters):
#         return base_case_value
#    recursive_function(modified_parameters)

def factorial(n):
    if n<2:               # hier is base case
        return 1
    return n*factorial(n-1) # hier is recursive case