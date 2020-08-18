# Problem of Binary Search in 2D array
# Left element will always be 0 and right will be (number of rows * number of columns - 1)
# Then to get row index of midpoint element we need to divide by col and to get column index of midpoint element we need to take mod by col.
# Time Complexity: O(log(m*n)).
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix == None or len(matrix) == 0:
            return False
        row = len(matrix)
        col = len(matrix[0])
        left = 0
        right = row * col - 1
        while left <= right:
            midpoint = left + (right - left)//2
            midpoint_element = matrix[midpoint // col][midpoint % col]
            if midpoint_element == target:
                return True
            elif midpoint_element > target:
                right = midpoint - 1
            else:
                left = midpoint + 1