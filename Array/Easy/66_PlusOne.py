"""
LeetCode 66: Plus One
Easy
Author: Tilak Bhattarai
"""


class Solution:
    def plusOne(self, digits):
        """
        Converts list of digits to integer, adds one, converts back to list.

        :param digits: List[int] - input digits
        :return: List[int] - result after adding one
        """
        # Convert list of digits to integer
        n = int("".join(map(str, digits)))

        # Add one
        n += 1

        # Convert back to list of digits
        return [int(d) for d in str(n)]


# Example run
if __name__ == "__main__":
    obj = Solution()
    digits = [1, 2, 3]
    output = obj.plusOne(digits)
    print(f"Input: {digits} -> Output: {output}")
