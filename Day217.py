# Maximum Diference between Increasing Elements

class Solution:
    def maximumDifference(self, nums):
        INF = 10 ** 20

        mn = INF
        best = -1

        for x in nums:
            if mn < x:
                best = max(best, x - mn)
            mn = min(mn, x)
        return best