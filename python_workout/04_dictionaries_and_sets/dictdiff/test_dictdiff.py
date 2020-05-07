import pytest

from dictdiff import dictdiff


def test_dictdiff():
    d1 = {'a':1, 'b':2, 'c':3}
    d2 = {'a':1, 'b':2, 'c':4}
    d3 = {'a':1, 'b':2, 'd':3}
    d4 = {'a':1, 'b':2, 'c':4}
    d5 = {'a':1, 'b':2, 'd':4}

    assert dictdiff(d1, d1) == {}
    assert dictdiff(d1, d2) == {'c': [3, 4]}
    assert dictdiff(d3, d4) == {'c': [None, 4], 'd': [3, None]}
    assert dictdiff(d1, d5) == {'c': [3, None], 'd': [None, 4]}
