# Pacific Atlantic water Flow

class Solution:
    def pacificAtlantic(self, heights):
        if not heights or not heights[0]:
            return []
        
        m, n = len(heights), len(heights[0])
        
        pacific = set()
        atlantic = set()
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def dfs(r, c, visited, prev_height):
            # Check boundaries and height constraints
            if (
                r < 0 or c < 0 or r >= m or c >= n or
                (r, c) in visited or heights[r][c] < prev_height
            ):
                return
            visited.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc, visited, heights[r][c])
        
        # DFS from Pacific Ocean (top row and left column)
        for i in range(m):
            dfs(i, 0, pacific, heights[i][0])
        for j in range(n):
            dfs(0, j, pacific, heights[0][j])
        
        # DFS from Atlantic Ocean (bottom row and right column)
        for i in range(m):
            dfs(i, n - 1, atlantic, heights[i][n - 1])
        for j in range(n):
            dfs(m - 1, j, atlantic, heights[m - 1][j])
        
        # Intersection of both reachable sets
        result = list(pacific & atlantic)
        return result
