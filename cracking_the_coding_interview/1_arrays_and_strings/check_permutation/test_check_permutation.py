import pytest

from check_permutation import check_permutation

def test_check_permutation():
    assert check_permutation('abc', 'cba') is True
    assert check_permutation('abc', 'dba') is False
    assert check_permutation('abcd', 'dba') is False
    assert check_permutation('ab', 'dba') is False
    assert check_permutation('', '') is True
