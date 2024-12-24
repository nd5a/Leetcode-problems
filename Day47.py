# Find Minimum Diameter After Merging Two Trees

import collections
class Solution:
    def minimumDiameterAfterMerge(self, edges1, edges2):
        def get_diameter(edges):
            adj_list = collections.defaultdict(list)

            for u, v in edges:
                adj_list[u].append(v)
                adj_list[v].append(u)

            farthest = None
            farthest_distance = 0

            def get_farthest(node, parent, distance):
                nonlocal farthest
                nonlocal farthest_distance
                if distance > farthest_distance:
                    farthest_distance = distance
                    farthest = node
                
                for v in adj_list[node]:
                    if v != parent:
                        get_farthest(v, node, distance + 1)
                
            get_farthest(0, -1, 1)
            first_farthest = farthest

            farthest = None
            farthest_distance = 0
            get_farthest(first_farthest, -1, 1)

            return farthest_distance
        
        d1 = get_diameter(edges1)
        d2 = get_diameter(edges2)

        return max(d1 // 2 + d2 // 2 + 1, d1 - 1, d2 - 1)