# Minimum Cost Walk in Weighted Graph

import collections

class Solution:
    def minimumCost(self, N: int, edges, query):
        adj_list = collections.defaultdict(list)
        for u, v, w in edges:
            adj_list[u].append((v, w))
            adj_list[v].append((u, w))
        
        visited = [False] *N
        def visit(node):
            tw = (1 << 20) -1
            q = collections.deque()
            q.append(node)
            visited[node] = True

            while len(q) > 0:
                current = q.popleft()
                root[current] = node

                for v, w in adj_list[current]:
                    tw &= w
                    if not visited[v]:
                        q.append(v)
                        visited[v] = True
            costs[node] = tw
        costs={}
        root = [None] * N

        ans = []
        for u, v in query:
            if not visited[u]:
                visit(u)
            if not visited[v]:
                visit(v)
            ru = root[u]
            rv = root[v]

            if ru == rv:
                ans.append(costs[ru])
            else:
                ans.append(-1)
        return ans