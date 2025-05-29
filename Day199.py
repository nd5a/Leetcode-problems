# Maximizes the Number of Target Nodes After Connecting Trees II

import collections
class Solution:
    def maxTargetNodes(self, edges1, edges2):
        def calculate_colors(edges):
            n = len(edges) + 1
            colors = [None] * n
            adj = collections.defaultdict(list)

            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)

            queue = collections.deque([0])
            colors[0] = 0

            while queue:
                curr = queue.popleft()
                for neighbor in adj[curr]:
                    if colors[neighbor] is None:
                        colors[neighbor] = 1 - colors[curr]
                        queue.append(neighbor)
            return colors

        g1 = calculate_colors(edges1)
        g2 = calculate_colors(edges2)

        f1 = collections.Counter(g1)
        f2 = collections.Counter(g2)

        max_color_count_in_g2 = max(f2[0], f2[1])

        # Precompute result per color
        value_for_color = {
            0: f1[0] + max_color_count_in_g2,
            1: f1[1] + max_color_count_in_g2
        }

        return [value_for_color[color] for color in g1]
