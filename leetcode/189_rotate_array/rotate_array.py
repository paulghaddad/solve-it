# Time Complexity: O(n)
# Space Complexity: O(n)

def rotate(nums, k):
    nums_length = len(nums)
    rotated_array = [None] * nums_length

    for i, num in enumerate(nums):
        rotated_index = (i + k) % nums_length
        rotated_array[rotated_index] = num

    for i in range(nums_length):
        nums[i] = rotated_array[i]

    return nums
