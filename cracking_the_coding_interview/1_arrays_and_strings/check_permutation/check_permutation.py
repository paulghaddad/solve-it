from collections import Counter

def check_permutation(str1, str2):
    # Approach 1
    # Time: O(nlogn)
    # Space: O(n) in Python

    # sorted_str1 = sorted(str1)
    # sorted_str2 = sorted(str2)
    #
    # if len(sorted_str1) != len(sorted_str2):
    #     return False
    #
    # for i, char in enumerate(sorted_str1):
    #     if char != sorted_str2[i]:
    #         return False
    #
    # return True

    # Approach 2
    # Time: O(n)
    # Space: O(n)

    counts1, counts2 = Counter(str1), Counter(str2)

    if len(counts1.keys()) != len(counts2.keys()):
        return False

    return len(counts1 - counts2) == 0
