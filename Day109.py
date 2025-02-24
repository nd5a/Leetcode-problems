# Most Profitable Path in a Tree

from typing import List
from collections import defaultdict

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        # Step 1: Build adjacency list representation of the tree
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Step 2: Find the path from Bob to root (0) and mark time taken
        bob_time = {}
        def find_bob_path(node, parent, time):
            if node == 0:
                bob_time[node] = time
                return True
            for neighbor in graph[node]:
                if neighbor != parent and find_bob_path(neighbor, node, time + 1):
                    bob_time[node] = time
                    return True
            return False
        
        find_bob_path(bob, -1, 0)

        # Step 3: DFS to find Alice's most profitable path
        max_profit = float('-inf')

        def dfs(node, parent, time, profit):
            nonlocal max_profit
            # Determine Alice's income at the node considering Bob's presence
            if node in bob_time:
                if bob_time[node] > time:  # Bob arrives later, Alice takes full amount
                    profit += amount[node]
                elif bob_time[node] == time:  # They arrive simultaneously, share the amount
                    profit += amount[node] // 2
                # If Bob arrives earlier, the node has already been processed by Bob (profit remains unchanged)
            else:
                profit += amount[node]

            # Check if the node is a leaf (no unvisited children)
            is_leaf = True
            for neighbor in graph[node]:
                if neighbor != parent:
                    is_leaf = False
                    dfs(neighbor, node, time + 1, profit)

            # Update max profit if Alice reaches a leaf
            if is_leaf:
                max_profit = max(max_profit, profit)

        dfs(0, -1, 0, 0)

        return max_profit
