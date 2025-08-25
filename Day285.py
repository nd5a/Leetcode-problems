# Diagonal Traverse

class Solution:
    def findDiagonalOrder(self, mat):
        R, C = len(mat), len(mat[0])
        ND = R + C - 1   

        arr = []
        for d in range(ND):
            # Collect elements for current diagonal
            temp = []
            for x in range(max(0, d - C + 1), min(R, d + 1)):
                y = d - x
                temp.append(mat[x][y])

            # Reverse order for even diagonals
            if d % 2 == 0:
                arr.extend(temp[::-1])
            else:
                arr.extend(temp)

        return arr
