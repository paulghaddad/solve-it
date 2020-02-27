import pytest

from string_to_integer import my_a_to_i

def test_my_a_to_i():
    assert my_a_to_i("42") == 42
    assert my_a_to_i("-42") == -42
    assert my_a_to_i("           -42") == -42
    assert my_a_to_i("4193 with words") == 4193
    assert my_a_to_i("words and 987") == 0
    assert my_a_to_i("-91283472332") == -2**31
    assert my_a_to_i("3.14") == 3
    assert my_a_to_i("+1") == 1
    assert my_a_to_i("+-1") == 0
    assert my_a_to_i("-+1") == 0
    assert my_a_to_i("+") == 0
    assert my_a_to_i("  -0012a42") == -12
