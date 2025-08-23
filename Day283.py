# Find the Minimum Area to Cover All Ones II

from functools import cache
from typing import List

fmin = lambda x, y: x if x < y else y

class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        INF = 10 ** 18

        @cache
        def go(x1, y1, x2, y2, left):
            # left = number of rectangles to cover this subgrid
            if left == 0:
                return 0
            if left == 1:
                mxx, mxy = -1, -1
                mnx, mny = INF, INF

                for i in range(x1, x2 + 1):
                    for j in range(y1, y2 + 1):
                        if grid[i][j] == 1:
                            mxx = max(mxx, i)
                            mnx = min(mnx, i)
                            mxy = max(mxy, j)
                            mny = min(mny, j)

                if mnx == INF:  # no 1's
                    return 0
                return (mxx - mnx + 1) * (mxy - mny + 1)

            best = INF

            # horizontal cuts
            for cut in range(x1, x2):
                for t in range(1, left):
                    best = fmin(best, go(x1, y1, cut, y2, t) + go(cut + 1, y1, x2, y2, left - t))

            # vertical cuts
            for cut in range(y1, y2):
                for t in range(1, left):
                    best = fmin(best, go(x1, y1, x2, cut, t) + go(x1, cut + 1, x2, y2, left - t))

            return best

        return go(0, 0, R - 1, C - 1, 3)
