import pytest

from first_unique_character_in_string import first_uniq_char

def test_first_uniq_char():
    assert first_uniq_char("leetcode") == 0
    assert first_uniq_char("loveleetcode") == 2
    assert first_uniq_char("") == -1
    assert first_uniq_char("aabbcc") == -1
