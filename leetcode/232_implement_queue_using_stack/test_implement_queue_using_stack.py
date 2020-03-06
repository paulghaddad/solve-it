import pytest

from implement_queue_using_stack import MyQueue


def test_my_queue():
    queue = MyQueue()

    assert queue.is_empty()

    queue.enqueue(1)
    queue.enqueue(2)

    assert queue.is_empty() is False

    assert queue.dequeue() == 1

    assert queue.is_empty() is False

    assert queue.dequeue() == 2

    assert queue.is_empty()

    queue.enqueue(10)

    assert queue.dequeue() == 10
