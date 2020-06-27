import pytest

def replace_elements(arr):
    max_so_far = -1
    arr_len = len(arr)

    for i, el in enumerate(reversed(arr)):
        arr[arr_len-1-i], max_so_far = max_so_far, max(max_so_far, el)

    return arr


def test_replace_elements():
    assert replace_elements([17,18,5,4,6,1]) == [18,6,6,6,1,-1]
