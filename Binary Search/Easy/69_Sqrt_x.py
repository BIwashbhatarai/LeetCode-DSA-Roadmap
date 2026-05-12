"""
LeetCode 69: Sqrt(x)
Easy
Author: Tilak Bhattarai
"""


class Solution(object):
    def mySqrt(self, x):
        """
        Binary Search approach to find integer square root of x.

        :type x: int
        :rtype: int
        """

        if x == 0:
            return 0

        left = 1
        right = x

        while left <= right:

            mid = (left + right) // 2

            if mid * mid == x:
                return mid

            elif mid * mid < x:
                left = mid + 1

            else:
                right = mid - 1

        return right


obj = Solution()
print(obj.mySqrt(4))
