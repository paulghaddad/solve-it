import pytest

from house_robber import rob


def test_rob():
    assert rob([]) == 0
    assert rob([1]) == 1
    assert rob([1, 2]) == 2
    assert rob([1, 2, 3]) == 4
    assert rob([1, 2, 3, 1]) == 4
    assert rob([2, 1, 1, 2]) == 4
    assert rob([2, 7, 9, 3, 1]) == 12
    assert rob([4, 1, 2, 7, 5, 3, 1]) == 14
