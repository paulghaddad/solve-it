from two_sum import (
    two_sum_approach_1,
    two_sum_approach_2,
    two_sum_approach_3
)



def test_two_sum():
    assert two_sum_approach_1([2, 7, 11, 15], target=9) == [0, 1]
    assert two_sum_approach_2([2, 7, 11, 15], target=9) == [0, 1]
    assert two_sum_approach_3([2, 7, 11, 15], target=9) == [0, 1]
