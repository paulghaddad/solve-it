import pytest


# Time: O(n)
# Space: O(n)

def compress(s):
    left = 0
    right = 0
    compressed_str = []

    str_len = len(s)

    while left < str_len:
        while right < str_len and s[left] == s[right]:
            right += 1

        compressed_str.append(s[left])
        compressed_str.append(str(right-left))

        left = right

    if str_len <= len(compressed_str):
        return s

    return ''.join(compressed_str)


def test_base_case():
    assert compress('aabcccccaaa') == 'a2b1c5a3'


def test_string_not_compressed():
    assert compress('aabbcc') == 'aabbcc'
    assert compress('aabcc') == 'aabcc'
