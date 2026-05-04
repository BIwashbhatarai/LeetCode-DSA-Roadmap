class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        n = len(nums)
        maxReach = 0

        for i in range(n):

            # If current index is beyond the farthest reachable point
            if i > maxReach:
                return False

            # Update the farthest reachable index
            maxReach = max(maxReach, i + nums[i])

        return True


if __name__ == "__main__":
    obj = Solution()
    print(obj.canJump([2, 3, 1, 1, 4]))
