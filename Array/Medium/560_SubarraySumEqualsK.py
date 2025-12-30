class Solution(object):
    def subarraySum(self, nums, k):
        n = len(nums)
        count = 0
        for start in range(n):
            curr_sum = 0
            for end in range(start, n):
                curr_sum += nums[end]
                if curr_sum == k:
                    count += 1
        return count


obj = Solution()
print(obj.subarraySum([1, 2, 3, 4], 5))
