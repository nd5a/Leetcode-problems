# Length of Longest V - Shaped Diagonal Segment

from functools import cache
class Solution:
    def lenOfVDiagonal(self, grid):
        R = len(grid)
        C = len(grid[0])

        directions = [
            (-1, -1),
            (-1, 1),
            (1,1),
            (1, -1)
        ]

        @cache
        def calc(x,y, left, direction):
            best = 0

            # Go straight
            dx, dy = directions[direction]
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C and grid[x][y] + grid[nx][ny] == 2:
                best = max(best, calc(nx, ny, left, direction) + 1, best)

            # go right (but only if we are able to)
            if left > 0:
                dx, dy = directions[(direction + 1) % 4]
                nx, ny = x + dx, y + dy
                if 0 <= nx < R and 0 <= ny < C and grid[x][y] + grid[nx][ny] == 2:
                    best = max(best, calc(nx, ny, left - 1, (direction + 1) % 4)+ 1, best)
            return best

        best = 0
        for x in range(R):
            for y in range(C):
                if grid[x][y] == 1:
                    best = max(best, 1)
                    for d in range(len(directions)):
                        dx, dy = directions[d]
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] == 2:
                            best = max(best, calc(nx, ny,1,d) + 2)
        return best