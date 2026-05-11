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

            i = 0
            j = i + 1
            k = n - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total == 0:
                    result.append((nums[i], nums[j], nums[k]))

                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1

                elif total < 0:
                    j += 1
                else:
                    k -= 1

        return result


if __name__ == "__main__":
    # Example usage
    nums = [-1, 0, 1, 2, -1, -4]
    solution = Solution()
    print("Input:", nums)
    print("3Sum Triplets:", solution.three_sum(nums))
