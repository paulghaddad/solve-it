# Time Cost: O(n)
# Space Cost: O(n)

def rob(nums):
    if not nums:
        return 0

    if len(nums) < 3:
        return max(nums)

    max_profit_at_each_house = [0] * len(nums)
    max_profit_at_each_house[0:2] = nums[0:2]
    max_profit_at_each_house[2] = nums[0] + nums[2]

    current_max = max(max_profit_at_each_house)

    for i in range(3, len(nums)):
        profit_two_back = max_profit_at_each_house[i-2]
        profit_three_back = max_profit_at_each_house[i-3]
        max_profit_at_each_house[i] = max(
            profit_two_back + nums[i],
            profit_three_back + nums[i]
        )

        if max_profit_at_each_house[i] > current_max:
            current_max = max_profit_at_each_house[i]

    return current_max
