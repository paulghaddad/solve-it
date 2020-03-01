import pytest

from baseball_game import cal_points


def test_cal_points():
    assert cal_points(['5' ,'2' ,'C' ,'D' ,'+']) == 30
    assert cal_points(['5', '-2', '4', 'C', 'D', '9', '+', '+']) == 27
    assert cal_points([]) == 0

    with pytest.raises(ValueError):
        cal_points(['a'])
