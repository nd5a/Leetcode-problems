# Count Submatrics with All Ones

class Solution:
    def numSubmat(self, mat):
        R = len(mat)
        C = len(mat[0])

        prefix = [[0] * C for _ in range(R + 1)]
        for x in range(R):
            for y in range(C):
                prefix[x + 1][y] = prefix[x][y] + mat[x][y]
        
        def ally(x1, x2,y):
            return (prefix[x2+1][y] - prefix[x1][y]) == (x2 - x1 + 1)
        
        total = 0
        for x1 in range(R):
            for x2 in range(x1, R):
                count = 0
                streak = 0 
                for y in range(C):
                    if ally(x1, x2, y):
                        streak += 1
                    else:
                        streak = 0
                    count += streak
                total += count
        return total