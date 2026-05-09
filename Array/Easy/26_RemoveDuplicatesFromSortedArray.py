"""
LeetCode 26: Remove Duplicates from Sorted Array
Easy
Author: Tilak Bhattarai
"""


class Solution:
    def removeDuplicates(self, nums):
        """
        Two-pointer approach (in-place) to remove duplicates from a sorted array.

        :param nums: List[int] - sorted input array
        :return: int - length of array after removing duplicates
        """

        i = 0

        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return nums


obj = Solution()
print(obj.removeDuplicates([1, 1, 3, 4, 5]))
