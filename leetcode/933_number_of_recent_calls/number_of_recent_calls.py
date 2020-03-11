from collections import deque

# Time Complexity: O(n) => n is number of queries made
# Space Complexity: O(1) => Max entries in queue is 3000, so constant space

class RecentCounter:

    def __init__(self):
        self._queue = deque()


    def ping(self, t):
        self._queue.appendleft(t)

        while t - 3000 > self._queue[-1]:
            self._queue.pop()

        return self.counter_size()

    def counter_size(self):
        return len(self._queue)
