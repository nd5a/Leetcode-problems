# Maximum Number of Fish in a Grid

class Solution:
    def findMaxFish(self, grid):
        R = len(grid)
        C = len(grid[0])

        # Connected Components
        done = [[False] * C for _ in range(R)]
        directions = [(1,0), (0, 1), (-1, 0), (0, -1)]

        def get(x, y):
            done[x][y] = True
            res = grid[x][y]

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] != 0 and not done[nx][ny]:
                    res += get(nx, ny)
                
            return res
        mx = 0
        for x in range(R):
            for y in range(C):
                if grid[x][y] != 0 and not done[x][y]:
                    mx = max(mx, get(x, y))
        return mx