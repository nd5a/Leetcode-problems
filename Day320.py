# Minimum Score Triangulation of Polygon

class Solution(object):
    def minScoreTriangulation(self, values):

        N = len(values)
        memo = {}
        def f(left, right):
            if (left, right) in memo:
                return memo[(left, right)]

            # Base: no triangle possible
            if right - left < 2:
                return 0

            best = float("inf")
            for mid in range(left + 1, right):
                score = values[left] * values[mid] * values[right]
                best = min(best, score + f(left, mid) + f(mid, right))

            memo[(left, right)] = best
            return best

        return f(0, N - 1)

