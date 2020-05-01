import pytest

from different_numbers import diff_numbers


def test_different_numbers():
    assert diff_numbers([10, 20, 30, 40, 30, 40, 50]) == 5
