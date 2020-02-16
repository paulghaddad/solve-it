import pytest

from intersection_of_two_arrays_2 import intersect

def test_intersect():
    assert intersect([1, 2, 2, 1], [2, 2]) == [2, 2]
    assert intersect([4, 9, 5], [9, 4, 9, 8, 4]) == [4, 9]
    assert intersect([4, 9, 5], [1, 2, 3]) == []
