import pytest

from remove_duplicates_from_sorted_array import remove_duplicates


def test_remove_duplicates():
    assert remove_duplicates([1, 1, 2]) == 2
    assert remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5
