from collections import deque


class MaxStack():
    def __init__(self):
        self._items = deque()
        self._max_stack = deque()


    def push(self, item):
        if not self._max_stack or item >= self.max():
            self._max_stack.append(item)

        self._items.append(item)


    def pop(self):
        if self.peek() == self.max():
            self._max_stack.pop()

        return self._items.pop()


    def peek(self):
        return self._items[-1]


    def max(self):
        return self._max_stack[-1]
