from collections import Counter

# Time Complexity: O(n)
# Space Complexity: O(n)

def intersect(nums1, nums2):
    nums1_counts = Counter(nums1)
    nums2_counts = Counter(nums2)

    intersection = []
    for num, count in nums1_counts.items():
        if nums2_counts[num]:
            num_common_elements = min(nums1_counts[num], nums2_counts[num])
            intersection.extend([num] * num_common_elements)

    return intersection
