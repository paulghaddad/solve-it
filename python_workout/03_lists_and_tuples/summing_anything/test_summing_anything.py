import pytest

from summing_anything import mysum


def test_mysum():
    assert mysum('abc', 'def') == 'abcdef'
    assert mysum([1,2,3], [4,5,6]) == [1,2,3,4,5,6]
    assert mysum(1, 2, 3) == 6
    assert mysum() == ()
