class Solution(object):
    def findMaxAverage(self, nums, k):
        n = len(nums)
        oldSum = sum(nums[:k])
        maxAvg = float(oldSum / len(nums[:k]))

        for i in range(k, n):
            newSum = oldSum - nums[i - k] + nums[i]
            maxAvg = max(maxAvg, float(newSum / k))
        return maxAvg


obj = Solution()
print(obj.findMaxAverage([1, 12, -5, -6, 50, 3], 4))
