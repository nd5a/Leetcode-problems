# Count Square Submatrices with All ones

class Solution:
    def countSquares(self, matrix):
        R = len(matrix)
        C = len(matrix[0])

        dp = [[0] * C for _ in range(R)]

        count = 0
        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 1:
                    dp[i][j] = 1

                    if i-1 >= 0 and j-1 >= 0:
                        dp[i][j] = max(dp[i][j], min(dp[i - 1][j], dp[i-1][j-1], dp[i][j - 1]) + 1)
                    count += dp[i][j]
        return count