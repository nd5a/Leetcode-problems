# Count Servers that Communicate

class Solution:
    def countServers(self, grid):
        R = len(grid)
        C = len(grid[0])

        rows = [0] * R
        cols = [0] * C
        for x in range(R):
            for y in range(C):
                if grid[x][y] == 1:
                    rows[x] += 1
                    cols[y] += 1
        
        count = 0
        for x in range(R):
            for y in range(C):
                if grid[x][y] == 1 and rows[x] == 1 and cols[y] == 1:
                    count += 1
        
        return sum(rows) - count