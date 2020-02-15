# Time Complexity: O(n)
# Space Complexity O(1)

def contains_duplicate_1(nums):
    return len(nums) != len(set(nums))


# Time Complexity: O(n)
# Space Complexity O(n)

def contains_duplicate_2(nums):
    prev_nums = {}

    for num in nums:
        if num in prev_nums:
            return True

        prev_nums[num] = True

    return False
