class Solution:
    def removeDuplicates(self, nums):
        i = 0

        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return nums


obj = Solution()
print(obj.removeDuplicates([1, 1, 3, 4, 5]))
