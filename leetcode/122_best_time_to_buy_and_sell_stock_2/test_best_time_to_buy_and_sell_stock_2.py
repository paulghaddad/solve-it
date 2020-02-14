import pytest

from best_time_to_buy_and_sell_stock_2 import max_profit

def test_best_time_to_buy_and_sell_stock_2():
    assert max_profit([7, 1, 5, 3, 6, 4]) == 7
    assert max_profit([1, 2, 3, 4, 5]) == 4
    assert max_profit([7, 6, 4, 3, 1]) == 0
