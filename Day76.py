# Map Of Highest Peak

import collections
class Solution:
    def highestPeak(self, isWater):
        R = len(isWater)
        C = len(isWater[0])

        q = collections.deque()
        ans = [[-1] * C for _ in range(R)]

        def enqueue(x, y, d):
            ans[x][y] = d
            q.append((x, y))
        
        for x in range(R):
            for y in range(C):
                if isWater[x][y] == 1:
                    enqueue(x, y, 0)
        
        directions = [
            (1, 0), (0, 1), (0, -1), (-1, 0)
        ]

        while len(q) > 0:
            x, y = q.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < R and 0 <= ny < C and ans[nx][ny] == -1:
                    enqueue(nx, ny, ans[x][y] + 1)

        return ans