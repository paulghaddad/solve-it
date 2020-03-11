from collections import deque


def is_palindrome(x):
    digits = list(str(x))

    deq = deque(digits)

    while len(deq) > 1:
        if deq.popleft() != deq.pop():
            return False

    return True
