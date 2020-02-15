from collections import Counter


# Time Complexity:  O(n)
# Space Complexity:  O(n)
def single_number_1(nums):
    nums_counter = {}

    for num in nums:
        nums_counter[num] = nums_counter.get(num, 0) + 1

    for num, count in nums_counter.items():
        if count == 1:
            return num


# Time Complexity:  O(n)
# Space Complexity:  O(n)

def single_number_2(nums):
    counts = Counter(nums)

    for num, count in counts.items():
        if count == 1:
            return num

# Time Complexity:  O(n)
# Space Complexity:  O(1)

def single_number_3(nums):
    # Observe 1 ^ 2 ^ 1 == 2

    single_number = 0

    for num in nums:
        single_number ^= num

    return single_number
