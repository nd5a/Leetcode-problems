# Set Matrix Zeroes

class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        R = len(matrix)
        C = len(matrix[0])
         
        first_row_zero = False
        first_col_zero = False

        for i in range(R):
            if matrix[i][0] == 0:
                first_col_zero = True
        for j in range(C):
            if matrix[0][j] == 0:
                first_row_zero = True
        
        for i in range(1, R):
            for j in range(1, C):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j]= 0
        
        for i in range(1, R):
            for j in range(1, C):
                if matrix[i][0] == 0:
                    matrix[i][j] = 0
                if matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if first_col_zero:
            for i in range(R):
                matrix[i][0] = 0
        
        if first_row_zero:
            for j in range(C):
                matrix[0][j] = 0