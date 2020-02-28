# Time Complexity: O(n)
# Space Complexity: O(1)

def longest_common_prefix(strs):
    if not strs:
        return ''

    if len(strs) == 1:
        return strs[0]

    shortest_word = min(strs, key=len)

    i = 0
    while i < len(shortest_word):
        current_char = strs[0][i]

        for word in strs:
            if word[i] != current_char:
                return shortest_word[:i]

        i += 1

    return shortest_word[:i]
