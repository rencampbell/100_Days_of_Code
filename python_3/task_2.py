"""
Write function which executes custom operation from math module
for given arguments.
Restrition: math function could take 1 or 2 arguments
If given operation does not exists, raise OperationNotFoundException
Examples:
     >>> math_calculate('log', 1024, 2)
     10.0
     >>> math_calculate('ceil', 10.7)
     11
"""
import math
from string import Template


def math_calculate(function: str, *args):
    args_string=str(args)
    t='math.'+function+str(args_string)
    if not hasattr(math,function):
        raise Exception('OperationNotFoundException')
        return None
    else:
        return eval(t)

"""
Write tests for math_calculate function
"""