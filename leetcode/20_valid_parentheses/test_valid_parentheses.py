import pytest

from valid_parentheses import is_valid


def test_is_valid():
    assert is_valid('()') == True
    assert is_valid('()[]{}') == True
    assert is_valid('(]') == False
    assert is_valid('([)]') == False
    assert is_valid('{[]}') == True
    assert is_valid('') == True
    assert is_valid('[') == False
    assert is_valid(']') == False
