class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        product = 1
        maxPro = float("-inf")
        n = len(nums)

        # Left to Right
        for num in nums:
            product *= num

            maxPro = max(maxPro, product)
            if product == 0:
                product = 1

        # Right to Left
        product = 1
        for num in reversed(nums):
            product *= num
            maxPro = max(maxPro, product)

            if product == 0:
                product = 1
        return maxPro


obj = Solution()
print(obj.maxProduct([2, -5, -2, -4, 3]))
