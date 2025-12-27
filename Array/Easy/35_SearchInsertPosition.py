"""
LeetCode 35: Search Insert Position
Easy
Binary Search | Time: O(log n), Space: O(1)
Author: Tilak Bhattarai
"""


class Solution:
    def searchInsert(self, nums, target):
        """
        Returns the index of the target if found.
        Otherwise, returns the index where it should be inserted.

        :param nums: List[int] - sorted input array
        :param target: int - target value
        :return: int - index of target or insertion position
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left


# Example run
if __name__ == "__main__":
    obj = Solution()
    arr = [1, 2, 4]
    target = 3
    output = obj.searchInsert(arr, target)
    print(f"Input: {arr}, Target: {target} -> Output: {output}")
