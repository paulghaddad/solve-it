import pytest

from maximum_subarray import max_subarray


def test_max_subarray():
    assert max_subarray([1]) == 1
    assert max_subarray([-2, 1, -3, 4, -1, 2, 1]) == 6
    assert max_subarray([34, -50, 42, 14, -5, 86]) == 137
