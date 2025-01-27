# Course Schedule IV

class Solution:
    def checkIfPrerequisite(self, N, prerequisites, queries):
        
        dp = [[False] * N for _ in range(N)]

        for u, v in prerequisites:
            dp[u][v] = True
        
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    dp[i][j] |= dp[i][k] and dp[k][j]

        ans = []
        for u, v in queries:
            ans.append(dp[u][v])
        return ans
    