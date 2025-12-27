"""
LeetCode 27: Remove Element
Easy
Two-Pointer Approach | Time: O(n), Space: O(1)
Author: Tilak Bhattarai
"""


class Solution:
    def removeElement(self, nums, val):
        """
        Removes all instances of val in-place and returns the new length.

        :param nums: List[int] - input array
        :param val: int - value to remove
        :return: int - new length of array
        """
        k = 0  # Pointer for next position of valid element
        for num in nums:
            if num != val:
                nums[k] = num
                k += 1
        return k


# Example run
if __name__ == "__main__":
    obj = Solution()
    nums = [3, 2, 2, 3]
    val = 3
    k = obj.removeElement(nums, val)
    print(
        f"Input: [3, 2, 2, 3], Value to remove: {val} -> Array after removal: {nums[:k]}, New length: {k}"
    )
