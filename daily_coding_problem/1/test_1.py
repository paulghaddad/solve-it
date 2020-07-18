import pytest


def two_elements_add_to_target(arr, k):
    for i, el in enumerate(arr):
        for summand in range(i+1, len(arr)):
            if el + summand == k:
                return True

    return False


def test_two_elements_add_to_target_true():
    arr = [10, 15, 3, 7]
    k = 17

    assert two_elements_add_to_target(arr, k) is True


def test_two_elements_add_to_target_false():
    arr = [10, 15, 3, 7]
    k = 19

    assert two_elements_add_to_target(arr, k) is False
