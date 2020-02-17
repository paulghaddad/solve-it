import pytest

from reverse_string import reverse_string

def test_reverse_string():
    assert reverse_string(["h", "e", "l", "l", "o"]) == ["o", "l", "l", "e", "h"]
    assert reverse_string(["H", "a", "n", "n", "a", "h"]) == ["h", "a", "n", "n", "a", "H"]
    assert reverse_string(["a"]) == ["a"]
