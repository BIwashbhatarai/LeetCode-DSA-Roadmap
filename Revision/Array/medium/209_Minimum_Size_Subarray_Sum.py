class Solution(object):
    def minSubArrayLen(self, target, nums):
        minLenght = float("inf")
        currSum = 0
        n = len(nums)
        left = 0

        for right in range(n):
            currSum += nums[right]

            while currSum >= target:
                minLenght = min(minLenght, right - left + 1)
                currSum -= nums[left]
                left += 1  # Making window smaller
        return minLenght


obj = Solution()
print(obj.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
