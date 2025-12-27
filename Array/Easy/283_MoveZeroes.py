"""
LeetCode 283: Move Zeroes
Easy
Two-Pointer Approach | Time: O(n), Space: O(1)
Author: Tilak Bhattarai
"""


class Solution:
    def moveZeroes(self, nums):
        """
        Moves all zeroes in the array to the end while maintaining relative order of non-zero elements.

        :param nums: List[int] - input array
        :return: List[int] - array after moving zeroes
        """
        lastNonZeroFoundAt = 0
        n = len(nums)

        # Move non-zero elements forward
        for i in range(n):
            if nums[i] != 0:
                nums[lastNonZeroFoundAt] = nums[i]
                lastNonZeroFoundAt += 1

        # Fill remaining positions with zeroes
        for i in range(lastNonZeroFoundAt, n):
            nums[i] = 0

        return nums


# Example run
if __name__ == "__main__":
    obj = Solution()
    arr = [0, 1, 0, 3, 12]
    output = obj.moveZeroes(arr)
    print(f"Input: {arr} -> After moving zeroes: {output}")
