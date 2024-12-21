# Maximum number of K-Divisible Components

import collections

class Solution:
    def maxKDivisibleComponents(self, n, edges, values, k):
        adj_list = collections.defaultdict(list)

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        def traverse(node, parent):
            stsumt = numt = 0
            for v in adj_list[node]:
                if v != parent:
                    stsum, num = traverse(v, node)
                    stsumt += stsum
                    numt += num
            stsumt += values[node]
            if stsumt % k == 0:
                numt += 1
            return stsumt, numt
        
        _, num = traverse(0, -1)
        return num