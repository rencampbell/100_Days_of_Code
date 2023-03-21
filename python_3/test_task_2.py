from task_2 import math_calculate
import pytest


def test_log():
    assert math_calculate('log', 1024, 2) == 10.0

def test_ceil():
    assert math_calculate('ceil', 10.7) == 11

def test_operation_not_found():
    func='lo'
    with pytest.raises(Exception):
        math_calculate(func, 10)