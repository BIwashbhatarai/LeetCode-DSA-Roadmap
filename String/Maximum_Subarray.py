# max_subarray.py


class Solution(object):
    def maxSubArray(self, nums):
        """
        # Intuition
        We want the maximum sum of a continuous subarray.
        Instead of checking all subarrays (O(n^2)), we can keep a running sum
        and reset it whenever it becomes negative, because a negative sum would
        only decrease future sums.

        # Approach
        Use Kadane's Algorithm:
        - Initialize maxSum = -infinity, currentSum = 0
        - Loop through each number:
            - Add it to currentSum
            - Update maxSum if currentSum > maxSum
            - If currentSum < 0, reset currentSum to 0

        # Complexity
        - Time complexity: O(n), we traverse the array once
        - Space complexity: O(1), we only use a few variables
        """

        maxSum = float("-inf")
        currentSum = 0

        for num in nums:
            currentSum += num
            if currentSum > maxSum:
                maxSum = currentSum
            if currentSum < 0:
                currentSum = 0

        return maxSum
