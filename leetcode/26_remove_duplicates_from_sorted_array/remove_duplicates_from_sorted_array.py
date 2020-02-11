# Time Complexity: O(n)
# Space Complexity: O(1)

def remove_duplicates(nums):
    unique = 0

    for i in range(len(nums)):
        if nums[i] != nums[unique]:
            unique += 1
            nums[unique] = nums[i]

    return unique + 1
