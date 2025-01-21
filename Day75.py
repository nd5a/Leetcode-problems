# Grid Game

class Solution:
    def gridGame(self, grid):
        R = len(grid)
        C = len(grid[0])

        INF = 10 ** 20
        
        top_row_sum = sum(grid[0])
        bottom_row_sum = sum(grid[1])

        best = INF
        current_top = grid[0][0]
        current_bottom = bottom_row_sum

        score = max((top_row_sum - current_top), (bottom_row_sum - current_bottom))
        best = min(best, score)
        for i in range(1, C):
            current_top += grid[0][i]
            current_bottom -= grid[1][i - 1]

            score = max((top_row_sum - current_top), (bottom_row_sum - current_bottom))
            best = min(best, score)
        return best