import pytest

from mysum import mysum


def test_mysum():
    assert mysum([1, 2, 3]) == 6
    assert mysum([10, 20, 30, 40, 50]) == 150
    assert mysum([]) == 0
