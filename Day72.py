# Minimum Cost to Make at Least one valid path in a Grid

import collections

class Solution:
    def minCost(self, grid):
        R = len(grid)
        C = len(grid[0])

        INF = 10 ** 20
        q = collections.deque()
        distances = [[INF] * C for _ in range(R)]

        q.append((0, 0))
        distances[0][0] = 0

        directions = [(3,1,0), (1,0,1), (2, 0, -1), (4, -1, 0)]
        while len(q) > 0:
            x, y = q.popleft()

            for d, dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < R and 0 <= ny < C:
                    nc = 1
                    if grid[x][y] == d:
                        nc = 0

                    if distances[nx][ny] > nc + distances[x][y]:
                        distances[nx][ny] = nc + distances[x][y]

                        if nc == 0:
                            q.appendleft((nx, ny))
                        else:
                            q.append((nx, ny))

        return distances[R - 1][C - 1]