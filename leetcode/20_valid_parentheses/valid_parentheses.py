from collections import deque

BRACKETS = {
    '(': ')',
    '[': ']',
    '{': '}',
}

# Time Complexity: O(n)
# Space Complexity: O(n)


def is_valid(s):
    stack = deque()

    for char in s:
        if char in BRACKETS:
            stack.append(char)
            continue

        try:
            matching_element = stack.pop()
            if not BRACKETS[matching_element] == char:
                return False
        except IndexError as e:
            return False

    return len(stack) == 0
