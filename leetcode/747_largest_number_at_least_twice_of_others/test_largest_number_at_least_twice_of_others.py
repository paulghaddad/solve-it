import pytest

from largest_number_at_least_twice_of_others import dominant_index_approach_1

def test_dominant_index_approach_1():
    assert dominant_index_approach_1([3, 6, 1, 0]) == 1
    assert dominant_index_approach_1([1, 2, 3, 4]) == -1
