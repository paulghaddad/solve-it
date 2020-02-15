import pytest

from contains_duplicate import (
    contains_duplicate_1,
    contains_duplicate_2,
)

def test_contains_duplicate_1():
    assert contains_duplicate_1([1, 2, 3, 1]) == True
    assert contains_duplicate_1([1, 2, 3, 4]) == False
    assert contains_duplicate_1([1,1,1,3,3,4,3,2,4,2]) == True


def test_contains_duplicate_2():
    assert contains_duplicate_2([1, 2, 3, 1]) == True
    assert contains_duplicate_2([1, 2, 3, 4]) == False
    assert contains_duplicate_2([1,1,1,3,3,4,3,2,4,2]) == True
