class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        answer = [1] * n

        leftProduct = 1
        for i in range(n):
            answer[i] = answer[i - 1] * nums[i - 1]

        rightProduct = 1

        for i in range(n - 1, -1, -1):
            answer[i] = answer[i + 1] * nums[i + 1]

        return answer


obj = Solution()
print(obj.productExceptSelf([1, 2, 3, 4]))
