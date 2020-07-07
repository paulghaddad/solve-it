import pytest

# Time: O(n)
# Space: O(1)

def delete_node(node):
    node.val = node.next.val
    node.next = node.next.next


def test_delete_middle_node():
    a = ListNode(4)
    b = ListNode(5)
    c = ListNode(1)
    d = ListNode(9)

    a.next = b
    b.next = c
    c.next = d

    delete_node(b)

    assert a.val == 4
    assert a.next.val == 1
    assert a.next.next.val == 9


class ListNode():
    def __init__(self, value):
        self.val = value
        self.next  = None
