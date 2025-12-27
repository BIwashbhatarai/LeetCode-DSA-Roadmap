"""
LeetCode 136: Single Number
Easy
Bit Manipulation | Time: O(n), Space: O(1)
Author: Tilak Bhattarai
"""


class Solution:
    def singleNumber(self, nums):
        """
        Finds the element that appears only once in an array where every other element appears twice.

        :param nums: List[int] - input array
        :return: int - single number
        """
        result = 0
        for num in nums:
            result ^= num  # XOR operation to find the single number
        return result


# Example run
if __name__ == "__main__":
    obj = Solution()
    arr = [4, 1, 2, 1, 2]
    output = obj.singleNumber(arr)
    print(f"Input: {arr} -> Single Number: {output}")
