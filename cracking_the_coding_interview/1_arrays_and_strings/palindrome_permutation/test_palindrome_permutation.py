import pytest

from collections import defaultdict


def palindrome_permutation(string):
    letter_stack = defaultdict(int)

    num_chars = 0
    for char in string.lower():
        if char == ' ':
            continue

        num_chars += 1
        if letter_stack[char]:
            letter_stack[char] -= 1
        else:
            letter_stack[char] += 1

    if num_chars % 2 == 0:
        return sum(letter_stack.values()) == 0
    else:
        return sum(letter_stack.values()) == 1


def test_palindrome_permutation():
    assert palindrome_permutation('Tact Coa') is True
    assert palindrome_permutation('Aabb') is True
    assert palindrome_permutation('Aabbcd') is False
