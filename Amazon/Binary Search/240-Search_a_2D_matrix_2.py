# Time complexity: O(M + N)
'''
Intuition is since row and column both are sorted Binary search solution is slower so we start from 1st row and last column. If matrix[row][col] > target we should not look into last column as target value is lessr and all the column values for rest of row are larget than matrix[row][col] so we start removing columns. And if target value is greater then we check subsequent rows for that column

'''
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == None or len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        row = 0
        col = len(matrix[0]) - 1
        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                return True
            if matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return False
