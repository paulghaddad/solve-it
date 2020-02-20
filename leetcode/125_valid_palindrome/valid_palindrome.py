# Time Complexity: O(n)
# Space Complexity: O(1)

def is_palindrome(s):
    left = 0
    right = len(s) -1

    s = s.lower()

    while left < right:
        left_char, right_char = s[left], s[right]

        if not left_char.isalnum():
            left += 1
            continue

        if not right_char.isalnum():
            right -= 1
            continue

        if left_char == right_char:
            left += 1
            right -= 1
        else:
            return False

    return True
