class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        column = len(matrix[0])
        
        r = 0
        c = column - 1
        
        while (r < row and c >= 0):
            if matrix[r][c] == target:
                return True
            elif(matrix[r][c] > target):
                c -= 1
            else:
                r += 1
        return False