import pytest

# Time Complexity: O(n)
# Space Complexity: O(n)

def remove_duplicates(head_node):
    previous_node = None
    current_node = head_node
    prev_values = set()

    while current_node:
        if current_node.value in prev_values:
            previous_node.next = current_node.next
            current_node = previous_node.next
        else:
            prev_values.add(current_node.value)
            previous_node, current_node = current_node, current_node.next


def test_remove_dups():
    a = LinkedListNode(5)
    b = LinkedListNode(3)
    c = LinkedListNode(8)
    d = LinkedListNode(3)
    e = LinkedListNode(5)
    f = LinkedListNode(2)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f

    remove_duplicates(a)

    assert a.next == b
    assert b.next == c
    assert c.next == f
    assert f.next is None


class LinkedListNode(object):
    def __init__(self, value):
        self.value = value
        self.next  = None
