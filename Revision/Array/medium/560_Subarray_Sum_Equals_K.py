# class Solution(object):
#     def subarraySum(self, nums, k):
#         count = 0
#         left = 0
#         n = len(nums)
#         for left in range(n):
#             currSum = 0
#             for rignt in range(left, n):
#                 currSum += nums[rignt]
#                 if currSum == k:
#                     count += 1
#         return count


# obj = Solution()
# print(obj.subarraySum([1, 1, 1], 2))


class Solution(object):
    def subarraySum(self, nums, k):
        count = 0
        n = len(nums)
        prefix = [0] * n
        prefix[0] = nums[0]

        for i in range(1, n):
            prefix[i] = prefix[i - 1] + nums[i]

        for left in range(n):  # 0 -> n
            for right in range(left, n):  # left -> n
                if left == 0:
                    currSum = prefix[right]
                else:
                    currSum = prefix[right] - prefix[left - 1]

                if currSum == k:
                    count += 1
        return count


obj = Solution()
print(obj.subarraySum([1, 2, 3, 4, 5], 3))
