"""
LeetCode 367: Valid Perfect Square
Easy
Author: Tilak Bhattarai
"""


class Solution(object):
    def isPerfectSquare(self, num):
        """
        Binary Search approach to check whether a number is a perfect square.

        :type num: int
        :rtype: bool
        """

        left = 1
        right = num

        if num == 1:
            return True

        while left <= right:

            mid = (left + right) // 2

            if mid * mid == num:
                return True

            elif mid * mid < num:
                left = mid + 1

            else:
                right = mid - 1

        return False


obj = Solution()
print(obj.isPerfectSquare(16))
