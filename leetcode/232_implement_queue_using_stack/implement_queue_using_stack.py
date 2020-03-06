from stack import Stack

# Time Complexity: O(1) for enqueue and amortized O(1) for dequeue
# Space Complexity: O(n)

class MyQueue():

    def __init__(self):
        self._s1 = Stack()
        self._s2 = Stack()


    def is_empty(self):
        return self._s1.is_empty() and self._s2.is_empty()


    def size(self):
        return self._s1.size() + self._s2.size()


    def enqueue(self, x):
        self._s1.push(x)


    def dequeue(self):
        if self._s2.is_empty():
            while not self._s1.is_empty():
                self._s2.push(self._s1.pop())

        return self._s2.pop()
