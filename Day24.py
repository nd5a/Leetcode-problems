import heapq
class Solution:
    def minimumTime(self, grid):
        R = len(grid)
        C = len(grid[0])
        INF = 10 ** 20
        
        for i in range(R):
            for j in range(C):  
                if (grid[i][j] % 2) != ((i + j) % 2):
                    grid[i][j] += 1
        
        if grid[0][1] != 1 and grid[1][0] != 1:
            return -1

        h = [(0, 0, 0)]
        distances = [[INF] * C for _ in range(R)]
        distances[0][0] = 0

        directions = [(1, 0),(0, 1), (-1, 0), (0, -1)]

        while len(h) > 0:
            d, x, y = heapq.heappop(h)

            if distances[x][y] < d:
                continue
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < R and 0 <= ny < C:
                    nd = max(d + 1, grid[nx][ny])

                    if nd < distances[nx][ny]:
                        distances[nx][ny] = nd
                        heapq.heappush(h, (nd, nx, ny))
        return distances[R - 1][C - 1]