# Time Complexity: O(n)
# Space Complexity: O(1)

def move_zeros(nums):
    # x is left pointer; y is right pointer
    x, y = 0, 1

    while (y < len(nums)):
        # element at left pointer is non-zero, move both pointers
        if nums[x]:
            x += 1
            y += 1
        # element at left pointer is zero, element at right pointer is non-zero
        # swap and increment both pointers
        elif nums[y]:
            nums[x], nums[y] = nums[y], nums[x]
            x += 1
            y += 1
        else:
        # Move right pointer until it reaches a non-zero value
            y += 1

    return nums
