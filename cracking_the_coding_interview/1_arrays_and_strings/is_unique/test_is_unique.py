import pytest

from is_unique import is_unique


def test_is_unique():
    assert is_unique("abc") is True
    assert is_unique("abca") is False
    assert is_unique("") is True
