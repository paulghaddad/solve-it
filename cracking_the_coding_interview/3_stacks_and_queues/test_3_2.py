from collections import deque

import pytest


# Approach 1
# class MinStack:
#     def __init__(self):
#         self._stack = deque()
#         self._min_stack = deque()
#         self._current_min = None
#
#     def push(self, item):
#         self._stack.append(item)
#
#     def pop(self):
#         popped_item = self._stack.pop()
#         if popped_item == self._current_min:
#             self._current_min = None
#
#     def peek(self):
#         return self._stack[-1]
#
#     def get_min(self):
#         if not self._current_min:
#             while self._stack:
#                 item = self._stack.pop()
#                 if self._current_min is None or item < self._current_min:
#                     self._current_min = item
#
#                 self._min_stack.append(item)
#
#             while self._min_stack:
#                 item = self._min_stack.pop()
#                 self._stack.append(item)
#
#         return self._current_min

# Approach 2

# Time: push, pop, peek and get_min are O(1)
# Space: O(n)

# class MinStack():
#     def __init__(self):
#         self._stack = deque()
#
#
#     def push(self, item):
#         if not self._stack:
#             self._stack.append((item, item))
#
#         self._stack.append((item, min(self._peek()[1], item)))
#
#
#     def pop(self):
#         self._stack.pop()
#
#
#     def _peek(self):
#         return self._stack[-1]
#
#
#     def peek(self):
#         return self._peek()[0]
#
#
#     def get_min(self):
#         return self._peek()[1]


# Time: push, pop, peek and get_min are O(1)
# Space: O(n) but less space than Approach 2

# Approach 3
class MinStack:
    def __init__(self):
        self._stack = deque()
        self._min_stack = deque()

    def push(self, item):
        self._stack.append(item)

        if not self._min_stack or item <= self._min_stack[-1]:
            self._min_stack.append(item)

    def pop(self):
        popped_item = self._stack.pop()
        if popped_item == self._min_stack[-1]:
            self._min_stack.pop()

    def peek(self):
        return self._stack[-1]

    def get_min(self):
        return self._min_stack[-1]


def test_min_stack():
    stack = MinStack()
    stack.push(-2)
    stack.push(0)
    stack.push(-3)

    assert stack.get_min() == -3

    stack.pop()

    assert stack.peek() == 0

    assert stack.get_min() == -2
