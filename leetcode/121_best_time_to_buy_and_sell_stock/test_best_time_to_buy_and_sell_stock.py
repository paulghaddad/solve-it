import pytest

from best_time_to_buy_and_sell_stock import max_profit


def test_max_profit():
    assert max_profit([7]) == 0
    assert max_profit([1, 5]) == 4
    assert max_profit([5, 1]) == 0
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5
    assert max_profit([[7, 6, 4, 3, 1]]) == 0
