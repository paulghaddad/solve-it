import pytest

from longest_common_prefix import longest_common_prefix


def test_longest_common_prefix():
    assert longest_common_prefix(['flower', 'flow', 'flight']) == 'fl'
    assert longest_common_prefix(['dog', 'racecar', 'car']) == ''
    assert longest_common_prefix([]) == ''
    assert longest_common_prefix(['']) == ''
    assert longest_common_prefix(['a']) == 'a'
    assert longest_common_prefix(['', '']) == ''
    assert longest_common_prefix(['aa', 'a']) == 'a'
