import pytest

from repeated_letters import most_repeating_word


def test_most_repeating_word():
    words = ['this', 'is', 'an', 'elementary', 'test', 'example']

    assert most_repeating_word(words) == 'elementary'
