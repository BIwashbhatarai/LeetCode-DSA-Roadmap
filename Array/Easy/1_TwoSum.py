"""
LeetCode 1: Two Sum
Easy
Author: Tilak Bhattarai
"""


class Solution:
    def twoSum(self, nums, target):
        """
        Brute-force solution (O(n^2))
        Finds indices of two numbers that add up to target.

        :param nums: List[int] - input array
        :param target: int - target sum
        :return: List[int] - indices of the two numbers
        """
        n = len(nums)

        # Check every pair of numbers
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return []  # No valid pair found


# Example run
if __name__ == "__main__":
    obj = Solution()
    nums = [1, 2, 3, 4]
    target = 8
    output = obj.twoSum(nums, target)
    print(f"Input: {nums}, Target: {target} -> Output: {output}")
