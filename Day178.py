# Find Minimum Time to reach last Room II

import heapq

class Solution:
    def minTimeToReach(self, moveTime):
        n = len(moveTime)
        m = len(moveTime[0]) if n else 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        INF = float('inf')
        
        # Initialize distance array with infinity for all (i,j, parity)
        dist = [[[INF] * 2 for _ in range(m)] for __ in range(n)]
        dist[0][0][0] = 0  # Starting at (0,0) with 0 steps (even parity)
        
        heap = []
        heapq.heappush(heap, (0, 0, 0, 0))
        
        while heap:
            time, i, j, p = heapq.heappop(heap)
            if i == n - 1 and j == m - 1:
                return time
            if time > dist[i][j][p]:
                continue
            for di, dj in directions:
                x, y = i + di, j + dj
                if 0 <= x < n and 0 <= y < m:
                    step_time = 1 if p == 0 else 2
                    start_time = max(time, moveTime[x][y])
                    new_time = start_time + step_time
                    new_p = 1 - p
                    if new_time < dist[x][y][new_p]:
                        dist[x][y][new_p] = new_time
                        heapq.heappush(heap, (new_time, x, y, new_p))
        return -1  