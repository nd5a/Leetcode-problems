from collections import collections
class Solution:
    def shortestDistanceAfterQueries(self, N, queries):
        Q = len(queries)

        edges = collections.defaultdict(list)

        ans = []
        for s, e in queries:
            edges[e].append(s)

            dist = [None] * N
            dist[0] = 0
            for i in range(1, N):
                dist[i] = dist[i-1] + 1
                for p in edges[i]:
                    dist[i] = min(dist[i], dist[p]+1)
            ans.append(dist[-1])
        return ans
        