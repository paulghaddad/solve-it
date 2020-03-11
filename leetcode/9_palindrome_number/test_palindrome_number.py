import pytest

from palindrome_number import is_palindrome


def test_is_palindrome():
    assert is_palindrome(121) == True
    assert is_palindrome(12) == False
    assert is_palindrome(-121) == False
    assert is_palindrome(1) == True
