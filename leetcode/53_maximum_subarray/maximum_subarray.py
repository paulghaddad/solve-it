def max_subarray(nums):
    max_sum_so_far = sum_of_current_subarray = nums[0]

    for i in range(1, len(nums)):
        num = nums[i]
        sum_of_current_subarray = max(sum_of_current_subarray + num, num)
        max_sum_so_far = max(max_sum_so_far, sum_of_current_subarray)

    return max_sum_so_far
