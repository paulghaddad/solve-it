import pytest
import json
from solution import Serializable, JSONMixin, XMLMixin, CSVMixin


def test_no_mixin(tmp_path):
    class Book(Serializable):
        def __init__(self, title, author, price):
            self.title = title
            self.author = author
            self.price = price

        def __repr__(self):
            return f"{self.title}, by {self.author}, for {self.price}"

    b = Book('title', 'author', 100)
    path = tmp_path / "hello.txt"
    b.dump(path)

    b.load(path)

    assert b.title == 'title'
    assert b.author == 'author'
    assert b.price == 100


def test_json_mixin(tmp_path):
    class Book(JSONMixin, Serializable):
        def __init__(self, title, author, price):
            self.title = title
            self.author = author
            self.price = price

        def __repr__(self):
            return f"{self.title}, by {self.author}, for {self.price}"

    b = Book('title', 'author', 100)
    p = tmp_path / "hello.txt"
    b.dump(p)

    b.load(p)

    assert b.title == 'title'
    assert b.author == 'author'
    assert b.price == 100

    assert type(json.load(open(p, 'rb'))) == dict


def test_csv_mixin(tmp_path):
    class Book(CSVMixin, Serializable):
        def __init__(self, title, author, price):
            self.title = title
            self.author = author
            self.price = price

        def __repr__(self):
            return f"{self.title}, by {self.author}, for {self.price}"

    b = Book('title', 'author', 100)
    p = tmp_path / "hello.txt"
    b.dump(p)

    book = b.load(p)

    assert b.title == 'title'
    assert b.author == 'author'
    assert int(b.price) == 100


# def test_xml_mixin(tmp_path):
#     class Book(XMLMixin, Serializable):
#         def __init__(self, title, author, price):
#             self.title = title
#             self.author = author
#             self.price = price
#
#         def __repr__(self):
#             return f"{self.title}, by {self.author}, for {self.price}"
#
#     b = Book('title', 'author', 100)
#     p = tmp_path / "hello.txt"
#     b.dump(p)
#
#     b.load(p)
#
#     assert b.title == 'title'
#     assert b.author == 'author'
#     assert int(b.price) == 100
