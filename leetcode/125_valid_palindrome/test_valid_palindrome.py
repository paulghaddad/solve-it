import pytest

from valid_palindrome import is_palindrome

def test_is_palindrome():
    assert is_palindrome('') == True
    assert is_palindrome('ana') == True
    assert is_palindrome('anb') == False
    assert is_palindrome('Ana') == True
    assert is_palindrome('A man, a plan, a canal: Panama') == True
    assert is_palindrome('race a car') == False
    assert is_palindrome('0P') == False
