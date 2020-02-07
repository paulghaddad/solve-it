# Time Complexity: O(n)
# Space Complexity O(1)

def contains_duplicate_1(elements):
    return len(elements) != len(set(elements))
