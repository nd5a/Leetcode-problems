# First Completly Painted Row or Column
class Solution:
    def firstCompleteIndex(self, arr, mat):
        R = len(mat)
        C = len(mat[0])

        lookup = {}
        for x in range(R):
            for y in range(C):
                lookup[mat[x][y]] = (x, y)
        
        row_count = [0] * R
        col_count = [0] * C

        for i, v in enumerate(arr):
            x, y = lookup[v]

            row_count[x] += 1
            col_count[y] += 1

            if row_count[x] == C or col_count[y] == R:
                return i
        else:
            assert(False)