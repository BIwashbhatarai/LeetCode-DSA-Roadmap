class Solution:
    def singleNonDuplicate(self, nums):
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # make mid even
            if mid % 2 == 1:
                mid -= 1

            if nums[mid] == nums[mid + 1]:
                left = mid + 2
            else:
                right = mid

        return nums[left]


if __name__ == "__main__":
    obj = Solution()
    print(obj.singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]))
