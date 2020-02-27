import pytest

from implement_str_str import strStr


def test_strStr():
    assert strStr('hello', 'll') == 2
    assert strStr('hello', 'llo') == 2
    assert strStr('aaaaa', 'bba') == -1
    assert strStr('aaaaa', 'ab') == -1
    assert strStr('aaaaa', '') == 0
