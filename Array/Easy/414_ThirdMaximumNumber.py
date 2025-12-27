"""
LeetCode 414: Third Maximum Number
Easy
Sorting + Set | Time: O(n log n), Space: O(n)
Author: Tilak Bhattarai
"""


class Solution:
    def thirdMax(self, nums):
        """
        Returns the third maximum number in the array.
        If it does not exist, return the maximum number.

        :param nums: List[int] - input array
        :return: int - third maximum or maximum if less than 3 distinct numbers
        """
        unique_nums = sorted(set(nums), reverse=True)
        if len(unique_nums) < 3:
            return unique_nums[0]
        return unique_nums[2]


# Example run
if __name__ == "__main__":
    obj = Solution()
    arr = [5, 6, 3, 8, 1]
    output = obj.thirdMax(arr)
    print(f"Input: {arr} -> Third Maximum Number: {output}")
