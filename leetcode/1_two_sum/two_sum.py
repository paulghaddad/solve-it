import pytest

# Time Complexity: O(n**2)
# Space Complexity: O(1)
def two_sum_approach_1(nums, target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


# Time Complexity: O(n)
# Space Complexity: O(n)
def two_sum_approach_2(nums, target):
    complements = {}

    for i, num in enumerate(nums):
        complements[num] = i

    for i, num in enumerate(nums):
        complement = target - num
        if complement in complements and complements[complement] != i:
            return [i, complements[complement]]


# Time Complexity: O(n)
# Space Complexity: O(n)
def two_sum_approach_3(nums, target):
    complements = {}

    for i, num in enumerate(nums):
        complements[num] = i

        complement = target - num
        if complement in complements:
            return [complements[complement], i]
