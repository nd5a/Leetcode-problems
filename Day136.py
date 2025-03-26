# Minimum Operation to Make a Uni-Value Grid

class Solution:
    def minOperations(self, grid, x):
        R = len(grid)
        C = len(grid[0])
        t = grid[0][0] % x

        arr = []
        for i in range(R):
            for j in range(C):
                if grid[i][j] % x != t:
                    return -1
                arr.append(grid[i][j])
        
        arr.sort()
        N = len(arr)

        median = arr[N // 2]
        moves = 0
        for i in range(R):
            for j in range(C):
                moves += abs(median- grid[i][j])//x

        return moves