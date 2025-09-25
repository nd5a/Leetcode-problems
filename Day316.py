# Triangle

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        N = len(triangle)

        INF = 10 ** 20
        dp = [[triangle[0][0]]]

        for i in range(1, N):
            dp.append([])
            for j in range(i + 1):
                dp[i].append(0)

                dp[i][j] = INF
                if i - 1 >= 0 and j - 1 >= 0:
                    dp[i][j] = min(dp[i][j], triangle[i][j] + dp[i - 1][j - 1])
                
                if i - 1 >= 0 and j < i:
                    dp[i][j] = min(dp[i][j], triangle[i][j] + dp[i - 1][j])
        return min(dp[-1])