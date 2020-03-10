import pytest

from max_stack import MaxStack


def test_push():
    stack = MaxStack()

    stack.push(10)

    assert stack.peek() == 10


def test_pop():
    stack = MaxStack()

    stack.push(10)

    assert stack.pop() == 10


def test_pop_no_items():
    stack = MaxStack()

    with pytest.raises(IndexError):
        stack.pop()


def test_max():
    stack = MaxStack()

    stack.push(10)
    stack.push(50)
    stack.push(1)

    assert stack.max() == 50


def test_max_with_duplicates():
    stack = MaxStack()

    stack.push(10)
    stack.push(50)
    stack.push(50)

    assert stack.max() == 50

    stack.pop()

    assert stack.max() == 50

    stack.pop()

    assert stack.max() == 10



def test_max_with_changes():
    stack = MaxStack()

    stack.push(10)
    stack.push(50)
    stack.push(75)
    stack.push(5)

    assert stack.max() == 75

    stack.pop()
    stack.pop()

    assert stack.max() == 50


def test_max_no_items():
    stack = MaxStack()

    with pytest.raises(IndexError):
        stack.max()
