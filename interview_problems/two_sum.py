"""
Two Sum Problem Implementation in Python

Given an array of integers and a target sum, find two numbers that add up to the target.
Return their indices.

Time Complexity: O(n) using hash table
"""

def two_sum(nums, target):
    """
    Find two numbers in nums that add up to target.
    Return their indices.
    """
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []  # No solution found

# Example usage and test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print("Two sum for", nums1, "target", target1, ":", two_sum(nums1, target1))  # [0, 1]

    # Test case 2
    nums2 = [3, 2, 4]
    target2 = 6
    print("Two sum for", nums2, "target", target2, ":", two_sum(nums2, target2))  # [1, 2]

    # Test case 3
    nums3 = [3, 3]
    target3 = 6
    print("Two sum for", nums3, "target", target3, ":", two_sum(nums3, target3))  # [0, 1]

    # Test case 4 (no solution)
    nums4 = [1, 2, 3]
    target4 = 10
    print("Two sum for", nums4, "target", target4, ":", two_sum(nums4, target4))  # []
