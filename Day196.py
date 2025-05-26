# Largest Color Value in a Directed Graph

from collections import deque

class Solution:
    def largestPathValue(self, colors: str, edges):
        n = len(colors)
        adj = [[] for _ in range(n)]
        in_degree = [0] * n
        
        for a, b in edges:
            adj[a].append(b)
            in_degree[b] += 1
        
        q = deque()
        # Initialize each node's color count: 26 letters
        color_counts = [[0] * 26 for _ in range(n)]
        
        for i in range(n):
            if in_degree[i] == 0:
                q.append(i)
                color = ord(colors[i]) - ord('a')
                color_counts[i][color] = 1
        
        processed_nodes = 0
        max_color_value = 0
        
        while q:
            u = q.popleft()
            processed_nodes += 1
            current_max = max(color_counts[u])
            max_color_value = max(max_color_value, current_max)
            
            for v in adj[u]:
                # Update the color counts for node v
                for c in range(26):
                    new_count = color_counts[u][c]
                    if c == (ord(colors[v]) - ord('a')):
                        new_count += 1
                    if new_count > color_counts[v][c]:
                        color_counts[v][c] = new_count
                
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    q.append(v)
        
        if processed_nodes != n:
            return -1
        return max_color_value