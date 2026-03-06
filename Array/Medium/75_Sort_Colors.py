# LeetCode 75 - Sort Colors
# Problem: https://leetcode.com/problems/sort-colors/


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None
        """
        n = len(nums)
        i = 0  # next position for 0
        j = 0  # current element being scanned
        k = n - 1  # next position for 2

        while j <= k:
            if nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[j] == 2:
                nums[k], nums[j] = nums[j], nums[k]
                k -= 1
            else:
                j += 1


# Example usage
if __name__ == "__main__":
    obj = Solution()
    print(obj.sortColors([2, 0, 2, 1, 1, 0]))
