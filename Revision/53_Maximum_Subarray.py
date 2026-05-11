class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Kadane Algorithm

        maxSum = float("-inf")
        currSum = 0

        for num in nums:
            currSum += num

            maxSum = max(maxSum, currSum)

            if currSum < 0:
                currSum = 0
        return maxSum


obj = Solution()
print(obj.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
