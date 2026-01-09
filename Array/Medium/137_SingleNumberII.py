"""
LeetCode Problem 137: Single Number II
Brute Force Count-Based Solution

Given an integer array where every element appears three times except for one,
find the single element that appears only once.

Time Complexity: O(n^2)
Space Complexity: O(1)
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Approach:
        - Loop through each number in the list
        - Count its occurrences using nums.count(num)
        - Return the number if it appears exactly once
        """
        for num in nums:
            if nums.count(num) == 1:
                return num


# Example usage
if __name__ == "__main__":
    obj = Solution()
    print(obj.singleNumber([2, 2, 3, 2]))  # Output: 3
    print(obj.singleNumber([0, 1, 0, 1, 0, 1, 99]))  # Output: 99
