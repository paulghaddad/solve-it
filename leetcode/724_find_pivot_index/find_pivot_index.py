# Time Complexity: O(n) - remember the sum is O(n) and the loop is O(n), but
# that's O(n + n) == O(n)
# Space Complexity: O(1)

def find_pivot_index_1(nums):
    total = sum(nums)
    left_sum = 0

    for i, el in enumerate(nums):
        if left_sum == total - left_sum - el:
            return i

        left_sum += el

    return -1
