import pytest

from single_number import (
    single_number_1,
    single_number_2,
    single_number_3,
)

def test_single_number_approach_1():
    assert single_number_1([2, 2, 1]) == 1
    assert single_number_1([4, 1, 2, 1, 2]) == 4


def test_single_number_approach_2():
    assert single_number_2([2, 2, 1]) == 1
    assert single_number_2([4, 1, 2, 1, 2]) == 4


def test_single_number_approach_3():
    assert single_number_3([2, 2, 1]) == 1
    assert single_number_3([4, 1, 2, 1, 2]) == 4
