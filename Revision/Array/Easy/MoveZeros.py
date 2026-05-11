class Solution(object):
    def moveZeroes(self, nums):
        i = 0
        n = len(nums)
        for j in range(n):
            if nums[j] != 0:
                nums[j], nums[i] = nums[i], nums[j]  # Pythonic swap
                i += 1
        return nums


obj = Solution()
print(obj.moveZeroes([1, 0, 0, 0, 1, 7]))
