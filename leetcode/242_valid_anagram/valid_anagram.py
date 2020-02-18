from collections import Counter

# Time Complexity: O(n)
# Space Complexity: O(1) - There are a finite number of possible characters so
# the size of the counters do not increase with the size of n.

def is_anagram_1(s, t):
    # Make sure lengths of strings are the same
    if len(s) != len(t):
        return False

    # Subtraction of char counts for each string will be 0 for an anagram
    return len(Counter(list(s)) - Counter(list(t))) == 0


# Time Complexity: O(nlog(n))
# Space Complexity: O(1) - although sorted creates a copy and is thus O(n),
# ignore this because it is a language implementation detail.

def is_anagram_2(s, t):
    return sorted(s) == sorted(t)
