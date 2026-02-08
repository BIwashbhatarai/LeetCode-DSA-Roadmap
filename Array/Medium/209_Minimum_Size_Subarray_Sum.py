class Solution:
    """
    Solution for the 'Minimum Size Subarray Sum' problem.

    Finds the length of the smallest contiguous subarray
    whose sum is greater than or equal to the target.
    """

    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        """
        Uses the sliding window approach to find the minimal subarray length.

        Args:
            target (int): The target sum.
            nums (list[int]): The list of positive integers.

        Returns:
            int: Length of the smallest subarray with sum >= target. Returns 0 if no such subarray exists.
        """
        left = 0
        curr_sum = 0
        min_length = float("inf")

        for right in range(len(nums)):
            curr_sum += nums[right]

            while curr_sum >= target:
                min_length = min(min_length, right - left + 1)
                curr_sum -= nums[left]
                left += 1

        return 0 if min_length == float("inf") else min_length


# Example usage
if __name__ == "__main__":
    obj = Solution()
    result = obj.minSubArrayLen(7, [2, 3, 1, 2, 4, 3])
    print(f"Minimum subarray length: {result}")  # Output: 2
