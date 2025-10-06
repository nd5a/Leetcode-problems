# Swim in Rising Water

import heapq

class Solution:
    def swimInWater(self, grid):
        n = len(grid)
        visited = [[False] * n for _ in range(n)]
        
        # Min-heap storing (time_to_reach, row, col)
        min_heap = [(grid[0][0], 0, 0)]
        visited[0][0] = True
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        time = 0
        
        while min_heap:
            t, r, c = heapq.heappop(min_heap)
            time = max(time, t)  # track max elevation on the path
            
            # If we reached destination, return time
            if r == n - 1 and c == n - 1:
                return time
            
            # Explore 4-directional neighbors
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    heapq.heappush(min_heap, (grid[nr][nc], nr, nc))
        
        return -1  # should never reach here
