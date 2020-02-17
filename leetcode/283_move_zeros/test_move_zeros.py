import pytest

from move_zeros import move_zeros

def test_move_zeros():
    assert move_zeros([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
    assert move_zeros([1, 2, 3]) == [1, 2, 3]
    assert move_zeros([0, 1, 2, 3]) == [1, 2, 3, 0]
    assert move_zeros([1, 2, 3, 0]) == [1, 2, 3, 0]
    assert move_zeros([]) == []
    assert move_zeros([0, 0, 0]) == [0, 0, 0]
