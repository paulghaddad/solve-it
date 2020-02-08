# Time complexity: O(n)
# Space complexity: O(n)

def dominant_index_approach_1(nums):
    max_num = max(nums)

    for num in nums:
        if num != max_num and num*2 > max_num:
            return -1

    return nums.index(max_num)
