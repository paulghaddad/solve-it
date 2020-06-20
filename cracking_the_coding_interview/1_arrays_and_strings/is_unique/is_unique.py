# Time: O(n)
# Space: O(n)

def is_unique(s):
    # Approach 1
    # chars_seen = set()
    #
    # for char in s:
    #   if char in chars_seen:
    #       return False
    #   else:
    #       chars_seen.add(char)
    #
    # return True

    # Approach 2
    return len(set(s)) == len(s)
