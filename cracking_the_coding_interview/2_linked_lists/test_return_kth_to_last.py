import pytest


def return_kth_to_last(head, k):
    if not head.value:
        raise ValueError("List is empty")

    length = 0
    current_node = head

    while current_node:
        length += 1
        current_node = current_node.next

    if k > length:
        raise ValueError("k exceeds the length of the list")

    current_node = head
    for _ in range(length-k):
        current_value = current_node.value
        current_node = current_node.next

    return current_value


def test_return_kth_to_last():
    a = LinkedListNode(5)
    b = LinkedListNode(7)
    c = LinkedListNode(8)
    d = LinkedListNode(3)
    e = LinkedListNode(5)
    f = LinkedListNode(2)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f

    assert return_kth_to_last(a, 2) == 3

def test_return_kth_to_last_empty():
    empty_list = LinkedListNode(None)

    with pytest.raises(ValueError):
        return_kth_to_last(empty_list, 0)


def test_return_kth_to_invalid_k():
    a = LinkedListNode(5)
    b = LinkedListNode(7)
    c = LinkedListNode(8)

    a.next = b
    b.next = c

    with pytest.raises(ValueError):
        assert return_kth_to_last(a, 4)

class LinkedListNode(object):
    def __init__(self, value):
        self.value = value
        self.next  = None
