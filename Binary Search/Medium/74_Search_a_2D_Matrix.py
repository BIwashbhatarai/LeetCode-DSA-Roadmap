class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        m = len(matrix)  # number of rows
        n = len(matrix[0])  # number of columns

        left = 0
        right = m * n - 1

        while left <= right:
            mid = (left + right) // 2

            row = mid // n
            col = mid % n

            value = matrix[row][col]

            if value == target:
                return True
            elif value < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
