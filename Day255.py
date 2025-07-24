# Minimum Score After Removals on a Tree

from typing import List
from collections import defaultdict

class Solution:
    def minimumScore(self, nums, edges):
        n = len(nums)
        graph = defaultdict(list)
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        parent = [-1] * n
        xor = [0] * n
        tin = [0] * n
        tout = [0] * n
        time = [1] 

        def dfs(u, p):
            xor[u] = nums[u]
            tin[u] = time[0]
            time[0] += 1
            for v in graph[u]:
                if v == p:
                    continue
                parent[v] = u
                dfs(v, u)
                xor[u] ^= xor[v]
            tout[u] = time[0]
            time[0] += 1
        
        dfs(0, -1)
        total_xor = xor[0]
        res = float('inf')

        def is_ancestor(u, v):
            return tin[u] <= tin[v] and tout[v] <= tout[u]
        
        for i in range(1, n):
            for j in range(i + 1, n):
                u, v = i, j
                if is_ancestor(u, v):
                    xor1 = xor[v]
                    xor2 = xor[u] ^ xor[v]
                    xor3 = total_xor ^ xor[u]
                elif is_ancestor(v, u):
                    xor1 = xor[u]
                    xor2 = xor[v] ^ xor[u]
                    xor3 = total_xor ^ xor[v]
                else:
                    xor1 = xor[u]
                    xor2 = xor[v]
                    xor3 = total_xor ^ xor[u] ^ xor[v]
                vals = [xor1, xor2, xor3]
                res = min(res, max(vals) - min(vals))
        
        return res
