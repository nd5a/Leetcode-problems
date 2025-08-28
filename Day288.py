# Sort Matrix by Diagonals

class Solution:
    def sortMatrix(self, grid):
        R = len(grid)
        C = len(grid[0])

        for d in range(-(C - 1), R):
            arr = []
            for x in range(max(d, 0), min(R, C + d)):
                y = x- d
                arr.append(grid[x][y])
            
            arr.sort(reverse=(not d < 0))

            for i, x in enumerate(range(max(d, 0), min(R, C + d))):
                y = x - d
                grid[x][y] = arr[i]
        return grid