from collections import collections
class Solution:
    def validArrangement(self, pairs):
        # Step 1: Build the graph and calculate degrees
        graph = collections.defaultdict(list)
        in_degree = collections.Counter()
        out_degree = collections.Counter()

        for u, v in pairs:
            graph[u].append(v)
            out_degree[u] += 1
            in_degree[v] += 1

        # Step 2: Find the starting node (if there's an Eulerian path)
        start_node = pairs[0][0]  # Default start node
        for node in graph:
            if out_degree[node] > in_degree[node]:
                start_node = node
                break

        # Step 3: Perform Hierholzer's Algorithm to find Eulerian path
        def dfs(node):
            while graph[node]:
                next_node = graph[node].pop()
                dfs(next_node)
                result.append([node, next_node])

        result = []
        dfs(start_node)
        return result[::-1]
