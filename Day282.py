# Find the Minimum Area to Cover All Ones I

class Solution:
    def minimumArea(self, grid):
        R = len(grid)
        C = len(grid[0])

        INF =10 ** 20

        mxx = mxy = 0
        mnx = mny = INF
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    mxx = max(mxx, i)
                    mnx = min(mnx, i)
                    mxy = max(mxy, j)
                    mny = min(mny, j)
        return (mxx - mnx + 1) * (mxy - mny + 1)