import pytest

from climbing_stairs import climb_stairs


def test_climb_stairs_base_cases():
    assert climb_stairs(1) == 1
    assert climb_stairs(2) == 2


def test_climb_stairs():
    assert climb_stairs(3) == 3
    assert climb_stairs(4) == 5
    assert climb_stairs(10) == 89
