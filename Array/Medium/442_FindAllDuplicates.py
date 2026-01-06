# =============================================================================
# Title: 442_FindAllDuplicatesInArray_Medium
# Problem: LeetCode 442 - Find All Duplicates in an Array
# Difficulty: Medium
# Language: Python
# =============================================================================


class Solution(object):
    """
    Solution for LeetCode Problem 442: Find All Duplicates in an Array.

    # Intuition
    Given an array of length n where numbers are in the range [1, n],
    some elements appear twice and others once. We need to find all duplicates.
    The straightforward idea is to count occurrences and track numbers appearing twice.

    # Approach
    1. Initialize an empty list `result` to store duplicates.
    2. Initialize a dictionary `frequency` to count occurrences of each number.
    3. Loop through each number in the array:
       - If the number already exists in `frequency`, increment its count.
           - If count becomes 2, append the number to `result`.
       - If the number is not in `frequency`, set its count to 1.
    4. Return `result`.

    # Complexity
    - Time complexity: O(n) — iterate through the array once.
    - Space complexity: O(n) — store counts for each number in the dictionary.
    """

    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        frequency = {}

        for num in nums:
            if num in frequency:
                frequency[num] += 1
                if frequency[num] == 2:
                    result.append(num)
            else:
                frequency[num] = 1

        return result


# ===================== Example Usage =====================

if __name__ == "__main__":
    obj = Solution()
    test_input = [4, 3, 2, 7, 8, 2, 3, 1]
    print("Input:", test_input)
    print("Duplicates found:", obj.findDuplicates(test_input))
