import pytest

from find_pivot_index import find_pivot_index_1


def test_find_pivot_index_1():
    assert find_pivot_index_1([1, 7, 3, 6, 5, 6]) == 3
    assert find_pivot_index_1([1, 2, 3]) == -1
    assert find_pivot_index_1([-1, -1, -1, 0, 1, 1]) == 0
    assert find_pivot_index_1([-1, -1, 0, 1, 1, 0]) == 5
