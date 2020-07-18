import pytest

# Time: O(n)
# Space: O(n)

def two_elements_add_to_target(arr, k):
    numbers_seen = set()

    for el in arr:
        complement = k - el
        if complement in numbers_seen:
            return True

        numbers_seen.add(el)

    return False



def test_two_elements_add_to_target_true():
    arr = [10, 15, 3, 7]
    k = 17

    assert two_elements_add_to_target(arr, k) is True


def test_two_elements_add_to_target_false():
    arr = [10, 15, 3, 7]
    k = 19

    assert two_elements_add_to_target(arr, k) is False
