import pytest

from plus_one import (
    plus_one_approach_1,
    plus_one_approach_2,
)

def test_plus_one_approach_1():
    assert plus_one_approach_1([1, 2, 3]) == [1, 2, 4]
    assert plus_one_approach_1([1, 2, 9]) == [1, 3, 0]
    assert plus_one_approach_1([1, 9, 9]) == [2, 0, 0]
    assert plus_one_approach_1([9, 9, 9]) == [1, 0, 0, 0]
    assert plus_one_approach_1([2, 9, 9]) == [3, 0, 0]


def test_plus_one_approach_2():
    assert plus_one_approach_2([1, 2, 3]) == [1, 2, 4]
    assert plus_one_approach_2([1, 2, 9]) == [1, 3, 0]
    assert plus_one_approach_2([1, 9, 9]) == [2, 0, 0]
    assert plus_one_approach_2([9, 9, 9]) == [1, 0, 0, 0]
    assert plus_one_approach_2([2, 9, 9]) == [3, 0, 0]
