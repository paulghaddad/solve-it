import pytest

from valid_anagram import (
    is_anagram_1,
    is_anagram_2,
)


def test_is_anagram_1():
    assert is_anagram_1(s="anagram", t="nagaram") == True
    assert is_anagram_1(s="rat", t="car") == False
    assert is_anagram_1(s="a", t="ab") == False


def test_is_anagram_2():
    assert is_anagram_2(s="anagram", t="nagaram") == True
    assert is_anagram_2(s="rat", t="car") == False
    assert is_anagram_2(s="a", t="ab") == False
