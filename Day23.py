from collections import collections

class Solution:
    def minimumObstacles(self, grid) -> int:
        R = len(grid)
        C = len(grid[0])

        q = collections.deque()

        distances = [[None] * C for _ in range(R)]

        o = 0
        if grid[0][0] == 1:
            o+=1
        q.append((0,0,0))
        distances[0][0] = 0
        directions = [
            (1,0), (0,1), (-1,0), (0,-1)
        ]

        while len(q) > 0:
            d, x, y = q.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < R and 0 <= ny < C and distances[nx][ny] is None:
                    if grid[nx][ny] == 1:
                        distances[nx][ny] = d + 1
                        q.append((d+1, nx, ny))
                    else:
                        distances[nx][ny] = d
                        q.appendleft((d, nx, ny))
        return distances[R - 1][C - 1]