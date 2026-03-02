class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ones = 0
        twos = 0

        for num in nums:
            ones = (num ^ ones) & ~twos
            twos = (num ^ twos) & ~ones
        return ones


obj = Solution()
print(obj.singleNumber([2, 2, 3, 2]))
