import pytest

from max_k_length_subarrays import max_k_length_subarrays


def test_max_k_length_subarrays():
    assert max_k_length_subarrays([10, 5, 2, 7, 8, 7], 3) == [10, 7, 8, 8]
