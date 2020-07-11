import pytest


# Time: O(n)
# Space: O(1)

def swap_every_other_node_iter(head):
    current = head

    while current and current.next:
        current.val, current.next.val = current.next.val, current.val

        current = current.next.next

    return head


def swap_every_other_node_rec(head):
    head.val, head.next.val = head.next.val, head.val

    if head.next.next is None:
        head.next.next = None
    else:
        head.next.next = swap_every_other_node_rec(head.next.next)

    return head


def test_swap_every_other_node_iter():
    a = LinkNode(1)
    b = LinkNode(2)
    c = LinkNode(3)
    d = LinkNode(4)

    a.next = b
    b.next = c
    c.next = d

    assert a.val == 1
    assert b.val == 2
    assert c.val == 3
    assert d.val == 4

    swapped_list = swap_every_other_node_iter(a)

    assert swapped_list.val == 2
    assert swapped_list.next.val == 1
    assert swapped_list.next.next.val == 4
    assert swapped_list.next.next.next.val == 3


def test_swap_every_other_node_rec():
    a = LinkNode(1)
    b = LinkNode(2)
    c = LinkNode(3)
    d = LinkNode(4)

    a.next = b
    b.next = c
    c.next = d

    assert a.val == 1
    assert b.val == 2
    assert c.val == 3
    assert d.val == 4

    swapped_list = swap_every_other_node_rec(a)

    assert swapped_list.val == 2
    assert swapped_list.next.val == 1
    assert swapped_list.next.next.val == 4
    assert swapped_list.next.next.next.val == 3


class LinkNode:
    def __init__(self, val):
        self.val = val
        self.next = None
