import pytest

from rotate_array import rotate

def test_rotate():
    assert rotate([1, 2, 3, 4, 5, 6, 7], 3) == [5, 6, 7, 1, 2, 3, 4]
    assert rotate([1, 2, 3], 3) == [1, 2, 3]
    assert rotate([1, 2, 3, 4], 2) == [3, 4, 1, 2]
    assert rotate([-1, -100, 3, 99], 2) == [3, 99, -1, -100]
    assert rotate([1], 0) == [1]
    assert rotate([1], 1) == [1]
    assert rotate([1, 2], 1) == [2, 1]
