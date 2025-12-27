"""
LeetCode 268: Missing Number
Easy
Math Approach | Time: O(n), Space: O(1)
Author: Tilak Bhattarai
"""


class Solution:
    def missingNumber(self, nums):
        """
        Finds the missing number from 0 to n in an array.

        :param nums: List[int] - input array containing n distinct numbers in the range [0, n]
        :return: int - the missing number
        """
        n = len(nums)
        expected_sum = (n * (n + 1)) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum


# Example run
if __name__ == "__main__":
    obj = Solution()
    nums = [0, 1, 3]
    output = obj.missingNumber(nums)
    print(f"Input: {nums} -> Missing Number: {output}")
