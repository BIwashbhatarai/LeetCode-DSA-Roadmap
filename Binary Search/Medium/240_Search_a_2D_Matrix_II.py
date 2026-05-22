class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        Search a target value in a 2D matrix.

        The matrix has the following properties:
        - Each row is sorted in ascending order.
        - Each column is sorted in ascending order.

        Approach:
        Start from the top-right corner and eliminate rows or columns
        based on comparison with the target.

        Time Complexity: O(m + n)
        Space Complexity: O(1)
        """

        if not matrix or not matrix[0]:
            return False

        row = 0
        col = len(matrix[0]) - 1

        while row < len(matrix) and col >= 0:
            current = matrix[row][col]

            if current == target:
                return True
            elif current > target:
                col -= 1
            else:
                row += 1

        return False
