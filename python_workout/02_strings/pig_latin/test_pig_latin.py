import pytest

from pig_latin import convert_to_pig_latin


def test_pig_latin():
    assert convert_to_pig_latin('I love eating pizza') == \
            'Iway ovelay eatingway izzapay'
    assert convert_to_pig_latin('this is a test translation') == \
            'histay isway away esttay ranslationtay'
