class Solution(object):
    def findMaxAverage(self, nums, k):
        n = len(nums)
        # Step 1: sum of first window
        windowSum = sum(nums[:k])
        maxAverage = float(windowSum) / k  # convert to float for decimal

        # Step 2: slide the window
        for i in range(k, n):
            windowSum = windowSum - nums[i - k] + nums[i]
            maxAverage = max(maxAverage, float(windowSum) / k)

        return maxAverage


# Example usage
obj = Solution()
print(obj.findMaxAverage([1, 12, -5, -6, 50, 3], 4))
