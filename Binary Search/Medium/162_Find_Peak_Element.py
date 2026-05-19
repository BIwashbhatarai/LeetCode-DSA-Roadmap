class Solution:
    def findPeakElement(self, nums):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left


if __name__ == "__main__":
    obj = Solution()
    print(obj.findPeakElement([1, 2, 1, 3, 5, 6, 4]))
