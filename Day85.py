# Making A large Island

from typing import List
import collections

class Solution:
    def largestIsland(self, grid):
        rows, cols = len(grid), len(grid[0])
        colors = [[-1] * cols for _ in range(rows)]  # Track island colors
        colorCount = collections.Counter()  # Store area of each island
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs_tra(x, y, color):
            """Mark island with a unique color and calculate size."""
            if colors[x][y] != -1 or grid[x][y] == 0:
                return 0
            
            colors[x][y] = color
            size = 1  # Each 1 contributes to island size
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                    size += dfs_tra(nx, ny, color)
            
            return size

        currentColor = 2 
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 1 and colors[x][y] == -1:
                    colorCount[currentColor] = dfs_tra(x, y, currentColor)
                    currentColor += 1
        
        maxIsland = max(colorCount.values(), default=0)        
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 0: 
                    used_colors = set()
                    new_size = 1
                    
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                            color = colors[nx][ny]
                            if color not in used_colors:
                                used_colors.add(color)
                                new_size += colorCount[color]
                    
                    maxIsland = max(maxIsland, new_size)
        
        return maxIsland
