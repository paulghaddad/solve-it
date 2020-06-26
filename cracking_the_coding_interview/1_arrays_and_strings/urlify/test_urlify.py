import pytest

from urlify import urlify


def test_urlify():
    assert urlify("Mr John Smith    ", 13) == "Mr%20John%20Smith"
