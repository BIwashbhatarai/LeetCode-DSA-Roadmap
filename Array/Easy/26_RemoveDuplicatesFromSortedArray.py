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
        if not nums:
            return 0

        # Pointer i tracks the position of the last unique element
        i = 0

        # Pointer j scans through the array
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1


# Example run
if __name__ == "__main__":
    obj = Solution()
    arr = [1, 1, 2, 3, 3]
    length = obj.removeDuplicates(arr)
    print(
        f"Input: [1,1,2,3,3] -> Length after removing duplicates: {length}, Array: {arr[:length]}"
    )
