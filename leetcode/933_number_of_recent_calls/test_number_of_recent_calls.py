import pytest

from number_of_recent_calls import RecentCounter


def test_number_of_recent_calls():
    counter = RecentCounter()

    inputs = [1, 100, 3001, 3002]

    pings = [counter.ping(input) for input in inputs]

    assert pings == [1, 2, 3, 3]
