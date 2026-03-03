class Solution:
    """
    Solution for the 3Sum problem:
    Given an integer array nums, return all the triplets [a, b, c] such that a + b + c == 0.
    Triplets must be unique.
    """

    def three_sum(self, nums):
        """
        :param nums: List[int] - input array of integers
        :return: List[List[int]] - list of unique triplets that sum to zero
        """
        nums.sort()  # Sort the array first
        result = []
        n = len(nums)

        for i in range(n):
            # Skip duplicates for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1
            target = -nums[i]  # We want nums[left] + nums[right] == -nums[i]

            while left < right:
                current_sum = nums[left] + nums[right]

                if current_sum == target:
                    # Found a valid triplet
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # Skip duplicates for left
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # Skip duplicates for right
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif current_sum < target:
                    left += 1  # Need a bigger sum
                else:
                    right -= 1  # Need a smaller sum

        return result


if __name__ == "__main__":
    # Example usage
    nums = [-1, 0, 1, 2, -1, -4]
    solution = Solution()
    print("Input:", nums)
    print("3Sum Triplets:", solution.three_sum(nums))
