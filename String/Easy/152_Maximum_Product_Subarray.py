class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        best = nums[0]
        worst = nums[0]
        answer = nums[0]

        for i in range(1, len(nums)):
            x = nums[i]
            tempbest = max(x, x * best, x * worst)
            worst = min(x, x * best, x * worst)
            best = tempbest

            answer = max(answer, best)
        return answer


obj = Solution()
print(obj.maxProduct([2, 3, -2, 4, -1]))
