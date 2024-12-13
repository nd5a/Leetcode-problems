import collections
class Solution:
    def maxEqualRowsAfterFlips(self, matrix) -> int:
        R = len(matrix)
        C = len(matrix[0])
        
        f = collections.Counter()
        for x in range(R):
            if matrix[x][0] == 1:
                # flip the row
                for y in range(C):
                    matrix[x][y] = 1 - matrix[x][y]
            
            r = []
            for y in range(C):
                r.append(str(matrix[x][y]))
            
            f["".join(r)] += 1
        return max(f.values())