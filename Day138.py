# Maximum Number of Points from grid Queries

from typing import List
import collections

class Solution:
    def maxPoints(self, grid, queries):
        Q = len(queries)
        R = len(grid)
        C = len(grid[0])
        N = R * C

        pqueue = []
        for x in range(R):
            for y in range(C):
                pqueue.append((grid[x][y], x, y))
        pqueue.sort()

        qs = []
        for index, q in enumerate(queries):
            qs.append((q, index))
        qs = collections.deque(sorted(qs))

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        ans = [None] * Q  # Fix: Initialize ans correctly
        
        while len(qs) > 0 and qs[0][0] <= grid[0][0]:
            ans[qs[0][1]] = 0
            qs.popleft()

        parents = [x for x in range(N)]
        sz = [1] * N

        def ufind(x):
            if parents[x] != x:
                parents[x] = ufind(parents[x])
            return parents[x]

        def uunion(a, b):
            ua = ufind(a)
            ub = ufind(b)

            if ua == ub:
                return

            parents[ua] = ub
            sz[ub] += sz[ua]

        for v, x, y in pqueue:
            while len(qs) > 0 and qs[0][0] <= v:
                ans[qs[0][1]] = sz[ufind(0)]
                qs.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < R and 0 <= ny < C and grid[x][y] >= grid[nx][ny]:
                    uunion(nx * C + ny, x * C + y)

        while len(qs) > 0:
            ans[qs[0][1]] = sz[ufind(0)]
            qs.popleft()

        return ans
