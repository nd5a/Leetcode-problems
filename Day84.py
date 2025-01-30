# Divide Nodes into the maximum number of Groups

import collections

class Solution:
    def magnificentSets(self, N, edges):
        INF = 10 ** 20
        adj_list = collections.defaultdict(list)

        for u, v in edges:
            u -= 1
            v -= 1

            adj_list[u].append(v)
            adj_list[v].append(u)
        
        def calc(x):
            # Start group 1 with x,

            distances = collections.defaultdict(lambda: INF)
            q = collections.deque()
            distances[x] = 1
            q.append(x)

            while len(q) > 0:
                now = q.popleft()

                for v in adj_list[now]:
                    if distances[v] == INF:
                        distances[v] = distances[now] + 1
                        q.append(v)
                    else:
                        if distances[v] % 2 == distances[now] % 2:
                            return (-1, -1)
            return (min(distances.keys()), max(distances.values()))
        
        best_by_parts = collections.defaultdict(lambda: 0)
        for i in range(N):
            g, r = calc(i)
            best_by_parts[g] = max(best_by_parts[g], r)
            if r == -1:
                return -1
        return sum(best_by_parts.values())