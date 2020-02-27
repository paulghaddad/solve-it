# Time Complexity: O(n*m)
# Space Complexity: O(n)

def strStr(haystack, needle):
    len_haystack = len(haystack)
    len_needle = len(needle)

    if not len_needle:
        return 0

    for i in range(len_haystack - len_needle + 1):
        if haystack[i:i+len_needle] == needle:
            return i

    return -1
