import pytest

from sorting_a_string import sort_string


def test_sort_string():
    assert sort_string('cba') == 'abc'
