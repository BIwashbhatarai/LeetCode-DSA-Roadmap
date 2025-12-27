"""
LeetCode 217: Contains Duplicate
Easy
HashSet Approach | Time: O(n), Space: O(n)
Author: Tilak Bhattarai
"""


class Solution:
    def containsDuplicate(self, nums):
        """
        Returns True if any value appears at least twice in the array, False otherwise.

        :param nums: List[int] - input array
        :return: bool - True if duplicate exists, False otherwise
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


# Example run
if __name__ == "__main__":
    obj = Solution()
    test_case = [1, 2, 3, 1]
    output = obj.containsDuplicate(test_case)
    print(f"Input: {test_case} -> Contains duplicate? {output}")
