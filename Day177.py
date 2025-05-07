# Find Minimum Time to reach last Room I

import heapq
class Solution:
    def minTimeToReach(self, moveTime):
        R = len(moveTime)
        C = len(moveTime[0])
        INF = 10 ** 20
        h = []

        heapq.heappush(h, (0, 0,0))
        best = [[INF] * C for _ in range(R)]
        best[0][0] = 0

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while len(h) > 0:
            d, x, y = heapq.heappop(h)

            if best[x][y] < d:
                continue
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < R and 0 <= ny < C:
                    cost = max(d + 1, moveTime[nx][ny] + 1)
                    if best[nx][ny] > cost:
                        best[nx][ny] = cost
                        heapq.heappush(h, (cost, nx, ny))
        return best[R -1][C - 1]