# Time Complexity: O(n)
# Space Complexity: O(1)

def reverse_string(s):
    # set a pointers at the front and back of the array
    left = 0
    right = len(s) - 1

    while (left < right):
        # swap chars
        s[left], s[right] = s[right], s[left]

        left += 1
        right -= 1

    return s
