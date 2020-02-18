from collections import Counter

# Time Complexity: O(n)
# Space Complexity: O(n)

def first_uniq_char(s):
    char_counts = Counter(s)

    for i, char in enumerate(list(s)):
        if char_counts[char] == 1:
            return i

    return -1
