# Find Eventual Safe States

import collections

class Solution:
    def eventualSafeNodes(self, graph):
        V = len(graph)

        rgraph = [[] for _ in range(V)]
        for i in range(V):
            for j in graph[i]:
                rgraph[j].append(i)
        
        edges = [None] * V
        terminal = []

        q = collections.deque()
        for i in range(V):
            edges[i] = len(graph[i])

            if edges[i] == 0:
                terminal.append(i)
                q.append(i)
            
        while len(q) > 0:
            current = q.popleft()

            for j in rgraph[current]:
                edges[j] -= 1
                if edges[j] == 0:
                    terminal.append(j)
                    q.append(j)
        
        return sorted(terminal)